def get_num_of_characters(inputStr):
    count = 0
    for i in range(len(inputStr)):
        count += 1
    return count

def output_without_whitespace(inputStr):
    inputStr = inputStr.replace(" ","")
    print("String with no whitespace: %s" %inputStr)

if __name__ == '__main__':
    inputStr = input("Enter a sentence or phrase:\n")
    print("")
    print("You entered: %s" %inputStr)
    print("")
    print("Number of characters: %s" %(get_num_of_characters(inputStr)))
    output_without_whitespace(inputStr)