1) Connect to PostgreSQL


2) Create a new database called school_db




3) Create environmental variables


for windows:
setx DB_USER "myuser"
setx DB_PASS "mypassword"


for mac:
export DB_USER="myuser"
export DB_PASS="mypassword"


OR manually type username/password -> in the in the code commented section




Paste into the pgadmin query:
Go to PostgreSQL(your server) -> Databases -> school_db -> Schemas -> Tables -> students table (right click and query tool)

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');



