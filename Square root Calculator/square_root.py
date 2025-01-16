number=int(input("Enter a number:"))
z=1
if number < 0:
     print("Square root of a negative number is not a real number.")
else:
    for num in range(number):
        if number==(z*z):
            break
        z=z+1
    z= (z+number/z)/2
    err=abs(number-z**2)
    if err==0:
        print("The Square root of ",number ,"is",z)