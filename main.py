from colorama import Fore, Back, Style

import encrypt
import decrypt
import genarateKeys
import time
import traceback
import os
import json

try:
    # Win32
    from msvcrt import getch
except ImportError:
    # UNIX
    def getch():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""\033[1;36m \033[1m  ____                      _               _
  / ___| _ __  _   _  _ __  | |_  ___     __| | _ __  __ _   __ _   ___   _ __
 | |    | '__|| | | || '_ \\ | __|/ _ \\   / _` || '__|/ _` | / _` | / _ \\ | '_ \\
 | |___ | |   | |_| || |_) || |_| (_) | | (_| || |  | (_| || (_| || (_) || | | |
  \\____||_|    \\__, || .__/  \\__|\\___/   \\__,_||_|   \\__,_| \\__, | \\___/ |_| |_|
               |___/ |_|                                    |___/


    ___------~~~~~~~~~~~----__         .:.         __----~~~~~~~~~~~------___
  ~~ ~--__          ......====\\\\~~    .:::.    ~~//====......          __--~ ~~
          ~\\ ...::::~~~~~~  //|||    .:::::.    |||\\\\  ~~~~~~::::... /~
         -~~\\_            //  |||***.(:::::).***|||  \\\\            _/~~-
              ~\\_        // *******.:|\\^^^/|:.******* \\\\        _/~
                 \\      / ********.::(>: :<)::.******** \\      /
                  \\   /  ********.::::\\\\|//::::.********  \\   /
                   \\ /   *******.:::::(o o):::::.*******   \\ /
                    /.   ******.::::'*|V_V|***`::.******   .\\
                      ~~--****.:::'***|___|*****`:.****--~~
                            *.::'***//|___|\\\\*****`.*
                            .:'  **/##|___|##\\**    .
                           .    (v(VVV)___(VVV)v)
                           \033[0;0m

┏━━━━━━━━━━━━━━━━━━┓
\033[1;31m1] \033[0;0mEncrypt
\033[1;31m2] \033[0;0mDecrypt
\033[1;31m3] \033[0;0mRegenarate Keys
\033[1;31m4] \033[0;0mFile locations
\033[1;31m5] \033[0;0mExit
┗━━━━━━━━━━━━━━━━━━┛""")
clear()
#print(os.name)
while True:
    with open("data.json", "r") as readFile:
        data = json.load(readFile)

    option = input(f"\033[2;37mSelect option: \033[0;0m\033[1;31m")
    print('\033[0;0m')

    if option not in ("1","2","3", "4", "5"):
        print(f"\033[91m[ERROR]\033[0;0m Invaid option")
        print(f"\033[2;37mPress any key to continue\033[0;0m\033[0;0m")
        getch()
    else:
        if option == "3":
            genarateKeys.create_key()
            print(f"\033[2;37mPress any key to continue\033[0;0m\033[0;0m")
            getch()

        elif option == "1":
            try:
                message = encrypt.encrypt()
                with open(data['data'], "wb") as file:
                    file.write(message)
            except Exception as e:
                print(f"\033[91m[ERROR]\033[0;0m {e}")
            else:
                print(f"\033[92m[Success] \033[0;0mMessage encrypted in file '{data['data']}'")
            print(f"\033[2;37mPress any key to continue\033[0;0m\033[0;0m")
            getch()


        elif option == "2":
            print(f"\033[93m[Working] \033[0;0mReading data from file '{data['data']}'")
            time.sleep(.2)
            try:
                message = decrypt.decrypt()
            except Exception as e:
                print(f"\033[91m[ERROR]\033[0;0m {e}")
                print(traceback.format_exc())
            else:
                print(f"\033[92m[Success] \033[0;0mOriginal message: \033[0;0m\033[1;31m{message}\033[0;0m")

            #os.system('pause' if os.name == 'nt' else 'read -p "Press any key to continue . . ."')
            print(f"\033[2;37m\nPress any key to continue\033[0;0m\033[0;0m")
            getch()
            #time.sleep(2)

        elif option == "4":
            print(
            f"""┏━━━━━━━━━━━━━━━━━━┓
\033[1;31m1] \033[0;0mPrivate key
\033[1;31m2] \033[0;0mPublic key
\033[1;31m3] \033[0;0mInput key
\033[1;31m4] \033[0;0mData storeage
\033[1;31m5] \033[0;0mShow data
┗━━━━━━━━━━━━━━━━━━┛
            """)
            option = input(f"\033[2;37mSelect option: \033[0;0m\033[1;31m")
            print('\033[0;0m')

            if option not in ("1","2","3", "4", "5"):
                print(f"\033[91m[ERROR]\033[0;0m Invaid option")
                print(f"\033[2;37mPress any key to continue\033[0;0m\033[0;0m")
                getch()
            else:
                with open("data.json", "r") as fileIn:
                    data = json.load(fileIn)
                if option != "5":

                    if option == "1":
                        option = input(f"\033[2;37mWhere would you like the new location to be: \033[0;0m\033[1;31m")
                        print('\033[0;0m')
                        data["private_key"] = option

                    elif option == "2":
                        option = input(f"\033[2;37mWhere would you like the new location to be: \033[0;0m\033[1;31m")
                        print('\033[0;0m')
                        data["public_key"] = option

                    elif option == "3":
                        option = input(f"\033[2;37mWhere would you like the new location to be: \033[0;0m\033[1;31m")
                        print('\033[0;0m')
                        data["public_key_in"] = option

                    elif option == "2":
                        option = input(f"\033[2;37mWhere would you like the new location to be: \033[0;0m\033[1;31m")
                        print('\033[0;0m')
                        data["data"] = option

                    try:
                        with open(option, "rb") as file:
                            file.read()
                    except Exception as e:
                        print(f"\033[91m[ERROR]\033[0;0m Invalid file location")
                        print(e)
                    else:
                        with open("data.json", "w") as fileOut:
                            json.dump(data, fileOut)
                    print(f"\033[2;37mPress any key to continue\033[0;0m\033[0;0m")
                    getch()

                else:
                    print(f"""Keys:
Private key: \033[91m{data['private_key']}\033[0;0m
Public key: \033[91m{data['public_key']}\033[0;0m
Public key input: \033[91m{data['public_key_in']}\033[0;0m
Data storeage: \033[91m{data['data']}\033[0;0m
""")
                print(f"\033[2;37mPress any key to continue\033[0;0m\033[0;0m")
                getch()
        elif option == "5":
            break

    clear()
