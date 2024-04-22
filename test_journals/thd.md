# THD Test

## Reason

* Affirm the THD of all the subsystems and compliance with the standards.

## Procedure
The test utilized an NI-PCI-4461 audio analyzer and the program "Swept Sine FRF VI."
AO0 is used as a signal generator and AI0, which was connected to the signal generator, measuring the output, and AI1, which measured the output from the element being tested.

1. To set up the test, AO0 is connected with a T-connector to AI0 and the subsystems input.
2. Then the subsystems output is connected to AI1.
4. Under DAQ Configuration it is important to set the output to AO0 in the program, as well as setting the two inputs as AI0 and AI1.
5. Then, sampling frequency is set to 204800 Hz, which is the maximum. (The default of 50 kHz is not sufficient, as it cannot make a proper Fourier transform from the recording.)
6. In Source Settings sweep frequencies is from 20Hz to 20kHz, well below its limits of 92kHz.
7. Then, the amplitude setting is adjusted depending on the subsystem expected output size, so that the output is within the range.
8. Under Processing Settings settle cycles and integration cycles 50 were used; choosing a higher value will not do much for this part.
9. In THD settings maximum settings is chosen to be 5 as well as % for the THD unit.
10. Then, the test is run by pressing start, the results are checked for any clear errors, and the frequency response output is saved as a TSV file.

**Schematic Diagram:**

**Setup Diagram:**


## Results

#### Class A

> Tables/Graphs:

#### Non inverting op-amp

> Tables/Graphs:

#### RIAA

> Tables/Graphs:

#### Equalizer and Volume Control

> Tables/Graphs:

## Conclusion


