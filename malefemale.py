def genderFunction(firstName, fullName):
    print("%s, what is your gender?"%firstName)
    genderInput = input("Enter 'M' for Male or 'F' for Female\n").upper()
    if genderInput == "M":
        gender = "Male"
    elif genderInput == "F":
        gender: str= "Female"