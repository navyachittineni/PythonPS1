#greatest of three numbers
def largest(a,b,c):
    greatest=a if a>b and b>c else(b if b>c else c)
    return greatest
print(largest(1,2,3))
#Leap year program
def is_leap_year(year):
    if not isinstance(year, int):  
        raise TypeError("Year must be an integer.")
    if year < 0:
        raise ValueError("Year must be a non-negative integer.")
    if (year % 4 == 0): 
        if (year % 100 == 0): 
            if (year % 400 == 0):   
                return True
            else:
                return False
        else:  
            return True
    else:
        return False
print(is_leap_year(1400))
#vowel,consonant or either
def classify_char(char):
    if 'a' <= char <= 'z':  # Check if it's an alphabet character
        if char in 'aeiou':
            return "vowel"
        else:
            return "consonant"
    else:
        return "neither"
print(classify_char('a'))
#grade check
marks=int(input("Enter marks: "))
if marks>=90 and marks<=100:
    print("Grade A")
elif marks>=80 and marks<90:
    print("Grade B")
elif marks>=70 and marks<80:
    print("Grade C")
else:
    print("Fail")
#triangle validation
a=int(input("Enter 1st side:"))
b=int(input("Enter 2nd side:"))
c=int(input("Enter 3rd side:"))
if a+b>c and a+c>b and b+c>a:
    print("valid triangle")
else:
    print("invalid triangle")
    



