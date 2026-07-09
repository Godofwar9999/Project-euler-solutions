sum_of_squares = 0
for i in range(100):
    sum_of_squares += ((i+1)*(i+1))

sum1 = 0
for i in range(100):
    sum1 += (i+1)
    
sum_of_square_1 = sum1*sum1

difference_of_squares = sum_of_square_1 - sum_of_squares
print(difference_of_squares)