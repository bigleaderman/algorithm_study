-- 이름, 날짜를 출력 
SELECT A.NAME, A.DATETIME
-- 들어온 돌물 테이블에
FROM ANIMAL_INS A 
-- 좌측을 기준으로 ANIMAL_OUTS를 조인했을 때
LEFT JOIN ANIMAL_OUTS B
-- A의 ANIMAL아이디와 B의 ANIMAL 아이디가 같을 때
-- 좌측인 A를 기준으로 하니 B가 없으면 B.ANIMAL_ID에는 NULL이 출력 
ON A.ANIMAL_ID = B.ANIMAL_ID
-- B가 NULL인 것만 들고오게 하기
WHERE B.ANIMAL_ID IS NULL
-- DATE타임을 기준으로 하되 A를 기준으로 한다
ORDER BY A.DATETIME
-- 3개를 제한으로 둔다.
LIMIT 3;