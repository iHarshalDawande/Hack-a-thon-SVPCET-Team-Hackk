medical_data = {}

while True:
    name = input("Enter the patient's name: ")
    test_name = input("Enter the name of the test: ")
    test_result = input("Enter the result of the test: ")
    
    if name not in medical_data:
        medical_data[name] = {}
        
    medical_data[name][test_name] = test_result
    
    continue_testing = input("Do you want to enter another test for this patient (yes/no)? ")
    if continue_testing.lower() == "no":
        break

print(medical_data)
