# BinaryToDecimal [ Function (str) ] -> Product [ Integer ]
def BinaryToDecimal(Binary):
    Numberline = 1
    Product = 0
    for i in range(0,len(Binary)):
        i = len(Binary)-i-1 # Reverse "i" to move backwards.
        if Binary[i] == "1":
            Product = Product + (Numberline) # If it's a (1) add the current numberline position to product.
        Numberline = Numberline * 2 # Double the current numberline for the next iteration.
    return Product

# DecimalToBinary [ Function (str) ] -> Unnamed [ Integer ]
def DecimalToBinary(Decimal):
    Decimal = int(Decimal)
    ## Create numberline.
    NumberlineObject = {}
    Numberline = 0.5
    i = 0
    while True:
        i = i+1
        Proposal = Numberline * 2
        if Proposal > Decimal:
            break
        NumberlineObject[Proposal] = "0"
        Numberline = Proposal

    i = 0
    while True:
        i = i+1
        if Decimal >= Numberline:
            Decimal = Decimal - Numberline
            NumberlineObject[Numberline] = "1"
        if Decimal == 0:
            break
        ##
        Numberline = Numberline / 2

    Decimal = ""
    for v in NumberlineObject:
        Decimal=Decimal+NumberlineObject[v]
    return Decimal[::-1]

while True:
    Choice = input("1 | Binary to decimal.\n2 | Decimal to binary.\n> Select a number.\n- >")
    if Choice == "1":
        print("Result: {}".format(BinaryToDecimal(input("Enter Binary\n>"))))
    elif Choice == "2":
        print("Result: {}".format(DecimalToBinary(input("Enter Decimal\n>"))))
