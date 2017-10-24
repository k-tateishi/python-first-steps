print('FizzBuzz Game!')
print('数値を入力してください')
a = input()

isNum = True
try:
    a = int(a)
except:
    print('数値ではありません')
    isNum = False

if isNum:
    if a % 15 == 0:
        print('FizzBuzz')
    elif a % 3 == 0:
        print('Fizz')
    elif a % 5 == 0:
        print('Buzz')
    else:
        print('Other')
