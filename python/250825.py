#Lv.0 저주의 숫자 3
def solution(n):
    count=0
    answer=0
    while count<n:
        answer+=1
        if answer % 3 != 0 and '3' not in str(answer):
            count+=1
    return answer
