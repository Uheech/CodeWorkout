def solution(numbers, k):
    # 배열의 길이를 늘려 index가 이어지도록 한다.
    numbers=numbers*k
    # 간격이 2이다.
    return numbers[2*k-2]
