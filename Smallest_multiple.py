number = 1
divisible_by_all_numbers_from_1_to_20 = False
while divisible_by_all_numbers_from_1_to_20 != True:
    if number%1 == 0 and number%2 == 0 and number%3 == 0 and number%4 == 0 and number%5 == 0 and number%6 == 0 and number%7 == 0 and number%8 == 0 and number%9 == 0 and number%10 == 0 and number%11 == 0 and number%12 == 0 and number%13 == 0 and number%15 == 0 and number%16 == 0 and number%17 == 0 and number%18 == 0 and number%19 == 0 and number%20 == 0:
        print(number)
        divisible_by_all_numbers_from_1_to_20 = True
    else:
        number += 1
        pass