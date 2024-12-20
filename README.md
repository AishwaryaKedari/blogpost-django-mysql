# install virtual environment
    pip install virtualenv

# install virtual environment
    virtualenv --version

# create virtual environment
    virtualenv env

# Activate virtual environment
    source virtualenv_name/bin/activate

# Install all required django verions or others using requirements.txt file
    pip install -r requirements.txt

# Changing Database Sqlite to MYSQL

# Access MySQL
# Log in to the MySQL database server as root.
    $ sudo mysql -u root -p

# Enter the root user password you set earlier when prompted.

# Create a new sample MySQL database. For example, my_database.
    mysql> CREATE DATABASE my_database;

# Create a new MySQL database user with a strong password. For example, my_user and replace my_password with your desired password depending on your password strength policy.

    mysql> CREATE USER 'my_user'@'localhost' IDENTIFIED BY 'my_password';

# Grant the database user my_user full privileges to your sample database my_database.

    mysql> GRANT ALL PRIVILEGES ON my_database.* TO 'my_user'@'localhost';

# Refresh the MySQL privilege tables to apply the new user changes.

    mysql> FLUSH PRIVILEGES;

# Exit the MySQL database console.

    mysql> Exit

#  Update Django Settings:
# In your project's settings.py file, modify the DATABASES setting:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'your_database_name',
            'USER': 'your_database_user',
            'PASSWORD': 'your_database_password',
            'HOST': 'your_database_host',  # Usually 'localhost'
            'PORT': '3306',  # Default MySQL port
        }
    }



