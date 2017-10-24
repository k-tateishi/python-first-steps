print('BMI を 計測します')

print('身長を入力してください（cm）')
height = input()
height = float(height)

print('体重を入力してください（Kg）')
weight = input()
weight = float(weight)

bmi = weight / ((height / 100) ** 2)
print('あなたのBMI値は ' + str(bmi) + ' です')

if bmi < 18.5:
    print('痩せていますね')
elif bmi < 25:
    print('標準体型です!')
elif bmi < 35:
    print('少し肥満気味ですね')
else:
    print('肥満です...')
