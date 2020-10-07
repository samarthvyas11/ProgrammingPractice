# cook your dish here
import math
remaing_test_cases = int(input())
while remaing_test_cases > 0:
    N = int(input())
    if N == 1 :
        print("1")
    elif N == 2:
        print("-1")
    else:
        log_base2 = int(math.log(N,2))
        if N % 2**log_base2 == 0:
            print(-1)
        else:
            s=[]
            while N > 3:
                log_base2 = int(math.log(N-1,2))
                if (N-1) % 2**log_base2 == 0:
                    s.append(N-1)
                    s.append(N)
                    N = N - 2
                    
                else:
                    s.append(N)
                    N = N - 1
            s.append(1)
            s.append(3)
            s.append(2)
            k1=len(s)
            for i in range(k1):
                print(s[k1-1-i],end=" ")
            print()    
    remaing_test_cases = remaing_test_cases - 1