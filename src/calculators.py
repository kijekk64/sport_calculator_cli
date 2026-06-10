def give_BMI_calculator():
    print('\n===== BMI Calculator =====')
   
    weight = float(input('\nEnter weight (kg): '))
    height = float(input('\nEnter heigh (m): '))
    
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