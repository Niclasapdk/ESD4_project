# THD and Frequency Response

## Purpose

Measure the THD and frequency response of all subsystems to determine whether they comply with the requirements.

## Equipment

- NI-PCI-4461 audio analyzer
- Analog Discovery 2 (footnote)
- Hameg HM7042 power supply
- DUT

## Procedure

1. Connect the equipment as shown in figure XXX
2. Set the audio analyzer to the following settings:
    - 204.8 kHz sampling rate
    - 20 Hz to 20 kHz frequency sweep in 300 steps
    - Input amplitude for the respective DUT is shown in figure XXX
    - 5th harmonic as maximum THD harmonic
3. Turn on power supply
4. Start frequency sweep
5. Save results as a tsv file
6. Use python script XXX (attachment XXX) to process results

**Setup Diagram**

**Test values table**

## Results

### Class A

### Non inverting op-amp

### RIAA

### Equalizer and Volume Control
