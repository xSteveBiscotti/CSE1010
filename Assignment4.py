cust_name =    input("Customer name: ")
cust_address = input("      Address: ")
cust_city =    input("         City: ")
cust_state =   input("        State: ")
cust_zip =     input("          Zip: ")
print(cust_name)
print(cust_address)
items = {"Chairs" : 25, "Tables" : 45, "Stools" : 20}
for x in items:
      print(x, items[x])
no_chairs =  input("Number of  Chairs: ")
no_tables =    input("Number of Tables: ")
no_stools = input("Number of Stools: ")
total_chairs =  int(no_chairs) * int(items["Chairs"])
total_tables =    int(no_tables) * int(items["Tables"])
total_stools = int(no_stools) * int(items["Stools"])
total_charge = int(total_chairs) + int(total_tables) + int(total_stools)
print(cust_name)
print(cust_address)
print(cust_city)
print(cust_zip)
print(total_charge)
mychairs = "You Bought {} number of chairs at {} = {} dollars."
print(mychairs.format(no_chairs, items["Chairs"], total_chairs))
mytables = "               {} number of tables at {} = {} dollars."
print(mytables.format(no_tables, items["Tables"], total_tables))
mystools = "         {} number of stools at {} = {} dollars."
print(mystools.format(no_stools, items["Stools"], total_stools))
mytotal = "                   Total Amount Due = {} dollars."
print(mytotal.format(total_charge))