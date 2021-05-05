import numpy as np
import math
import random
from datetime import datetime, timedelta
from pytz import timezone
import pytz
import matplotlib.pyplot as plt
import os.path
import operator
from dateutil.relativedelta import relativedelta

from astral import geocoder
from astral import location
import astral

import os
import subprocess
import time
from PIL import Image
from numpy import asarray


db = geocoder.database()
# for key in db.keys():
  # print()
locations = geocoder.all_locations(db)
locList = []
usaLocList = {}
for location in locations:
  locList.append(location)
  if location.region == 'USA':
    usaLocList[location.name] = location
    # print(location)
# print(locList[0].name)
CityName = 'Wilmington' #Aberdeen' # 'Honolulu' # 'Nairobi'
City = usaLocList[CityName]

#print(usaLocList)
#print(usaLocList["San Diego"])

#####################################
#setup GLOBALs time and sun calculations
utc = pytz.UTC
# astral = Astral()
# astral.solar_depression = 'civil'
# AllCities = ['Aberdeen', 'Abuja', 'Accra', 'Addis Ababa', 'Adelaide', 'Al Jubail', 'Albany', 'Albuquerque', 'Algiers', 'Amman', 'Amsterdam', 'Anchorage', 'Andorra la Vella', 'Ankara', 'Annapolis', 'Antananarivo', 'Apia', 'Ashgabat', 'Asmara', 'Astana', 'Asuncion', 'Athens', 'Atlanta', 'Augusta', 'Austin', 'Avarua', 'Baghdad', 'Baku', 'Baltimore', 'Bamako', 'Bandar Seri Begawan', 'Bangkok', 'Bangui', 'Banjul', 'Barrow-In-Furness', 'Basse-Terre', 'Basseterre', 'Baton Rouge', 'Beijing', 'Beirut', 'Belfast', 'Belgrade', 'Belmopan', 'Berlin', 'Bern', 'Billings', 'Birmingham', 'Birmingham', 'Bishkek', 'Bismarck', 'Bissau', 'Bloemfontein', 'Bogota', 'Boise', 'Bolton', 'Boston', 'Bradford', 'Brasilia', 'Bratislava', 'Brazzaville', 'Bridgeport', 'Bridgetown', 'Brisbane', 'Bristol', 'Brussels', 'Bucharest', 'Bucuresti', 'Budapest', 'Buenos Aires', 'Buffalo', 'Bujumbura', 'Burlington', 'Cairo', 'Canberra', 'Cape Town', 'Caracas', 'Cardiff', 'Carson City', 'Castries', 'Cayenne', 'Charleston', 'Charlotte', 'Charlotte Amalie', 'Cheyenne', 'Chicago', 'Chisinau', 'Cleveland', 'Columbia', 'Columbus', 'Conakry', 'Concord', 'Copenhagen', 'Cotonou', 'Crawley', 'Dakar', 'Dallas', 'Damascus', 'Dammam', 'Denver', 'Des Moines', 'Detroit', 'Dhaka', 'Dili', 'Djibouti', 'Dodoma', 'Doha', 'Douglas', 'Dover', 'Dublin', 'Dushanbe', 'Edinburgh', 'El Aaiun', 'Fargo', 'Fort-de-France', 'Frankfort', 'Freetown', 'Funafuti', 'Gaborone', 'George Town', 'Georgetown', 'Gibraltar', 'Glasgow', 'Greenwich', 'Guatemala', 'Hanoi', 'Harare', 'Harrisburg', 'Hartford', 'Havana', 'Helena', 'Helsinki', 'Hobart', 'Hong Kong', 'Honiara', 'Honolulu', 'Houston', 'Indianapolis', 'Islamabad', 'Jackson', 'Jacksonville', 'Jakarta', 'Jefferson City', 'Jerusalem', 'Juba', 'Jubail', 'Juneau', 'Kabul', 'Kampala', 'Kansas City', 'Kathmandu', 'Khartoum', 'Kiev', 'Kigali', 'Kingston', 'Kingston', 'Kingstown', 'Kinshasa', 'Koror', 'Kuala Lumpur', 'Kuwait', 'La Paz', 'Lansing', 'Las Vegas', 'Leeds', 'Leicester', 'Libreville', 'Lilongwe', 'Lima', 'Lincoln', 'Lisbon', 'Little Rock', 'Liverpool', 'Ljubljana', 'Lome', 'London', 'Los Angeles', 'Louisville', 'Luanda', 'Lusaka', 'Luxembourg', 'Macau', 'Madinah', 'Madison', 'Madrid', 'Majuro', 'Makkah', 'Malabo', 'Male', 'Mamoudzou', 'Managua', 'Manama', 'Manchester', 'Manchester', 'Manila', 'Maputo', 'Maseru', 'Masqat', 'Mbabane', 'Mecca', 'Medina', 'Memphis', 'Mexico', 'Miami', 'Milwaukee', 'Minneapolis', 'Minsk', 'Mogadishu', 'Monaco', 'Monrovia', 'Montevideo', 'Montgomery', 'Montpelier', 'Moroni', 'Moscow', 'Moskva', 'Mumbai', 'Muscat',  'Nairobi', 'Nashville', 'Nassau', 'Naypyidaw', 'New Delhi', 'New Orleans', 'New York', 'Newark', 'Newcastle', 'Newcastle Upon Time', 'Ngerulmud', 'Niamey', 'Nicosia', 'Norwich', 'Nouakchott', 'Noumea', 'Nuuk', 'Oklahoma City', 'Olympia', 'Omaha', 'Oranjestad', 'Orlando', 'Oslo', 'Ottawa', 'Ouagadougou', 'Oxford',  'Pago Pago', 'Palikir', 'Panama', 'Papeete', 'Paramaribo', 'Paris', 'Perth', 'Philadelphia', 'Phnom Penh', 'Phoenix', 'Pierre', 'Plymouth', 'Podgorica', 'Port Louis', 'Port Moresby', 'Port of Spain', 'Port-Vila', 'Port-au-Prince', 'Portland', 'Portland', 'Porto-Novo', 'Portsmouth', 'Prague', 'Praia', 'Pretoria', 'Pristina', 'Providence', 'Quito', 'Rabat', 'Raleigh', 'Reading', 'Reykjavik', 'Richmond', 'Riga', 'Riyadh', 'Road Town', 'Rome', 'Roseau', 'Sacramento', 'Saint Helier', 'Saint Paul', 'Saint Pierre', 'Saipan', 'Salem', 'Salt Lake City', 'San Diego', 'San Francisco', 'San Jose', 'San Juan', 'San Marino', 'San Salvador', 'Sana', 'Santa Fe', 'Santiago', 'Santo Domingo', 'Sao Tome', 'Sarajevo', 'Seattle', 'Seoul', 'Sheffield', 'Singapore', 'Sioux Falls', 'Skopje', 'Sofia', 'Southampton', 'Springfield', 'Sri Jayawardenapura Kotte', 'St. Peter Port', 'Stanley', 'Stockholm', 'Sucre', 'Suva', 'Swansea', 'Swindon', 'Sydney', 'Taipei', 'Tallahassee', 'Tallinn', 'Tarawa', 'Tashkent', 'Tbilisi', 'Tegucigalpa', 'Tehran', 'Thimphu', 'Tirana', 'Tirane', 'Tokyo', 'Toledo', 'Topeka', 'Torshavn', 'Trenton', 'Tripoli', 'Tunis', 'Ulan Bator', 'Vaduz', 'Valletta', 'Vienna', 'Vientiane', 'Vilnius', 'Virginia Beach', 'W. Indies', 'Warsaw', 'Washington DC', 'Wellington', 'Wichita', 'Willemstad', 'Wilmington', 'Windhoek', 'Wolverhampton', 'Yamoussoukro', 'Yangon', 'Yaounde', 'Yaren', 'Yerevan', 'Zagreb', 'Albany', 'Albuquerque', 'Anchorage', 'Annapolis', 'Atlanta', 'Augusta', 'Austin', 'Baltimore', 'Baton Rouge', 'Billings', 'Birmingham', 'Bismarck', 'Boise', 'Boston', 'Bridgeport', 'Buffalo', 'Burlington', 'Carson City', 'Charleston', 'Charlotte', 'Cheyenne', 'Chicago', 'Cleveland', 'Columbia', 'Columbus', 'Concord', 'Dallas', 'Denver', 'Des Moines', 'Detroit', 'Dover', 'Fargo', 'Frankfort', 'Harrisburg', 'Hartford', 'Helena', 'Honolulu', 'Houston', 'Indianapolis', 'Jackson', 'Jacksonville', 'Jefferson City', 'Juneau', 'Kansas City', 'Lansing', 'Las Vegas', 'Lincoln', 'Little Rock', 'Los Angeles', 'Louisville', 'Madison', 'Manchester', 'Memphis', 'Miami', 'Milwaukee', 'Minneapolis', 'Montgomery', 'Montpelier', 'Nashville', 'New Orleans', 'New York', 'Newark', 'Oklahoma City', 'Olympia', 'Omaha', 'Orlando', 'Philadelphia', 'Phoenix', 'Pierre', 'Portland', 'Portland', 'Providence', 'Raleigh', 'Richmond', 'Sacramento', 'Saint Paul', 'Salem', 'Salt Lake City', 'San Diego', 'San Francisco', 'Santa Fe', 'Seattle', 'Sioux Falls', 'Springfield', 'Tallahassee', 'Toledo', 'Topeka', 'Trenton', 'Virginia Beach', 'Wichita', 'Wilmington']
# CityName = AllCities[10] #pick the city
# City = astral[CityName]
TimeZone = timezone(City.timezone)
DataPath = "./reflector/" + CityName + "/"
# DataPath = 'C:/Users/Nicholas Flann/Dropbox/LEEDtracker/reflector/'+ CityName + '/'
#DataPath = 'C:/Users/nickf/Dropbox/LEEDtracker/reflector/' + CityName + '/'
if not os.path.exists(DataPath):
    os.makedirs(DataPath)

