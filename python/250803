def solution(a, b):
    # 유클리드 호제법으로 최대공약수 구하기 
    def gcd(a, b):
        while a != 0:
            b, a = a, b % a
        return b
    
    # 최대공약수 변수에 저장하기 
    gcd_value = gcd(a, b)
    # 분모를 최대공약수로 나누어 약분
    b = b // gcd_value
    
    # 분모를 2로 계속 나누기
    while b % 2 == 0:
        b = b // 2
        
    # 분모를 5로 계속 나누기
    while b % 5 == 0:
        b = b // 5
    
    # 남은 분모가 1이면 유한소수, 아니면 무한소수
    if b == 1:
        return 1
    else:
        return 2
