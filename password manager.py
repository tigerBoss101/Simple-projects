"""
Password manager
"""

import getpass
import secrets
from collections import OrderedDict
import pyperclip
from string import ascii_letters as al


master_pass = "^h3elloworldYAY$"
master = ""
services = OrderedDict()

while master != master_pass:
    master = getpass.getpass("Enter masterpass here: ")

print("Welcome to Password manager v 1.0.0!")
print("(A)dd new password, (G)et password or (C)hange password? (L)ist all Services or (Q)uit")

command = ""
while True:
    command = input(">> ")
    match command.upper():
        case "Q":
            break

        case "A":
            service = input("Service name: ")
            exit_input = None
            while exit_input != "":
                password = "".join(secrets.choice(al + "1234567890" + "!@#$%^&*()") for _ in range(10))
                print("Generated password: " + password)
                exit_input = input("Enter to continue / Any key to change password")
            services[service] = password

        case "C":
            service = input("Service name: ")
            while service not in services:
                print("Service doesn't exist")
                service = input("Service name: ")
            exit_input = None
            while exit_input != "":
                password = "".join(secrets.choice(al + "1234567890" + "!@#$%^&*()") for _ in range(10))
                print("Generated password: " + password)
                exit_input = input("Enter to continue / Any key to change password")
            services[service] = password

        case "L":
            if len(services) == 0:
                print("No services")
            else:
                for service in services:
                    print(f"| {service} |")

        case "G":
            service = input("Service name: ")
            while service not in services:
                print("Service doesn't exist")
                service = input("Service name: ")
            pyperclip.copy(services[service])
            print("Copied text to clipboard!")

        case _:
            print("Command not found.")

    print("(A)dd new password, (G)et password or (C)hange password? (L)ist all Services or (Q)uit")