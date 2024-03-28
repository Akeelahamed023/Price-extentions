## Running the Server

### Versopn
> Python 3.10.9

### Prerequisites
 Installing the required packages
```bash
pip install -r requirements.txt
```

### Running the server

!!! warning
    Make sure you are in the server directory 


### migrate the database
```bash
python manage.py makemigrations
python manage.py migrate
```

### create a superuser
```bash
python manage.py createsuperuser
```
!!! note
    You will be prompted to enter a username, email and password. You can use these credentials to login to the admin panel.

```bash
python manage.py runserver
```

