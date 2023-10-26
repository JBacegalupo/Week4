#### challenge 1
def ValidateInput(num):
    if 0 <= num <= 100:
        return True
    else:
        return False
#print(ValidateInput(12))
#print(ValidateInput(2000))

########################################
#### challenge 2

def UpperCase_LowerCase(message):
    LowerCase = 0
    UpperCase = 0
    for n in message:
        if n.islower():
            LowerCase += 1
        elif n.isupper():
            UpperCase += 1
    print(f"there are {str(UpperCase)} upper case characters and {str(LowerCase)} lower case characters")

#UpperCase_LowerCase(input("Please enter a string"))
#### chalenge 3

def greetings():
    name = input("Please enter your name: ")
    if not name:
        print("Hello stranger")
    else:
        first = True
        newname = ""
        for n in name:
             if first == True:
                newname += n.upper()
                first = False
             else:
                newname += n.lower()
        print(print("Hello " + newname + ". Good to meet you!"))
#greetings()
########################################
#### challenge 4
def LastCharRemove(message):
    if len(message) <=1:
        return message
    else:
        return message[:-1]

#print(LastCharRemove(input("Enter a string")))
######################### challenge 5 ###############

def CelciusConversion(DegreesC):
    return((DegreesC * 9/5) + 32)




def FarenheightConversion(DegreesF):
    return(( DegreesF - 32) * 5/9)
print(FarenheightConversion(int(12)))

######## challenge 6 ########

# print(str(CelciusConversion(int(input("Please enter a temperature in celcius followed directly by C without a space ")[:-1]))) + "C")

###### challenge 7
def TempList():
    TemperatureList = []
    TotalTemp = 0
    for i in range(6):
        temperature = input(f"enter temp {i+1} : ")
        temperature = temperature[:-1]
        TemperatureList.append(int(temperature))
        TotalTemp += int(temperature)

    print("Highest Temp: " + str(max(TemperatureList)))
    print("Lowest Temp: " + str(min(TemperatureList)))
    print("average Temp: " + str(TotalTemp / 6))

###### challenge 8

def TempListModified():
    TemperatureList = []
    TotalTemp = 0
    UserContinue = True
    while UserContinue:
        temperature = input(f"enter temp {str(int(len(TemperatureList) + 1))} : ")
        if temperature == "":
            UserContinue = False
        else:
            temperature = temperature[:-1]
            TemperatureList.append(int(temperature))
            TotalTemp += int(temperature)

    print("Highest Temp: " + str(max(TemperatureList)))
    print("Lowest Temp: " + str(min(TemperatureList)))
    print("average Temp: " + str(TotalTemp / 6))

TempListModified()