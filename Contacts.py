from time import sleep as sleep

contacts = {
    "Krzysztof Kononowicz" : {"phone" : "12345678", "email" : "kkononowicz@bio.pl"},
    "Major Suchodolski" : {"phone": "87654321", "email" : "majorsuchodolski@bio.pl"},
    "Jarosław Andrzejewski" : {"phone" : "11111111", "email" : "mexicanotv@bio.pl"}
}
keys = list(contacts)

def displayMenu():
    print("1. View contacts")
    print("2. Add a new contact")
    print("3. Quit")
    choice = input("What do you want to do: ")
    if choice == "1":
        viewContacts()
    elif choice == "2":
        addContact()
    elif choice == "3":
        print("Good bye!")
    else:
        print()
        displayMenu()

def addContact():
    name = input("Enter a name of a new contact (or enter q to go back to menu): ")
    if name == "q":
        displayMenu()
    elif len(name) != 0:
        phone = input("Enter a phone: ")
        email = input("Enter a email: ")
        contacts[name] = {"phone" : phone, "email" : email}
        print(f"{name} added to contacts!")
        sleep(1)
        displayMenu()

    else:
        print("No name entered.")
        sleep(1)
        displayMenu()
        
def viewContacts():
    print("---CONTACTS---")
    for i in range(len(keys)):
        print(f"{i+1}. {keys[i]}")
    choice = input("Choose a contact or enter q to go back to menu: ")
    if choice == "q":
        displayMenu()
    elif len(choice) == 0:
        print("Wrong choice.")
        sleep(1)
        viewContacts()
    else:
        print(keys[int(choice)-1])
        for k, v in contacts[keys[int(choice)-1]].items():
            print(k + ": " + v)
    print("U - update this contact, D - delete this contact, q - get back to contacts")
    
    while True:
        contact_choice = input("Enter your choice: ")
        if contact_choice == "" or contact_choice not in ("q", "U", "D"):
            print("Wrong choice.")
        else:
            break
    if contact_choice == "q":
        viewContacts()
    elif contact_choice == "U":
        updateContact(keys[int(choice)-1], contacts[keys[int(choice)-1]])
    elif contact_choice == "D":
        deleteContact(keys[int(choice)-1], contacts[keys[int(choice)-1]])
    else:
        print("you should not see this message :(")


def updateContact(contact, data):
    print(type(data))
    while True:
        choice = input(f"Do you want to change {contact}'s phone number? (y/n): ")
        if choice == "" or choice not in ("y", "n"):
            print("Wrong choice.")
            sleep(1)
        else:
            break
    if choice == "y":
        new_phone = input("Enter a new phone number: ")
        data["phone"] = new_phone
        print(f"{contact}'s new number is {new_phone}!")
        sleep(1)
    while True:
        choice = input(f"Do you want to change {contact}'s email? (y/n): ")
        if choice == "" or choice not in ("y", "n"):
            print("Wrong choice.")
            sleep(1)
        else:
            break
    if choice == "y":
        new_name = input("Enter a name for email (e.g. not frodo@shire.com, only frodo): ")
        new_domain = input("Enter a domain for mail (e.g. shire.com):")
        data["email"] = new_name + new_domain
        print(f"{contact}'s new number is {new_name + "@"+ new_domain}!")
        sleep(1)
    print("Getting back to menu...")
    sleep(0.5)
    print()
    print()
    displayMenu()

def deleteContact(contact, data):
    while True:
        choice = input(f"Are you sure you want to remove {contact} from your contacts? (y/n): ")
        if choice == "y":
            keys.remove(contact)
            del contacts[contact]
            print("Contact removed.")
            sleep(1)
        elif choice not in ("y", "n"):
            print("Wrong choice")
            continue
        break
    print("Getting back to menu...")
    sleep(0.5)
    displayMenu()

displayMenu()