# swe_574

## How to start the Ocial project

### Local

Open the project(ocial/ocial_project) at your favorite Python IDE

Add (create new file) local_settings.py file in the ocial directory

Add SECRET_KEY to the local_settings.py

Add database settings to local_settings.py

Example code for local_settings.py

```
SECRET_KEY = 'rk?(5*xs(fh1z3d9qd+b=lx?(&mjbxmf_f1va%nbqa7b#d#(j7'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ocialdb',
        'USER': '******',
        'PASSWORD': '******',
        'HOST':'localhost',
        'PORT':'5432'

    }
}
```

Create the database if it does not exist 

Create the user if it does not exist 

Add password to the user if it does not exist 

Create an virtual environment if it does not exist

Activate the environment

Go to the project directory (ocial/ocial_project)

Run the fallowing codes:

```
pip install -r requirements.txt

python manage.py migrate

python manage.py collectstatic

python manage.py runserver
```

The project should be running now

More detailed guide: https://github.com/onurasiliskender/ocial/wiki/07.-System-Deployment-Guide

