import os
os.system("cls")
email = input("Insert email: ")
index = email.find("@")
indexDot = email.find(".")
username = email[:index]
domain = email[index+1:indexDot]
if "gmail" in domain or "hotmail" in domain or "outlook" in domain or "yahoo" in domain:
    print("Email is persional email")
else:
    if "@" in email or "." in email:
        print("USERNAME:",username)
        print("DOMAIN:",domain)
    else:
        print("Email is invalid")