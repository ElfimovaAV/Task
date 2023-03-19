from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass
def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []

def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")


def add_new_contact():
    global last_id
    array = ["surname", "name", "patronymic", "phone_number"]
    string = ""
    temp = ""
    for i in array:
        while temp == "":
            temp = input(f"Enter {i} ")
        string += temp + " "
        temp = ""
    last_id += 1

    with open(file_base, "a", encoding="utf-8") as f:
        f.write(f"{last_id} {string}\n")


def change_contact(old_text, new_text):
    with open(file_base, 'r', encoding='utf-8') as f:
        count = 0
        for line in f:
            if old_text in line:
                with open(file_base, "r", encoding='utf-8') as f:
                    lines = f.readlines()
                    id_lines = lines[count].split()[0]
                del lines[count]

                with open(file_base, "w", encoding='utf-8') as f:
                    f.writelines(lines)
                data = open(file_base, 'a', encoding='utf-8')
                data.write(id_lines + ' ' + new_text['surname'] + ' ' + new_text['name'] + ' '
                           + new_text['patronymic'] + ' ' + new_text['phone_number'] + '\n')
            else:
                count += 1

def find_contact(text):
    with open(file_base.title(), 'r', encoding='utf-8') as f:
        res_list = []
        for line in f:
            if text in line:
                res_list.append(line[:-1])
        return print(res_list)

def find_first(text):
    with open(file_base, 'r', encoding='utf-8') as f:
        for line in f:
            if text in line:
                return [line[:-1]]
        return []


def delete_contact(text):
    with open(file_base, 'r', encoding='utf-8') as f:
        count = 0
        for line in f:
            if text in line:
                with open(file_base, "r", encoding='utf-8') as f:
                    lines = f.readlines()
                del lines[count]

                with open(file_base, "w", encoding='utf-8') as f:
                    f.writelines(lines)
                return True
            else:
                count += 1

        return False

def import_data(file_to_add, phonebook):
    try:
        with open(file_to_add, 'r', encoding='utf-8') as new_contacts, open(phonebook, 'a', encoding='utf-8') as file:
            contacts_to_add = new_contacts.readlines()
            file.writelines(contacts_to_add)
    except FileNotFoundError:
        print(f'{file_to_add} не найден')

def export_data(export_base):
    global all_data
    with open(export_base, 'w', encoding="utf-8") as f:
        for all_data in all_data:
            f.write(all_data + '\n')
    print("Export completed \n")

def main_menu():
    play = True
    while play:
        read_records()
        print(f"{'*' * 20}")
        answer = input("Phone book:\n"
                       "1. Show all records\n"
                       "2. Add a record\n"
                       "3. Search a record\n"
                       "4. Change\n"
                       "5. Delete\n"
                       "6. Exp/Imp\n"
                       "7. Exit\n")
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                find_contact(input("Enter searching name or number: ").title())
            case "4":
                search = input("Enter searching name or number: ").title()
                data = find_first(search)
                if len(data) == 0:
                    print('User not found')
                else:
                    data = {'surname': input('Enter surname: ').title(),
                            'name': input('Enter name: ').title(),
                            'patronymic': input('Enter patronymic: ').title(),
                            'phone_number': input('Enter phone number: ')}
                    change_contact(search, data)
            case "5":
                found = delete_contact(input("Enter searching name or number: ").title())
                if found == False:
                    print('User not found')
                else:
                    print('User deleted')
            case "6":
                play = True
                while play:
                    read_records()
                    print(f"{'*' * 20}")
                    answer = input("Export\import menu:\n"
                                   "1. Export phone book\n"
                                   "2. Import phone book\n"
                                   "3. Exit\n")
                    match answer:
                        case "1":
                            export_data((input("Enter a name of file without (.txt)\n")).strip()+".txt")
                        case "2":
                            import_data((input("Enter a imported base without (.txt)\n")).strip()+".txt", file_base)
                        case "3":
                            play = False
                        case _:
                            print("Try again!\n")

            case "7":
                play = False
            case _:
                print("Try again!\n")

main_menu()