from math import sqrt, pi
from matplotlib.ticker import EngFormatter
# Class AB amplifier component calculation script (DC step)

# Enter all values in ISQ

def fmt_unit(var, unit, col=12):
    formatter = EngFormatter(unit=unit)
    num = globals()[var]
    return var.ljust(col, " ") + "= " + formatter(num)

# Choose these constants
Vcc = 30
R_load = 8
P_load_rms = 15
hfe = 1e3  # Output Stage Darlington HFE
TJ_max = 80  # max transistor temperature
TA = 20  # ambient temperature
print("Chosen values")
print(fmt_unit("Vcc", "V"))
print(fmt_unit("R_load", "Ohm"))
print(fmt_unit("P_load_rms", "W RMS"))
print(fmt_unit("hfe", ""))
print(fmt_unit("TJ_max", "degree Celsius"))
print(fmt_unit("TA", "degree Celsius"))

print("Power Calculations")
P_load = sqrt(2) * P_load_rms
V_load = sqrt(2 * P_load * R_load)
print(fmt_unit("P_load", "W"))
print(fmt_unit("V_load", "V"))
V_load += 0.5  # add 0.5V for headroom
P_load = (V_load ** 2) / (2 * R_load)
I_load = V_load / R_load
print("After adding headroom")
print(fmt_unit("V_load", "V"))
print(fmt_unit("P_load", "W"))
print(fmt_unit("I_load", "A"))

print("Efficiency Calculations")
Pcc = (2/pi) * V_load * Vcc / R_load
print(fmt_unit("Pcc", "W"))
Pd_max = 2 * Vcc**2 / (pi**2 * R_load)
print(fmt_unit("Pd_max", "W"))

print("Transistor Calculations")
I_base = I_load / hfe
print(fmt_unit("I_base", "A"))

print("Thermal examination (max values)")
Theta_SA = (TJ_max - TA) / Pd_max
print(fmt_unit("Theta_SA", "degree Celsius / W"))
