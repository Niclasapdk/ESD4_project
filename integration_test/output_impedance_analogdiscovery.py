import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import numpy as np
import os
import cmath
import math
import ast

parser = argparse.ArgumentParser()
parser.add_argument("--title", help="Plot title", default="Plot Title")
parser.add_argument("--outfile", help="Generated figure output filename (.png)", default=None)
parser.add_argument("--quiet", help="Do not display generated figure", default=False, action="store_true")
parser.add_argument("--logx", help="Make x-axis logarithmic", default=False, action="store_true")
parser.add_argument("--autodetect", help="Automatically detect filenames", default=False, action="store_true")
args = parser.parse_args()

def read_and_filter_csv_file(filename):
    import tempfile
    with open(filename, "r") as f:
        lines = f.readlines()
    lines = list(filter(lambda s: not s.startswith("#"), lines))
    with tempfile.TemporaryFile(mode='w+t') as temp_file:
        temp_file.writelines(lines)
        temp_file.seek(0)  # Go back to the start of the file
        return pd.read_csv(temp_file, sep=',', header=0)

title = args.title               # Plot title
x_csv_column = "Frequency (Hz)"           # TSV file column name of x_axis (case sensitive)
xlabel = "Frequency [Hz]"        # x axis label
y_csv_column = "Channel 1 Magnitude (dB)"         # TSV file column name of y_axis (case sensitive)
ylabel = "Impedance [Ohm]"           # y axis label
# data filenames
data_L = []
data_R = []
if args.autodetect:
    for name in os.listdir("."):
        if name.startswith("zo"):
            if name.endswith("k.csv"):
                expr = name.split("_")[-1].split(".")[0].replace("k", "e3")
                rseries = int(ast.parse(expr, mode='eval').body.n)
                df = read_and_filter_csv_file(name)
                if name.split("_")[-2] == "l":
                    data_L.append((df, rseries))
                elif name.split("_")[-2] == "r":
                    data_R.append((df, rseries))
                else:
                    print("fuck")
                    exit()
else:
    print("fuck")
    exit()

def zo(fs, a1s, a2s, r1, r2):
    zo = np.zeros(len(fs))
    a1s = 10**(a1s/20)
    a2s = 10**(a2s/20)
    for i, (f, a1, a2) in enumerate(zip(fs, a1s, a2s)):
        # Zs1 = (Zs1/V1) * Vin - Zo
        A = np.asarray([[r1/a1, -1], [r2/a2, -1]])
        y = np.asarray([r1, r2])
        x = np.linalg.solve(A, y)
        zo[i] = x[1]
    return zo

if len(data_L) != 2 or len(data_R) != 2:
    print("Not enough data files")
    exit()

f = data_R[0][0][x_csv_column]
assert f.all() == data_R[1][0][x_csv_column].all(), "frequency step in data not the same"
assert f.all() == data_L[0][0][x_csv_column].all(), "frequency step in data not the same"
assert f.all() == data_L[1][0][x_csv_column].all(), "frequency step in data not the same"
f = f.to_numpy()

# Left channel
a1, r1 = data_L[0]
a1 = a1[y_csv_column].to_numpy()
a2, r2 = data_L[1]
a2 = a2[y_csv_column].to_numpy()
zo_L = zo(f, a1, a2, r1, r2)

# Right channel
a1, r1 = data_R[0]
a1 = a1[y_csv_column].to_numpy()
a2, r2 = data_R[1]
a2 = a2[y_csv_column].to_numpy()
zo_R = zo(f, a1, a2, r1, r2)

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
ax.plot(f, zo_L, label="Left Channel")
ax.plot(f, zo_R, label="Right Channel")

# Customize axes and grids for better aesthetics
plt.grid(True)  # Show grid
plt.legend(loc='best')

# Use tight layout to automatically adjust subplot params
plt.tight_layout()

# Save the plot with high resolution
if args.outfile:
    plt.savefig(args.outfile, dpi=300)  # Save as PNG file with high DPI

# Show the plot
if not args.quiet:
    plt.show()