#####################################
# setup GLOBALs design: tower hight in meters, mirror dimensions and list of reflectors
TowerHeight = 100
TowerRadius = 8
DistanceToSun = 10200 # far away so all rays are parallel
DistanceToCamera = 200
MirrorWidth = 10
MirrorHeight = 10
MirrorRadius = 6
PoleHeight = 10 #hight above ground of the mirrors
Size = 400 #size of the domain with tower in center

# make a simple spiral for testing
#MirrorsPer = 16
#Rotations =4
#MirrorPolar = [(math.radians(360*(i%MirrorsPer)/(1.0*MirrorsPer)), 20 + 100.0*i/(MirrorsPer*Rotations)) for i in range(0,MirrorsPer*Rotations)]


#MirrorPolar = [(math.radians(360*(i)/(1.0*10)), 25) for i in range(0,10)]
#MirrorPolar += [(math.radians(360*(i)/(1.0*20)), 40) for i in range(0,20)]
#MirrorPolar += [(math.radians(360*(i)/(1.0*30)), 55) for i in range(0,30)]
#MirrorPolar += [(math.radians(360*(i)/(1.0*40)), 70) for i in range(0,40)]
#MirrorPoints = [(r*math.cos(angle), r*math.sin(angle), 0) for (angle, r) in MirrorPolar]

