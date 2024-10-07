def gcdFinder(num1,num2):
    smallerNumebr = min(num1,num2)
    for i in range(smallerNumebr,0,-1):
        if num1 % i == 0 and num2 % i == 0:
            return i

number_list = list(map(int,input("Enter two numbers: ").split(",")))
print(f"GCD of {number_list[0]} and {number_list[1]} is : {gcdFinder(number_list[0],number_list[1])}")