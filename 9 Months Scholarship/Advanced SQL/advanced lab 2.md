
1- create a db from an erd:

```
create table instructor(
	id int,
	fname varchar(14) not null,
	lname varchar(14) not null,
	salary int default 3000,
	address varchar(50),
	hiredate date default (current_date()),
	bdate date,
	overtime int,
	primary key(id),
	unique (salary)
);
create table course(
	cid int,
	cname varchar(14) not null,
	duration int,
	unique (cname),
	primary key(cid)
);
create table course_intrustor(
	cid int,
	iid int,
	foreign key (cid) references course(cid),
	foreign key (iid) references instructor(id),
	primary key (cid, iid)
);
create table lab(
	lid int not null,
	cid int not null,
	location varchar(20),
	capacity int,
	foreign key(cid) references course(cid),
	primary key (lid,cid)
);
```

2- Update Employee By Increase Bonus to 10% of Salary For Employee In Department "Marketing".  
`update employees set bonus= bonus+salary*0.1 where dept_no=(select dept_no from departments where dept_name="Marketing");`
3- Delete Courses Which No Students Learn it And No Employees Teach it. 
`delete from courses where course_no not in (select c.course_no from (select * from courses) as c, students_course as sc where c.course_no=sc.course_no) and course_no not in (select distinct c.course_no from (select * from courses) as c, emp_course as sc where c.course_no=sc.course_no);`

4- Increase Salary by 10% of it For Smallest 2 Different salaries on Employees Table. 
`update employees set salary=1.1*salary order by salary asc limit 2;`
5- Display Employee Data Which Working Since More Than 30 Years 
`select * from employees where date_add(hire_date, interval 30 year) < curdate();`
6- Display Employee Name with title (‘No Title’ in case NULL) 
`select concat(first_name, ' ', last_name), ifnull(title,"No Title") from employees;`
7- Display Employee Name , age which earns no salary 
`select concat(first_name, ' ', last_name), timestampdiff(year, birth_date,curdate()) from employees where salary=NULL;`
8- Display Employee Name and category of hiredate ‘New when years less than 5 years , old when years less than 15, very old when years more than 15
```
select concat(first_name, ' ', last_name), timestampdiff(year, birth_date,curdate()),
case
when timestampdiff(year, birth_date,curdate()) < 5 then "New"
when timestampdiff(year, birth_date,curdate()) < 15 then "Old"
else "Very Old"
end category
from employees;
```
9- Create view which display course name with student name 
`create view student_course_view as select s.student_name, c.course_name from students as s, students_course as sc, courses as c where s.student_no=sc.student_no and c.course_no=sc.course_no;`
10- Create view which display students data and no one can change age in this view to more than 25
`create view student_view as select * from students where age < 25 with check option;`