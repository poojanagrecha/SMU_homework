select * from employees
select * from salaries
select * from dept_manager
select * from departments
select * from dept_emp
select * from titles

-- Question 1
select 
	e.emp_no,
	e.last_name,
	e.first_name,
	e.sex,
	s.salary
from 
	employees e
join salaries s ON e.emp_no = s.emp_no

-- Question 2
select
	first_name,
	last_name,
	hire_date
from employees
where hire_date between '1986-01-01' and '1986-12-31'

-- Question 3
select 
	dm.dept_no,
	d.dept_name,
	dm.emp_no,
	e.last_name,
	e.first_name
from 
	dept_manager dm 
join departments d on dm.dept_no = d.dept_no
join employees e on dm.emp_no = e.emp_no
	
-- Question 4
select 
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
from 
	employees e
join dept_manager dm on e.emp_no = dm.emp_no
join departments d on dm.dept_no = d.dept_no

-- Question 5
select 
	first_name,
	last_name,
	sex
from employees
where first_name = 'Hercules' AND last_name LIKE 'B%'

-- Question 6
select 
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
from 
	employees e
join dept_manager dm on e.emp_no = dm.emp_no
join departments d on dm.dept_no = d.dept_no
where dept_name = 'Sales'

-- Question 7
select 
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
from 
	employees e
join dept_manager dm on e.emp_no = dm.emp_no
join departments d on dm.dept_no = d.dept_no
where d.dept_name IN ('Sales','Development')

-- Question 8
select
	COUNT (last_name) as "Number of Occurences",
	last_name
from employees
GROUP BY last_name 
ORDER BY "Number of Occurences" desc



