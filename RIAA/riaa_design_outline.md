# RIAA amplifier

## Design outline:

> RIAA equalisation accuracy:

$\pm 0.1$ dB

> Input impedance:

47k ohms resistor (per standard?)

And a capacitor?

> Input voltage:

0.5 to 5.0mVrms

> Output voltage:

30dB at 1kHz $\approx 158.1mVrms$ with 5 mVrms.

> RIAA output gain factor to professional audio:

$1.228\:V_{RMS} = 158.1\:mV_{rms}\cdot x \Longleftrightarrow x = 7.76 [\cdot]$

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

Required known gain: $7.76 = -\frac{R_f}{R_{in}}$

Due to restrictions the $R_{in}$ is chosen to be $147k\Omega$

$7.76 = -\frac{1.21M}{R_1} \Longleftrightarrow R_{1} = 155.9k\Omega $

Since it is in series with with the 2k the final resistor for $R_1$ should be $154k\Omega$

From here the final gain is $\frac{1.21E6}{154E3+2E3} = 7.756$