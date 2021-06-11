# Program to check if a number is prime or not

#num = 29

# To take input from the user
num = int(input("Enter a number other than one ,which you want to check is prime or not: "))

# define a flag variable
flag = False
#if (num) == 1
#print("one is neither prime nor composite")
# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")