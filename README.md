# Blog Application
This project is similar to an blog application where a user can post, comment, like, delete or edit blog based on roles nad chat with persons who are online. 

![](https://i.imgur.com/fryPSkj.png)


The picture above will shows how the UI looks when the application is running and user had blogs.
- **Note**: The pagination that has applied here for single entitiy is for reference by default it was applied for 10 blogs/page.

### Overview of project 
- Users has divided into two role like admin and user.
- Users can see a list of posts in there dashboard once they login. It will be a paginatead view with 10 posts per page.
- A SignUp page to take basic inputs like name, email, password and role(just for this project :) ).
- A SignIn page to redirect to users dashboard page (containing all posts) after authentication.
- A separate page to add a new post and
- A separate page to view each post through a unique link.

### User flow
- step1:
  - Go to home page of app, if the user is authenticated it will go to users home page
  - If user is not authenticated it will redirects to signin page, if user doesnt have account he can create it by providing necessary details including role(user/admin) by sign up.
- step2:
  - User can post an blog from home page and he had full control of the post related to editing/deleting the post and like/unlike for his post.
  - If there are many post he can see all the posts by going through pagination.
  - If he want to view blog in different page he can copy blog link/by clicking on share icon on post he can view the post.
  - If he wants to delete/edit blog he can click on 3dots on card and can perfrom actions.
- step3:
  - If user wants to change firstname/lastname he can change in users setting page.
  - If the user role is admin the he has all the above permissions of all the posts (delete/edit) and enable/disabling user for the app.
  
### Other UI pages
##### SignUp Page
![](https://i.imgur.com/8YECDTu.png)
  
##### SignIn page
![](https://i.imgur.com/2Pbw8LP.png)
  
##### Edit, Delete, blog url in blog card
![](https://i.imgur.com/bps8EWw.png)

- **Note**: Edit,delete options can be seen only by admin/owner of the post.
  
##### Logout
![](https://i.imgur.com/U5ahSnk.png)
  
##### Post Blog
![](https://i.imgur.com/0NYy4QB.png)
- **Note** : The post button will get enabled when user starts typing in the input box.
  
##### Settings
![](https://i.imgur.com/lDHcRfy.png)
-  **Note**:Users tab on right side can be seen only by admins where they can enable/disable the users access to app.

## Real time chat support
This project supports real time chat with the users that has logged in and it uses Django channels
- just click on the chat icon in right side of navbar

![](https://i.imgur.com/h5yYziO.png)
- After that it will redirect to chats page where you can see all the usershad been logged in.
![](https://i.imgur.com/rhc7D8q.png)
- Then click on the radio button user that you want to chat with so that it can display weather the user is oneline or not.
- In order to check the other user is online create dummy account and login in another `Incognito tab`
- If both are connected you will be able to chat
  - In the below example i Logged in with `Goutham `  and connected with JohnDoe 
![](https://i.imgur.com/vWbyTOE.png)






  
## Stack details
```bash
Framework : python-Django
version : Django-3.0.3

Database:
Db : sqlite (default)

Backend:
Language : python
verison : python3

Front-end:
HTML : HTML5
css : bootstrap4
js

Hostname:
host : localhost (default)
```

## Installation

#### Run Redis docker
- By enabling chanel layer allows multiple consumer instances to talk with each other[Ref](https://channels.readthedocs.io/en/latest/tutorial/part_2.html#enable-a-channel-layer)
```bash
docker run -p 6379:6379 -d redis:2.8
```
```bash
mkdir new_project
cd new_project
python3 -m venv env
source env/bin/activate
git clone https://github.com/goutham2945/blog-app-with-chat.git
cd blog-app-with-chat/
```

```bash
pip3 install -r requirements.txt
```

```bash
python3 manage.py makemigrations
```

```bash
python3 manage.py migrate
```

```bash
python3 manage.py runserver 0:2222 
```
> Note: when you want to run this application on server, please add domain name/ip address in ALLOWEDHOSTS in settings.py

## In browser
```python
http://localhost:2222 
     or
http://<ipaddress/domain name>:2222 # when you are running on server
```


