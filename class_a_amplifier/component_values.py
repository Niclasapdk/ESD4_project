# Class A amplifier component calculation script (DC step)

# Enter all values in ISQ

# Choose these constants
Vcc = 10
Iq = 10e-3  # quiescent collector current (10% of max collector current)
hfe = 270  # transistor current amplification
IC = 5e-3
V_activation = 0.7  # transistor "turn on" voltage

# Calculate load resistor RL
RL = Vcc / Iq

# Calculate emitter voltage VE
VE = 0.12 * Vcc  # should be about 10% to 15% of Vcc

# Assume emitter current IE approximately equal to collector current IC
IE = IC

# Calculate emitter resistor RE
RE = VE / IE

# Calculate base current IB
IB = IC / hfe

# Calculate base voltage VB
VB = VE + V_activation

# Calculate bias current through R1 and R2
Ibias = 10 * IB

# Calculate R1 and R2
R1 = (Vcc - VB) / Ibias
R2 = VB / Ibias

# Display values
print("Class A amplifier values", end="\n\n")
print("Chosen values:")
print(f"Vcc\t= {round(Vcc, 3)} V")
print(f"Iq\t= {round(Iq*1e3, 3)} mA")
print(f"hfe\t= {round(hfe, 3)}")
print(f"IC\t= {round(IC*1e3, 3)} mA")
print()
print("Calculated values:")
print("Voltages and currents")
print(f"VE\t= {round(VE, 3)} V")
print(f"IE\t= {round(IE*1e3, 3)} mA")
print(f"VB\t= {round(VB, 3)} V")
print(f"IB\t= {round(IB*1e6, 3)} uA")
print(f"Ibias\t= {round(Ibias*1e6, 3)} uA")
print("Components")
print(f"RL\t= {round(RL*1e-3, 3)} kOhm")
print(f"RE\t= {round(RE, 3)} Ohm")
print(f"R1\t= {round(R1*1e-3, 3)} kOhm")
print(f"R2\t= {round(R2*1e-3, 3)} kOhm")
