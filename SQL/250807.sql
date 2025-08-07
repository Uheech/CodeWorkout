#Lv2. 조건에 맞는 사원 정보 조회하기

SELECT h3.SCORE as SCORE,h2.EMP_NO,h2.EMP_NAME,h2.POSITION,h2.EMAIL FROM HR_DEPARTMENT h1
INNER JOIN HR_EMPLOYEES h2 
ON h1.DEPT_ID=h2.DEPT_ID
# 평가점수= 상반기 + 하반기 점수
# EMP_NO을 기준으로 묶은 뒤에 그 둘의 합 자체를 서브쿼리로 테이블에 반환함. 
INNER JOIN (SELECT EMP_NO, SUM(SCORE) as SCORE FROM HR_GRADE GROUP BY EMP_NO) h3
ON h2.EMP_NO=h3.EMP_NO
# 점수를 기준으로 내림차순해주고 
ORDER BY h3.SCORE DESC
# 점수가 가장 맨 위에 있는 한 행만 가져오기 
LIMIT 1;
