/* Create a table name - "Employee Details" */
/* CREATING TABLE Employee Details */

CREATE TABLE EmployeeDetails(
	Emp_id INT PRIMARY KEY NOT NULL,
    Emp_name VARCHAR(50) NOT NULL,
    Job_name VARCHAR(50) NOT NULL,
    Manager_id INT NOT NULL,
    Hire_date DATE NOT NULL,	-- YYYY-MM-DD
    Salary INT NOT NULL,
    Dep_id INT NOT NULL    
);