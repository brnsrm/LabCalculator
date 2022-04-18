#Length
def length(x,y,z):
    if x == "mm" and y == "cm":
        result = z / 10
    elif x == "cm" and y == "mm":
        result = z * 10
    elif x == "cm" and y == "dm":
        result = z / 10
    elif x == "dm" and y == "cm":
        result = z * 10
    elif x == "dm" and y == "m":
        result = z / 10
    elif x == "m" and y == "dm":
        result = z * 10
    elif x == "m" and y == "km":
        result = z / 1000
    elif x == "km" and y == "m":
        result = z * 1000
    return result

#Area
def area(x,y,z):
    if x == "mm^2" and y == "cm^2":
        result = z / 100
    elif x == "cm^2" and y == "mm^2":
        result = z * 100
    elif x == "cm^2" and y == "dm^2":
        result = z / 100
    elif x == "dm^2" and y == "cm^2":
        result = z * 100
    elif x == "dm^2" and y == "m^2":
        result = z / 100
    elif x == "m^2" and y == "dm^2":
        result = z * 100
    elif x == "m^2" and y == "a":
        result = z / 100
    elif x == "a" and y == "m^2":
        result = z * 100
    elif x == "a" and y == "ha":
        result = z / 100
    elif x == "ha" and y == "a":
        result = z * 100
    elif x == "ha" and y == "km^2":
        result = z / 100
    elif x == "km^2" and y == "ha":
        result = z * 100
    return result

#Volume
def volume(x,y,z):
    if x == "mm^3" and y == "cm^3":
        result = z / 1000
    elif x == "cm^3" and y == "mm^3":
        result = z * 1000
    elif x == "cm^3(ml)" and y == "dm^3(l)":
        result = z / 1000
    elif x == "dm^3(l)" and y == "cm^3(ml)":
        result = z * 1000
    elif x == "dm^3(l)" and y == "m^3":
        result = z / 1000
    elif x == "m^3" and y == "dm^3(l)":
        result = z * 1000
    return result

#Weight
def weight(x,y,z):
    if x == "mg" and y == "g":
        result = z / 1000
    elif x == "g" and y == "mg":
        result = z * 1000
    elif x == "g" and y == "kg":
        result = z / 1000
    elif x == "kg" and y == "g":
        result = z * 1000
    elif x == "kg" and y == "t":
        result = z / 1000
    elif x == "t" and y == "kg":
        result = z * 1000
    return result

#Concentration
def concentration(x,y,z):
    #M = Molar (Mol/l), mM = Millimolar (mMol/l)
    if x == "mM" and y == "M":
        result = z / 1000
    elif x == "M" and y == "mM":
        result = z * 1000
    elif x == "ng/µl" and y == "ng/ml":
        result = z * 1000
    elif x == "ng/ml" and y == "ng/µl":
        result = z / 1000
    elif x == "ng/ml" and y == "ng/l":
        result = z * 1000
    elif x == "ng/l" and y == "ng/ml":
        result = z / 1000
    elif x == "µg/ml" and y == "µg/l":
        result = z * 1000
    elif x == "µg/l" and y == "µg/ml":
        result = z / 1000
    elif x == "mg/ml" and y == "mg/l":
        result = z * 1000
    elif x == "mg/l" and y == "mg/ml":
        result = z / 1000
    elif x == "g/ml" and y == "g/l":
        result = z * 1000
    elif x == "g/l" and y == "g/ml":
        result = z / 1000
    return result

#Optical Density OD600
def density(x,y,z):
    if x == "Spectrophotometer at OD600" and y == "Cells/ml":
        result = z * 800000000
    else:
        result = z / 800000000

print("Which unit do you want to convert?")
print("Here are the following options:")
print("1. Length")
print("2. Area")
print("3. Volume")
print("4. Weight")
print("5. Concentration")
print("6. Optical Density")

scndunitconverter = ""

while not scndunitconverter == "no":
    #Input choice 
    try:
        choice = input("Enter choice (1, 2, 3, 4, 5 or 6):")
    except:
        print("Unknown choice!")
        continue

    #Input adding numbers
    if choice in("1", "2", "3", "4", "5", "6"):
        try:
            num = float(input("Enter the number that you want to convert:"))
        except:
            print("This is not a number!")
            continue
        
        #Converter Options
        if choice in ("1", "2", "3", "4", "5", "6"):
            print("From unit")
            fromunit = input()
            print("To unit")
            tounit = input()
            if choice == "1":
                converted = length(fromunit, tounit, num)
            elif choice == "2":
                converted = area(fromunit, tounit, num)
            elif choice == "3":
                converted = volume(fromunit, tounit, num)
            elif choice == "4":
                converted = weight(fromunit, tounit, num)
            elif choice == "5":
                converted = concentration(fromunit, tounit, num)
            elif choice == "6":
                converted = density(fromunit, tounit, num)
            print("Converted unit:", num, "->", converted)

    #Second time
    print("Do you want to convert a number again? (Yes/NO)")
    scndunitconverter = input()



