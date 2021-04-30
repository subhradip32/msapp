from tkinter import *

root = Tk()


def place_buttons(btns, row=0, col=1, x=70, y=70, btn1h=60, btn1w=60, marx=0, mary=0):
      for btn in btns:
            if row >= 4:
                  row = 0
                  col += 1
            if col >= 5: break

            x_c = (x * row) + marx
            y_c = (y * col) + mary
            row += 1

            try:
                  btn.place(x=x_c, y=y_c, height=btn1h, width=btn1w)
            except:
                  return False
      return True


def btn_press(char):
      pass


root.title("Calculator")
root.geometry("300x400")
root.minsize(300, 400)
root.maxsize(300, 400)

userInput = Label(text="1344", font=('', 30))
userInput.place(x=20, y=30)

btn_texts = ["1", "2", "3", "+", "4", "5", "6", "-", "7", "8", "9", "x", "C", "0", "=", "÷"]

btns = []
btns.append(Button(root, text=btn_texts[0], border="0", command=lambda: btn_press(btn_texts[0])))
btns.append(Button(root, text=btn_texts[1], border="0", command=lambda: btn_press(btn_texts[1])))
btns.append(Button(root, text=btn_texts[2], border="0", command=lambda: btn_press(btn_texts[2])))
btns.append(Button(root, text=btn_texts[3], border="0", command=lambda: btn_press(btn_texts[3])))
btns.append(Button(root, text=btn_texts[4], border="0", command=lambda: btn_press(btn_texts[4])))
btns.append(Button(root, text=btn_texts[5], border="0", command=lambda: btn_press(btn_texts[5])))
btns.append(Button(root, text=btn_texts[6], border="0", command=lambda: btn_press(btn_texts[6])))
btns.append(Button(root, text=btn_texts[7], border="0", command=lambda: btn_press(btn_texts[7])))
btns.append(Button(root, text=btn_texts[8], border="0", command=lambda: btn_press(btn_texts[8])))
btns.append(Button(root, text=btn_texts[9], border="0", command=lambda: btn_press(btn_texts[9])))
btns.append(Button(root, text=btn_texts[10], border="0", command=lambda: btn_press(btn_texts[10])))
btns.append(Button(root, text=btn_texts[11], border="0", command=lambda: btn_press(btn_texts[11])))
btns.append(Button(root, text=btn_texts[12], border="0", command=lambda: btn_press(btn_texts[12])))
btns.append(Button(root, text=btn_texts[13], border="0", command=lambda: btn_press(btn_texts[13])))
btns.append(Button(root, text=btn_texts[14], border="0", command=lambda: btn_press(btn_texts[14])))
btns.append(Button(root, text=btn_texts[15], border="0", command=lambda: btn_press(btn_texts[15])))

place_buttons(btns, marx=12, mary=30)

root.mainloop()





