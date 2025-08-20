# Lv2. 노선별 평균 역 사이 거리 조회하기
SELECT ROUTE, CONCAT(SUM_DIST,'km') as TOTAL_DISTANCE, CONCAT(AVG_DIST,'km') as AVERAGE_DISTANCE FROM (SELECT ROUTE, ROUND(SUM(D_BETWEEN_DIST),1) as SUM_DIST, ROUND(AVG(D_BETWEEN_DIST),2) as AVG_DIST FROM SUBWAY_DISTANCE GROUP BY ROUTE ORDER BY SUM_DIST DESC) as d;
---CONCAT 안에 ROUND를 바로 사용하면 ORDER BY 절에 문제 생김
--- CONCAT은 숫자를 문자열로 변환함, 그래서 TOTAL_DISTANCE는 더이상 숫자가 아니라 VARCHAR같은 문자열이 됨
--- ORDER BY는 문자열 데이터를 기준으로 정렬함.
--- 정확한 결과를 얻으려면 숫자계산과 정렬을 먼저 완료하고, 마지막에 문자열을 붙여서 출력해야 함.