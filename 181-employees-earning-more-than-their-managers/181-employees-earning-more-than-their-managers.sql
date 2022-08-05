# Write your MySQL query statement below
SELECT e.name AS Employee
FROM employee e
WHERE e.salary > (
  SELECT m.salary
  FROM employee m
  WHERE m.id = e.managerId
);