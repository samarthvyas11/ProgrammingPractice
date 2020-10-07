remaining_test_cases = int(input())
while remaining_test_cases > 0:
    dividend,divisor = map(int,input().split())
    remainder = dividend % divisor
    print(remainder)
    remaining_test_cases = remaining_test_cases - 1
