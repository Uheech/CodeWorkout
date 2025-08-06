# 둘째짜리까지 반올림(ROUND)
SELECT ROUND(AVG(LENGTH),2) as AVERAGE_LENGTH FROM
# LENGTH 가 NULL 값이면 모두 10으로 바꾼 테이블로 만들어서 원하는 값을 구한다.
# 주의! CASE WHEN 조건에 IS NULL을 쓰고 싶으면 반드시 ELSE도 써줘야 한다.
# 그렇지 않으면 WHEN 조건이 모두 FALSE가 됨 
(SELECT 
CASE WHEN LENGTH IS NULL 
THEN 10 
ELSE LENGTH
END as LENGTH FROM FISH_INFO) as a;
# 또한 FROM 절에 서브쿼리를 넣고 싶으면 as 로 꼭 별칭도 추가해줘야 한다.
