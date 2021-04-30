import time
print("hiii,  visitor ")  # welcome
print("nice meeting you")
print("what is your name?")  # asking details
name1 = input()
print("what is your age ? ")

while 1 == 1 :
    try :
        name2  = input()
        name2 = int(name2)
        break
    except :
        print("you entered a wrong integer")
if name2 < 18 :
    print("you are not an adult!!!!")

if name2 >= 18:
    wel = f'Welcome {name1.upper()} to the programme'
    print(wel)
    print("PRESS ENTER TO PROCCED")
    input()
print("what is the reason behind with you ......")
print("why do you approched us ? ")
stm = input()
msg = f'we understand your message !! ({stm}) '
print(msg)
msg2 = f'Is your given age {name2} is correct ..'
print(msg2)
conf = input("Yes \ No")
if conf == "Yes":
    print("ok nice")

    for a in range(1,6)
        print("NOW WE ARE SYNING YOUR DATA .........")
        time.sleep(1)
    fname = f'Your name is {name1}'
    aname = f'your age is {name2}'
    print(fname)
    print(aname)
    conf2 = input("Is we are correct Yes \ No ")
    if conf2 == "Yes" :
        print("ok your details has been recorded")
    else :
        print("start from beginning ")
else:
    print("again start from the beginning ")
