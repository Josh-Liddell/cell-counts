SELECT condition_name, COUNT(*) AS [Subjects Available]
FROM conditions c
  JOIN patient p ON c.id = p.condition_id
GROUP BY condition_name
ORDER BY 2 DESC;


SELECT *
FROM samples s
  JOIN patient p ON p.id = s.patient_id
  JOIN conditions c ON c.id = p.condition_id
WHERE condition_name = 'melanoma' 
  AND stype = 'PBMC'
  AND patientid IN (SELECT patientid 
                    FROM patient_treatment 
                    WHERE treatmentid = 'tr1' 
                      AND time_from_treatment_start = 0);



SELECT project_name, COUNT(*) AS [Count]
FROM samples s
  JOIN project p ON p.id = s.project_id
GROUP BY project_name
ORDER BY 2 DESC;


SELECT
  COUNT(CASE WHEN response = 'yes' THEN 1 END) AS yes_count,
  COUNT(CASE WHEN response = 'no' THEN 1 END) AS no_count
FROM samples;


SELECT
  COUNT(CASE WHEN sex = 'M' THEN 1 END) AS male_count,
  COUNT(CASE WHEN sex = 'F' THEN 1 END) AS female_count
FROM patient;
