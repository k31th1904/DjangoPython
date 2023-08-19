DROP DATABASE IF EXISTS WORKREPORT;
CREATE DATABASE IF NOT EXISTS WORKREPORT;

USE WORKREPORT;


CREATE TABLE employees (
employee_id INT PRIMARY KEY AUTO_INCREMENT,
user_id INT UNIQUE,
fname VARCHAR(45) NOT NULL,
lname VARCHAR(45) NOT NULL,
telephone VARCHAR(12) NOT NULL,
address VARCHAR(45) NOT NULL,
email VARCHAR(45) NOT NULL);

CREATE TABLE client_categories (
category_id INT PRIMARY KEY AUTO_INCREMENT,
category_name VARCHAR(45) NOT NULL
);

CREATE TABLE clients (
client_id INT PRIMARY KEY AUTO_INCREMENT,
cname VARCHAR(100) NOT NULL,
email VARCHAR(45) NOT NULL,
telephone VARCHAR(12),
address VARCHAR(100) NOT NULL,
category_id INT NOT NULL,
CONSTRAINT clients_fk_client_category FOREIGN KEY (category_id) REFERENCES client_categories(category_id) ON DELETE CASCADE
);

CREATE TABLE projects (
project_id INT PRIMARY KEY AUTO_INCREMENT,
client_id INT NOT NULL,
project_code VARCHAR(45) UNIQUE NOT NULL,
description VARCHAR(200),
date_created DATE,
project_mang INT NOT NULL,
CONSTRAINT projects_fk_clients FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,
CONSTRAINT projects_fk_employees FOREIGN KEY (project_mang) REFERENCES employees(employee_id) ON DELETE CASCADE
);

CREATE TABLE assignment (
assignment_id INT PRIMARY KEY AUTO_INCREMENT,
employee_id INT NOT NULL,
project_id INT NOT NULL,
task_date DATE NOT NULL,
hours INT NOT NULL,
task_type VARCHAR(20) DEFAULT "On-Site",
salary_hour INT NOT NULL,
claimed BOOLEAN DEFAULT 0,
CONSTRAINT task_records_fk_employees FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE,
CONSTRAINT task_records_fk_projects FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);


CREATE TABLE claims (
claim_id INT PRIMARY KEY AUTO_INCREMENT,
assignment INT NOT NULL,
approved VARCHAR(20) DEFAULT "Pending",
claim_date DATE NOT NULL,
payment_amount INT,
processed_by INT,
CONSTRAINT claims_fk_assignment FOREIGN KEY (assignment) REFERENCES assignment(assignment_id) ON DELETE CASCADE,
CONSTRAINT claims_fk_employees FOREIGN KEY (processed_by) REFERENCES employees(employee_id) ON DELETE CASCADE
);


