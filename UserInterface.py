from Modules.functions import menu, info, listoffactors, intToBool, createJSONFile

# --------------- MAIN ------------------

# ask for the design number via menu function
design = menu()

# as long as the design equals 0, provide information and reorder design
while design == 0:
    info()
    design = menu()

# ask for de number of factors
factors = int(input(" Enter the number of factors: "))

# for the BB design, the min number of factors is 3
if design == 5 and factors == 2:
    print('\n The minimum number of factors is 3')
    factors = 3
    
# for the Fract Fact design, the min number of factors is 3
if design == 3 and factors == 2:
    print('\n The minimum number of factors is 3')
    factors = 3

# for de number of factors, ask for the name, the min range and the max range and save this info in factor list
listOfFactors = listoffactors(factors, design, )
  
# ask for the number of reply
reply = int(input(" Number of reply: "))

# do you want to randomise the results?
random = int(input(" Display results randomly? (1/0): "))

# ensure that the random option is correct
while random < 0 or random > 1:
    print ("\n INCORRECT PARAMETER: Enter a 1 (Yes) or a 0 (No)")
    random = int(input(" Display results randomly? (1/0): "))

# convert random variable from integer to bool
random_bool = intToBool(random)

# inizialise design-specific variables in a generic way
resolution = 0
centresbb = 0
centrescc1 = centrescc2 = 0
alpha = "o"
face = "ccc"

# for each design enter specific input parameters  
if design == 1:
    print ("\n Parameters correctly entered")
    
elif design == 2:
    print ("\n Parameters correctly entered")
    
elif design == 3:
    if factors == 3:
        resolution = int(input(" Desired resolution: "))
        
        # ensure that the resolution option is correct
        while resolution != 0 and resolution != 3:
            print ("\n INCORRECT PARAMETER: Full (0) or Resolution III (3)")
            resolution = int(input(" Desired resolution: "))
    print ("\n Parameters correctly entered")
    
elif design == 4:
    print ("\n Parameters correctly entered")
    
elif design == 5:
    centresbb = int(input(" Número of central points: "))
    print ("\n Parameters correctly entered")
    
elif design == 6:
    centrescc1 = int(input(" Number of central points of the factorial block: "))
    centrescc2 = int(input(" Number of central points of the star block: "))
    alpha = input(" Alpha: ")

    # ensure that the alpha option is correct
    while alpha != "o" and alpha != "r":
        print ("\n INCORRECT PARAMETER: Enter 'o' or 'r'")
        alpha = input(" Alpha: ")
    
    face = input(" Face: ")
    
    # ensure that the face option is correct
    while face != "ccc" and face != "cci" and face != "ccf":
        print ("\n INCORRECT PARAMETER: Enter 'ccc', 'cci' or 'ccf'")
        face = input(" Face: ")
    
    print ("\n Parameters correctly entered")
   
# does the user want to create the JSON file with the entered info? 
createJson = int(input(" Do you want to create the JSON file with the entered parameters? (1/0): "))

# ensure that the createJson option is correct
while createJson < 0 or createJson > 1:
    print ("\n INCORRECT PARAMETER: Enter a 1 (Yes) or a 0 (No)")
    createJson = int(input(" Do you want to create the JSON file with the entered parameters? (1/0): "))

#create JSON file
createJSONFile(createJson, design, listOfFactors, reply, random_bool, resolution, centresbb, centrescc1, centrescc2, alpha, face)        