MirrorPoints = [(round(random.uniform(-100, 100),2),round(random.uniform(-100, 100),2),0) for i in range(100)]
# front of mirror
#MirrorPov = "    texture {pigment {color rgb <1,1,1>} finish {diffuse 0 ambient 0.01 reflection 1.0 phong 1 phong_size 100}}\n"
MirrorPov = "    texture {pigment {color rgb <1,1,1>} finish {diffuse 0.0 ambient 1.0 reflection 0.0 phong 1 phong_size 100}}\n"
# back of mirror which could be customized
BlackPov = "    texture {pigment {color rgb <0,0,0>} finish {diffuse 0 ambient 0.00 reflection 0.0 phong 0 phong_size 0}}\n"
#we put a yellow ball around the sun so we can see it
SunPov = "//sun\nlight_source{ <0,0,0> color rgb<1,1,1>\n   looks_like{ sphere{<0.000, 0.000, 0.000>, 3.000\n       texture{pigment{color Yellow} finish{ambient 0.75 diffuse 2.0}}}}\n translate <%.3f, %.3f, %.3f>}\n"
#just for debugging from the side
#CameraPov = "//camera\ncamera {orthographic angle 60\n   location <100.000, 100.000, 500.000>\n    look_at <0.000, 0.000, 100.000>\n  rotate<80, 0, 0> }\n"
#just for debugging from the top
#CameraPov = "//camera\ncamera {orthographic angle 60\n   location <0.000, 400.000, 00.000>\n    look_at <0.000, 0.000, 000.000>\n  rotate<90, 0, 0> }\n"
# for debugging at the tower top
#CameraPov = "//camera\ncamera {fisheye angle 120\n   location <0.000, 100.000, 00.000>\n    look_at <0.000, 0.000, 000.000>\n  rotate<90, 0, 0> }\n"
CameraPov = "" #camera is defined later
#Draws the primary lightsource (sun) at <x,y,z>...     
def povDrawSun(dayTime):
    # draws the sun
    sunPoint = tuple([i * DistanceToSun for i in sunVector(dayTime)])
    with open(filePath(dayTime), 'a') as fp:
        fp.write(SunPov % sunPoint)   

def povDrawMirror(dayTime, mirrorP):
    # bisect vector
    sunV = sunVector(dayTime)
    towerV = towerVector(mirrorP)
    bisectV = tuple(map(operator.add, sunV, towerV))
    # make the mirror
    half = (MirrorWidth/2, MirrorHeight/2,0)
    cornerLL = tuple(map(operator.sub, bisectV, half))
    cornerUR = tuple(map(operator.add, bisectV, half))
    # location of the mirror center
    centerP = tuple(map(operator.add, mirrorP, (0 , 0, PoleHeight)))
    centerBelowP = tuple(map(operator.add, mirrorP, (0 , 0, PoleHeight-0.1)))
    # DEBUG
    #povDrawVector(dayTime, multiVector(sunV, 20), centerP, color = 'Red')
    #povDrawVector(dayTime, multiVector(towerV, 50), centerP, color = 'Green')
    #povDrawVector(dayTime, multiVector(bisectV, 20), centerP, color = 'Blue')
    # rotations of mirror to face the bisect vector
    #https://groups.google.com/forum/#!topic/comp.graphics.algorithms/vuHUqZnYxtA
    (x, y, z) = unitVector(bisectV)
    azimuth = -1*math.degrees(math.atan2(x,y)) # rotate around the z axis
    elevation = -1*math.degrees(math.acos( z)) # rotate around the x axis
    # top mirror surface
    with open(filePath(dayTime), 'a') as fp:
        fp.write("//mirror\nbox{ <%.3f, %.3f, %.3f>, <%.3f, %.3f, %.3f>\n" % (cornerLL + cornerUR))
        fp.write(MirrorPov)
        fp.write("    rotate <%.3f, %.3f, %.3f>\n" % (elevation,0,0))
        fp.write("    rotate <%.3f, %.3f, %.3f>\n" % (0,0,azimuth))
        fp.write("    translate <%.3f, %.3f, %.3f>}\n" % centerP)
    '''#back of mirror surface (black)
    with open(filePath(dayTime), 'a') as fp:
        fp.write("//mirror\nbox{ <%.3f, %.3f, %.3f>, <%.3f, %.3f, %.3f>\n" % (cornerLL + cornerUR))
        fp.write(BlackPov)
        fp.write("    rotate <%.3f, %.3f, %.3f>\n" % (elevation,0,0))
        fp.write("    rotate <%.3f, %.3f, %.3f>\n" % (0,0,azimuth))
        fp.write("    translate <%.3f, %.3f, %.3f>}\n" % centerBelowP)   
    # draw pole supporting mirror 
    with open(filePath(dayTime), 'a') as fp:
       # fp.write("// tower\nsphere{<%.3f, %.3f, %.3f>, %.3f\n"  % (0, 0, TowerHeight, TowerRadius))
       # fp.write("   texture{pigment{color White} \n   finish{ambient 0.15 diffuse 2.0}}}\n")
       fp.write("//pole\ncylinder{<%.3f, %.3f, %.3f>, <%.3f, %.3f, %.3f>, %.3f\n"  % (mirrorP +  centerP + (0.5,)))
       fp.write("   texture{pigment{color White} \n   finish{ambient 0.15 diffuse 2.0}}}\n")
    '''
        
