# cook your dish here
import math
remaining_test_cases = int(input())
while remaining_test_cases > 0:
    flag = 0
    total_number_of_query,query_per_day=map(int,input().split())
    query = list(map(int,input().split()))
    sum_query = 0
    days_taken = 0
    for i in range(total_number_of_query):
        sum_query = sum_query + query[i]
        if sum_query < (i+1)*query_per_day:
            flag = 1
            print(i+1)
            break
    if flag == 0:
        print(total_number_of_query+((sum_query - total_number_of_query*query_per_day)//query_per_day)+1)
    
    
    
    remaining_test_cases = remaining_test_cases - 1