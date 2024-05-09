import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import numpy as np
import os
import cmath
import math

parser = argparse.ArgumentParser()
parser.add_argument("--title", help="Plot title", default="Plot Title")
parser.add_argument("--r-series", help="Series Resistor Value", default=1e3, type=int)
parser.add_argument("--outfile", help="Generated figure output filename (.png)", default=None)
parser.add_argument("--quiet", help="Do not display generated figure", default=False, action="store_true")
parser.add_argument("--loglog", help="Make log-log plot", default=False, action="store_true")
parser.add_argument("--autodetect", help="Automatically detect filenames", default=False, action="store_true")
args = parser.parse_args()

title = args.title               # Plot title
x_tsv_column = "Freq."           # TSV file column name of x_axis (case sensitive)
xlabel = "Frequency [Hz]"        # x axis label
#y_tsv_column = "Amplitude"         # TSV file column name of y_axis (case sensitive)
ylabel = "Amplitude [dB]"           # y axis label
# data filenames
filename_ref = "./no_dut_10k.txt"
if args.autodetect:
    try:
        filename_L = list(filter(lambda s: s.startswith("impedance") and s.endswith("l.tsv"), os.listdir(".")))[0]
        filename_R = list(filter(lambda s: s.startswith("impedance") and s.endswith("r.tsv"), os.listdir(".")))[0]
    except:
        print("Data files not found")
        exit()
else:
    filename_L = "exampledata1.tsv"  # Left channel data filename
    filename_R = "exampledata2.tsv"  # Right channel data filename

def read_and_filter_tsv_file(filename):
    import tempfile
    with open(filename, "r") as f:
        lines = f.readlines()
    lines = list(filter(lambda s: not s.startswith("%\t"), lines))
    lines = list(filter(lambda s: not s.startswith("% ["), lines)) #]
    assert len(list(filter(lambda s: s.startswith("% "), lines)))==1, "more than one header line after filtering"
    assert lines[0].startswith("% "), "more than one header line after filtering"
    lines[0] = lines[0].replace("% ", "")
    with tempfile.TemporaryFile(mode='w+t') as temp_file:
        temp_file.writelines(lines)
        temp_file.seek(0)  # Go back to the start of the file
        return pd.read_csv(temp_file, sep='\t', header=0)

df_L = read_and_filter_tsv_file(filename_L)
# df_R = read_and_filter_tsv_file(filename_R)
df_ref = read_and_filter_tsv_file(filename_ref)

def calculate_Z(Rseries, dbFund, degFund):
    vratio = cmath.rect(pow(10, dbFund/20), math.radians(degFund))
    return Rseries * vratio / (1-vratio)

def calculate_Zi(Zboth, Zai1):
    return 1/(1/Zboth - 1/Zai1)

def calculate_Zi_sweep(Rseries, df, df_ref):
    RiDUTs = []
    XiDUTs = []
    for dbFund, degFund, refdbFund, refdegFund in zip(df["Amplitude"], df["Phase"], df_ref["Amplitude"], df_ref["Phase"]):
        Zboth = calculate_Z(Rseries, dbFund, degFund)
        Zai1 = calculate_Z(Rseries, refdbFund, refdegFund)
        ZiDUT = calculate_Zi(Zboth, Zai1)
        RiDUTs.append(ZiDUT.real)
        XiDUTs.append(ZiDUT.imag)
        print(dbFund, degFund, Zboth, Zai1, ZiDUT)
    return (np.asarray(RiDUTs), np.asarray(XiDUTs))

(Ri_L, Xi_L) = calculate_Zi_sweep(args.r_series, df_L, df_ref)
# (Ri_R, Xi_R) = calculate_Zi_sweep(args.r_series, df_R, df_ref)

# Set seaborn style to improve aesthetics
sns.set(style="whitegrid")  # You can change the style to "darkgrid", "whitegrid", etc.

# Set seaborn color palette
sns.set_palette("pastel")  # Other options: "muted", "bright", "deep", etc.
sns.set_palette("pastel")  # Other options: "muted", "bright", "deep", etc.

# Customize matplotlib font settings
plt.rc('font', size=10)  # Sets the default font size
plt.rc('axes', titlesize=14)  # Font size of the axes title
plt.rc('axes', labelsize=10)  # Font size of the x and y labels

# Create a plot to demonstrate the style
fig, (ax1, ax2) = plt.subplots(nrows=2)
plt.title(title)
plt.xlabel(xlabel)
#plt.ylabel(ylabel)
ax1.set_ylabel("Real part [Ohm]")
ax2.set_ylabel("Imaginary part [Ohm]")
if args.loglog:
    ax1.set_xscale("log")
    ax1.set_yscale("symlog")
    ax2.set_xscale("log")
    ax2.set_yscale("symlog")

ax1.plot(df_L[x_tsv_column].to_numpy(), Ri_L, label="Left Channel")
# ax1.plot(df_R[x_tsv_column].to_numpy(), Ri_R, label="Right Channel")
ax2.plot(df_L[x_tsv_column].to_numpy(), Xi_L, label="Left Channel")
# ax2.plot(df_R[x_tsv_column].to_numpy(), Xi_R, label="Right Channel")

# Customize axes and grids for better aesthetics
plt.grid(True)  # Show grid
plt.legend(loc='upper left')

# Use tight layout to automatically adjust subplot params
plt.tight_layout()

# Save the plot with high resolution
if args.outfile:
    plt.savefig(args.outfile, dpi=300)  # Save as PNG file with high DPI

# Show the plot
if not args.quiet:
    plt.show()
