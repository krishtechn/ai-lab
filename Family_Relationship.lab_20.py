# Program to identify family relationship

gender = input("Enter a gender of person A(male/female): ").lower()
relation = input("Enter relationship (parent/sibling/child): ").lower()

if relation == "parent":
    if gender == "male":
     print("person A is the father: ")
    else:
     print("person A is the mother")
elif relation == "child":
    if gender == "male":
     print("person A is the son")
    else: 
     print("person A is the Daughter")
elif relation == "sibling": 
    if gender == "male":
     print("person A is the Brother")
    else:  
     print("person A is the sister")
else:
    print("unknown relationship:")
