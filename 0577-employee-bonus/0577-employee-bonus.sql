SELECT e.name , b.bonus
FROM Employee e
LEFT JOIN Bonus b
ON e.empID = b.empID
WHERE b.Bonus < 1000 OR b.Bonus is Null;
