def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command format."
        except Exception as e:
            return str(e)
    return inner

@input_error
def hello():
    return "How can I help you?"

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        raise KeyError("test")
        return "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(args, contacts):
    name, = args
    return f"Phone number for {name}: {contacts[name]}"

@input_error
def show_all(args, contacts):
    if contacts:
        result = "All contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()
    else:
        raise KeyError("No contacts found.")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = user_input.split()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print(hello())

        elif command == "add":
            if len(args) == 2:
                print(add_contact(args, contacts))
            else:
                print("Invalid 'add' command. Usage: add [username] [phone]")

        elif command == "change":
            if len(args) == 2:
                print(change_contact(args, contacts))
            else:
                print("Invalid 'change' command. Usage: change [username] [new_phone]")

        elif command == "phone":
            if len(args) == 1:
                print(show_phone(args, contacts))
            else:
                print("Invalid 'phone' command. Usage: phone [username]")

        elif command == "all":
            print(show_all(args, contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
