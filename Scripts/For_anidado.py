# A program to print all the prime numbers
# between 2 and 50

start_number = 2
end_number = 50
current_number = start_number
for current_number in range (start_number, end_number+1):
    is_current_number_prime = True
    for current_divisor in range (2, current_number):
        if current_number % current_divisor == 0:
            is_current_number_prime = False
            break
    if is_current_number_prime:
        print (current_number, " is prime")
print ("All done!")
