##########################################
#           Delta-V Calculator           #
#        Creator: Matthew Toadvine       #
#          Last Edit: 3/15/2017          #
##########################################

import math
import sys

###### SET PLANETARY VARIABLES ############

### KERBOL ###
kbl_gp = 1172332800000000000 # m^3/s^2

### MOHO ###
moh_sma = 5263138304 # meters
moh_gp = 168609380000 # m^3/s^2
moh_rad = 250000 # meters

### EVE ###
eve_sma = 9832684544 # meters
eve_gp = 8171730200000 # m^3/s^2
eve_rad = 700000 # meters

### KERBIN ###
kbn_sma = 13599840256 # meters
kbn_gp = 3531600000000 # m^3/s^2
kbn_rad = 600000 # meters

### DUNA ###
dna_sma = 20726155264 # meters
dna_gp = 301363210000 # m^3/s^2
dna_rad = 320000 # meters

### DRES ###
drs_sma = 40839348203 # meters
drs_gp = 21484489000 # m^3/s^2
drs_rad = 138000 # meters

### JOOL ###
jol_sma = 68773560320 # meters
jol_gp = 282528000000000 # m^3/s^2
jol_rad = 6000000 # meters

### EELOO ###
elo_sma = 90118820000 # meters
elo_gp = 74410815000 # m^3/s^2
elo_rad = 210000 # meters


###### DO THE MATHS #######################

print(" ")
print("*---------*---*")
print("|  MOHO   | 0 |")
print("|---------|---|")
print("|  EVE    | 1 |")
print("|---------|---|")
print("|  KERBIN | 2 |")
print("|---------|---|")
print("|  DUNA   | 3 |")
print("|---------|---|")
print("|  DRES   | 4 |")
print("|---------|---|")
print("|  JOOL   | 5 |")
print("|---------|---|")
print("|  EELOO  | 6 |")
print("*---------*---*")
print(" ")

### JUST SOME ARRAYS ###
planet_sma = [moh_sma, eve_sma, kbn_sma, dna_sma, drs_sma, jol_sma, elo_sma]
planet_gp = [moh_gp, eve_gp, kbn_gp, dna_gp, drs_gp, jol_gp, elo_gp]
planet_rad = [moh_rad, eve_rad, kbn_rad, dna_rad, drs_rad, jol_rad, elo_rad]

### GATHER INPUT DATA ###
origin = int(input("Enter number of planet of origin: "))
orbit1 = int(input("Enter the size of initial parking orbit: "))
dest = int(input("Enter number of destination planet: "))
orbit2 = int(input("Enter desired parking orbit at destination: "))
print(" ")

### SET MATH VARIABLES ###
gp1 = planet_gp[origin]
gp2 = planet_gp[dest]
r1 = planet_sma[origin]
r2 = planet_sma[dest]
a1 = planet_rad[origin] - orbit1
a2 = planet_rad[dest] - orbit2

### OK....NOW DO MATHS ###

## FIRST...THE DV ##
vt1 = math.sqrt((2*kbl_gp*r2)/(r1*(r1+r2))) - math.sqrt(kbl_gp/r1)
veject = math.sqrt((vt1**2)+(2*gp1/a1)) - math.sqrt(gp1/a1)
vins = math.sqrt((2*kbl_gp*r1)/(r2*(r1+r2))) - math.sqrt(kbl_gp/r2)
vinsert = math.sqrt((vins**2)+(2*gp2/a2)) - math.sqrt(gp2/a2)
vtotes = veject + vinsert

## NOW...THE ANGLES! ##
th = 3.14159*math.sqrt((r1+r2)**3/(8*kbl_gp))
theta = math.sqrt(kbl_gp/r2)*(th/r2)*(180/3.14159)
phase = 180 - theta

while phase <= -360:
	phase = phase + 360

print("*------------------------*---------")
print("| Planetary Phase Angle  | %.2f " % phase)
print("|------------------------|---------")
print("| Total Delta V Required | %.2f " % vtotes)
print("*------------------------*---------")
