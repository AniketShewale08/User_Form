# User_Form

#DJANGO NSTALLATION
    
    #INSTALL ANACONDA 
    
        LINK -> [ https://docs.anaconda.com/anaconda/install/ ]


    # Once the anaconda is installed in the system, then Open command prompt and paste this command to install django.
    
        -> conda install -c anaconda django
    
    # Check the django version
    
        -> python -m django --verson  


#TO RUN PROJECT
    
    # Create a new Environment for django devlopment.
    
        -> conda create --name MyDjangoEnv Django 
    
    # Activate the Django Environment.
    
        -> conda activate MyDjangoEnv

    

    # DATABASE

        # Creating a superuser.
    
        -> python3 manage.py createsuperuser
    
           # fill the following fields -
                - name
                - email
                - password

        # Apply migrations to do changes in database, Execute this three commands.
        
            -> python manage.py migrate
            -> python manage.py makemigrations
            -> python manage.py migrate  



    # Run Django server.

        -> python manage.py runserver

    # Copy the below address and paste this url into browser to run the project.
        
        -> [ http://127.0.0.1:8000/ ]


# To Logging in and using django admin site  
    
    -> http://127.0.0.1:8000/admin

    # Enter your superuser userid and password credentials.
    # This part of the site display all our models installed by the application.
    # You can further click on the model name to go to a screen that lists all its associated records.



    
