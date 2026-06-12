from calculators import give_BMI_calculator, give_category, give_pace, give_HR_max, give_heart_rate_zones
from input_utils import input_numbers, input_good_str, input_good_int
from user_storage import save_profile, load_profile

def give_menu():
    print('\n===== Sport Calculators CLI =====')
    print('1. Create/Edit Profile')
    print('2. Show Profile')
    print('3. BMI Calculator')
    print('4. Running Pace Calculator')
    print('5. Maximum Heart Rate And Heart Rate Zones')
    print('6. Exit')

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

    save_profile(profile)

    print('\nThe profile has been saved')

def show_profile():
    
    profile = load_profile()

    if profile is None:
        print('\nNie masz jeszcze zapisanego profilu.')
        print('Najpierw wybierz opcję 1.')
        return
    
    print('\n===== Profile =====\n')

    print('-'*20)

    for given, answer in profile.items():
        
        print(f'{given}: {answer}')
    
    print('-'*20)

def get_profile_or_show_message():
    profile = load_profile()

    if profile is None:
        print('\nNajpierw utwórz profil.')
        print('Wybierz opcję 1 w menu.')
        return None

    return profile

def main():
    while True:
        
        give_menu()
        
        option = input('Select an option: ')
        
        if option == '1':

            print('\n===== Profile Creator =====')
                
            create_pofile()

        elif option == '2':

            print('\n===== Profile =====')

            show_profile()
            
        elif option == '3':
            
            print('\n===== BMI Calculator =====')

            profile = get_profile_or_show_message()

            if profile is None:
                return
    
            weight = profile['weight']
            height = profile['height']

            BMI = give_BMI_calculator(weight, height)
            print(f'\nBMI = {round(BMI,2)}')

            give_category(BMI)
        
        elif option == '4':
            
            print('\n===== Pace =====')

            distance = input_numbers('\nEnter distance (km): ')
            time = input_numbers('\nEnter time (min): ')

            pace = give_pace(distance, time)

            print(f'\nRunning pace = {round(pace,2)} min/km')
        
        elif option == '5':
            
            print('\n===== Maximum Heart Rate And Heart Rate Zones =====')
            
            profile = get_profile_or_show_message()

            if profile is None:
                return
            
            age = profile['age']

            weight = profile['weight']

            hr_max = give_HR_max(age,weight)
            print(f'\nMaximum Heart Rate = {round(hr_max,2)} bpm')

            zones = give_heart_rate_zones(hr_max)

            print('\n===== Heart Rate Zones =====\n')

            print('-'*35)

            for zone_name, heart_range in zones.items():
                
                low, high = heart_range
                print(f'{zone_name}: {low}-{high}  bpm')
            
            print('-'*35)

        elif option == '6':
            break
        
        else:
            print('Invalid option.')

if __name__ == "__main__":
    main()