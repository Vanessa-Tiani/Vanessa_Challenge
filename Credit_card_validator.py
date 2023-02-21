
# importing the regex(re) module
import re

#Customer inputs the number of credit cards and converts it to integer
number_of_cards = int(input())

#Base on the number of cards interate through the list
for number in range(number_of_cards):
    
    #Get the actual card number and add it to the input
    get_card_number = input().strip()
    #Look for invalid special characters to exclude from the card number
    character_to_exclude = re.compile('[@_!#$%^&*()<>?/\|}{~: A-zA]')
    #Find all the ivalid special character in the card number
    invalid_characters = character_to_exclude.findall(get_card_number)

    #If the lenght of my list is not equal to 0, then there is special character
    if (len(invalid_characters) == 0): 
        #Strip all hypen(-)         
        credit_removed_hiphen = get_card_number.replace('-','')
        
        #Return true or false if card number is 16 and starts with 4,5 or 6
        check_if_length_16 = bool(re.match(r'^[4-6]\d{15}$', get_card_number))
        
        #Return true or false if card number is 19 or not and starts with 4,5 or 6
        check_if_length_19 = bool(re.match(r'^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$', get_card_number))  
        
        #Return true or false if card number has 4 or more consecutive numbers
        check_if_consecutive = bool(re.findall(r'(?=(\d)\1\1\1)', credit_removed_hiphen))
        
        #Check for conditions
        if (check_if_consecutive == True):
            print('Invalid') 
        elif (check_if_length_16 == True or check_if_length_19 == True): 
            print('Valid')
        elif (check_if_length_16 == False or check_if_length_19 == False):
            print('Invalid') 
         
    #This else print invalid if the card has any of the invalid special charaters   
    else:
        print('Invalid')         