def povDrawDisk(dayTime, point): #This draws a round mirror
    # bisect vector
    sunV = sunVector(dayTime)
    towerV = towerVector(point)
    bisectV = tuple(map(operator.add, sunV, towerV))
    # location of the mirror center
    center = tuple(map(operator.add, point, (0 , 0, PoleHeight)))
    offset = tuple(map(operator.add, center, unitVector(bisectV)))
    #  DEBUG
    # povDrawVector(dayTime, multiVector(sunV, 20), center, color = 'Red')
    # povDrawVector(dayTime, multiVector(towerV, 50), center, color = 'Green')
    # povDrawVector(dayTime, multiVector(bisectV, 20), center, color = 'Blue')
    # rotations of mirror to face the bisect vector
    #https://groups.google.com/forum/#!topic/comp.graphics.algorithms/vuHUqZnYxtA
    with open(filePath(dayTime), 'a') as fp:
        fp.write("//mirror disk\ncylinder{ <%.3f, %.3f, %.3f>, <%.3f, %.3f, %.3f>, %.3f\n" % (center + offset + (MirrorRadius,)))
        fp.write(MirrorPov + '}\n')
        
def povDrawVector(dayTime, vector, offset, color = 'red'):
    # DEBUG! DRAW EACH VECTOR AS A ROD
    with open(filePath(dayTime), 'a') as fp:
       # fp.write("// tower\nsphere{<%.3f, %.3f, %.3f>, %.3f\n"  % (0, 0, TowerHeight, TowerRadius))
       # fp.write("   texture{pigment{color White} \n   finish{ambient 0.15 diffuse 2.0}}}\n")
       toP = tuple(map(operator.add, vector, offset))
       #print(offset + toP + (1,))
       fp.write("cylinder{<%.3f, %.3f, %.3f>, <%.3f, %.3f, %.3f>, %.3f\n"  % (offset + toP + (1,)))
       fp.write("   texture{pigment{color %s} \n   finish{ambient 0.15 diffuse 2.0}}}\n" % (color,))
        
def povDrawGround(dayTime):
    half = (Size/2, Size/2,0)
    cornerLL = tuple(map(operator.sub, (0,0,0), half))
    cornerUR = tuple(map(operator.add, (0,0,0), half))
    with open(filePath(dayTime), 'a') as fp:
        fp.write("//ground\nbox{ <%.3f, %.3f, %.3f>, <%.3f, %.3f, %.3f>\n" % (cornerLL + cornerUR))
        fp.write("    texture{pigment{color YellowGreen}}}\n")
    
def povDrawTower(dayTime):
    with open(filePath(dayTime), 'a') as fp:
        # draw a white sphere at tower top
       fp.write("// tower\nsphere{<%.3f, %.3f, %.3f>, %.3f\n"  % (0, 0, TowerHeight, TowerRadius))
       fp.write("   texture{pigment{color White} \n   finish{ambient 1.0 diffuse 0.0}}}\n") #low diffuse means external light sources have less of an effect. Origanally ambient 0.15 diffuse 2.0
       #Draw tower cylinder
       fp.write("cylinder{<%.3f, %.3f, %.3f>, <%.3f, %.3f, %.3f>, %.3f\n"  % (0, 0, TowerHeight, 0, 0, 0, 1))
       fp.write("   texture{pigment{color Black} \n   finish{ambient 0.15 diffuse 2.0}}}\n")



def povSetup(dayTime):
    #print(sunVector(dayTime))
    #This is an orthographic camera from the sun's perspective
    sunV = sunVector(dayTime)
    CameraPov = "//camera\ncamera {orthographic right 150 up 150\n   location <%.3f, %.3f, %.3f>\n    look_at <0.000, 0.000, 000.000>\n  rotate<90, 0, 0> }\n"% (sunV[0]*DistanceToCamera, sunV[2]*DistanceToCamera, -sunV[1]*DistanceToCamera)

    # delete old and create new
    if os.path.exists(filePath(dayTime)):
        os.remove(filePath(dayTime)) 
    with open(filePath(dayTime), 'w') as fp:
       fp.write("#include \"colors.inc\"\n#include \"textures.inc\"\n")
       fp.write(CameraPov)
 
