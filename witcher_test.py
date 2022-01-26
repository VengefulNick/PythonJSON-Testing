from fileinput import filename
import json
import csv
from encodings import utf_8_sig

from pkg_resources import ensure_directory

def main():
    show_menu = True
    
    while show_menu:
        print('1. CSV to Json')
        print('2. Show Json')
        print('3. Add')
        print('4. Delete')
        print('5. Save to CSV')
        print('6. Exit')
        
        menu_select = input('Pick an option from menu: ')
        
        if menu_select == '1':
            csv_to_json()
            
        elif menu_select == '2':
            show_json()
            
        elif menu_select == '3':
            x = {"Name": "Calanthe", "Alias": "Lioness", "Profession": "Queen", "Hair-Color": "Black", "Eye-Color": "Blue"}
            add_char(x)

        elif menu_select == '4':
            del_char()
            
        elif menu_select == '5':
            save_to_csv()
            
        elif menu_select == '6':
            show_menu = False
        else:
            print('Invalid option, try again!')
    
    
def csv_to_json():
    print('\nRead CSV to Json\n')
    json_data = {}
    
    with open('witcherraw.csv', 'r', encoding='utf-8-sig') as csvfile:
        csvData = csv.DictReader(csvfile)
        for row in csvData:
            json_data[row['Name']] = row
            
        print('\tRead Successful!\n')
    
    with open('witcher.json', 'w', encoding='utf-8-sig') as jsonfile:
        jsonString = json.dumps(json_data, ensure_ascii=False, indent=4)
        jsonfile.write(jsonString)
        print('\tWrite Successful!\n')

def show_json():
    print('\nShow JSON Content\n')
    with open('witcher.json', 'r', encoding='utf-8-sig') as file:
        read = json.load(file)
    
    for i in read:
        print(i)
    print()

def add_char(new):
    print('\nAdd new character!\n')


def del_char():
    print('\nDelete character!\n')


def save_to_csv():
    print('\nSave json to CSV\n')


main()