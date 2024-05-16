#!/bin/sh

cwd=$(pwd)
dirs=(\
    "eq_volctrl/pot_max"\
    "eq_volctrl/pot_min"\
    "eq_volctrl"\
    "power_amplifier"\
    "preamp_class_a"\
    "preamp_opamp"\
    "preamp_riaa"\
    "preamp_riaa_opamp"\
)
titles=(\
    "EQ and VC (max)"\
    "EQ and VC (min)"\
    "EQ and VC"\
    "Power Amplifier"\
    "Class A Preamp"\
    "Opamp Preamp"\
    "RIAA without preamp"\
    "RIAA with preamp"\
)
args=(\
    "--simfile simulation_data.txt"\
    "--simfile simulation_data.txt"\
    ""\
    "--simfile simulation_data.txt"\
    "--simfile simulation_data.txt"\
    "--simfile simulation_data.txt"\
    "--simfile simulation_data.txt --calfile calculation_data.csv"\
    "--simfile simulation_data.txt"\
)
zi_args=(\
    ""\
    ""\
    ""\
    "--logy"\
    ""\
    ""\
    ""\
    ""\
)
length=${#dirs[@]}
for ((i=0; i<length; i++)); do
    dir=${dirs[i]}
    title=${titles[i]}
    arg=${args[i]}
    zi_arg=${zi_args[i]}
    echo "# $title"
    pushd $dir >/dev/null || continue
    echo THD plot
    python3 $cwd/audio_analyser_plot.py --autodetect --quiet --outfile "thd_${dir//\//_}.png" --title "${title} THD" --type "thd" --logx
    echo FreqResp plot
    python3 $cwd/audio_analyser_plot.py --autodetect --quiet --outfile "freqresp_${dir//\//_}.png" --title "${title} Frequency Response" --type "freqresp" --logx $arg
    echo Input Impedance plot
    python3 $cwd/input_impedance_analogdiscovery.py --autodetect --quiet --outfile "zi_${dir//\//_}.png" --title "${title} Input Impedance" --logx $zi_arg
    echo Output Impedance plot
    python3 $cwd/output_impedance_analogdiscovery.py --autodetect --quiet --outfile "zo_${dir//\//_}.png" --title "${title} Output Impedance" --logx
    popd >/dev/null
done
