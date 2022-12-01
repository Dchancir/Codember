def check_zeros(number):
    for digit in str(number):
        if digit == '0':
            return False
    return True

def checkNumber(number):
    old_digit = int(str(number)[0])
    temp = int(str(number)[1:])
    quantity_of_5s = 1 if old_digit == 5 else 0
    while(temp > 0):
        digit = int(str(temp)[0])
        # Check > rule
        if(old_digit > digit):
            return False

        # Check if it's a five
        if (digit == 5):
            quantity_of_5s += 1
        
        temp = int(str(temp)[1:]) if temp//10 > 0 else 0
        old_digit = digit
    if (quantity_of_5s < 2):
        return False
    return True
        

candidate_numbers = list(range(11098, 98123, 1))
candidate_numbers = list(filter(check_zeros, candidate_numbers))
candidate_numbers = list(filter(checkNumber, candidate_numbers))

print(len(candidate_numbers))
        
    

