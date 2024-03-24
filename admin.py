from colorama import Fore, Style
import os
import time
import socket
import requests
import sys

print(Fore.YELLOW + "" ) 
url = input("Programı çalıştırmak için enter basınız...")

time.sleep(0.5)
print("Bekleyin...")
time.sleep(1)

print(Fore.RED + "")
print("""
                    Coded by enesxsec
                  --------------------
                     Team İHT Junior
                         __    _
                    _wr""        "-q__
                 _dP                 9m_
               _#P                     9#_
              d#@                       9#m
             d##                         ###
            J###                         ###L
            {###K                       J###K
            ]####K      ___aaa___      J####F
        __gmM######_  w#P""   ""9#m  _d#####Mmw__
     _g##############mZ_         __g##############m_
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_
  a###""          ,Z"#####@" '######"\g          ""M##m
 J#@"             0L  "*##     ##@"  J#              *#K
 #"               `#    "_gmwgm_~    dF               `#_
7F                 "#_   ]#####F   _dK                 JE
]                    *m__ ##### __g@"                   F
                       "PJ#####LP"
 `                       0######_                      '
                       _0########_
     .               _d#####^#####m__              ,
      "*w_________am#####P"   ~9#####mw_________w*"
          ""9@#####@M""           ""P@#####@M""
""")

url = input("Site URL'sini girin (HTTPS/HTTP): ")
print("Girilen site için aşağıdaki parametreleri deneyin ")
time.sleep(2)
print(Fore.MAGENTA + "Girilen site: " + url + "/admin")
time.sleep(2)
print("Girilen site: " + url + "/login")
time.sleep(2)
print("Girilen site: " + url + "/wp-admin")
time.sleep(2)
print("Girilen site: " + url + "/cpanel")
time.sleep(2)
print("Girilen site: " + url + "/cpanel_login")
time.sleep(2)
print("Girilen site: " + url + "/login.php")
time.sleep(2)
print("Girilen site: " + url + "/wp-admin.php")
time.sleep(2)
print("Girilen site: " + url + "/cpanel.php")
time.sleep(2)
print("Girilen site: " + url + "/cpanel_login.php")

admin_urls = [
    "https://" + url + "/admin",
    "https://" + url + "/login",
    "https://" + url + "/wp-admin",
    "https://" + url + "/cpanel",
    "https://" + url + "/cpanel_login",
    "https://" + url + "/admin.php",
    "https://" + url + "/login.php",
    "https://" + url + "/wp-admin.php",
    "https://" + url + "/cpanel.php",
    "https://" + url + "/cpanel_login.php"
]
