from calculators import give_BMI_calculator, give_category, give_pace, give_HR_max
from input_utils import input_numbers, input_good_str, input_good_int

def give_menu():
    print('\n===== Sport Calculators CLI =====')
    print('1. Create/Edit Profile')
    print('2. BMI Calculator')
    print('3. Running Pace Calculator')
    print('4. Maximum Heat Rate')
    print('5. Heart Rate Zones')
    print('6. Calorie Calculator')
    print('7. Exit')

def create_pofile():
    name = input_good_str('\nEnter name: ')
    age = input_good_int('\nEnter age: ')
    weight = input_numbers('\nEnter weight (kg): ')
    height = input_numbers('\nEnter heigh (m): ')
    profile = {
    'name': name,
    'age' : age,
    'weight' : weight,
    'height' : height
    }
    return profile

def main():
    while True:
        
        give_menu()
        
        option = input("Select an option: ")
        
        if option == '1':
            
            create_pofile()
            
        elif option == '2':
            print('\n===== BMI Calculator =====')
        
            weight = input_numbers('\nEnter weight (kg): ')
            height = input_numbers('\nEnter heigh (m): ')

            BMI = give_BMI_calculator(weight, height)
            print(f'\nBMI = {round(BMI,2)}')

            give_category
        
        elif option == '3':
            
            print('\n===== Pace =====')

            distance = input_numbers('\nEnter distance (km): ')
            time = input_numbers('\nEnter time (min): ')

            pace = give_pace(distance, time)

            print(f'\nRunning pace = {round(pace,2)} min/km')
        
        elif option == '4':
            
            print('\n===== Maximum Heart Rate =====')
            
            age = input_numbers('\nEnter age: ')
            weight = input_numbers('\nEnter weight (kg): ')
            
            hr_max = give_HR_max(age,weight)
            print(f'\nMaximum Heart Rate = {round(hr_max,2)} bpm')
        
        elif option == '5':
            print('here will be a Heart Rate Zones')
        
        elif option == '6':
            print('here will be a Calorie Calculator')
        
        elif option == '7':
            break
        
        else:
            print('Invalid option.')

if __name__ == "__main__":
    main()