def filePath(dayTime):
    return DataPath + dayTime.strftime('%Y_%m_%d_%H_%M') + '.pov'
            
def sunPosition(dayTime):
    obs = City.observer 
    azimuth = astral.sun.azimuth(observer=obs, dateandtime=dayTime)
    elevation = astral.sun.elevation(observer=obs, dateandtime=dayTime)
    return (math.radians(elevation), math.radians(azimuth))
    
def sunVector(dayTime):
    # https://math.stackexchange.com/questions/1150232/finding-the-unit-direction-vector-given-azimuth-and-elevation
    (el, az) = sunPosition(dayTime)
    return (math.sin(az) * math.cos(el), math.cos(az) * math.cos(el), math.sin(el))
    
def towerVector(mirrorPoint):
    # return the vector to the tower from this point
    mirrorPoint = tuple(map(operator.add, mirrorPoint, (0, 0, PoleHeight)))
    # then take the difference between the sun and tower vector
    vector = tuple(map(operator.sub, (0, 0, TowerHeight), mirrorPoint)) #BUG FIXED
    return vectorUnit(vector)
    
def generateSolarCollector(dayTime):
    if (os.path.split(os.getcwd())[-1] == "Wilmington"):
        os.chdir(os.path.abspath(os.path.expanduser('../../')))  # navigate to the target folder with the pov files.
    # generate a pov ray file named for this date and time
    # all mirrors are positioned to reflect the sun to the tower
    povSetup(dayTime) #create file and add includes
    povDrawGround(dayTime) # put in ground
    povDrawTower(dayTime) # tower 
    povDrawSun(dayTime) # sun
    for mirrorP in MirrorPoints:
        #povDrawDisk(dayTime, mirrorP) # alternative round reflector
        povDrawMirror(dayTime, mirrorP)

def oneDaySimulation(dayTime, sampleTime = 60):
    if (os.path.split(os.getcwd())[-1] == "Wilmington"):
        os.chdir(os.path.abspath(os.path.expanduser('../../')))  # navigate to the target folder with the pov files.
    #computes the POVray file sequence for different times this dayTime
    timeZone = timezone(City.timezone)
    obs = City.observer
    sun = astral.sun.sun(observer=obs, date=dayTime)
    # start 30 minutes before sunrise and end 30 minutes after sunset
    sunRise = relativedelta(minutes=-0) + sun['sunrise'].replace(second=0, microsecond=0).astimezone(timeZone)
    sunSet =  relativedelta(minutes=+0) + sun['sunset'].replace(second=0, microsecond=0).astimezone(timeZone)
    # loop through each time sample
    for sample in range(0,24*60//sampleTime):
        dayTime = dayTime + relativedelta(minutes=+sampleTime)
        if (dayTime >= sunRise and dayTime <= sunSet):
            #print "Animation = "+str(dayTime)
            generateSolarCollector(dayTime)
    print("POV files created")

def oneYearSimulation(year = 2019, sampleTime = 60, sampleDays = 30):
    # generate pov sequence for each of these days
    zeroDay = datetime(year, 1, 1, 0, 0, 0, 0, TimeZone)
    allDays =  [zeroDay + timedelta(days=x) for x in range(0, 365, sampleDays)] 
    for dayTime in allDays:
        oneDaySimulation(dayTime, sampleTime)

# utilities
def multiVector(vector, magnitude):
    return tuple([i * magnitude for i in list(vector)])
    
def unitVector(v):
    size = math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2])
    return tuple([i/size for i in list(v)])
    
def vectorUnit(v):
    l=  math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2])
    return tuple([c/l for c in v])
######################################################
#testDay = datetime(2019, 6, 21, 0, 0, 0, 0, TimeZone)
#oneDaySimulation(testDay, 5)


# oneYearSimulation(sampleDays=5);

def createPNGFiles(sampleTime = 60):
    #subprocess.call("cd", shell=True)
    if (not os.path.split(os.getcwd())[-1] == "Wilmington"):
        os.chdir(os.path.abspath(os.path.expanduser('reflector/Wilmington')))  # navigate to the target folder with the pov files.
    istart = 4
    iend = 21
    jstart = 0
    jend = 60
    jinc = sampleTime
    for j in range(jstart, jend, jinc):
        files = []
        for i in range(istart, iend):
            if (os.path.isfile(f"2019_06_21_{i:02d}_{j:02d}.pov") == False): #dont render if the pov file doesnt exist (duh)
                continue
            if (os.path.isfile(f"2019_06_21_{i:02d}_{j:02d}.png") == True): #dont render if the png file already exist (duh)
                continue
            subprocess.Popen(f"start pvengine 2019_06_21_{i:02d}_{j:02d}.pov -d Grayscale_Output=true /exit",shell=True)
            #Old resolution was 512x384, No AA
            #Grayscale_Output=true
            files.append([i,j])
        # wait for the processes to finish
        done = False
        while (not done):
            done = True
            #files = [os.path.isfile(f"2019_06_21_{i:02d}_{j:02d}.png") for i in range(istart, iend)]
            for k in range(len(files)):
                if os.path.isfile(f"2019_06_21_{files[k][0]:02d}_{files[k][1]:02d}.png") == False:
                    done = False
    #time.sleep(1)
    print("PNG files created")

