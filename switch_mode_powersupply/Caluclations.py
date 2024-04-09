# https://www.ti.com/lit/an/slva477b/slva477b.pdf?ts=1711517988809
# The bigger the coil the higher the henry the more max power can be drawn from the switching regulator

import math
mega = math.pow(10,6)
kilo = math.pow(10,3)
milli = math.pow(10,-3)
micro = math.pow(10,-6)
nano = math.pow(10,-9)

Vout = 5
Vin = 30
Imax = 200*milli
efficience = 0.60

max_duty_cycle = Vout/(Vin*efficience)

print(f"max duty cycle: {max_duty_cycle*100}%")

# inductor ripple is guestimated to be between 20 and 40 % so we will use 30%

inductor_ripple_current = 0.3 * Imax

# to find inductor size we have to know max frequency of the swicth
rise_time = 74*nano+7.1*nano
fall_time = 29*nano+20*nano

max_fq = 1/(rise_time+fall_time) 
print(f"max switching frequency {max_fq}Hz")

#define the wanted switching speed, this should just be below the max
min_fq = 50*kilo#max_fq - 500*kilo

print(f"fq: {min_fq}Hz")

# inductor size
L =  (Vout*(Vin-Vout))/(inductor_ripple_current*min_fq*Vin)
print(f"coil: {L/micro}uH")


# use schottky diodes, cause this shit is going to go fast!

# avrage forward current on the diode
diode_current = Imax *(1- max_duty_cycle)
print(f"forward current for diode: {diode_current}A")

# i assume you are using a silicon diode
diode_dissepation = diode_current*0.7
print(f"diode power dissepation: {diode_dissepation}W")

# the cap should be low series resistance (such as a ceramic cap) as this reduces output voltage ripple

output_voltage_ripple = 0.1
C = inductor_ripple_current/(8*output_voltage_ripple*min_fq)
print(f"capacitor: {C/nano}nF")

