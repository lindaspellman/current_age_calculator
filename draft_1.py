from datetime import datetime

current_day = datetime.now().day
current_month = datetime.now().month
current_year = datetime.now().year

print("Current Month: " + str(current_month))
print("Current Year: " + str(current_year))

name = input('Name of Person: ')
sex = input('Male or female (M/F): ').upper() 
# print(f"Sex: {sex}")
birth_month = int(input('Birth Month (number format): '))
birth_day = int(input('Birthday: '))
birth_year = int(input('Birth Year: '))

approx_age = current_year - birth_year
# print("Will turn: " + str(approx_age))

if sex == 'M':
    third_person_pronoun = 'He'
else: 
    third_person_pronoun = 'She'


if birth_month > current_month:
    approx_age -= 1

    print(f"{name} is currently {approx_age} year(s) old. {third_person_pronoun} will turn {approx_age + 1} later this year.")
else: 
    print(f"{name} is currently {approx_age} year(s) old.")