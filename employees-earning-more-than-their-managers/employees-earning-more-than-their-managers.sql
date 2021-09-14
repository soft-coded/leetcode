# Write your MySQL query statement below
SELECT e1.name AS Employee
FROM employee as e1, employee as e2
WHERE e2.id = e1.managerId
  AND e1.salary > e2.salary;