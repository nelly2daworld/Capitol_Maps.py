# Capitol Maps: Find your way around D.C.!
import math
#WHITE HOUSE
latitude = float(input("Insert your latitude: "))
longitude = float(input("Insert your longitude: "))

if(latitude >= 38.902649):
    print("You are north of K St")
elif(latitude < 38.902649):
    print("You are south of K St")
else: 
    print("")
    
if(latitude >= 38.897789):
    print("You are north of the White House")
elif(latitude < 38.897789):
    print("You are south of the White House")
else:
    print("")

if(longitude >= -77.036562):
    print("You are east of the White House")
elif(longitude < -77.036562):
    print("You are west of the White House")
else:
    print("")
    
# DOWNING Hall

if(latitude >= 38.921669):
    print("You are north of Downing Hall")
elif(latitude < 38.921669):
    print("You are south of Downing Hall")
else:
    print("")

if(longitude >= -77.021361):
    print("You are east of Downing Hall")
elif(longitude < -77.021361):
    print("You are west of Downing Hall")
else:
    print("")
    
#DUPONT Circle
if(latitude >= 38.909760):
    print("You are north of Dupont Circle")
elif(latitude < 38.909760):
    print("You are south of Dupont Circle")
else:
    print("")

if(longitude >= -77.043479):
    print("You are east of Dupont Circle")
elif(longitude < -77.043479):
    print("You are west of Dupont Circle")
else:
    print("")
    
#UNION STATION

if(latitude >= 38.897698):
    print("You are north of Union Station")
elif(latitude < 38.897698):
    print("You are south of Union Station")
else:
    print("")

if(longitude >= -77.007200):
    print("You are east of Union Station")
elif(longitude < -77.007200):
    print("You are west of Union Station")
else:
    print("")
    
downing_longitude = -77.021361
downing_latitude = 38.921669
longitude_miles_from_downing = (abs(longitude) -  abs(downing_longitude)) * 53
latitude_miles_from_downing = (abs(latitude) -  abs(downing_latitude)) * 69
sum = math.pow(longitude_miles_from_downing, 2) + math.pow(latitude_miles_from_downing, 2)
num_miles = math.sqrt(sum)
print("You are", round(num_miles , 1), "miles from Downing Hall")
