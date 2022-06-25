# skyqraft_python_coding_challenge
Rest Api using Flask 

#How to run the Programme 
Go to the project root directory and run below command to create virtual envirement for the project
>py -m venv env

Activate the virtual envirement
>.\env\Scripts\activate
 
Upgrade the PIP
>python.exe -m pip install --upgrade pip
 
Install dependancy libraries to run the project 
>pip install -r requirements.txt

Set Default file to start to application server
>set FLASK_APP=app.py

Up and run the Rest server 
>flask run   
  
Once it up and run the server you can perform api calls using API clinet like postman
>http://127.0.0.1:5000/


CRUD users
-----------------------------------------
user add elon       -> Add the user elon
>ex: POST http://127.0.0.1:5000/user     
>{
>"name":"elon",
>"email":"test@gmail.com",
> "status":"1",
> "title":"Mrs"  
> }

user delete elon    -> Delete the user elon
>DELETE http://127.0.0.1:5000/user/elon

user show elon      -> Show elon, his projects (and his groups)
> ex: GET http://127.0.0.1:5000/user/elon


user show           -> Show all user names
>ex: GET http://127.0.0.1:5000/user


same way we can perform project and groups CRUD operations also. All the API call well explain in code comment sections.

#Assigning
---------
assign user elon group tesla

> ex: POST http://127.0.0.1:5000/assign/group
> { 
> "name":"tesla",
> "user":"elon"
> }

assign user elon project model3 owner

> ex: POST http://127.0.0.1:5000/assign/user
> {
> "name":"elon",
> "project":"model3",
> "role":"owner" 
> }
>


assign group tesla project model3 employee

> ex: POST http://127.0.0.1:5000/assign/project
> {   
> "name":"model3",
> "group":"tesla",
> "role":"owner" 
> }

