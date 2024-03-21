# RIAA amplifier

## Design outline:

> RIAA equalisation accuracy:

$\pm 0.1$ dB

> Input impedance:

47k ohms resistor (per standard?)

And a wack capacitor?

> Input voltage:

0.5 to 5.0mVrms

> Output voltage:

30dB at 1kHz $\approx 147.7mVrms$

> RIAA output gain factor to professional audio:

$1.228\:V_{RMS} = 147.7\:mV_{rms}\cdot x \Longleftrightarrow x = 8.3 [\cdot]$

> Output impedance:

Dunno

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

* $T_1 = 2.48\:s$ with freq of f1: $20.02Hz = 1/(T_1 \cdot 2 \cdot \pi)$
    * Infrasonic
* $T_2 = 7.95E-3\:s$ with freq of f2: $20.02Hz = 1/(T_2 \cdot 2 \cdot \pi)$
    * IEC amendment fixed value
* $T_6 = 2.40E-6\:s$ with freq of f6: $2122.1Hz = 1/(T_6 \cdot 2 \cdot \pi)$
    * Sonic

> RIAA output amplifier:

Non inverting amplifier:

Gain(Av) = -$\frac{V_{out}}{V_{in}}=-\frac{R_f}{R_{in}}$

Required known gain: $8.3 = -\frac{R_f}{R_{in}}$

Due to component restrictions $R_f$ is chosen to be 47.5k since $R_5$ is in series with the amplifier the final equation is:

$8.3 = -\frac{R_f}{100k\Omega} \Longleftrightarrow R_{f} = 830k\Omega $


Increase these two resistors with a factor of 10 to increase the impedance of the amplifier.