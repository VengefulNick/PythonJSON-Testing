
import json
import csv


def main():
    show_menu = True
    
    while show_menu:
        mainmenu()
        menu_select = input('Pick an option from menu: ')
        
        if menu_select == '1':
            csv_to_json()
            
        elif menu_select == '2':
            show_json()
            
        elif menu_select == '3':
            new = input_new()
            add_char(new)

        elif menu_select == '4':
            del_char()
            
        elif menu_select == '5':
            modify_char()
            
        elif menu_select == '6':
            new_property()
            
        elif menu_select == '9':
            save_to_csv()
            
        elif menu_select == '0':
            show_menu = False
        else:
            print('Invalid option, try again!')
    
"""
Menu Functions
"""

def csv_to_json():  # 1
    print('Read CSV to Json\n')

                    # Objects in Array / Dicts in List
    json_data = []
    with open('witcher.csv', 'r', encoding='utf-8') as csvfile:
        csvData = csv.DictReader(csvfile)
        for row in csvData:
            json_data.append(row)
            
                    # Objects in Object / Dicts in Dict
#    json_data = {}  
#    with open('witcher.csv', 'r', encoding='utf-8') as csvfile:
#        csvData = csv.DictReader(csvfile)
#        for row in csvData:
#            json_data[row['Name']] = row
            
        print('\n\tRead Successful!\n')
    
    with open('witcher.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile, ensure_ascii=False, indent=4)
        print('\tWrite Successful!\n')


def show_json():    # 2
    print('\nShow JSON Content\n')
    with open('witcher.json', 'r', encoding='utf-8') as jsonfile:
        read = json.load(jsonfile)
    
    for row in read:
        print(row)


def add_char(new):  # 3
    print('\nAdd new character!\n')
    with open('witcher.json', 'r', encoding='utf_8') as jsonfile:
        read = json.load(jsonfile)

    with open('witcher.json', 'w', encoding='utf-8') as jsonfile:
        data = read
        print('\n\tReading old content OK!')
        
        data.append(new)
        print('\n\tSuccess adding new input!')
        
        json.dump(data, jsonfile, indent=4)
        print(f'\nOverwrite Successful!\n{new} was added!')


def del_char(): # 4
    print('\nDelete character!\n')
    with open('witcher.json', 'r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)

        for index, value in enumerate(data):
            print(f'{index}: {value}')
        print('\nEnter index of character you want to delete:')
        del_input = input_num()
        try:
            data.pop(del_input)
            print(f'\n\tSuccessfully removed character on index: {del_input}')
        except IndexError:
            print('Number is not in list, returning to menu!')


    with open('witcher.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)


def modify_char():  # 5
    print('\nModify character!\n')
    with open('witcher.json', 'r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
        
    for index, value in enumerate(data):
        print(f'{index}: {value}')
    print('\nEnter index of character to modify:')
    mod_input = input_num()
    try:
        print(data[mod_input])
        modmenu()
        mod_select = input('Enter number from menu: ')
        if mod_select == '1':
            print('\nModify name')
            new_name = input_str()
            data[mod_input]['Name'] = new_name
            print(f'Successfully modified character name to: {new_name}')
        elif mod_select == '2':
            print('\nModify alias')
            new_alias = input_str()
            data[mod_input]['Alias'] = new_alias
            print(f'Successfully modified character name to: {new_alias}')
        elif mod_select == '3':
            print('\nModify proffession')
            new_prof = input_str()
            data[mod_input]['Profession'] = new_prof
            print(f'Successfully modified character name to: {new_prof}')
        elif mod_select == '4':
            print('\nModify hair-color')
            new_hair = input_str()
            data[mod_input]['Hair-Color'] = new_hair
            print(f'Successfully modified character name to: {new_hair}')
        elif mod_select == '5':
            print('\nModify eye-color')
            new_eye = input_str()
            data[mod_input]['Eye-Color'] = new_eye
            print(f'Successfully modified character name to: {new_eye}') 
        else:
            print('Invalid choice. Returning to menu!\n')
    except IndexError:
        print('Number is not in list, returning to menu!\n')
        
    with open('witcher.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)


def new_property(): #6
    with open('witcher.json', 'r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
    prop_name = input('Enter new property name: ')
    count = 0
    for row in data:
        data[count][prop_name] = ""
        print(f'Added property {prop_name} to {row}')
        count += 1
                
    with open('witcher.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)


def save_to_csv(): #9
    print('\nSave json to CSV\n')
    with open('witcher.json', 'r', encoding='utf-8') as jsonfile:
        json_data = json.load(jsonfile)
        
    with open('witcher.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_data = csv.writer(csvfile)
        count = 0
        
        for character in json_data:
            if count == 0:
                header = character.keys()
                csv_data.writerow(header)
                count += 1
            characters = character.values()
            csv_data.writerow(characters)
    print('\n\tSave to CSV Successful!\n')

"""
Extra functions
"""

def mainmenu():
    print("""
«-------Main-Menu-------»
 |   1. CSV to Json    |
 |   2. Show Json      |
 |   3. Add Char       |
 |   4. Delete Char    |
 |   5. Modify Char    |
 |   6. New Property   |
 |   9. Save to CSV    |
 |   0. Exit           |
«-----------------------»
    """)


def modmenu():
    print('''
    Which value do you want to modify:
    1. Name
    2. Alias
    3. Proffession
    4. Hair-Color
    5. Eye-Color
    ''')

    
def input_new():
    print('Enter name:')
    name_input = input_str()
    print('Enter alias:')
    alias_input = input('')
    print('Enter profession:')
    prof_input = input_str()
    print('Enter hair-color:')
    hair_input = input_str()
    print('Enter eye-color:')
    eye_input = input_str()
   
    new = {'Name': name_input, 'Alias': alias_input, 'Profession': prof_input, 'Hair-Color': hair_input, 'Eye-Color': eye_input}
    # new = {"Name": "Calanthe", "Alias": "Lioness", "Profession": "Queen", "Hair-Color": "Black", "Eye-Color": "Blue"}
    return new


def input_str():        # Input checker for empty string.
    str = input('')
    if(len(str.strip())):
        return str
    else:
        print('Input cannot be empty!')
        return input_str()


def input_num():        # Inputchecker for integer.
    int_input = input('Enter number: ')
    try:
        return int(int_input)
    except ValueError:
        print('Input is not a number, try again!')
        return input_num()


"""
Run Program
"""


main()