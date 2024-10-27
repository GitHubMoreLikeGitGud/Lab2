def calculate_bmi(height, weight):
    print("Height=" + str(height))
    print("Weight=" + str(weight))
    
    # Calculate BMI
    bmi = weight / (height * height)
    
    # Display calculated BMI
    print("BMI = " + str(bmi))
    
    # Determine weight classification
    if bmi < 18.5:
        classification = "Under Weight"
    elif 18.5 <= bmi <= 25.0:
        classification = "Normal Weight"
    else:
        classification = "Over Weight"
    
    print("Weight Classification:", classification)

calculate_bmi(weight=57, height=1.73)
