# Lv.1 자연수 뒤집어 배열로 만들기
# 1. 자연수를 문자로 바꿔줌(자연수는 iterable 하기 때문에 for문을 쓸 수가 없다)
# 2. 바뀐 문자를 다시 숫자로 변환해줌
# 3. 슬라이싱으로 뒤집어준다. 
def solution(n):
    return [int(x) for x in str(n)][::-1]
