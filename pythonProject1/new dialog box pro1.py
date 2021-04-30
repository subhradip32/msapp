print("hiii,  visitor ")  # welcome
print("nice meeting you")
print("what is your name?")  # asking details
name1 = input()
print("what is your age ? ")

while 1 == 1:
    try:
        name2 = input()
        name2 = int(name2)
        break
    except :
        print("you entered a wrong number")

if name2 < 18 :  # asking
    print("ok welcome ")
    print("are you a robo ?")
    input()
    if name2 == "20":
        print("here is your password ? ")
        msg = f'{name1} you are a fool'
        print(msg)
    else:
        print("sorry you are not applicable")

if name2 > 18 :  # asking part 2
    print("sorry......")
    print("we are seeking for the adult ")
    print("press ENTER to proceed")
    input()
    print("1234 is the password")
    input()
    print("maze karo")




