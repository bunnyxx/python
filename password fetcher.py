#! python3
# pw.py - password program
import pyperclip

password = {"email": "homura", "discord": "kyouko", "youtube": "madoka"}
accountName = str(input("Account name? "))

def passwordObtainer(account):
  if account == "quit":
    print("Thank you for using pwmanager")
  elif account in password:
    pyperclip.copy(password[account])
    pyperclip.paste()
    print("Password:",password[account],"was pasted to the clipboard!")
  else:
    print("There is no account named",account+".")
    adder = input("Add one? (y/n) ")
    if adder == "y":
      print("Account name",account)
      newPw = str(input('What is the password?: '))
      password[account] = newPw
      print("Account",account,"was added to the password database.")
    newAccName = str(input("Account name?: "))
    passwordObtainer(newAccName)

passwordObtainer(accountName)
