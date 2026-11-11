import CoolProp.CoolProp as CoolP


oxidizer = "Oxygen"
fuel = "n-Dodecane" # Coolprop language for kerosine, stand in for RP-1 data as it's not native to Coolprop

#Some of the following are from LimeLight MasterSheet


tankPressureOx = 200 #psig #total estimate rn
tankPressureFuel = 200 #psig #total estimate rn
#Propellant needs some subcooling so that vapor pressure < local static pressure at pump inlet
subcoolOx = 5 # kelvin (guessing)
subcoolFuel = 5 # kelvin (guessing)

tankSatTempOx = CoolP.PropsSI("T", "P", tankPressureOx * 6894.757, "Q", 0, oxidizer) #K
tankSatTempFuel = CoolP.PropsSI("T", "P", tankPressureFuel * 6894.757, "Q", 0, fuel) #K

tankTempOx = tankSatTempOx - subcoolOx # K
tankTempFuel = tankSatTempFuel - subcoolFuel # K

#Assuming incompressible through the system rn
densityOx = CoolP.PropsSI("D", "P", tankPressureOx * 6894.757, "T", tankTempOx, oxidizer) #kg/m^3
densityFuel = CoolP.PropsSI("D", "P", tankPressureFuel * 6894.757, "T", tankTempFuel, fuel) #kg/m^3

#Inlet Conditions for Pump
#Need to account for frictional losses from tank to pump later
tI_Ox = tankTempOx 
tI_Fuel = tankTempFuel 
pI_Ox = tankPressureOx
pI_Fuel = tankPressureFuel

#Outlet conditions requirements from phoenix
pO_Ox = 390.5 #psig
pO_Fuel = 609.4 #psig

#MDots requirements from phoenix
mDot_Ox = 4.47 # kg/s
mDot_Fuel = 2.71 # kg/s

#Volumetric flow rates
q_Ox = (mDot_Ox / densityOx) * 15850.3
q_Fuel = (mDot_Fuel / densityFuel) * 15850.3 #15850.3 is the conversion factor from m^3/s to gal/min

#Design Decisions
npshRatio = 1.2 # available/required

#Ns Calcs
headriseOx = (pO_Ox - pI_Ox) * 2.31 #2.31 is psi to ft converstion factor
headriseFuel = (pO_Fuel - pI_Fuel) * 2.31 #also called pump-developed head
speed = 20000 #rpm, guess right now try to maximize
nsOx = ((speed * (q_Ox**(.5))) / (headriseOx**(.75)))
nsFuel = ((speed * (q_Fuel**(.5))) / (headriseFuel**(.75)))


print(f"Ns OX: {nsOx}")
print(f"Ns Fuel: {nsFuel}")


