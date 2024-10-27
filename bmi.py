def calculate_bmi(height, weight):
    print("Height=" + str(height))
    print("Weight=" + str(weight))
    
    # Calculate BMI
    bmi = weight / (height * height)
    
    # Display calculated BMI
    print("BMI = " + str(bmi))
    
    # Determine weight classification and return value based on Table 1
    if bmi < 18.5:
        classification = "Under Weight"
        return_value = -1
    elif 18.5 <= bmi <= 25.0:
        classification = "Normal Weight"
        return_value = 0
    else:
        classification = "Over Weight"
        return_value = 1
    
    print("Weight Classification:", classification)
    return return_value

# Example usage
result = calculate_bmi(weight=57, height=1.73)
print("Return Value:", result)