def createSinglePNGFiles(sampleTime):
    if (not os.path.split(os.getcwd())[-1] == "Wilmington"):
        os.chdir(os.path.abspath(os.path.expanduser('reflector/Wilmington')))  # navigate to the target folder with the pov files.
    subprocess.Popen(f"start pvengine 2019_06_21_{sampleTime.hour:02d}_{sampleTime.minute:02d}.pov -d Grayscale_Output=true /exit", shell=True)
    done = False
    while (not done):
        done = True
        if os.path.isfile(f"2019_06_21_{sampleTime.hour:02d}_{sampleTime.minute:02d}.png") == False:
            done = False
    print("PNG files created")

def deleteFiles(sampleTime):
    istart = 4
    iend = 21
    jstart = 0
    jend = 60
    jinc = sampleTime
    for j in range(jstart, jend, jinc):
        for i in range(istart, iend):
            if (os.path.isfile(f"2019_06_21_{i:02d}_{j:02d}.pov") == True): #dont render if the pov file doesnt exist (duh)
                os.remove(f"2019_06_21_{i:02d}_{j:02d}.pov")
            if (os.path.isfile(f"2019_06_21_{i:02d}_{j:02d}.png") == True): #dont render if the png file already exist (duh)
                os.remove(f"2019_06_21_{i:02d}_{j:02d}.png")

def deleteFilesSingle(sampleTime):
    result = None
    while result is None:
        try:
            if (os.path.isfile(f"2019_06_21_{sampleTime.hour:02d}_{sampleTime.minute:02d}.pov") == True):  # dont render if the pov file doesnt exist (duh)
                os.remove(f"2019_06_21_{sampleTime.hour:02d}_{sampleTime.minute:02d}.pov")
            if (os.path.isfile(f"2019_06_21_{sampleTime.hour:02d}_{sampleTime.minute:02d}.png") == True):  # dont render if the png file already exist (duh)
                os.remove(f"2019_06_21_{sampleTime.hour:02d}_{sampleTime.minute:02d}.png")
            result = True
        except:
            pass

def computeScore(sampleTime = 60):
    if (not os.path.split(os.getcwd())[-1] == "Wilmington"):
        os.chdir(os.path.abspath(os.path.expanduser('reflector/Wilmington')))  # navigate to the target folder with the pov files.
    istart = 4
    iend = 21
    jstart = 0
    jend = 60
    jinc = sampleTime
    totalPixels = 0;
    framesun = []
    for m in range(jstart, jend, jinc):
        for n in range(istart, iend):
            if (os.path.isfile(f"2019_06_21_{n:02d}_{m:02d}.png") == False):
                continue
            # load the image
            image = Image.open(f'2019_06_21_{n:02d}_{m:02d}.png')
            # convert image to numpy array
            data = asarray(image)
            totalPixels = len(data) * len(data[0])
            sunPixels = 0
            for i in range(len(data)):
                for j in range(len(data[0])):
                    #k = 0;  # k is the red channel
                    #if (data[i][j][k] > 240):
                    if (data[i][j] == 65535): #Now that I render the images in grayscale, no need to access "red channel"
                        sunPixels += 1
            framesun.append(sunPixels)

    finalScore = 0
    for i in range(len(framesun)):
        finalScore += framesun[i]
    finalScore /= (totalPixels * len(framesun))
    print("Final Score computed: " + str(finalScore))
    return finalScore

def computeScoreSingle(sampleTime):
    result = None
    while result is None:
        try:
            if (not os.path.split(os.getcwd())[-1] == "Wilmington"):
                os.chdir(os.path.abspath(os.path.expanduser('reflector/Wilmington')))  # navigate to the target folder with the pov files.
            if (os.path.isfile(f"2019_06_21_{sampleTime.hour:02d}_{sampleTime.minute:02d}.png") == True):
                result = True
        except:
            pass
    time.sleep(1.0)

    # load the image

    image = Image.open(f"2019_06_21_{sampleTime.hour:02d}_{sampleTime.minute:02d}.png")
    data = asarray(image)
    totalPixels = len(data) * len(data[0])
    sunPixels = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            # k = 0;  # k is the red channel
            # if (data[i][j][k] > 240):
            if (data[i][j] == 65535):  # Now that I render the images in grayscale, no need to access "red channel"
                sunPixels += 1


    sunPixels /= (totalPixels)
    print("Final Score computed: " + str(sunPixels))
    return sunPixels




def saveCurrentProgress(DNAStrand):
    with open("generationProgress.txt", 'a') as fp:
        for i in range(len(DNAStrand)):
            fp.write(str(DNAStrand[i][0])+","+str(DNAStrand[i][1])+",")
        fp.write("\n")
        fp.close()



def saveChildren(DNAStrands,DNAScores):
    if (os.path.split(os.getcwd())[-1] == "Wilmington"):
        os.chdir(os.path.abspath(os.path.expanduser('../../')))  # navigate to the target folder with the pov files.
    with open("generationProgress.txt", 'a') as fp:
        fp.write("generation \n")
    for i in range(len(DNAStrands)):
        saveCurrentProgress(DNAStrands[i])
    with open("generationProgress.txt", 'a') as fp:
        fp.write("Results ")
        for i in range(len(DNAScores)):
            fp.write(str(DNAScores[i]) + " ")
        fp.write("\n")




