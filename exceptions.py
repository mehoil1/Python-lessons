print("Введите математическое действие и два положительных числа через пробелы:")
string = input()
pn = []
for element in string.split(" "):
    pn.append(element)

operations = ["+", "-", "*", "/"]
assert pn[0] in operations, "Действие с числами не определено, начните с математического действия между числами"

try:
    if pn[0] == "+":
        result = int(pn[1]) + int(pn[2])
        print(result)
    elif pn[0] == "-":
        result = int(pn[1]) - int(pn[2])
        print(result)
    elif pn[0] == "*":
        result = int(pn[1]) * int(pn[2])
        print(result)
    elif pn[0] == "/":
        result = int(pn[1]) / int(pn[2])
        print(result)
except ZeroDivisionError:
    print("Деление на ноль невозможно")
except ValueError:
    print("Деление строк невозможно, необходимо использовать только числа")
except IndexError:
    print("Введены не все числа для математического действия")
