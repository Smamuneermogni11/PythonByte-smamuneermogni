# **PythonByte**   
## IST303-Group-Project    
## **Team members:** 
KRISTINA, NAIF, MUNEER, DESMEND       

## **Team name: PythonByte**   

## **Development Environment:**
GUI frontend: HTML, CSS, Bootstrap , Javascript   
## **Backend:** Python, Django Web Framework    
## **Database:** Microsoft Sql Server   

## **Product:**
Student Enrollment System webpage   

## **Project Description:**
	The system would allow educational organizations to enroll students into courses and set the program timetable and assign who teaches these courses.
	The system would have a website as the front end and a database as the back end.      
  
## **Stakeholders:**
Professors, Students, Organisation Staff members, Managers, Head Officials   
    
## **Decomposed User Stories into Tasks and Allocate tasks to each team member and record the allocation:**  
 [Link](https://github.com/Smamuneermogni11/PythonByte/blob/dbd955c6568bd190501809b20042b123f04677fa/User%20Stories%20broken%20into%20Tasks%20with%20Team%20Member%20Allocated.pdf)       

## Features in Milestone 1: 

Backend: Database Backbone (Create Tables, Users Table and rols)  

Frontend: Web Page (Main: login page ,Student: Enrolment, Student: Courses Plan, Student: future Courses Plan, Lecturer: Timetable, Lecturer: Student Lists)

## 2 Iterations for Milestone 1 (4 weeks):
Iteration 1 (2 weeks): 

1. Develop Database Design 

2. Create Flask Project and Venv 

3. Create Database.	 

Iteration 2 (2 weeks): 

1. Create Template and Style.  

2. Create Webpage: (Main: login page ,Student: Enrolment, Student: Courses Plan, Student: future Courses Plan, Lecturer: Timetable, Lecturer: Student Lists) 

## Calculate Velocity:

Timeline: 4 weeks to milestone 1, 5 weeks to milestone 2

Iteration 1: 3 user stories x 8 story points = 24
Iteration 2: 7 user stories x 8 story points = 56

Total = 80

So, your average velocity is 80 ÷ 2 = 40.

Starting velocity: 40 %
Total: 6 hours per week
Current: 4 hours per week


# Burn Down Chart:

[Link](https://cgu0-my.sharepoint.com/:x:/g/personal/naif_alblawi_cgu_edu/EbCUGVcGgQhFhw6ms9QRkyoBjbVyxxy0AC-dhmHFM0yjsQ?e=fc0rfN)

# Stand Up Meeting:

[Link](https://cgu0-my.sharepoint.com/:w:/g/personal/naif_alblawi_cgu_edu/ETbM1UMhSCBIk1TWXlAk8RgB1zL2sjUGkMI1gdLABZNXiQ?e=b1Bibx)

# Instructions for Visual Studio Code:

# Instruction to virtual environment:

1. venv\Scripts\activate.bat
2. python -m pip install --upgrade pip

3. python -m pip install flask

## To run the code:


    
    paste this code in visual studio code
    
    Then run this code in terminal:

python -m flask run

After getting the website link:

Hold Ctrl button and click on the link:

(venv) C:\Users\Muneer\Desktop\work>python -m flask run
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [01/Oct/2022 16:01:51] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [01/Oct/2022 16:01:51] "GET /favicon.ico HTTP/1.1" 404 -

 *  History restored 

# Testing the web page: 

$ pip install pytest
from front_page import app

def test_front_page():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'PythonByte!'
    
## To run the test:
pytest test_front_page.py

Output:
(venv) C:\Users\Muneer\Desktop\work>pytest test_front_page.py
========================================================== test session starts ===========================================================
platform win32 -- Python 3.10.6, pytest-7.1.3, pluggy-1.0.0
rootdir: C:\Users\Muneer\Desktop\work
collected 1 item

test_front_page.py .                                                                                                                [100%]






















