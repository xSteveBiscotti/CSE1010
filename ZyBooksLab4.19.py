# Type your code here
def automobile():
 
 
# Display the menu
 
 print("Davy's auto shop services")
 
 print("Oil change -- $35")
 
 print("Tire rotation -- $19")
 
 print("Car wash -- $7")
 
 print("Car wax -- $12")
 
 print('')
 
# Declare and initialize the Variables
 
changeOil = 35;
 
rotationTire = 19;
 
washCar = 7;
 
waxCar = 12;
 
t = 0;
 
service1 = 0;
 
service2 = 0;
 
# Call to the function
 
automobile()
 
# Prompt the user to enter the service.
 
first_ser = input("Select first service:\n")
 
# Check whether the service is oil change or not
 
if (first_ser == "Oil change"):
 
# Add the cost of oil Change.
 
  t = t + changeOil;
 
  service1 = changeOil;
 
# Check whether the service is Tire rotation or not
 
elif (first_ser == "Tire rotation"):
 
# Add the cost of Tire rotation.
 
  t = t + rotationTire;
 
# Assigning value to variable.
 
  service1 = rotationTire;
 
# Check whether the service is Car wash or not
 
elif (first_ser == "Car wash"):
 
# Add the cost of Car wash.
 
  t = t + washCar;
 
# Assigning value to variable.
 
  service1 = washCar;
 
# Check whether the service is Car wax or not
 
elif (first_ser == "Car wax"):
 
# Add the cost of Car wax.
 
  t = t + waxCar;
 
# Assigning value to variable.
 
  service1 = waxCar;
 
# Check whether the service is - or not
 
elif (first_ser == "-"):
 
  first_ser = "No service";
 
# Add the cost of no service.
 
  t = t + 0;
 
# Prompt the user to enter the service.
 
secondService = input("Select second service:\n")
 
# Check whether the service is oil change or not
 
if (secondService == "Oil change"):
 
# Add the cost of Car wax.
 
  t = t + changeOil;
 
# Assigning value to variable.
 
  service2 = changeOil;
 
# Check whether the service is Tire rotation or not
 
elif (secondService == "Tire rotation"):
 
# Add the cost of Tire rotation.
 
  t = t + rotationTire;
 
# Assigning value to variable.
 
  service2 = rotationTire;
 
# Check whether the service is Car wash or not
 
elif (secondService == "Car wash"):
 
# Add the cost of Car wash.
 
  t = t + washCar;
 
# Assigning value to variable.
 
  service2 = washCar;
 
# Check whether the service is Car wax or not
 
elif (secondService == "Car wax"):
 
# Add the cost of Car wax.
 
  t = t + waxCar;
 
# Assigning value to variable.
 
  service2 = waxCar;
 
# Check whether the service is - or not
 
elif (secondService == "-"):
 
  secondService = "No service";
 
  service2 = 0;
 
  t = t + 0;
 
# Display the results.
 
print()
 
print("Davy's auto shop invoice")
 
print()
 
if (first_ser == "No service") and (secondService == "No service"):
 
    print("Service 1: " + first_ser)
    print('')
    
 
    print("Service 2: " + secondService)
    print('')
    print()
 
 
 
elif (secondService == "No service"):
 
  print("Service 1: " + first_ser + ", $" + str(service1))
 
  print("Service 2: " + secondService)
 
  print()
 
elif (first_ser == "No service"):
 
  print("Service 1: " + first_ser)
 
  print("Service 2: " + secondService + ", $" + str(service2))
 
  print()
 
else:
 
  print("Service 1: " + first_ser + ", $" + str(service1))
 
  print("Service 2: " + secondService + ", $" + str(service2))
 
  print()
 
print("Total: $" + str(t))