# RIAA amplifier

## Design outline:

> RIAA equalisation accuracy:

2%

> Input impedance:

47k ohms resistor (per standard?)

> Input voltage:

0.5 to 5.0mVrms

> Output voltage:

30dB at 1kHz $\approx 158.1Vrms$

> RIAA output gain factor to professional audio:

$1.228\:V_{RMS} = 158.1\:mV_{rms}\cdot x \Longleftrightarrow x = 7.767 [\cdot]$

> Output impedance:

> THD: Unknown

> HF correction pole:

yes

> IEC Amendment:

yes

## Calculations:

>RIAA time constants:

* $T_3 = 3180E-6\:s$ with freq of f3: $50.05Hz = 1/(T_3 \cdot 2 \cdot \pi)$ - Fixed value
* $T_4 = 318E-6\:s$ with freq of f4: $500.5Hz = 1/(T_4 \cdot 2 \cdot \pi)$ - Fixed value
* $T_5 = 75E-6\:s$ with freq of f5: $2122.1Hz = 1/(T_5 \cdot 2 \cdot \pi)$ - Fixed value

>The 3 additional time constants for infrasonic and sonic filtering and IEC amementment:

* $T_1 = 7950E-6\:s$ with freq of f1: $20.02Hz = 1/(T_1 \cdot 2 \cdot \pi)$
    * Infrasonic
* $T_2 = 7950E-6\:s$ with freq of f2: $20.02Hz = 1/(T_2 \cdot 2 \cdot \pi)$
    * IEC amendment fixed value
* $T_6 = 75E-6\:s$ with freq of f6: $2122.1Hz = 1/(T_6 \cdot 2 \cdot \pi)$
    * Sonic

> RIAA output amplifier:

Non inverting amplifier:

Gain(Av) = $\frac{V_{out}}{V_{in}}=-\frac{R_f}{R_{in}}$

Required known gain: $7.767 = -\frac{R_f}{R_{in}}$

Due to component restrictions $R_f$ is chosen to be 47.5k since $R_5$ is in series with the amplifier the final equation is:

$7.767 = -\frac{47.7k}{2k\: + \: x} \Longleftrightarrow x = 4.4k\Omega $
