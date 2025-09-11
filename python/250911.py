# Lv.0 직사각형 넓이 구하기
def solution(dots):
    # 좌표를 정렬하게 되면 x축이 같은 순서대로 정렬됨
    dots=sorted(dots)
    # 그 상태에서 x축, y축 길이를 구해서 곱함
    a=dots[0][1]-dots[1][1]
    b=dots[1][0]-dots[3][0]
    print(dots)
