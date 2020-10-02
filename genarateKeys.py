from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

from colorama import Fore, Back, Style
import time
import random
import json

def create_key():
    try:
        y = input("\033[2;37mAre you sure you want to overwrite the current keys? (y/n) \033[1;31m")
        print('\033[0;0m')
        if y.lower() != "y":
            print(f"\033[91m[ERROR]\033[0;0m Key genaration canseld")
            return None

        size = input("\033[2;37mKey size (2048 recommended): \033[1;31m")
        print('\033[0;0m')

        print(f"\033[93m[Working] \033[0;0mCreating keys")    #GETTING THE KEY
        timerNow = time.time()

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=int(size),
            backend=default_backend()
        )
        public_key = private_key.public_key()
        print(f"\033[92m[Success] \033[0;0mKeys genarated")

        #STOREING THE KEY
        print(f"\033[93m[Working] \033[0;0mUpdateing files")

        private_key = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

        public_key = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        with open("data.json", "r") as fileIn:
            data = json.load(fileIn)
            public_key_file = data["public_key"]
            private_key_file = data["private_key"]

        with open(public_key_file, "wb") as file:
            file.write(public_key)

        with open(private_key_file, "wb") as file:
            file.write(private_key)
    except Exception as e:
        print(f"\033[91m[ERROR]\033[0;0m An error occurred while creating and or uploading the keys\n")
    else:
        print(f"\033[92m[Success] \033[0;0mKeys updated in files \033[91m{public_key_file}\033[0;0m, \033[91m{private_key_file}\033[0;0m\n Process took \033[91m{round(time.time() - timerNow, 4)}\033[0;0m seconds")
