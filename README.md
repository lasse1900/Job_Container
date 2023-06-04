# Job Seacher Master New


## Getting started

- **Notes for team updating the repository**
- Please read the GitLab Flow short notes from the Documents directory
- If your are handling the repository mainly alone, please read *GitLab_readme.md*


### Basic Info 1

- **Note1 env variables** 
- App needs RadipAPI-key to get valid response to requests, you can see find the _env -file at the root directory
- You might need also password for sending emails with Etteplan's smtprelay
- While using Etteplan's 'internal mail relay' you don't need password

- **Note2 csv files** 
- contacts.csv file is used to read needed emails to send attachments, colums are: name, email
- search_terms.csv file is used to read keywords according to location, colums are: keyword, location

### Basic Info 2
- **Running the application** 
- At this point the program will be run at command line with command: [python request_jobs.py]

### Basic Info 3
- **Running the application with Flask** 
- the application is started with command [python app.py] is open at: http://localhost:5000

### Basic Info 4
- **Running the dockerized application** 
- First build the container and then run it, the application is open at: http://localhost:5000

### First build Docker, Secondly run Docker:
docker build -t my-flask-app .
docker run -p 5000:5000 my-flask-app

### Delete both:
docker rm -vf $(docker ps -a -q)
docker rmi -f $(docker images -a -q)

(docker system prune -a) if really needed

### To stop Docker container:
- docker ps
- docker stop <container_id_or_name>

### To see the app at 5000:
- http://localhost:5000