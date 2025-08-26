# Lv.0 특이한 정렬 

def solution(numlist, n):
    # 빈 딕셔너리를 만들어 주고 
    new_dic={}
    for i in numlist:
        # 절대값을 씌운 거리의 값을 구해주고
        distance=abs(n-i)
        # 해당 원소에 따른 거리값을 함께 딕셔너리에 추가 
        new_dic[i]=distance
        # 정렬하기 > 정렬할 기준을 튜플로 감싸 여러 개로 지정할 수 있음
        # sorted(정렬할 대상, 정렬기준: 내림차순으로 하고 싶을땐 -, 오름차순은 (+))
        sorted_items=sorted(new_dic.items(), key=lambda item:(item[1], -item[0]))
        # 정렬된 값중에서 키값만 골라서 list에 담음
        # dictionary 형태였다면 list(my_dic.keys()) 이렇게 하면 되겠지만
        # 이건 튜플형태라서 슬라이싱으로 append 해주기 
    result = [item[0] for item in sorted_items]
    return result
