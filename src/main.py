from calculators import give_BMI_calculator
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
            give_BMI_calculator()
        elif option == '2':
            print('here will be a Running Pace Calculator')
        elif option == '3':
            print('here will be a Maximum Heat Rate')
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