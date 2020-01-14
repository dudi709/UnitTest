
def calcBMI(height, weight):
    if height == 0:
        return "You cannot divide a number by 0"
    if height < 0 or weight <= 0:
        return "Invalid value" 
    return float("%.3f" %(weight/(height*height)))

def weightCheck(bmi_value):
    if bmi_value <= 0:
        return "Invalid value" 
    elif bmi_value < 18.5:
        return "Underweight"
    elif bmi_value >= 18.5 and bmi_value < 25:
        return "Normal weight"
    elif bmi_value >= 25 and bmi_value < 30:
        return "Overweight"
    elif bmi_value >= 30 and bmi_value < 35:
        return "Obesity Rank 1"
    elif bmi_value >= 35 and bmi_value < 40:
        return "Obesity Rank 2"
    elif bmi_value >= 40:
        return "Obesity Rank 3"
    
