# Lv.0 소인수분해 
def solution(n):
    num=2
    num_list=[]
# n의 값이 1이 될때까지 나눔
    while n!=1:
# 만약 n이 num으로 나눠진다면 
        if n%num==0:
# n에 num으로 나눈 값을 반환하고 빈 리스트에 추가한다
            n=n//num
            num_list.append(num)
# 만약 나눠지지 않는다면 num값에 1을 더해서 숫자를 올려준다
        else:
            num+=1
# set 함수를 통해 중복을 제거하고 
    num_list=set(num_list)
# 튜플 형태를 다시 list 형태로 변경 및 정렬해준다. 
    list_num=sorted(list(num_list))
    return(list_num)
