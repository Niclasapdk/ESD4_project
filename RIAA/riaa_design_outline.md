# RIAA amplifier

## Design outline:

> RIAA equalisation accuracy: 2%

> Input impedance: 47k ohms resistor (per standard?)

> Input voltage: 0.5 to 5.0mVrms

> Output voltage: 30dB at 1kHz $\approx 158.1Vrms$

> Output impedance:

> THD: Unknown

> HF correction pole: yes

> IEC Amendment: yes

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
