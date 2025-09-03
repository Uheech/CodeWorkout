# Lv.0 팩토리얼 
def solution(n):
    num=1
    factory=1
    # 1부터 1씩 늘려가면서 정수를 곱한다
    # 그리고 그 정수의 곱이 주어진 정수 n보다 커지게 되면 멈춘다
    while factory < n:
        num+=1
        factory*=num
    # 만약 정수의 곱이 정수 n과 같다면 num을 반영
    if factory==n:
        return num
    # 정수의 곱이 정수 n보다 커지면 num-1을 반영
    elif factory > n:
        return num-1
