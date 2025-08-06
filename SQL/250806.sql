-- 코드를 입력하세요
SELECT 
USER_ID, 
NICKNAME, 
CONCAT(CITY,' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) as 전체주소, 
# CONCAT은 이어붙여주는 역할
CONCAT(SUBSTRING(TLNO,1,3),'-',SUBSTRING(b.TLNO,4,4),'-',SUBSTRING(b.TLNO,8,4)) as 전화번호 
# SUBSTRING은 쪼개주는 역할 
FROM USED_GOODS_BOARD a 
INNER JOIN USED_GOODS_USER b
on a.WRITER_ID=b.USER_ID
GROUP BY b.USER_ID
# USER_ID 로 묶었고 USER_ID를 count하면 당연히 1밖에 안 나옴 
HAVING COUNT(a.WRITER_ID)>=3
# 묶인 상태에서 또 구분지을 수 있는 컬럼을 선택해서 개수를 count 
ORDER BY b.USER_ID DESC;