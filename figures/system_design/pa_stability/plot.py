import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
import numpy as np
import os
import cmath
import math

figs = [
("closed_loop_test.txt", "Closed Loop Test"),
("closed_loop_transient.txt", "Closed Loop Transient"),
("closed_loop_with_HF_comp_cap.txt", "Closed loop with HF comp cap"),
("open_loop_test.txt", "Open loop test"),
("open_loop_with_miller.txt", "Open loop with miller")
]

def csv_to_df(filename):
    import tempfile
    with open(filename, "rb") as f:
        lines = f.readlines()
    lines = list(map(lambda x: x.replace(b"dB", b""), lines))
    lines = list(map(lambda x: x.replace(b"\xb0", b""), lines))
    lines = list(map(lambda b: b.decode(), lines))
    with tempfile.TemporaryFile(mode='w+t') as temp_file:
        temp_file.writelines(lines)
        temp_file.seek(0)  # Go back to the start of the file
        return pd.read_csv(temp_file, sep='\t', header=0)


def genplot(filename, title):
    outfile = filename.replace(".txt", ".png")
    print(filename, outfile)
    df = csv_to_df(filename)
    print(df)
    exit()
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
    ax1.set_ylabel("Real part [Ohm]")
    ax2.set_ylabel("Imaginary part [Ohm]")
    ax1.set_xscale("log")
    ax2.set_xscale("log")
    ax1.plot(df_L[x_tsv_column].to_numpy(), Ri_L, label="Left Channel")
    ax1.plot(df_R[x_tsv_column].to_numpy(), Ri_R, label="Right Channel")
    ax2.plot(df_L[x_tsv_column].to_numpy(), Xi_L, label="Left Channel")
    ax2.plot(df_R[x_tsv_column].to_numpy(), Xi_R, label="Right Channel")
    # Customize axes and grids for better aesthetics
    plt.grid(True)  # Show grid
    plt.legend(loc='upper left')
    # Use tight layout to automatically adjust subplot params
    plt.tight_layout()
    # Save the plot with high resolution
    plt.savefig(args.outfile, dpi=300)  # Save as PNG file with high DPI
    # Show the plot
    plt.show()

for fig in figs:
    genplot(fig[0], fig[1])
