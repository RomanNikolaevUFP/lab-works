import math

def input_number(s, number=float):
    s1 = s
    while True:
        try:
            return number(input(s1))
        except:
            s1 = "Введенный элемент не является числом, " + s[0].lower() + s[1:]

f = input("Введите функцию (+, -, *, /, **, log, roundup, rounddown)\n")

if f == "+":
    a = input_number("Введите первый элемент:\n") 
    b = input_number("Введите второй элемент:\n")
    print(a + b)
elif f == "-":
    a = input_number("Введите первый элемент:\n") 
    b = input_number("Введите второй элемент:\n")
    print(a - b)
elif f == "*":
    a = input_number("Введите первый элемент:\n") 
    b = input_number("Введите второй элемент:\n")
    print(a * b)
elif f == "/":
    a = input_number("Введите первый элемент:\n") 
    b = input_number("Введите второй элемент:\n")
    print(a * b)
elif f == "**":
    a = input_number("Введите первый элемент:\n")
    b = input_number("Введите второй элемент:\n")
    print(a ** b)
elif f == "log":
    a = input_number("Введите аргумент:\n") 
    b = input_number("Введите основание:\n") 
    print(math.log(a, b))
elif f == "roundup":
    a = input_number("Введите число:\n") 
    b = input_number("Введите N:\n", int)
    print(math.ceil(a * 10**b) / 10**b)
elif f == "rounddown":
    a = input_number("Введите число:\n") 
    b = input_number("Введите N:\n", int)
    print(math.floor(a * 10**b) / 10**b)
