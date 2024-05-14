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
y_csv_column = "Trace |Z| (Ohm)"         # TSV file column name of y_axis (case sensitive)
ylabel = "Impedance [Ohm]"           # y axis label
# data filenames
df_L = df_R = None
if args.autodetect:
    found = 0
    for name in os.listdir("."):
        if name.startswith("zi"):
            if name.endswith("l.csv"):
                found += 1
                df_L = read_and_filter_csv_file(name)
            elif name.endswith("r.csv"):
                found += 1
                df_R = read_and_filter_csv_file(name)
else:
    print("fuck")
    exit()

if found > 2:
    print("More than 2 data files in directory")
    exit(1)
if found < 2:
    print("Less than 2 data files in directory")
    exit(1)

f = df_R[x_csv_column]
assert f.all() == df_R[x_csv_column].all(), "frequency step in data not the same"
f = f.to_numpy()

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
ax.plot(f, df_L[y_csv_column].to_numpy(), label="Left Channel")
ax.plot(f, df_R[y_csv_column].to_numpy(), label="Right Channel")

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
