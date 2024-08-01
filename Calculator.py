str = input()
def main(str):
    try:
        arr = str.split()
        num1 = int(arr[0])
        num2 = int(arr[2])

        if (num1 < 0 or num1 > 10):
            raise Exception("Первое число не верно")
        if (num2 < 0 or num2 > 10):
            raise Exception("Второе число не верно")
        if (arr[1] != '+' and arr[1] != '-' and arr[1] != '*' and arr[1] != '/'):
            raise Exception("Неверный оператор")
        if len(arr) != 3:
            raise Exception("Неверный ввод" )

    except Exception as e:
        return e

    else:
        if arr[1] == "+":
        elif arr[1] == "-":
            return(num1 - num2)
        elif arr[1] == "*":
            return(num1 * num2)
        elif arr[1] == "/":
            return(int(num1 / num2))
print(main(str))