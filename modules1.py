import time
print("PLEASE PRESS ENTER TO START..")
input()
for e in range(1,6):
    print("wait a sec....")
    time.sleep(1)
name = input("please enter your name ")
passw = input("please enter the given password")
passw = int(passw)
if passw == 1234:
    print(f'hii {name} welcome to our company')
    print("where you want to create the new file ")
    name2 = input()
    if name2 == "desktop" or "Desktop" or "DESKTOP":
        a = open("C:\\Users\\Personal\\Desktop\\souvik sirs notes.txt" ,"w" )
        a.write("here is the code of the life......\n chal hat bahen k lau")
        print("please check your desktop for codes")
    else :
        print("please enter a valid area to store")
