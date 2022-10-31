-- 코드를 입력하세요
-- 아이디, 타입, 이름 컬럼을 출력한다.
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
-- 들어온 동물의 테이블
FROM ANIMAL_INS A
-- 위 테이블과 이 테이블의 교집합
JOIN ANIMAL_OUTS B
-- 외래키와 기본키 기준으로 JOIN함
ON A.ANIMAL_ID = B.ANIMAL_ID
-- 처음 들어왔을 때랑 나갈때가 다르면 중성화한거임
WHERE A.SEX_UPON_INTAKE != B.SEX_UPON_OUTCOME
-- 아이디를 기준으로 
ORDER BY A.ANIMAL_ID