import CoolProp.CoolProp as CoolP


#coolprop outputs density as kg/m^3

oxidizer = "Oxygen"
fuel = "n-Dodecane" # Coolprop language for kerosine, stand in for RP-1 data as it's not native to Coolprop

#Some of the following are from LimeLight MasterSheet

ambientPressure = 14.7 #psia

tankPressureOx = 214.7 #psia #total estimate rn
tankPressureFuel = 214.7 #psia #total estimate rn

tankSatTempOx = CoolP.PropsSI("T", "P", ambientPressure * 6894.757, "Q", 0, oxidizer) #K

#LOx is stored as saturation temp (in dewers cuz it's cold)
#Fuel is stored heavily subcooled cuz room temp makes it that way lol so that's why the constant
tankTempOx = tankSatTempOx 
tankTempFuel = 293.15 # K

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
pO_Ox = 405.2 #psia
pO_Fuel = 624.1 #psia

#MDots requirements from phoenix
mDot_Ox = 4.47 # kg/s
mDot_Fuel = 2.71 # kg/s

#Volumetric flow rates
q_Ox = (mDot_Ox / densityOx) * 15850.3
q_Fuel = (mDot_Fuel / densityFuel) * 15850.3 #15850.3 is the conversion factor from m^3/s to gal/min

#Design Decisions
npshRatio = 1.2 # available/required

#Ns Calcs
headriseOx = ((144 * (pO_Ox - pI_Ox)) / (densityOx * .062428)) #.062428 is kg/m^3 to lbm/ft^3 converstion factor
headriseFuel = ((144 * (pO_Fuel - pI_Fuel)) / (densityFuel * .062428)) #also called pump-developed head
speed = 20000 #rpm, guess right now try to maximize
nsOx = ((speed * (q_Ox**(.5))) / (headriseOx**(.75)))
nsFuel = ((speed * (q_Fuel**(.5))) / (headriseFuel**(.75)))




print(f"Ns OX: {nsOx}")
print(f"Ns Fuel: {nsFuel}")


