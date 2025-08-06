def solution(A, B):
    count=0
# A와 B가 같아진다면? > 이동시킨 횟수를 반환해 
    while True:
        if A==B:
            return count
# A와 B가 같지 않다면? > 같아질 때까지 이동, 횟수를 더해 
        elif A!=B:
            A=A[len(A)-1]+A[0:len(A)-1]
            count+=1
# 영원히 B랑 같지 않은 A도 있을테니까 
# 원래의 A와 같아질 때까지 이동시켜야지.
# 그 횟수는 A 문자열의 길이를 초과하지 않을거야
            if count>len(A):
                return -1
