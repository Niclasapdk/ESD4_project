from math import sqrt, pi
from matplotlib.ticker import EngFormatter
from colorama import Fore, Style
# Class AB amplifier component calculation script (DC step)

# Enter all values in ISQ

def fmt_unit(var, unit, col=11):
    formatter = EngFormatter(unit=unit)
    num = globals()[var]
    return var.ljust(col, " ") + "= " + formatter(num)

def headline(txt):
    return "\n" + Fore.RED + txt + Style.RESET_ALL

# Choose these constants
Vcc = 30
R_load = 8
P_rms = 15
hfe = 1e3  # Output Stage Darlington HFE
TJ_max = 80  # max transistor temperature
TA = 20  # ambient temperature
print(headline("Chosen values"))
print(fmt_unit("Vcc", "V"))
print(fmt_unit("R_load", "Ohm"))
print(fmt_unit("P_rms", "W RMS"))
print(fmt_unit("hfe", ""))
print(fmt_unit("TJ_max", "degree Celsius"))
print(fmt_unit("TA", "degree Celsius"))

print(headline("Power Calculations"))
I_rms = sqrt(P_rms/R_load)
V_rms = P_rms/I_rms
print(fmt_unit("I_rms", "A"))
print(fmt_unit("V_rms", "V"))

print(headline("Peak values"))
I_peak = sqrt(2) * I_rms
V_peak = sqrt(2) * V_rms
print(fmt_unit("I_peak", "A"))
print(fmt_unit("V_peak", "V"))

# print(headline("Power Calculations"))
# V_peak = sqrt(sqrt(2) * P_rms * R_load)
# P_peak = sqrt(2) * V_load
# I_peak = V_load / R_load
# print(fmt_unit("P_peak", "W"))
# print(fmt_unit("V_peak", "V"))
# print(fmt_unit("I_peak", "A"))
# print(headline("After adding headroom"))
# V_headroom = V_peak + 0.5
# P_rms_headroom = (V_headroom ** 2) / (sqrt(2) * R_load)
# I_headroom = V_headroom / R_load
# P_headroom = sqrt(2) * P_rms_headroom
# print(fmt_unit("P_rms_headroom", "W RMS"))
# print(fmt_unit("P_headroom", "W"))
# print(fmt_unit("V_headroom", "V"))
# print(fmt_unit("I_headroom", "A"))

print(headline("Efficiency Calculations"))
# Pcc = (2/pi) * V_peak * Vcc / R_load
# print(fmt_unit("Pcc", "W"))
Pcc = Vcc * I_rms
print(fmt_unit("Pcc", "W"))
Pd_max = 2 * Vcc**2 / (pi**2 * R_load)
print(fmt_unit("Pd_max", "W"))
efficiency = 100*P_rms / Pcc # in percent
print(fmt_unit("efficiency", "%"))

print(headline("Transistor Calculations"))
I_base = I_peak / hfe
print(fmt_unit("I_base", "A"))

print(headline("Thermal examination (max values)"))
Theta_SA = (TJ_max - TA) / Pd_max
print(fmt_unit("Theta_SA", "degree Celsius / W"))
