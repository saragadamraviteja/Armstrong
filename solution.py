# Write a program determine whether the given number is Armstrong number or not.
# The program should return true or false

def checkArmstrong(num):
        # Your code goes here
        s = 0
        temp = num
        while temp>0:
                dig = temp%10
                s += dig **3
                temp //= 10
        if num == sum:
                return True
        return False
