# cook your dish here
remainig_test_cases = int(input())
while remainig_test_cases > 0:
    flag=0
    total_person,jump_to,infected_start,your_position=map(int,input().split())
    if jump_to%total_person==0:
        if infected_start == your_position:
            print("YES")
        else:
            print("NO")
    else: 
        jump_to=jump_to%total_person
        infected = infected_start
        flag = 0
        s=[0]*total_person
        while True:
            if s[infected]=="?":
                break
            else:
                if infected==your_position:
                    flag=1
                    break
                else:
                    s[infected]="?"
                    infected = (infected+jump_to)%total_person
        if flag==1:
            print("YES")
        else:
            print("NO")
           
    
        
    remainig_test_cases = remainig_test_cases - 1