num = int(input("\nEnter a Number: "))

if num < 0:
    print("Square root of a negative number is not a real number.")
elif num == 0 or num == 1:  
    print("\nSquare Root:", num)
else:
    a = num
    b = (a + (num / a)) / 2
    while abs(b - a) >= 0.000001:  
        a = b
        b = (a + (num / a)) / 2
    print("\nSquare Root:", round(b, 6))  