def getRecentChildren():
    if (os.path.split(os.getcwd())[-1] == "Wilmington"):
        os.chdir(os.path.abspath(os.path.expanduser('../../')))

    with open("generationProgress.txt", 'r') as fp:
        childrenList = []
        latestGenPos = 0
        line = " "
        # find the last generation in the file
        while(line != ""):
            line = fp.readline()
            if (line.startswith("generation")):
                latestGenPos = fp.tell()
        fp.seek(latestGenPos)
        line = " "
        while(line != ""):
            line = fp.readline()
            if (line.startswith("generation") or line == "" or line.startswith("Results")):
                pass
            else:
                testArray = line.split(",")
                testArray.pop() #Removes the last element in the list.
                desiredArray = [(float(testArray[i]),float(testArray[i+1]),0) for i in range(0,len(testArray),2)]
                childrenList.append(desiredArray)
        fp.close()
        return childrenList

def getRecentChildrenScores():
    if (os.path.split(os.getcwd())[-1] == "Wilmington"):
        os.chdir(os.path.abspath(os.path.expanduser('../../')))

    with open("generationProgress.txt", 'r') as fp:
        line = " "
        latestResults = 0
        # find the last generation in the file
        while(line != ""):
            line = fp.readline()
            if (line.startswith("Results")):
                latestResults = line
        latestResults = latestResults[8:]
        childrenScoresList = [float(item) for item in latestResults.split()]
        return childrenScoresList

def getAllChildrenScores():
    if (os.path.split(os.getcwd())[-1] == "Wilmington"):
        os.chdir(os.path.abspath(os.path.expanduser('../../')))

    with open("generationProgress.txt", 'r') as fp:
        line = " "
        results = []
        latestResults = ""
        # find the last generation in the file
        while(line != ""):
            line = fp.readline()
            if (line.startswith("Results")):
                latestResults = line
                latestResults = latestResults[8:]
                #results.append([float(item) for item in latestResults.split()])
                results.append(float(latestResults.split()[-1]))
        return results

def saveRecentChildrenScores(scores):
    if (os.path.split(os.getcwd())[-1] == "Wilmington"):
        os.chdir(os.path.abspath(os.path.expanduser('../../')))  # navigate to the target folder with the pov files.
    latestGenPos = 0
    with open("generationProgress.txt", 'r+') as fp:
        line = " "
        # find the last generation in the file
        while(line != ""):
            line = fp.readline()
            #if (line.startswith("generation")):
        latestGenPos = fp.tell()
        fp.seek(latestGenPos-0)
        fp.write("Results ")
        for i in range(len(scores)):
            fp.write(f"{scores[i]} ")
        fp.write("\n")
        fp.close()

#def SimulateGeneration():

# import glob
# povFiles=  glob.glob('*.pov')
testDay = datetime(2019, 6, 21, 8, 0, 0, 0, TimeZone)





childrenScores = []
def fitnessFunction(DNAstrandId):
    #Assume that childrenScores has already been computed
    return childrenScores[DNAstrandId]

#The below 2 function randomly mixes the two sets of DNA to create a "child"
def crossoverFunction(childDNA,parentDNA1, parentDNA2, start):
    finish = (start+7) % len(parentDNA1)
    i = start
    while (i != finish):
        #index = parentDNA1.index(parentDNA2[i])
        #childDNA[i], childDNA[index] = childDNA[index],childDNA[i]
        childDNA[i] = parentDNA2[i]
        i = (i+1) % len(parentDNA1)

def crossoverMain(DNA1,DNA2):
    childDNA = [DNA1[i] for i in range(len(DNA1))]
    num1 = 0
    num2 = 0
    while(abs(num1 - num2) < 15):
        num1 = random.randint(0, len(DNA1)-1)
        num2 = random.randint(0, len(DNA1)-1)
    i = num1
    while (i != num2):
        # index = parentDNA1.index(parentDNA2[i])
        # childDNA[i], childDNA[index] = childDNA[index],childDNA[i]
        childDNA[i] = DNA2[i]
        i = (i + 1) % len(DNA2)

    return childDNA

def generateRandomPoint(radius):
    randRadius = random.uniform(0, radius ** 2) ** 0.5
    randAngle = random.uniform(0, 2*math.pi)
    return (round(randRadius*math.cos(randAngle),2), round(randRadius*math.sin(randAngle),2), 0)

def mutate(DNAstrand):
    newDNAStrand = DNAstrand.copy()
    for i in range(1):
        num1 = random.randint(0, len(DNAstrand)-1)
        #newDNAStrand[num1] = (round(random.uniform(-100, 100),2),round(random.uniform(-100, 100),2),0)
        newDNAStrand[num1] = generateRandomPoint(60)
    return newDNAStrand

def mutateAnealing(DNAstrand):
    newDNAStrand = DNAstrand.copy()
    for i in range(1):
        num1 = random.randint(0, len(DNAstrand) - 1)
        # newDNAStrand[num1] = (round(random.uniform(-100, 100),2),round(random.uniform(-100, 100),2),0)
        smallX = round(random.uniform(0, 2),2)
        smallY = round(random.uniform(0, 2),2)
        newDNAStrand[num1] = (newDNAStrand[num1][0]+smallX,newDNAStrand[num1][1]+smallY,0)
    return newDNAStrand

