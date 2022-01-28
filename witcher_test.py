
import json
import csv
from encodings import utf_8
from textwrap import indent

def main():
    show_menu = True
    
    while show_menu:
        print('1. CSV to Json')
        print('2. Show Json')
        print('3. Add')
        print('4. Delete')
        print('5. Save to CSV')
        print('6. Exit\n')
        
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
            save_to_csv()
            
        elif menu_select == '6':
            show_menu = False
        else:
            print('Invalid option, try again!')
    
""" Menu Functions """
 
def csv_to_json():
    print('\nRead CSV to Json\n')

                    # Objects in Array / Dicts in List
    json_data = []
    with open('witcher.csv', 'r', encoding='utf-8') as csvfile:
        csvData = csv.DictReader(csvfile)
        for row in csvData:
            json_data.append(row)
            
                    # Objects in Object / Dicts in Dict
#    json_data = {}  
#    with open('witcher.csv', 'r', encoding='utf-8-sig') as csvfile:
#        csvData = csv.DictReader(csvfile)
#        for row in csvData:
#            json_data[row['Name']] = row
            
        print('\n\tRead Successful!\n')
    
    with open('witcher.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile, ensure_ascii=False, indent=4)
        print('\tWrite Successful!\n')


def show_json():
    print('\nShow JSON Content\n')
    with open('witcher.json', 'r', encoding='utf-8') as jsonfile:
        read = json.load(jsonfile)
    
    for i in read:
        print(i)
    print()


def add_char(new):
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


def del_char():
    print('\nDelete character!\n')
    with open('witcher.json', 'r', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
        
        for index, value in enumerate(data):
            print(index, value)
        print('\nEnter index of character you want to delete: ')
        del_input = input_num()
        data.pop(del_input)
        print(f'\n\tSuccessfully removed character on index: {del_input}')
        
    with open('witcher.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)


def save_to_csv():
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


""" Extra functions """

def input_new(): 
    print('Enter name: ')
    name_input = input_str()
    print('Enter alias: ')
    alias_input = input('')
    print('Enter profession: ')
    prof_input = input_str()
    print('Enter hair-color: ')
    hair_input = input_str()
    print('Enter eye-color: ')
    eye_input = input_str()
       
    new = {'Name': name_input, 'Alias': alias_input, 'Profession': prof_input, 'Hair-Color': hair_input, 'Eye-Color': eye_input}
    # new = {"Name": "Calanthe", "Alias": "Lioness", "Profession": "Queen", "Hair-Color": "Black", "Eye-Color": "Blue"}
    return new


def input_str():
    str = input('')
    if(len(str)):
        return str
    else:
        print('Input cannot be empty!')
        return input_str()


def input_num():
    int_input = input('Enter number: ')
    try:
        return int(int_input)
    except ValueError:
        print('Input is not a number, try again!')
        return input_num()


""" Run Program """

main()