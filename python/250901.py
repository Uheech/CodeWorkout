# Lv.0 나머지가 1이 되는 수 찾기

def solution(n):
    for x in range(1,n+1):
        if n%x==1:
            return x
