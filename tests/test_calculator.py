from src.calculators import give_BMI_calculator, give_HR_max, give_pace

def test_give_BMI_calculator():
    result = give_BMI_calculator(85,1.84)

def test_give_bmi_calculator():
        
    result = give_BMI_calculator(80, 1.8)

    assert round(result, 2) == 24.69
    
def test_give_pace():

    result = give_pace(10,50)

    assert result == 5
    
def test_give_HR_max():

    result = give_HR_max(20,80)

    assert result == 198.24