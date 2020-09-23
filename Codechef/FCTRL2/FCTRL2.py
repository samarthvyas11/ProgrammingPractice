remaining_test_cases = int(input())
while remaining_test_cases > 0:
    fact_of_number = 1
    number = int(input())
    if number == 0 or number == 1:
        print(number)
    else:        
      for j in range(2,number + 1):
          fact_of_number = fact_of_number * j
      print(fact_of_number)   
    remaining_test_cases = remaining_test_cases - 1
