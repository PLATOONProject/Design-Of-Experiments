from tabulate import tabulate
import json
import random
import numpy 

# ------------ FUNCTIONS -----------------

# menu function
def menu():
    print("\n ----------------------- OPTIONS MENU -------------------- ")
    print (" \n 0- Additional information \n 1- Full Factorial \n 2- 2 levels Full Factorial \n 3- Fraccional Factorial \n 4- Placket-Burman \n 5- Box-Behnken \n 6- Central Composite Design")
    print ('\n -----------------------------------------------------------------')   
    print('\n                         DESIGN CHOICE')
    designOption = int(input(" Enter the design type: "))

    # ensure that the design is between 0 and 6
    while designOption > 6 or designOption < 0:
        print ("\n INCORRECT PARAMETER: Choose between designs 0 and 6")
        designOption = int(input("\n Enter the design type: "))
        
    return designOption
    
# information function    
def info():  
    print (" \n -------------------------- INFORMATION ------------------------ \n")
    print ("SCREENING DESIGNS (more than 6 factors): designed to run on a large number of factors. They are used to determine which factors are important and which can be ruled out. ")
    print (" \n Available screening designs: \n 3- Fraccional Factorial \n 4- Placket-Burman (Fraccional factorial design of de Resolution 3) \n")
    print ("OPTIMIZATION DESIGNS (2 to 5 factors): designed to identify the optimal configuration of critical factors. They are used to examine the main factors and their interactions. ")
    print (" \n Available optimization designs: \n 1- Full Factorial \n 2- 2 levels Full Factorial \n 3- Fraccional Factorial \n 5- Box-Behnken \n 6- Central Composite Design")
    print ()
    print ('-----------------------------------------------------------------')   
    print('\n                          INPUT PARAMETERS \n')
    print('  GENERIC PARAMETERS: \n') 
    print('- TYPE OF DESIGN: between 1 and 6 (int)') 
    print('- Number of factors: (int)')
    print('- Factors: for each of the factors enter the following data: ')
    print('                - Name (String)')
    print('                - Number of levels: only necessary in case of full factorial design (int)')
    print('                - Min and Max: minimum and maximum range of each of the factors (float)')
    print('- Number of reply: how many times you want to repeat each of the rolls of the experiment, in order to avoid distortions by external agents (int)')
    print('- Randomise the order of the rolls?: To balance the effect of external or non-controllable conditions that may influence the results of an experiment (Yes = 1 / No = 0)') 
    print('\n  SPECIFIC PARAMETERS OF EACH DESIGN: \n') 
    print('  - FULL FACTORIAL (1) \n') 
    print('- No further information required \n')
    print('  - FULL FACTORIAL DE 2 NIVELES (2)\n') 
    print('- No further information required \n')
    print('  - FRACCIONAL FACTORIAL (3) \n') 
    print('- Resolution: Indicates the level of confounding allowed in the experiment (int), (Full Resolution = 0)\n')
    
    ResolutionMatrix = [['4', 'Com', 'III'],
             ['8', ' ', 'Com', 'IV', 'III', 'III', 'III'],
             ['16', ' ', ' ', 'Com', 'V', 'IV', 'IV'],
             ['32', ' ', ' ', ' ', 'Com', 'VI', 'IV'],
             ['64', ' ', ' ', ' ', ' ', 'Com', 'VII'],
             ['128', ' ', ' ', ' ', ' ', ' ', 'Com']] 
    
    print ("                          FACTORS")
    print(tabulate(ResolutionMatrix, headers=['Rollls', '2', '3', '4', '5', '6', '7'], tablefmt='fancy_grid', stralign='right',))
    print ()
    print ('      - RESOLUTION III: Confuses main effects with order 2 interactions, only maintains the main effects.')
    print ('      - RESOLUTION IV: Confuses main effects with order 3 interactions and order 2 interactions with order 2 interactions. Maintains main effects with order 2 interactions.')
    print ('      - RESOLUTION V: Confuses main effects with order 4 interactions and order 2 interactions with order 3 interactions. Keeps main effects with order 2 interactions and with order 3 interactions, and also keeps all order 2 interactions between them.')
    print()
    
    print('  - PLACKET-BURMAN (4) \n') 
    print('- No further information required \n')
    print('  - BOX-BEHNKEN (5) \n') 
    print('- Number of central points: (int)\n')
    print('  - CENTRAL COMPOSITE DESIGN (6) \n') 
    print('- Pair of centre points: first number indicates the number of centre points in the factor block and the second number indicates the number of centre points in the star block (int, int)')
    print('- Alpha: "o" ortogonal / "r" rotativ (char)')
    print('- Face: "ccc" circumscribed  / "cci" inscribed / "ccf" on the face of the cube (String) \n')

