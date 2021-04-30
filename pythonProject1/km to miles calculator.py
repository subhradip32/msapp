print("what is th distance in miles ? ")
while 1 == 1:
    try:
        name2 = input()
        name2 = int(name2)
        break
    except:
        print("Enter a valid number..")
def calculator():
    cal = name2 * 1.60
    msg = f'{name2} miles in kilometre is....'
    print(msg)
    print(f'{cal} is the distance of the given {name2} miles..  ')
result =calculator()


