import pandas as pd
import numpy as np
import sys

quiet = False
save = False

if len(sys.argv) > 1:
    if sys.argv[1] == "export":
        quiet = True
        save = True

figs = [
#("unregulated_powersupply/unregulated_supply_rails.txt", "Unregulated Power Supply", "t"),
#("pa_stability/closed_loop_test.txt", "Closed Loop Test", "f"),
#("pa_stability/closed_loop_transient.txt", "Closed Loop Transient", "t"),
#("pa_stability/closed_loop_with_HF_comp_cap.txt", "Closed loop with HF comp cap", "f"),
#("pa_stability/open_loop_test.txt", "Open loop test", "f"),
#("pa_stability/open_loop_with_miller.txt", "Open loop with miller", "f"),
#("auxPreAmp/ClassAPreAmp.txt", "Class A Preamp Transient Response", "t"),
#("auxPreAmp/opamp_preamp_transient.txt", "Opamp Preamp Transient Response", "t"),
#("equalizer/equaliserMax.txt", "EQ Frequency Response (max)", "f"),
("equalizer/equaliserMin.txt", "EQ Frequency Response (min)", "f"),
("volume_control/volume_control.txt","Volume Control Transient Response","ts")
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

def parse_vout(vout: pd.Series):
    l = len(vout)
    A = np.zeros(l)
    phase = np.zeros(l)
    for i, vstr in enumerate(vout):
        a, p = list(map(float, vstr[1:-1].split(",")))
        A[i] = a
        phase[i] = p
    return A, phase

def gentransient(filename, title, save=False, quiet=False):
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.figure()
    outfile = filename.replace(".txt", ".png")
    df = csv_to_df(filename)
    t = df["time"].to_numpy()
    Vs = df.filter(regex='^V', axis=1)
    sns.set(style="whitegrid")  # You can change the style to "darkgrid", "whitegrid", etc.
    sns.set_palette("pastel")  # Other options: "muted", "bright", "deep", etc.
    sns.set_palette("pastel")  # Other options: "muted", "bright", "deep", etc.
    plt.rc('font', size=14)  # Sets the default font size
    plt.rc('axes', titlesize=14)  # Font size of the axes title
    plt.rc('axes', labelsize=10)  # Font size of the x and y labels
    plt.title(title)
    plt.xlabel("Time [s]")
    plt.ylabel("Voltage [V]")
    for V in Vs.columns:
        plt.plot(t, Vs[V], label=V)
    plt.grid(True)  # Show grid
    plt.tight_layout()
    if save:
        plt.savefig(outfile, dpi=300)  # Save as PNG file with high DPI
    if not quiet:
        plt.show()

def step_csv_to_df_list(filename):
    import tempfile
    out = []
    with open(filename, "rb") as f:
        lines = f.readlines()
    header = lines[0]
    i = 2
    run = 1
    while True:
        if i >= len(lines):
            return out
        cur_lines = [header]
        for j, l in enumerate(lines[i:]):
            i += 1
            if b"Step Information" in l:
                run += 1
                i += 1
                break
            else:
                cur_lines.append(l)
        cur_lines = list(map(lambda b: b.decode(), cur_lines))
        with tempfile.TemporaryFile(mode='w+t') as temp_file:
            temp_file.writelines(cur_lines)
            temp_file.seek(0)  # Go back to the start of the file
            out.append(pd.read_csv(temp_file, sep='\t', header=0))

def gentransientstep(filename, title, save=False, quiet=False):
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.figure()
    outfile = filename.replace(".txt", ".png")
    dfs = step_csv_to_df_list(filename)
    sns.set(style="whitegrid")  # You can change the style to "darkgrid", "whitegrid", etc.
    sns.set_palette("pastel")  # Other options: "muted", "bright", "deep", etc.
    plt.rc('font', size=14)  # Sets the default font size
    plt.rc('axes', titlesize=14)  # Font size of the axes title
    plt.rc('axes', labelsize=10)  # Font size of the x and y labels
    plt.title(title)
    plt.xlabel("Time [s]")
    plt.ylabel("Voltage [V]")
    for df in dfs:
        plt.plot(df["time"], df["V(out)"])
    plt.grid(True)  # Show grid
    plt.tight_layout()
    if save:
        plt.savefig(outfile, dpi=300)  # Save as PNG file with high DPI
    if not quiet:
        plt.show()

def genfreq(filename, title, save=False, quiet=False):
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.figure()
    outfile = filename.replace(".txt", ".png")
    df = csv_to_df(filename)
    f = df["Freq."]
    Adb, phase = parse_vout(df["V(out)"])
    sns.set(style="whitegrid")  # You can change the style to "darkgrid", "whitegrid", etc.
    sns.set_palette("pastel")  # Other options: "muted", "bright", "deep", etc.
    plt.rc('font', size=14)  # Sets the default font size
    plt.rc('axes', titlesize=14)  # Font size of the axes title
    plt.rc('axes', labelsize=10)  # Font size of the x and y labels
    plt.plot(f,phase)
    plt.xscale("log")
    plt.grid(True)
    plt.yticks(np.arange(-30,30,45))
#    fig, (ax1, ax2) = plt.subplots(nrows=2)
#    fig.suptitle(title)
#    plt.xlabel("Frequency [Hz]")
#    ax1.set_ylabel("Amplitude [dB]")
#    ax1.plot(f, Adb)
#    ax2.set_ylabel("Phase [\xb0]")
#    ax2.plot(f, phase)
#    ax1.set_xscale("log")
#    ax2.set_xscale("log")
#    ax2.set_yticks(np.arange(-30, 30, 45))
#    plt.grid(True)  # Show grid
#    plt.tight_layout()
#    fig.tight_layout()
    if save:
        plt.savefig(outfile, dpi=300)  # Save as PNG file with high DPI
    if not quiet:
        plt.show()

def genplot(filename, title, save=False, quiet=False, type="f"):
    print(filename.replace(".txt", ".png"))
    if type == "f":
        genfreq(filename, title, save=save, quiet=quiet)
    if type == "t":
        gentransient(filename, title, save=save, quiet=quiet)
    if type == "ts":
        gentransientstep(filename, title, save=save, quiet=quiet)

for fig in figs:
    genplot(fig[0], fig[1], type=fig[2], save=save, quiet=quiet)
