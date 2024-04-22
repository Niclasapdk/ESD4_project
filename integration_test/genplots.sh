#!/bin/bash

cwd=$(pwd)
dirs=(\
    "boom_boom"\
    "eq_volctrl/pot_max"\
    "eq_volctrl/pot_mid"\
    "eq_volctrl/pot_min"\
    "power_amplifier"\
    "preamp_class_a"\
    "preamp_opamp"\
    "preamp_riaa"\
    "preamp_riaa_opamp"\
)
titles=(\
    "HiFi Amplifier"\
    "EQ and VC (max)"\
    "EQ and VC (mid)"\
    "EQ and VC (min)"\
    "Power Amplifier"\
    "Class A Preamp"\
    "Opamp Preamp"\
    "RIAA without preamp"\
    "RIAA with preamp"\
)
length=${#dirs[@]}
for ((i=0; i<length; i++)); do
    dir=${dirs[i]}
    title=${titles[i]}
    echo "# $title"
    pushd $dir >/dev/null
    echo THD plot
    python3 $cwd/audio_analyser_plot.py --autodetect --quiet --outfile "thd_${dir//\//_}.png" --title "${title} THD" --type "thd"
    echo FreqResp plot
    python3 $cwd/audio_analyser_plot.py --autodetect --quiet --outfile "freqresp_${dir//\//_}.png" --title "${title} Frequency Response" --type "freqresp"
    popd >/dev/null
done