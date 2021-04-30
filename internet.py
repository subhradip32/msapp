print("hii sir , kindly ENTER your name ?")
emp1 = input()
print("Now Enter the password ")
passw = input()
if emp1 == "Souvik" or "souvik" or "Subhradip" or "Subhradip" :
  msg1 = f'welcome {emp1}...'
  print(msg1)
  while 1==1 :
    try :
      passw2 = input("Enter a new password")

      break
    except :
      print("PLEASE ENTER A VALID NUMBER")
      continue
print("Which file you want to create")
print(".txt , .docx , .ppt ")
input1 = input()
if input1 == ".txt":
  a = open("C:\\Users\\Personal\\Desktop\\websitepassword.txt" , 'w+')
  a.write("here is your new password : "+ passw2)

  print(f"check your destop")

if input1 == ".ppt":
  a = open("C:\\Users\\Personal\\Desktop\\websitepassword.ppt" , 'w+')
  a.write("here is your new password : "+ passw2)

  print(f"check your destop")