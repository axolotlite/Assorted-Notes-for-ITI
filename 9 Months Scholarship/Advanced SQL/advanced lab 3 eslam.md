
1. Create a stored procedure to calculate the average grades for a certain subject:

```sql
DELIMITER //
CREATE PROCEDURE calculateAverageGrade(IN courseName VARCHAR(40))
BEGIN
    DECLARE average DECIMAL(5, 2);
    SELECT AVG(sc.grade) INTO average
    FROM courses AS c
    JOIN students_course AS sc ON sc.course_no = c.course_no
    WHERE c.course_name = courseName;
    SELECT average;
END //
```

2. Create a stored procedure to display the full result for a student:

```sql
DELIMITER //
CREATE PROCEDURE displayStudentResults(IN studentId INT)
BEGIN
    SELECT *
    FROM students AS s
    JOIN students_course AS sc ON s.student_no = sc.student_no
    JOIN courses AS c ON c.course_no = sc.course_no
    WHERE s.student_no = studentId;
END //
```

3. Create a stored procedure that will swap the departments of two employees:

```sql
DELIMITER //
CREATE PROCEDURE swapEmployeeDepartments(IN empNo1 INT, IN empNo2 INT)
BEGIN
    START TRANSACTION;
    UPDATE employees
    SET dept_no = (SELECT dept_no FROM employees WHERE emp_no = empNo2)
    WHERE emp_no = empNo1;
    UPDATE employees
    SET dept_no = (SELECT dept_no FROM employees WHERE emp_no = empNo1)
    WHERE emp_no = empNo2;
    COMMIT;
END //
```

4. Create a stored procedure to handle transactions for the students table:

```sql
DELIMITER //
CREATE PROCEDURE addStudentTransaction(IN studentNo INT, IN studentName VARCHAR(40), IN studentAge INT)
BEGIN
    START TRANSACTION;
    INSERT INTO students (student_no, student_name, age)
    VALUES (studentNo, studentName, studentAge);
    COMMIT;
END //
```

5. Create a trigger that fills the history of employee salary changes:

```sql
DELIMITER //
CREATE TRIGGER recordSalaryChangeHistory
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    INSERT INTO salary_change_history (emp_no, old_salary, new_salary, change_date)
    VALUES (OLD.emp_no, OLD.salary, NEW.salary, NOW());
END //
```

6. Create triggers to fill the history of employee department changes for insert, update, and delete operations (each as separate triggers) with updated trigger names:

For INSERT:

```sql
DELIMITER //
CREATE TRIGGER recordDepartmentChangeHistoryInsert
AFTER INSERT ON employees
FOR EACH ROW
BEGIN
    DECLARE newDeptName VARCHAR(40);
    SET newDeptName = (SELECT dept_name FROM departments WHERE dept_no = NEW.dept_no);
    INSERT INTO department_change_log (old_dept_no, new_dept_no, old_dept_name, new_dept_name, operation, change_date)
    VALUES (NULL, NEW.dept_no, NULL, newDeptName, 'INSERT', NOW());
END //
```

For UPDATE:

```sql
DELIMITER //
CREATE TRIGGER recordDepartmentChangeHistoryUpdate
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    DECLARE oldDeptName, newDeptName VARCHAR(40);
    SET oldDeptName = (SELECT dept_name FROM departments WHERE dept_no = OLD.dept_no);
    SET newDeptName = (SELECT dept_name FROM departments WHERE dept_no = NEW.dept_no);
    INSERT INTO department_change_log (old_dept_no, new_dept_no, old_dept_name, new_dept_name, operation, change_date)
    VALUES (OLD.dept_no, NEW.dept_no, oldDeptName, newDeptName, 'UPDATE', NOW());
END //
```

For DELETE:

```sql
DELIMITER //
CREATE TRIGGER recordDepartmentChangeHistoryDelete
AFTER DELETE ON employees
FOR EACH ROW
BEGIN
    DECLARE oldDeptName VARCHAR(40);
    SET oldDeptName = (SELECT dept_name FROM departments WHERE dept_no = OLD.dept_no);
    INSERT INTO department_change_log (old_dept_no, new_dept_no, old_dept_name, new_dept_name, operation, change_date)
    VALUES (OLD.dept_no, NULL, oldDeptName, NULL, 'DELETE', NOW());
END //
```

7. Create a trigger on the Employees table to prevent users from updating the salary with a value greater than 200,000:

```sql
CREATE TRIGGER preventExcessiveSalaryUpdate
BEFORE UPDATE ON employees
FOR EACH ROW
BEGIN
    IF NEW.salary > 200000 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Salary cannot exceed 200,000';
    END IF;
END //
```

8. Create an event to add a value to a column by 100 every 1 minute until 10 minutes in a new table ("Task8"):

Create the "Task8" table:

```sql
CREATE TABLE Task8 (
    counter INT PRIMARY KEY,
    value INT
);

INSERT INTO Task8 VALUES (0, 0);

DELIMITER //
CREATE EVENT incrementCounterValue
ON SCHEDULE EVERY 1 MINUTE
STARTS CURRENT_TIMESTAMP
ENDS CURRENT_TIMESTAMP() + INTERVAL 10 MINUTE
DO
BEGIN
    UPDATE Task8
    SET counter = counter + 100
    WHERE counter = 0;
END //
```

9. Dump your database into a file:

```shell
mysqldump -u root -p iti_db > EslamLab.sql
```

Please replace 'root' with your actual MySQL username and 'password' with your MySQL password when running the mysqldump command.