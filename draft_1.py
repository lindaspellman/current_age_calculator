from datetime import datetime

current_day = datetime.now().day
current_month = datetime.now().month
current_year = datetime.now().year
sex_not_real = False 

def input_sex():
    sex = input('Male or female (M/F): ').upper()
    third_person_pronoun = ''
    if sex != 'M' or sex != 'F':
        sex_not_real == True  
        while sex_not_real:
            print('Please enter a valid answer.')
            if sex == 'M':
                return 'He'
            elif sex == 'F':
                return 'She'
            else:
                input_sex()

print("Current Month: " + str(current_month))
print("Current Day: " + str(current_day))
print("Current Year: " + str(current_year))

name = input('Name of Person: ').title()

third_person_pronoun = input_sex()

    

# print(f"Sex: {sex}")
birth_month = int(input('Birth Month (number format): '))
birth_day = int(input('Birth Day (only the day number): '))
birth_year = int(input('Birth Year: '))

approx_age = current_year - birth_year
# print("Will turn: " + str(approx_age))





# if birth_month >= current_month and birth_day >= current_day:
#     print(f"{name} is currently {approx_age} year(s) old.")


if current_month == birth_month:
    if current_day < birth_day:
        approx_age -= 1
        print(f"{name} is currently {approx_age} year(s) old. {third_person_pronoun} will turn {approx_age + 1} this month in about {birth_day - current_day} days.")
    if current_day >= birth_day:
        print(f"{name} is currently {approx_age} year(s) old.")

elif current_month < birth_month:
    approx_age -= 1
    print(f"{name} is currently {approx_age} year(s) old. {third_person_pronoun} will turn {approx_age + 1} in about {birth_month - current_month} months.")

elif current_month > birth_month:
    print(f"{name} is currently {approx_age} year(s) old. {third_person_pronoun} will turn {approx_age + 1} next year in about {12 - current_month + birth_month} months.")

    
     

