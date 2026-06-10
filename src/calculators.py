def give_BMI_calculator(weight,height):
    
    BMI = weight/(height**2)
    return BMI

def give_category(BMI):
    if BMI <= 18.5:
        print("\nCategory: underweight")
    elif BMI > 18.5 and BMI <= 24.9:
        print('\nCategory: standart')
    elif BMI > 24.9 and BMI <= 29.9:
        print('\nCategory: overweight')
    else:
        print('\nCategory: obesity')
    
def give_pace(distance, time):
    
    pace = time/distance 
    return pace

def give_HR_max(age,weight):
    
    hr_max = 210 - (0.5*age) - (0.022*weight)
    return hr_max