# DSCSM
## By Michael Armstrong
### Requirements
- Docker
- See requirements.txt and docker-compose.yml for dependencies

**THIS IS CONFIGURED FOR DEVELOPMENT PURPOSES. PLEASE SEE THE DEPLOYMENT SECTION BEFORE DEPLOYING.**

### Setup Instructions
1. Clone this repository. 
2. Navigate to your newly created directory and run the below commands to setup the docker container, static files, and migrations.
```
docker-compose build
docker-compose run web python manage.py collecstatic
docker-compose run web python manage.py migrate
```
3. To start the server, run the below code.
```
docker-compose up
```

4. The webpage should now be available at localhost:8000. 
    - If you get an error here, ensure that no other process is using port 8000.

### Administration
- To setup an administator account, run the below command. You will be prompted to create a username and password (the email is optional).
```
docker-compose run web python manage.py createsuperuser
```
- To log into the administration dashboard, go to localhost:8000/admin. 
- Once logged in, you can manage the models and database.
- The demo database is prebuilt with 7 sample blog posts and 3 sample portfolio entries. 

### Deployment
**TODO**
1. Follow the steps found in the [official Django documentation](https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/)
2. Create a /media/ directory in the root of the project
3. In the portfolio.Project model, change where Project previews are saved in by changing 
```
preview = models.ImageField(upload_to = "../demo_media/portfolio/images/")
```
to
```
preview = models.ImageField(upload_to = "../media/portfolio/images/")
```
4. Follow the **Setup Instruction** in this readme. 
