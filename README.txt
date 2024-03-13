COMP3005 Assignment 3 Question 1: Database Interaction with PostgreSQL and Application Programming
Author: Eric Wang, Student ID: 101183647

Github link: https://github.com/C1erlc/COMP3005Assignment3

Instructions:
1. Install and set up PostgreSQL, as it is required for this application and assignment. It can be 
installed from https://www.postgresql.org/download/

2. Install and set up Python, as it will also be required for this application. It can be installed 
from https://www.python.org/downloads/

3. Download psycopg3 as this is what the application uses to connect to the postgreSQL database.
Instructions to install it can be found at https://www.psycopg.org/psycopg3/docs/basic/install.html

4. Download all files from the linked github. This includes two .sql files, studentsfunctions.py, 
and this README.txt.

5. Now that PostgreSQL is set up, open pgAdmin. Set your username and password to whatever you like 
and create a database. Name it whatever you like, it is recommended to keep it relatively short 
as you will need to retype it to use this application.

6. Open the table creation and population files in postgreSQL by clicking on the query tool 
and then the Open File button on the top menu bar. First execute the table creation file, 
then the table population file.

7. If you are on Windows OS, use the Windows menu to search for the Python IDLE. If not, use 
whatever your current OS has to open the Python IDLE. Within the Python IDLE, select File -> Open
in the top menu bar and navigate to wherever you have downloaded the studentsfunctions.py file.

8. With studentsfunctions.py open, either use the top menu bar to select Run -> Run Module, or 
use whatever hotkey runs the file (on Windows it's F5).

9. Enter your postgreSQL database name, username, and password as requested. You may now use the 
application functions as listed on the assignment page, as well as in the studentsfunctions.py code.
Please note that student_id can be entered as just a number (integer) while all other arguments 
must be enclosed within double quotes, "". Enrollment date is entered as YYYY/MM/DD, but still 
within double quotes.

Demonstration video can be found at:
https://drive.google.com/file/d/1r-aqp9QSbfwBz-vflQgTRZseVZKIEruA/view?usp=sharing
The video is about 75MB, if it does not load in browser feel free to download it and view it 
on your own computer.