def is_prime(num):#function that returns true or false if the number is a prime number
    for i in range(2, num ):
        if num % i == 0:
            return False
    return True

a = 2
c = 0
while c < 10:
    if is_prime(a) == True:
        print(a)
        c += 1
    a +=1