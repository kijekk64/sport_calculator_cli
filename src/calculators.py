from input_utils import input_numbers

def give_BMI_calculator():
    
    print('\n===== BMI Calculator =====')
   
    weight = input_numbers('\nEnter weight (kg): ')
    height = input_numbers('\nEnter heigh (m): ')
    
    BMI = weight/(height**2)
    print(f'\nBMI = {round(BMI,2)}')
    
    if BMI <= 18.5:
        print("\nCategory: underweight")
    elif BMI > 18.5 and BMI <= 24.9:
        print('\nCategory: standart')
    elif BMI > 24.9 and BMI <= 29.9:
        print('\nCategory: overweight')
    else:
        print('\nCategory: obesity')
    
def give_pace():
    
    print('\n===== Pace =====')
    
    distance = input_numbers('\nEnter distance (km): ')
    time = input_numbers('\nEnter time (min): ')

    pace = time/distance 
    print(f'\nRunning pace = {round(pace,2)} min/km')

def give_HR_max():
    
    print('\n===== Maximum Heart Rate =====')
    
    age = input_numbers('\nEnter age: ')
    weight = input_numbers('\nEnter weight (kg): ')
    hr_max = 210 - (0.5*age) - (0.022*weight)
    print(f'\nMaximum Heart Rate = {round(hr_max,2)} bpm')