str = input()

try:
    arr = str.split()
    num1 = int(arr[0])
    num2 = int(arr[2])

    if (num1 < 0 or num1 > 10):
        raise Exception
    if (num2 < 0 or num2 > 10):
        raise Exception
    if (arr[1] != '+' and arr[1] != '-' and arr[1] != '*' and arr[1] != '/'):
        raise Exception
    if len(arr) != 3:
        raise Exception

except:
    print("Исключение")

else:
    if arr[1] == "+":
        print(num1 + num2)
    elif arr[1] == "-":
        print(num1 - num2)
    elif arr[1] == "*":
        print(num1 * num2)
    elif arr[1] == "/":
        print(int(num1 / num2))