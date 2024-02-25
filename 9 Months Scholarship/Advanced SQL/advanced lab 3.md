1- Create stored procedure to calculate the average grades for certain subject.  
```
delimiter //
create procedure calcAvgGrade(in course_name varchar(40))
begin
declare avgGrade int;
select avg(sc.grade) into avgGrade from courses as c, students_course as sc where sc.course_no=c.course_no and course_name = c.course_name;
select avgGrade;
end //
```
2- Create stored procedure to display the full result for a student 
```
delimiter //
create procedure studentResults(in studentId int)
begin
select * from students as s, students_course as sc, courses as c where s.student_no=sc.student_no and c.course_no=sc.course_no and s.student_no=studentId; 
end //
```
3- Create a stored procedure that will swap the departments of two Employees. 
```
delimiter //
create procedure swapEmployees(in emp_no1 int, emp_no2 int)
begin
update employees set dept_no = (select dept_no from employees where emp_no = emp_no2) where emp_no = emp_no1;
update employees set dept_no = (select dept_no from employees where emp_no = emp_no1) where emp_no = emp_no2;
end //
```
4- Create Stored Procedure to handle transactions of students table. 
```
delimiter //
create procedure addStudent(in studentNo int, in studentName varchar(40), in age int)
begin 
start transaction;
insert into students(student_no, student_name, age) values(studentNo, studentName, age);
commit; 
end//
```
5- Create Trigger That Fill History of Employee Salary. 
```
delimiter //
create trigger recordSalaryHistory after update on employees for each row
begin
insert into sal_history(emp_no, old_sal, new_sal, chg_date) values (OLD.emp_no, OLD.salary, NEW.salary, now()); 
end //
```
6- Create a trigger that Fill History of Employee On Different Departments.  
## insert
```
delimiter //
create trigger recordDepartmentHistory
after insert on employees for each row 
begin
declare dept_name2 varchar(40);
set dept_name2 = (select dept_name from departments where dept_no=NEW.dept_no);
insert into dept_log values (NULL, new.dept_no, NULL, dept_name2, 'INSERT', now());
end//
```
## update
```
delimiter //
create trigger recordDepartmentHistory
after update on employees for each row 
begin
declare dept_name1, dept_name2 varchar(40);
set dept_name1 = (select dept_name from departments where dept_no=OLD.dept_no);
set dept_name2 = (select dept_name from departments where dept_no=NEW.dept_no);
insert into dept_log values (old.dept_no, new.dept_no, dept_name1, dept_name2, 'UPDATE', now());
end//
```
## delete
```
delimiter //
create trigger recordDepartmentHistory
after delete on employees for each row 
begin
declare dept_name1 varchar(40);
set dept_name1 = (select dept_name from departments where dept_no=OLD.dept_no);
insert into dept_log values (old.dept_no, NULL, dept_name1, NULL, 'DELETE', now());
end//
```
7- Create a trigger on Employees table to prevent user from update salary with value greater than 200000. 
```
create trigger limitSalaryUpdate
before update on employees
for each row
begin
if new.salary > 200000 then
signal sqlstate '45000'
set message_text = 'Salary cannot exceed 200,000';
end if;
end //
```
8- Create event to add Value On Column by 100 every 1 minute till 10   minute On new table (“Task8”). 
## create table
```
create table task8(
counter int primary key,
value int
);
```
## insert into table
`insert into task8 value(0,0);`
## create an event
```
delimiter //
create event incrementCounter
on schedule every 1 minute
ends current_timestamp() + interval 10 minute
do
begin
update task8 set counter = counter + 100 where counter=0;
end //
```
9- Dump your database into file.  
`mysql -u root -ppassword iti_db > ahmed_said_youssef_lab4.sql`