from pyDOE2 import fullfact    # full factorial
from pyDOE2 import ff2n        # 2 levels full factorial 
from pyDOE2 import fracfact    # 2 levels fractional factorial 
from pyDOE2 import pbdesign    # Placket-Burman 
from pyDOE2 import bbdesign    # Box-Behnken 
from pyDOE2 import ccdesign    # Central Composite Design
import json

from Modules.functions import rangesData, fraccionalgenerator, randomizeResult, outputJSONFile

# --------------- MAIN ------------------

# read 'input.json' file 
with open('input.json') as file:
    data = json.load(file)

# extract JSON variables
design = (data['TypeOfDesign'])
factors = (data['Factors'])
reply =(data['Reply'])
randomize =(data['Random'])
resolution =(data['Resolution'])
centresbb =(data['Centresbb'])
centrescc =(data['Centrescc'])
alpha =(data['Alpha'])
face =(data['Face'])

# Number of factors is the factor list length
numOfFactors = len(factors)

# initialise internal list
levels = []
rangeMin = []
rangeMax = []
Names = []

# extract data from the factors
for i in range(numOfFactors):
    
    # choose dict of the factor list and enter in the list of keys
    a = factors[i]
    listOfKeys = list(a.values())
    
    # extract data from list of keys (levels, min, max and name)
    b = listOfKeys[1] 
    levels.append(b)
    c = listOfKeys[2]
    rangeMin.append(c)
    d = listOfKeys[3]
    rangeMax.append(d)
    e = listOfKeys[0]
    Names.append(e)
    i = i + 1

# create a full factorial design
if design == 1:
    print("\n ---------- FULL FACTORIAL ---------")
    result = fullfact(levels)
    designName = "FULL FACTORIAL"

# create a 2 levels full factorial design    
elif design == 2:
    print("\n ---------- 2 LEVELS FULL FACTORIAL ---------")
    result = ff2n(numOfFactors)
    designName = "2 LEVELS FULL FACTORIAL"
 
# create a fraccional factorial design 
elif design == 3:
    print("\n ---------- FRACCIONAL FACTORIAL ---------")
    gen = fraccionalgenerator(numOfFactors, resolution)   
    result = fracfact(gen)
    designName = "FRACCIONAL FACTORIAL"

# create a placket-burman design 
elif design == 4:
    print("\n ---------- PLACKET-BURMAN ---------")
    result = pbdesign(numOfFactors)
    designName = "PLACKET-BURMAN"

# create a box-behnken design     
elif design == 5:
    print("\n ---------- BOX-BEHNKEN ---------")
    result = bbdesign(numOfFactors, centresbb)
    designName = "BOX-BEHNKEN"

# create a central composite design 
elif design == 6:
    print("\n ---------- CENTRAL COMPOSITE DESIGN ---------")
    result = ccdesign(numOfFactors, centrescc, alpha, face)
    designName = "CENTRAL COMPOSITE DESIGN"

else:
    print ("Diseño incorrecto")

# Number of reply
result = result.repeat(reply, 0)

# Randomize results or not
result = randomizeResult (randomize, result) 

# Show information on screen
length = len(result)  
print('\n  Factors: ' + str(numOfFactors)) 
print('  Reply: ' + str(reply)) 
print('  Rolls: ' + str(length)) 
print('  Random: ' + str(randomize) + '\n') 
print (result)
print()

# Show result as a function of the factors ranges
RangesData = rangesData(numOfFactors, rangeMin, rangeMax, Names, design, levels, face, alpha)
        
# create output JSON file
outputJSONFile (result, designName, numOfFactors, RangesData, reply, length, randomize)