import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--title", help="Plot title", default="Plot Title")
parser.add_argument("--type", help="Plot type", choices=["thd", "freqresp"])
parser.add_argument("--outfile", help="Generated figure output filename (.png)", default=None)
parser.add_argument("--simfile", help="Simulation data (LTSpice polar text output)", default=None)
parser.add_argument("--calfile", help="Theoretical data (csv)", default=None)
parser.add_argument("--quiet", help="Do not display generated figure", default=False, action="store_true")
parser.add_argument("--logx", help="Make x-axis logarithmic", default=False, action="store_true")
parser.add_argument("--autodetect", help="Automatically detect filenames", default=False, action="store_true")
args = parser.parse_args()

title = args.title               # Plot title
x_tsv_column = "Freq."           # TSV file column name of x_axis (case sensitive)
xlabel = "Frequency [Hz]"        # x axis label
if args.type == "thd":
    args.simfile = None
    y_tsv_column = "THD"         # TSV file column name of y_axis (case sensitive)
    ylabel = "THD [%]"           # y axis label
elif args.type == "freqresp":
    y_tsv_column = "Amplitude"   # TSV file column name of y_axis (case sensitive)
    ylabel = "Amplitude [dB]"    # y axis label
# data filenames
if args.autodetect:
    try:
        filename_L = list(filter(lambda s: s.startswith("audioanalyzer") and s.endswith("l.tsv"), os.listdir(".")))[0]
        filename_R = list(filter(lambda s: s.startswith("audioanalyzer") and s.endswith("r.tsv"), os.listdir(".")))[0]
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

def read_ltspice_simdata(filename):
    df = pd.read_csv(filename, sep='\t', header=0)
    complex_in = df["V(in)"].apply(lambda x: complex(*map(float, x.split(','))))
    complex_out = df["V(out)"].apply(lambda x: complex(*map(float, x.split(','))))
    return pd.DataFrame({"f": df["Freq."], "in": complex_in, "out": complex_out, "outampl": complex_out.apply(lambda x: abs(x))})

df_L = read_and_filter_tsv_file(filename_L)
df_R = read_and_filter_tsv_file(filename_R)
if args.simfile:
    df_sim = read_ltspice_simdata(args.simfile)
if args.calfile:
    df_cal = pd.read_csv(args.calfile)

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
fig, ax = plt.subplots()
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
if args.logx:
    ax.set_xscale("log")
ax.plot(df_L[x_tsv_column].to_numpy(), df_L[y_tsv_column].to_numpy(), label="Left Channel")
ax.plot(df_R[x_tsv_column].to_numpy(), df_R[y_tsv_column].to_numpy(), label="Right Channel")
if args.simfile:
    ax.plot(df_sim["f"].to_numpy(), df_sim["outampl"].to_numpy(), label="Simulation")
if args.calfile:
    ax.plot(df_cal["Freq."].to_numpy(), df_cal["Amplitude"].to_numpy(), label="Theoretical target")

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
