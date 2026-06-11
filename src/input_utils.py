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

def input_good_str(message):
    
    while True:
        input_str = input(message).strip()
        
        if input_str:
            return input_str
        
        print('\nEnter your name!')
    
def input_good_int(message):
    
    while True:
       
        try:
            
            input_str = int(input(message))

            if input_str <= 0:
                print('\nValue must be greater than 0')
                continue
            return input_str
        
        except ValueError:
            print('\nEnter the correct number')