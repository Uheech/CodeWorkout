SELECT ao.ANIMAL_ID, ao.NAME 
FROM ANIMAL_INS ai
# 입양 보낸 기록은 있는데 보호소 기록은 없어야 하므로 OUTS을 기준으로 JOIN
RIGHT JOIN ANIMAL_OUTS ao
on ai.ANIMAL_ID = ao.ANIMAL_ID
# 보호소 기록이 null이어야 함
WHERE ai.DATETIME IS NULL
ORDER BY ao.ANIMAL_ID;