def computeFitnessScores(DNAList,length):
    global MirrorPoints
    childrenScores = [0 for i in range(length)]
    for i in range(length):
        sampleTime = 60
        print("Begin " + str(i) + " ",end="")
        MirrorPoints = DNAList[i]

        testDay = datetime(2019, 6, 21, 15, 0, 0, 0, TimeZone)

        generateSolarCollector(testDay)
        createSinglePNGFiles(testDay)
        childrenScores[i] = computeScoreSingle(testDay)
        deleteFilesSingle(testDay)
        #oneDaySimulation(testDay, sampleTime)
        #createSinglePNGFiles(sampleTime)
        #childrenScores[i] = computeScore(sampleTime)
        #deleteFiles(sampleTime)
    return childrenScores

DNALength = 100 #There is 100 Solar Panels for each "child"
parentpopulation = 12 #each generation will save the top 12 children, to be the next parents
childPopulation = 30 #each generation will populate 30 children
generations = 100

#I used this cite to guess https://www.engineeringtoolbox.com/smaller-circles-in-larger-circle-d_1849.html
#tempDNAList = [[(round(random.uniform(-100, 100),2),round(random.uniform(-100, 100),2),0) for i in range(100)] for j in range(12)]
#tempDNAList = [[generateRandomPoint(60) for i in range(90)] for j in range(12)]
#saveChildren(tempDNAList,[0,0,0,0,0,0,0,0,0,0,0,0])

#This is my old version, when I used cross-over
while (False):
    print("Starting new Generation")
    parents = getRecentChildren()  # Get the most recent 10 parents saved in the file
    parentsScores = getRecentChildrenScores()
    children = [0 for i in range(childPopulation + parentpopulation)]


    #randomly cross-over the DNA strands to form next generation
    #for i in range(childPopulation):
    #    children[i] = crossoverMain(parents[random.randint(0,parentpopulation-1)], parents[random.randint(0,parentpopulation-1)])

    #I also include the parents in the next generation
    #for i in range(parentpopulation):
    #    children[i+childPopulation] = parents[i]

    #mutate the DNA a little bit
    for i in range(childPopulation):
        #I mutate about about 3/4 of the time
        #if (random.randint(0, 3) >= 1):
        mutate(children[i])


    #fitnessResults = [i for i in range(childPopulation)]
    #for i in range(childPopulation):
    #    fitnessResults[i] = fitnessFunction(DNAListNew[i])

    #Compute fitness results
    childrenScores = computeFitnessScores(children,childPopulation)
    childrenScores = childrenScores + parentsScores

    print(childrenScores)
    for i in children:
        print(str(i[0]) + " | ", end="")
    print()


    #select the best survivors. The best survivors will be in the BACK of Z
    Z = [x for _,x in sorted(zip(childrenScores,children))]
    childrenScores = sorted(childrenScores, key=float)

    print(childrenScores)
    for i in Z:
        print(str(i[0]) + " | ", end="")
    print()

    # Save the best children into the file for the next generation
    print(Z)
    print(childrenScores)
    saveChildren(Z[-parentpopulation:],childrenScores[-parentpopulation:])
    #saveRecentChildrenScores(childrenScores)
    print("Finished saving a generation")

def plotTheGenerations():
    results = getAllChildrenScores()
    from matplotlib import pyplot as plt
    plt.plot([i for i in range(len(results))], results)
    plt.xlabel("Generations")
    plt.ylabel("efficiency")
    plt.show()

#plotTheGenerations()

#This is my new version, when I solely rely on mutation
while (True):
    print("Starting new Generation")
    parents = getRecentChildren()  # Get the most recent 10 parents saved in the file
    parentsScores = getRecentChildrenScores()
    children = [0 for i in range(childPopulation)]

    #mutate the DNA a little bit
    for i in range(childPopulation):
        #I mutate about about 3/4 of the time
        #if (random.randint(0, 3) >= 1):
        children[i] = mutateAnealing(parents[random.randint(0, parentpopulation-1)])

    children = children + parents

    #fitnessResults = [i for i in range(childPopulation)]
    #for i in range(childPopulation):
    #    fitnessResults[i] = fitnessFunction(DNAListNew[i])

    #Compute fitness results
    childrenScores = computeFitnessScores(children,childPopulation)
    childrenScores = childrenScores + parentsScores
    #select the best survivors. The best survivors will be in the BACK of Z
    print(childrenScores)
    print(children)
    Z = [x for _,x in sorted(zip(childrenScores,children))]
    childrenScores = sorted(childrenScores, key=float)

    # Save the best children into the file for the next generation
    print(Z)
    print(childrenScores)
    saveChildren(Z[-parentpopulation:],childrenScores[-parentpopulation:])
    #saveRecentChildrenScores(childrenScores)
    print("Finished saving a generation")

def visualizeBestChild():
    global MirrorPoints
    parents = getRecentChildren()
    MirrorPoints = parents[-1]
    testDay = datetime(2019, 6, 21, 15, 0, 0, 0, TimeZone)
    generateSolarCollector(testDay)
    createSinglePNGFiles(testDay)

visualizeBestChild()
plotTheGenerations()