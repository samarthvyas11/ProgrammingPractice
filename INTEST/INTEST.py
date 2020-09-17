number_of_divisibility_test,dividend = map(int,input().split())
count_of_divisible_number = 0
for i in range(number_of_divisibility_test):
    divisor = int(input())
    if divisor % dividend == 0:
        count_of_divisible_number = count_of_divisible_number + 1
print(count_of_divisible_number)        
        
