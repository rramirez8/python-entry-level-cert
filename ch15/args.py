def contact_card(name, age, car_model):
	return f"{name} is {age} and drives a {car_model}."

strCall1 = contact_card("Richard",52, "Escalade")
strCall2 = contact_card(age=52, name="Richard", car_model="Escalade")
strCall3 = contact_card("Richard", car_model="Escalade", age=52)

print(strCall1)
print(strCall2)
print(strCall3)

# so arguments refer to what is passed when the function is being called
# and parameters refer to what is being passed into the def of the function

# you can pass arguments positionally, or using keywords with an equals
# you can mix the 2 but once you start using keywords with equals you cannot use positional

#NEXT example - setting defaults values to parameters
# when call a function with arguments and default arguments, all normal args must be passed before any defaulted args.

def can_drive(age, driving_age=16):
	return age >= driving_age

print("Calling can_drive with 15")
print(can_drive(15))
print("Calling can_drive with 17")
print(can_drive(17))
