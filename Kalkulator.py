

num = 0
operation = None
reset = True
result = None
calcOperations = ["+", "-", "*", "/", "**"]

while True:
    if reset == True:
        num = int(input("Podaj liczbę startową:") )
        reset = False

    operation = input("Podaj operację arytmetyczną jak np. " 
        + str(calcOperations) + "lub exit jeśli koniec lub reset : ")
    if operation == "exit" : break
    if operation == "reset": 
        reset == True
        continue

    if not operation in calcOperations:
        print("Error, błędna operacja!")
        continue

    secondnum = int(input("Podaj drugą liczbę:"))

    if operation == "+":
        result = num + secondnum

    if operation == "-":
        result = num - secondnum

    if operation == "*":
        result = num * secondnum

    if operation == "/":
        result = num / secondnum

    if operation == "**":
        result = num ** secondnum

    print("Wynik operacji" + str(num) + "" + operation + " " + str(secondnum)
            + " =" + str(result))

    num = result
    result = None