# initialise factor list
listOfFactors = []

# list of factors function
def listoffactors(num_factors, design_number):
    for i in range(num_factors):
        factor_name = input(" Name of factor number " + str(i+1) + ": ")
        
        # in case of Full Factorial ask for the number of levels of each factor
        if design_number == 1:
            num_levels = int(input(" Number of levels of " + factor_name + ": "))
        else:
            num_levels = 0
        minimun = float(input(" Minimun of factor " + factor_name + ": "))
        maximun = float(input(" Maximun of factor " + factor_name + ": "))
        
        # save in a dict variable 
        dictionary = {'Name' : factor_name, 'NumOfLevels' : num_levels, 'Min' : minimun, 'Max' : maximun }
        
        # enter the dictionary in the factor list
        listOfFactors.append(dictionary)
        i = i + 1
        
    return listOfFactors
     
# integer to bool function
def intToBool(intNum):
    if intNum == 1:
        boolNum = True
    elif intNum == 0:
        boolNum = False
    return boolNum

# create input JSON file function
def createJSONFile (createJson, design, listOfFactors, reply, random_bool, resolution, centresbb, centrescc1, centrescc2, alpha, face):
    # create JSON file
    if createJson == 1:   
    
        # initialise dict to create JSON file
        data = {}
        
        # enter data in the dict
        data ={
            'TypeOfDesign': design,
            'Factors': listOfFactors,
            'Reply': reply,
            'Random': random_bool,
            'Resolution': resolution,
            'Centresbb': centresbb,
            'Centrescc': (centrescc1, centrescc2),
            'Alpha': alpha,
            'Face': face}

        # create 'input.json' file in the same path as this file 'UserInterface.py'
        with open('input.json', 'w') as file:
            json.dump(data, file, indent=4)
            
        print("\n JSON file successfully created!!")

    # not create JSON file     
    elif createJson == 0:
        print("\n Until next time, have a nice day.")

# initialise ranges data list
RangesData = []

# ranges data function
def rangesData(numOfFactors, rangeMin, rangeMax, Names, design, levels, face, alpha):
    for i in range(numOfFactors):
        minimun = rangeMin[i]
        maximun = rangeMax[i]
        name = Names[i]
        totalRange = maximun - minimun
        mediumRange = (maximun - minimun) / 2   
        RangesData.append(name)
    
        if design == 1:    
            print (" Factor " + name + ": Level 0: " + str(minimun), end="")
            RangesData.append(minimun)
            numlevels = levels[i]
            relativeRange = totalRange / (numlevels - 1)
            aux = minimun
            for j in range(numlevels - 2): 
                mediumLevel = aux + relativeRange
                aux = mediumLevel       
                print (", Level " + str(j + 1) + ": " + str(round(aux, 2)), end="")
                RangesData.append(round(aux, 2))
            if numlevels == 2:
                print (", Level 1: " + str(maximun))
            else:
                print (", Level " + str(j + 2) + ": " + str(maximun))
            RangesData.append(maximun)
              
        elif design == 5:    
            central= minimun + (totalRange / 2)
            print (" Factor " + name + ": Min = " + str(minimun) + ", Central Level = " + str(central) + ", Max = " + str(maximun))
            RangesData.append(minimun)
            RangesData.append(central)
            RangesData.append(maximun)
          
        elif design == 6:
            if face == 'ccc':  
                if alpha == 'r':
                    FactorBlockMax = maximun + (mediumRange * 0.68179283) 
                    FactorBlockMin = minimun - (mediumRange * 0.68179283)
                if alpha == 'o':
                    FactorBlockMax = maximun + (mediumRange * 0.87082869) 
                    FactorBlockMin = minimun - (mediumRange * 0.87082869)
                central = minimun + mediumRange 
                print (" Factor " + name + ": FactorBlockMin = " + str(round(FactorBlockMin, 2)) + ", Min = " + str(minimun) + ", Central Level = " + str(central) + ", Max = " + str(maximun) + ", FactorBlockMax = " + str(round(FactorBlockMax, 2)))                
                RangesData.append(round(FactorBlockMin, 2))
                RangesData.append(minimun)
                RangesData.append(central)
                RangesData.append(maximun)  
                RangesData.append(round(FactorBlockMax, 2))
                
            if face == 'cci': 
                if alpha == 'r':
                    StarBlockMax = maximun - (mediumRange * (1 - 0.59460356)) 
                    StarBlockMin = minimun + (mediumRange * (1 - 0.59460356))
                if alpha == 'o':
                    StarBlockMax = maximun - (mediumRange * (1 - 0.53452248)) 
                    StarBlockMin = minimun + (mediumRange * (1 - 0.53452248))
                central = minimun + mediumRange      
                print (" Factor " + name + ": Min = " + str(minimun) + ", StarBlockMin = " + str(round(StarBlockMin, 2)) + ", Central Level = " + str(central) + ", StarBlockMax = " + str(round(StarBlockMax, 2)) + ", Max = " + str(maximun))           
                RangesData.append(minimun)
                RangesData.append(round(StarBlockMin, 2))
                RangesData.append(central)
                RangesData.append(round(StarBlockMax, 2))  
                RangesData.append(maximun)  
                
            if face == 'ccf': 
                central = minimun + mediumRange            
                print (" Factor " + name + ": Min = " + str(minimun) + ", Central Level = " + str(central) + ", Max = " + str(maximun))
                RangesData.append(minimun)
                RangesData.append(central)
                RangesData.append(maximun) 
                                  
        else:     
            print (" Factor " + name + ": Min = " + str(minimun) + ", Max = " + str(maximun))
            RangesData.append(minimun)
            RangesData.append(maximun)

    return RangesData

