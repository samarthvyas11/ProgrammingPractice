remaining_test_cases = int(input())
while remaining_test_cases > 0:
    number_as_string = input()
    total_sum = 0
    for str_chr in range(len(number_as_string)):
        char_from_str = number_as_string[str_chr]
        char_to_int = int(char_from_str)
        total_sum = total_sum + char_to_int
    print(total_sum)
    remaining_test_cases = remaining_test_cases - 1
    
