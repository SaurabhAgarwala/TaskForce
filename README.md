# fsf_2019_screening_task1
Task Manager App developed as part of FOSSEE Fellowship Selection Test - 2019.


## Features of this Task Manager App
1. Allow users to Sign Up and Login after authentication.
2. Allows authenticated users to create teams.
3. Only the team creator can edit/delete the team.
4. A user can create a task and assign it to one or more than one members of a team.
5. In case the task creator does not belong to any team, then the task will be self assigned to himself.
6. A user from the same team can comment on any tasks of that team, and also reply to comments of that task.
7. Only the task creator is allowed to edit/delete the task created by himself.
8. Other users from the same team can only view/comment on the tasks created.
9. Users not belonging to a particular team will not be able to view/edit/assign/comment on tasks belonging to that team.
10. A UserPage is present for a comprehensive view of all the tasks assigned to the user, and list of teams of which the user is a member of.
11. A user belonging to a team can also assign a task to self by not selecting any team while creating the task.
12. The tasks also have a deadline field.


## Requirements
The folowing technologies, libraries/packages and CDNs were used for making this web application:
1. Python 3.6.7
2. Django 1.11.11
3. django_markdownx 2.0.21
4. HTML5
5. CSS3
6. Bootstrap 4.1.0
7. W3 Schools CSS
8. Git


## Setting Up the Project
1. Clone this repo
2. Install required packages.
3. Go to taskmanager directory which contains manage.py script.
4. Run the command `python3 manage.py runserver`
5. Go to http://127.0.0.1:8000

## TestCases
The flow of the app is quite smooth and a observer can easily follow after setting up the project.
The test cases are all the features mentioned above which can be easily tested by using the app.
The following are credentials of the users created by default to test the app. New users can also be created. Few teams and tasks have also been created by default.
1. SuperUser: saurabh
    Password: fossee2019
2.  User: dev1
    Password: developer
3.  User: dev2
    Password: development
4.  User: algo1
    Password: algorithms
5.  User: algo2
    Password: algorithms
6.  User: sys1
    Password: systemsgroup
7.  User: sys2
    Password: systemsgroup
8.  User: int1
    Password: intelligence
9.  User: int2
    Password: intelligence