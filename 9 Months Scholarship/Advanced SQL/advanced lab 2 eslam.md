lab answers
1. Create a database from an ERD:

```sql
CREATE TABLE instructor (
    id INT,
    fname VARCHAR(14) NOT NULL,
    lname VARCHAR(14) NOT NULL,
    salary INT DEFAULT 3000,
    address VARCHAR(50),
    hiredate DATE DEFAULT (CURRENT_DATE()),
    bdate DATE,
    overtime INT,
    PRIMARY KEY (id),
    UNIQUE (salary)
);

CREATE TABLE course (
    cid INT,
    cname VARCHAR(14) NOT NULL,
    duration INT,
    UNIQUE (cname),
    PRIMARY KEY (cid)
);

CREATE TABLE course_instructor (
    cid INT,
    iid INT,
    FOREIGN KEY (cid) REFERENCES course (cid),
    FOREIGN KEY (iid) REFERENCES instructor (id),
    PRIMARY KEY (cid, iid)
);

CREATE TABLE lab (
    lid INT NOT NULL,
    cid INT NOT NULL,
    location VARCHAR(20),
    capacity INT,
    FOREIGN KEY (cid) REFERENCES course (cid),
    PRIMARY KEY (lid, cid)
);
```

2. Update employee by increasing bonus to 10% of salary for employees in the "Marketing" department:

```sql
UPDATE employees
SET bonus = bonus + salary * 0.1
WHERE dept_no = (SELECT dept_no FROM departments WHERE dept_name = "Marketing");
```

3. Delete courses with no students learning it and no employees teaching it:

```sql
DELETE FROM courses
WHERE course_no NOT IN (
    SELECT c.course_no
    FROM courses AS c, students_course AS sc
    WHERE c.course_no = sc.course_no
)
AND course_no NOT IN (
    SELECT DISTINCT c.course_no
    FROM courses AS c, emp_course AS ec
    WHERE c.course_no = ec.course_no
);
```

4. Increase salary by 10% for the smallest 2 different salaries in the employees table:

```sql
UPDATE employees
SET salary = 1.1 * salary
ORDER BY salary ASC
LIMIT 2;
```

5. Display employee data for those working for more than 30 years:

```sql
SELECT *
FROM employees
WHERE DATE_ADD(hire_date, INTERVAL 30 YEAR) < CURDATE();
```

6. Display employee names with titles (display "No Title" in case of NULL):

```sql
SELECT CONCAT(first_name, ' ', last_name), IFNULL(title, "No Title")
FROM employees;
```

7. Display employee names and ages of those who earn no salary (assuming you want to check for NULL salaries):

```sql
SELECT CONCAT(first_name, ' ', last_name), TIMESTAMPDIFF(YEAR, birth_date, CURDATE())
FROM employees
WHERE salary IS NULL;
```

8. Display employee names and categories based on hire date (e.g., "New," "Old," "Very Old"):

```sql
SELECT CONCAT(first_name, ' ', last_name), TIMESTAMPDIFF(YEAR, birth_date, CURDATE()),
    CASE
        WHEN TIMESTAMPDIFF(YEAR, birth_date, CURDATE()) < 5 THEN "New"
        WHEN TIMESTAMPDIFF(YEAR, birth_date, CURDATE()) < 15 THEN "Old"
        ELSE "Very Old"
    END AS category
FROM employees;
```

9. Create a view to display course names with student names:

```sql
CREATE VIEW student_course_view AS
SELECT s.student_name, c.course_name
FROM students AS s
JOIN students_course AS sc ON s.student_no = sc.student_no
JOIN courses AS c ON c.course_no = sc.course_no;
```

10. Create a view to display student data, and no one can change the age in this view to more than 25:

```sql
CREATE VIEW student_view AS
SELECT *
FROM students
WHERE age < 25
WITH CHECK OPTION;
```