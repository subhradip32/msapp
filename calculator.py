from tkinter import *
window=Tk()
btnadd=Button(window, text="+", fg='blue')
btnsub=Button(window, text="-", fg='blue',height= 4,width= 4)
btnmult=Button(window, text="*", fg='blue',height= 4,width= 4)
btndivid=Button(window, text="/", fg='blue',height= 4,width= 4)
btn1=Button(window, text="1" ,fg='blue',height= 4,width= 4)
btn2=Button(window, text="2", fg='blue',height= 4,width= 4)
btn3=Button(window, text="3", fg='blue',height= 4,width= 4)
btn4=Button(window, text="4", fg='blue',height= 4,width= 4)
btn5=Button(window, text="5", fg='blue',height= 4,width= 4)
btn6=Button(window, text="6", fg='blue',height= 4,width= 4)
btn7=Button(window, text="7", fg='blue',height= 4,width= 4)
btn8=Button(window, text="8", fg='blue',height= 4,width= 4)
btn9=Button(window, text="9", fg='blue',height= 4,width= 4)
btn0=Button(window, text="0", fg='blue',height= 4,width= 4)
btnequalto=Button(window, text="=", fg='blue',height= 4,width= 4)

btnadd.place(x=80, y=100,height= 80,width= 40)
btnsub.place(x=80, y=200)
btnmult.place(x=80, y=300)
btndivid.place(x=80, y=400)
btn1.place(x=160, y=100)
btn2.place(x=160, y=200)
btn3.place(x=160, y=300)
btn4.place(x=160, y=400)
btn5.place(x=240, y=100)
btn6.place(x=240, y=200)
btn7.place(x=240, y=300)
btn8.place(x=240, y=400)
btn9.place(x=160, y=500)
btn0.place(x=240, y=500)
btnequalto.place(x=80, y=500)

window.title('Calculator')
window.configure(bg="gray")
window.geometry("720x500+10+10")
window.mainloop()

def num_input():
    while 2>1:
      try:
        name1 = input("Enter a digit ?")
        name1 = int(name1)
        return name1
        break
      except:
        print("Enter a valid number...")
        continue

num1 = num_input()
num2 = num_input()
print("What you want to do ? (+,-,*,/,**,/*")
name3 = input()
class Basic_calculate:
    def add(name1,name2):
      addition = name1 + name2
      return addition
    def sub(name1,name2):
      subtraction = name1 - name2
      return subtraction
    def multi(name1,name2):
        multiplication = name1 * name2
        return multiplication
    def divid(name1,name2):
        devsiiii = name1 / name2
        return devsiiii

class Squares:
    def square(name1):
      square = name1 * name1
      return square

    def square_root(name1):
      i = 1
      while 1==1:
        if name1 / i == i :
          break
        i = i + 1
      print(i)

if name3 == "+":
    print(Basic_calculate.add(num1,num2))
if name3 == "-":
    print(Basic_calculate.sub(num1,num2))
if name3 == "*":
    print(Basic_calculate.multi(num1,num2))
if name3 == "/":
    print(Basic_calculate.divid(num1,num2))
if name3 == "**":
    print(Squares.square(num1,num2))
if name3 == "/*":
    print(Squares.square_root(num1,num2))






