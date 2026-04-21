# Write your MySQL query statement below


SELECT name, bonus FROM Employee e
LEFT JOIN Bonus b ON b.empId = e.empId
WHERE bonus < 1000 or b.bonus IS NULL;