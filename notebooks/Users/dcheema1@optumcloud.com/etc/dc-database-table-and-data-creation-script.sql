-- Databricks notebook source
Drop Table if exists [dbo].[employees];

Create Table [dbo].[employees](
    employee_id int primary key,
    first_name  varchar(64),
    last_name   varchar(64),
    hire_date   datetime
);

Insert into [dbo].[employees] (employee_id, first_name, last_name, hire_date) values (1, 'Dave', 'Cheema', '01/02/2019');
Insert into [dbo].[employees] (employee_id, first_name, last_name, hire_date) values (2, 'Toaster', 'Boy', '02/03/2020');

Select * from [dbo].[employees];