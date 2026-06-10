from calculators import give_BMI_calculator, give_category, give_pace, give_HR_max
from input_utils import input_numbers

def give_menu():
    print('\n===== Sport Calculators CLI =====')

    print('\n1. BMI Calculator')
    print('2. Running Pace Calculator')
    print('3. Maximum Heat Rate')
    print('4. Heart Rate Zones')
    print('5. Calorie Calculator')
    print('6. Exit')
def main():
    while True:
        
        give_menu()
        
        option = input("Select an option: ")
        
        if option == '1':
            print('\n===== BMI Calculator =====')
        
            weight = input_numbers('\nEnter weight (kg): ')
            height = input_numbers('\nEnter heigh (m): ')

            BMI = give_BMI_calculator(weight, height)
            print(f'\nBMI = {round(BMI,2)}')

            give_category
        
        elif option == '2':
            
            print('\n===== Pace =====')

            distance = input_numbers('\nEnter distance (km): ')
            time = input_numbers('\nEnter time (min): ')

            pace = give_pace(distance, time)

            print(f'\nRunning pace = {round(pace,2)} min/km')
        
        elif option == '3':
            
            print('\n===== Maximum Heart Rate =====')
            
            age = input_numbers('\nEnter age: ')
            weight = input_numbers('\nEnter weight (kg): ')
            
            hr_max = give_HR_max(age,weight)
            print(f'\nMaximum Heart Rate = {round(hr_max,2)} bpm')
        
        elif option == '4':
            print('here will be a Heart Rate Zones')
        
        elif option == '5':
            print('here will be a Calorie Calculator')
        
        elif option == '6':
            break
        
        else:
            print('Invalid option.')

if __name__ == "__main__":
    main()