# TaskForce

TaskForce is an app developed as part of IIT-Bombay FOSSEE Fellowship Selection Test - 2019.

## Features of this TaskForce Application

1. Allow users to Sign Up and Login after authentication.
2. Allows authenticated users to create teams.
3. Only the team creator can edit/delete the team.
4. A user can create a task and assign it to one or more than one members of a team.
5. In case the task creator does not belong to any team, then the task will be self assigned to himself.
6. A user from the same team can comment on any tasks of that team, and also reply to comments of that task.
7. Only the task creator is allowed to edit/delete the task created by himself.
8. Other users can only view/comment on the tasks created, of the same team they belong to.
9. Users not belonging to a particular team will not be able to view/edit/assign/comment on tasks belonging to that team.
10. A UserPage is present for a comprehensive view of all the tasks assigned to the user, and list of teams of which the user is a member of.
11. A user belonging to a team can also assign a task to self by not selecting any team while creating the task.
12. The tasks also have a deadline field.

## Primary Technologies Used

The folowing technologies, libraries/packages and CDNs were used for making this web application:

1. Python
2. Django
3. django_markdownx
4. HTML5
5. CSS3
6. Bootstrap
7. W3 Schools CSS
8. Git

## Setting Up the Project

1. Clone this repo
2. Set up an environment and install the required packages from `requirements.txt`
3. Go to taskmanager directory which contains `manage.py` script.
4. Run the following commands:  
 ```python3 manage.py makemigrations```  
 ```python3 manage.py migrate```  
 ```python3 manage.py runserver```  

5. Go to <http://127.0.0.1:8000> and you are good to use the application.
