# 19.Write a program to find the sum of the digits of a given number.
def digit_sum(number):
   
    digits = list(str(number))

   
    digit_sum = 0

   
    for digit in digits:
        digit_sum += int(digit)

    return digit_sum



number = 12345
sum_of_digits = digit_sum(number)
print(f"The sum of the digits of {number} is {sum_of_digits}.")
