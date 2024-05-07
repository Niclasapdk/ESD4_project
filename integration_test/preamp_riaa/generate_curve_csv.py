from cmath import *
import numpy as np
import pandas as pd

def riaa(s):
    T1 = 3180e-6
    T2 = 318e-6
    T3 = 75e-6
    return (T2*s+1)/((T1*s+1)*(T3*s+1))

freqs = np.arange(20, 20e3, 10)
freqs = np.append(freqs, [20e3])
amplitudes = np.empty(0)

for f in freqs:
    H = abs(riaa(1j*2*pi*f))
    Hdb = (20*log10(H)).real + 50
    amplitudes = np.append(amplitudes, Hdb)

df = pd.DataFrame({"Freq.": freqs, "Amplitude": amplitudes})
df.to_csv("calculation_data.csv")
