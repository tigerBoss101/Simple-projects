# Password manager

import getpass
import random
from string import ascii_letters as al
import pyperclip
from collections import OrderedDict
master_pass = "^h3elloworldYAY$"
master = ""
services = OrderedDict()
while master != master_pass:
    master = getpass.getpass("Enter masterpass here: ")
print("Welcome to Password manager v 1.0.0!")
print("(A)dd new password, (G)et password or (C)hange password? (L)ist all Services or (Q)uit")
command = ""
while True:
    command = input(">>")
    if command.upper() == "Q":
        break
    elif command.upper() == "A":
        service = input("Service name: ")
        exit_input = None
        while exit_input != "":
            password = "".join(random.choice(al + "1234567890" + "!@#$%^&*()") for _ in range(10))
            print("Generated password: " + password)
            exit_input = input("Enter to continue / Any key to change password")
        services[service] = password
    elif command.upper() == "C":
        service = input("Service name: ")
        while service not in services:
            print("Service doesn't exist")
            service = input("Service name: ")
        exit_input = None
        while exit_input != "":
            password = "".join(random.choice(al + "1234567890" + "!@#$%^&*()") for _ in range(10))
            print("Generated password: " + password)
            exit_input = input("Enter to continue / Any key to change password")
        services[service] = password
    elif command.upper() == "L":
        if len(services) == 0:
            print("No services")
        else:
            for service in services:
                print("| {} |".format(service))
    elif command.upper() == "G":
        service = input("Service name: ")
        while service not in services:
            print("Service doesn't exist")
            service = input("Service name: ")
        pyperclip.copy(services[service])
        print("Copied text to clipboard!")
    print("(A)dd new password, (G)et password or (C)hange password? (L)ist all Services or (Q)uit")