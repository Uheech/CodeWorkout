# Lv.1 약수의 합
def solution(n):
    sum_num=0
    for i in range(1,n+1):
        if n%i==0:
            sum_num+=i
    return sum_num

# sum을 쓰려고 했는데 안되어서 0에다가 약수를 순차적으로 더하는 식으로 풀이함.
# sum은 리스트 형태에서만 사용 가능.
