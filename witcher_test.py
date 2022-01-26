from fileinput import filename
import json
import csv
from encodings import utf_8_sig

def main():
    show_menu = True
    
    while show_menu:
        print('1. CSV to Json')
        print('2. Show Json')
        print('3. Add')
        print('4. Delete')
        print('5. Save to CSV')
        print('6. Exit')
        
        menu_select = input('Välj ett alternativ från menyn: ')
        
        
        if menu_select == '1':
            csv_to_json()
            
        elif menu_select == '2':
            show_json()
            
        elif menu_select == '3':
            add_char()

        elif menu_select == '4':
            del_char()
            
        elif menu_select == '5':
            save_to_csv()
            
        elif menu_select == '6':
            show_menu = False
        else:
            print('Ogiltigt val, välj ett alternativ från menyn.')
    
    
def csv_to_json():
    print('Read CSV to Json')
    json_data = []
    
    with open('witcherraw.csv', 'r', encoding='utf-8-sig') as csvfile:
        csvData = csv.DictReader(csvfile)
        for row in csvData:
            json_data.append(row)
            
        print('Read Successful!')
    
    with open('witcher.json', 'w', encoding='utf-8-sig') as jsonfile:
        jsonString = json.dumps(json_data, ensure_ascii=False, indent=4)
        jsonfile.write(jsonString)


def show_json():
    print('Show json content')
    with open('witcher.json', 'r', encoding='utf-8-sig') as file:
        read = json.load(file)
    
    for row in read:
        print(row)


def add_char():
    print('add new character!')


def del_char():
    print('delete character!')


def save_to_csv():
    print('Save json to CSV')


main()