input_str = input()
def main (input_str):
    try:
        arr = input_str.split()
        if len(arr) != 3:
            raise Exception("Неверный ввод" )
        num1 = int(arr[0])
        num2 = int(arr[2])

        if (num1 < 0 or num1 > 10):
            raise Exception("Первое число не верно")
        if (num2 < 0 or num2 > 10):
            raise Exception("Второе число не верно")
        if (arr[1] != '+' and arr[1] != '-' and arr[1] != '*' and arr[1] != '/'):
            raise Exception("Неверный оператор")

    except Exception as e:
        return str(e)

    else:
        if arr[1] == "+":
            return str(num1 + num2)
        elif arr[1] == "-":
            return str(num1 - num2)
        elif arr[1] == "*":
            return str(num1 * num2)
        elif arr[1] == "/":
            return str(num1 // num2)
print(main(input_str))