import CoolProp.CoolProp as CoolP


oxidizer = "Oxygen"
fuel = "n-Dodecane" # Coolprop language for kerosine, stand in for RP-1 data as it's not native to Coolprop

#Some of the following are from LimeLight MasterSheet


tankPressureOx = 100 #psig #total estimate rn
tankPressureFuel = 100 #psig #total estimate rn
#Propellant needs some subcooling so that vapor pressure < local static pressure at pump inlet
subcoolOx = 5 # kelvin (guessing)
subcoolFuel = 5 # kelvin (guessing)

tankSatTempOx = CoolP.PropsSI("T", "P", tankPressureOx * 6894.757, "Q", 0, oxidizer)
tankSatTempFuel = CoolP.PropsSI("T", "P", tankPressureFuel * 6894.757, "Q", 0, fuel)

tankTempOx = tankSatTempOx - subcoolOx # K
tankTempFuel = tankSatTempFuel - subcoolFuel # K

#Assuming incompressible through the system rn
densityOx = CoolP.PropsSI("D", "P", tankPressureOx * 6894.757, "T", tankTempOx, oxidizer)
densityFuel = CoolP.PropsSI("D", "P", tankPressureFuel * 6894.757, "T", tankTempFuel, fuel)

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
q_Ox = mDot_Ox / densityOx
q_Fuel = mDot_Fuel / densityFuel


print(q_Ox)
print(q_Fuel)