def input_numbers(message):
    
    while True: 
        
        number = input(message)
        
        try:
            
            value = float(number.replace(',','.'))
            
            if value <= 0:
                print('\nValue must be greater than 0')
                continue
            return value
        
        except ValueError:
            print('\nEnter the correct number')