def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    #name, phone = args
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "data entered incorrectly"

def change_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact changed."
    except ValueError:
        return "data entered incorrectly"
def all_contact(contacts):

    line = "|{:^15}|{:^15}|".format("name", "phone")
    separator = "_"*len(line)
    body = ""
    itm = 0
    for key, val in contacts.items():
        body += ("|{:<15}|{:>15}|\n".format(key, val))
        #itm +=1
    table = "\n".join([separator, line, separator, body, separator])
    return table

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(all_contact(contacts))
        else:
            print("Invalid command.")
if __name__ == "__main__":
    main()