# 조건에 따라서 이름을 다르게 부여하고 싶으면 case when ~ then ~ end as 사용
# 주의 ! and를 사용해서 끊는 게 아님 when으로 구분된다. 
SELECT ID, 
CASE WHEN SIZE_OF_COLONY <= 100 THEN 'LOW'
WHEN SIZE_OF_COLONY>100 AND SIZE_OF_COLONY<=1000 THEN 'MEDIUM'
WHEN SIZE_OF_COLONY > 1000 THEN 'HIGH' END as SIZE
FROM ECOLI_DATA
ORDER BY ID ASC;
