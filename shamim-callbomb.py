logo ="""\033[1;96m
   _____ _    _          __  __ _____ __  __ 
  / ____| |  | |   /\   |  \/  |_   _|  \/  |
 | (___ | |__| |  /  \  | \  / | | | | \  / |
  \___ \|  __  | / /\ \ | |\/| | | | | |\/| |
  ____) | |  | |/ ____ \| |  | |_| |_| |  | |
 |_____/|_|  |_/_/    \_\_|  |_|_____|_|  |_|
                                             
                                             """

import requests
number = input("Enter Your Number: ")
amount = int(input ("Enter Your Amount: "))
for i in range (amount):
 r= requests.get("http://pikachu-call-bomber.ezyro.com/babyyy.php?phone="+number)
 f= r.content
 print(f)
