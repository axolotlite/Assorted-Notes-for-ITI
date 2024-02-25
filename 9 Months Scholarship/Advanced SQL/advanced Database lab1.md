## Write Queries For Following Questions:

1 - Display Employees Which First Name contains Character 'm' 
`select * from employees where first_name like "m%";
`
2 - Display Employees Data Which Earn Salary greater than 60000 
`select * from employees where salary > 60000;
`
3 - Display Employee Full Name With Department Name Which is Working On It 
`select concat(e.first_name, ' ', e.last_name), d.dept_name from employees as e, departments as d where e.dept_no=d.dept_no`

4 – Display Student Data Which has Grade Greater than 70 on any Course 
`select distinct s.student_no, s.student_name from students as s, students_course as sc where s.student_no=sc.student_no and sc.grade > 70;`

5 – Display 2 maximum Different Salary For Employees 
`select * from employees order by salary desc limit 2;`

6 - Display Departments & Employees Data which have Employees or not 
`select * from departments as d left join employees as e on d.dept_no=e.dept_no;`

7 – Display Employee Who earn salary greater than 100000 and work in Department “Sales Manager” 
`select * from employees where salary>100000 and dept_no=(select dept_no from departments where dept_name="Sales Manager");`

8 – Display Student Name and Course Name and Grade for him 
`mysql> select s.student_name, c.course_name, sc.grade from students as s, students_course as sc, courses as c where s.student_no=sc.student_no and c.course_no=sc.course_no;`

9 – Display Employees Data which Has salary and has no bonus 
`select * from employees where salary>0 and bonus=0;`
`select * from employees where salary is not null and bonus is null;`

10 – Display Departments which contains employees with No Title  
`select d.dept_no from departments as d, employees as e where d.dept_no=e.dept_no and e.title is null group by d.dept_no;`

11 – Display Courses Data Where duration greater than 70 
`select * from courses where course_duration > 70;`

12 – Display Minimum Grade to Course “PHP”  
`select "PHP", min(grade) from students_course where course_no=(select course_no from courses where course_name="PHP");`
 
13 – Display Employee Data which supervise By Employee No 10010 
`select * from employees where super_no=10010;`

14 – Display Employee Data Which earn maximum salary for all employees 
`select * from employees where salary=(select max(salary) from employees);`
15 - Display Departments Data Which Contains More Than 200 Employees 
`select * from departments where dept_no in (select dept_no from employees group by dept_no having count(emp_no) > 200);`

16 – Display employee Data which earn salary greater than all Employees which first name is “Bedir” 
`select * from employees where salary > all (select salary from employees where first_name="bedir");`

17 - Display Maximum Salary On Each Department 
`select d.dept_name, d.dept_no, max(e.salary) from employees as e, departments as d where d.dept_no=e.dept_no group by d.dept_no;`

18 - Display Departments Data Which Total Salary of employees on This Department is more than 1000000 
`select d.dept_no, d.dept_name, sum(e.salary) from departments as d, employees as e where d.dept_no=e.dept_no group by d.dept_no having sum(e.salary) > 1000000;`

19 - Display Top 5 different Salary On Department "Finance"
 `select * from employees where dept_no=(select dept_no from departments where dept_name="Finance") order by salary desc limit 5;`

20 - Display Courses Which No Learning for Any Student. 
`select * from courses where course_no not in (select distinct course_no from students_course);`

21 - Display Total Grade For All Courses With Student Name. 
`select s.student_name, sum(sc.grade) from students as s, students_course as sc where sc.student_no=s.student_no group by s.student_name;`

22 - Display Departments Which Average Salary For All Employees is less than 75000. 
`select d.dept_no, d.dept_name, avg(e.salary) from employees as e, departments as d where d.dept_no=e.dept_no group by d.dept_no having avg(e.salary) < 75000;`

23 - Display Students Which Learn More Than 300 Hours. 
`select s.student_name, s.student_no, sum(c.course_duration) from students as s, students_course as sc, courses as c where s.student_no=sc.student_no and c.course_no=sc.course_no group by s.student_no having sum(c.course_duration) > 300;`

24 - Using “Union” & “Multiple Fuction” Display 2 Maximum different salary.
```
select max(salary) from employees
union
select max(salary) from employees where salary != (select max(salary) from employees);
```