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