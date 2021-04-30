print("what is your Name ? ")
name1 = input()
print("what is your weight in kilogram (kg) ? ")
a = 1
while a == 1 :
    try:
        name2 = input()
        name2 = int(name2)
        break
    except:
        print("ENTER A VALID NUMBER")
print("what is your  height in  meter(m) ?")
while 1 == 1:
    try:
        name3 = input()
        name3 = int(name3)
        break
    except:
        print("enter a valid height in  meter(m) ?")
def bmi_calculator(name1,name2,name3):
    bmi = name2 / (name3 ** 2)
    print("bmi : ")
    print(bmi)
    if bmi < 25 :
        msg = f'{name1} , you are over weight ..'
        print(msg)
    else:
        msg2 = f'{name1} , you are  underweight ..'
        print(msg2)
bmi_calculator(name1, name2 ,name3)