# fraccional factorial generator function
def fraccionalgenerator(numOfFactors, resolution):
    if (numOfFactors == 3 and resolution == 0):
        gen = 'a b c'  
    elif (numOfFactors == 3 and resolution == 3):
        gen = 'a b ab' 
    elif (numOfFactors == 4 and resolution == 0):
        gen = 'a b c d' 
    elif (numOfFactors == 4 and resolution == 4):
        gen = 'a b c abc' 
    elif (numOfFactors == 5 and resolution == 0):
        gen = 'a b c d e' 
    elif (numOfFactors == 5 and resolution == 5):
        gen = 'a b c d abcd' 
    elif (numOfFactors == 5 and resolution == 3):
        gen = 'a b c ab ac' 
    elif (numOfFactors == 6 and resolution == 0):
        gen = 'a b c d e f' 
    elif (numOfFactors == 6 and resolution == 6):
        gen = 'a b c d e abcde' 
    elif (numOfFactors == 6 and resolution == 4):
        gen = 'a b c d abc abd' 
    elif (numOfFactors == 6 and resolution == 3):
        gen = 'a b c ab ac bd' 
    elif (numOfFactors == 7 and resolution == 0):
        gen = 'a b c d e f g' 
    elif (numOfFactors == 7 and resolution == 7):
        gen = 'a b c d e f abcdef' 
    elif (numOfFactors == 7 and resolution == 4):
        gen = 'a b c d abc abd acd'
    elif (numOfFactors == 7 and resolution == 3):
        gen = 'a b c ab ac bc abc'
    else:
        print('ERROR')   
        
    return gen

# randomize result function
def randomizeResult (randomize, result):
    if randomize == True:
        d = result.tolist()
        list_length = len(d)

        for i in range(list_length):
            random_index = random.randint(0, list_length - 1)
            temporal = d[i]
            d[i] = d[random_index]
            d[random_index] = temporal

        result = numpy.array(d, dtype=numpy.float64)

    return result

# create output JSON file
def outputJSONFile (result, designName, numOfFactors, RangesData, reply, length, randomize):
    output = {}
    result = result.tolist()

    output ={
            'Name': designName,
            'Factors': numOfFactors,
            'RangesData': RangesData,
            'Reply': reply,
            'Rolls': length,
            'Random': randomize,
            'DOE': result}

    # create 'output.json' file in the same path as this file 'DOEProcesing.py'
    with open('output.json', 'w') as file:
        json.dump(output, file, indent=4)
