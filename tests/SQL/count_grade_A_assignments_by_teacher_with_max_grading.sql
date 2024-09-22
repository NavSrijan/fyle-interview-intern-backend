-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH TeacherGradedAssignments AS (
    SELECT
        teacher_id,
        COUNT(*) AS total_graded
    FROM
        assignments
    WHERE
        state = 'GRADED'
    GROUP BY
        teacher_id
),
MaxTeacher AS (
    SELECT
        teacher_id
    FROM
        TeacherGradedAssignments
    ORDER BY
        total_graded DESC
    LIMIT 1
)
SELECT
    COUNT(*) AS grade_a_count
FROM
    assignments
WHERE
    teacher_id = (SELECT teacher_id FROM MaxTeacher)
    AND grade = 'A'
    AND state = 'GRADED';
