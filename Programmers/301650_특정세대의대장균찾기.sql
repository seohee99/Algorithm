WITH first_gen AS(
    SELECT ID
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
),
second_gen AS (
    SELECT ECOLI_DATA.ID, ECOLI_DATA.PARENT_ID
    FROM ECOLI_DATA JOIN first_gen ON ECOLI_DATA.PARENT_ID = first_gen.ID
)
SELECT ECOLI_DATA.ID
FROM ECOLI_DATA JOIN second_gen ON second_gen.ID = ECOLI_DATA.PARENT_ID