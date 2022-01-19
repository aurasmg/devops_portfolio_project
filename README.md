# devops_portfolio_project
Students Management
1. Use existing Django project to create API endpoints to display list of student’s records 
2. Using Get, Post, Put/Patch, and Delete to retrieve information about students
3. A database which contains 3 tables to manage the data for a software school Students

  Course
  Registrations
  
  
API Reference Table of endpoint paths, methods, parameters API for students


   Index  
Show all the students in the database
GET http://localhost:5000/students


   Show
   
Show the student with specific id
GET http://localhost:5000/students/id


 Create
 
Add a new student to the database using JSON format 
POST http://localhost:5000/students

E.g.
 {
"id": 13,
"first_name": "Abel",
"last_name": "Castillo",
"email": "abel.castillo@escuela.com", 
"course_id": 4
}

   Delete
   
Delete the student with the specific id DELETE http://localhost:5000/students/id

API for courses


 Index
 
Show all the courses in the database 
GET http://localhost:5000/courses
 
  Create
  
Add a new course to the database using JSON format 
POST http://localhost:5000/courses

{
"id": 5,
"name": "R", 
"units": 4
}

  Delete

Delete the course with the specific id 
DELETE http://localhost:5000/courses/id
