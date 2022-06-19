🇬🇧

# FlaskCourseFCC

```In progress```

## Table of contents:

- [The aim of the project](#the-aim-of-the-project)
- [What is my motivation?](#what-is-my-motivation)
- [Features](#features)
- [Technologies & Documentation](#technologies--documentation)
- [Installation](#installation)
- [Run](#run)
- [Useful commands](#useful-commands)

## The aim of the project

E-commerce website from [FreeCodeCamp](https://www.youtube.com/watch?v=Qr4QMBUPxWo&list=PL_U5mRW0SoP3ekwozd40G-6Q4WQCBWSsn&index=3) Flask youtube course.

Stopped at 2:25:37 / 6:21:03.

## What is my motivation?

I want to consolidate Flask framework doing some bigger app.

## Features

```In progress```

- [ ] Functionality of buttons on market site,
- [x] Created base.html and other pages are extends from base,
- [x] Added functionality for buttons on navbar (which are redirecting to Home and Market pages),
- [x] Created a SQLite3 database to store items,
- [x] Listing items from database,
- [x] Added user model which can own items,

## Technologies & Documentation

- [Python 3](https://docs.python.org/3/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [SQLite3](https://www.sqlite.org/docs.html)
- [SQLite3 browser](https://sqlitebrowser.org/dl/)

## Installation

<details>
<summary>Python:</summary>

Visit https://www.python.org/downloads/ and type which installing package you prefer (by your operating system) and download the package.

After download, go through installation process.

After above, let's check if Python is installed on your computer. To do this, open your terminal or command prompt and type:

For MacOS/Linux:
```
python3 --version
```

For Windows:
```
python --version
```
</details>

<details>
<summary>Virtual environment:</summary>

[More info about venv](https://docs.python.org/3/library/venv.html)

Open terminal/command prompt and create directory where you will create a django project using commands below:

```
ls                                                   # to check content of your domain directory
mkdir <directory_name>                               # to create a separated directory for project
cd <directory_name>                                  # just to go into new directory
python3 -m venv <virtualenv_name>                    # to create virtualenv using MacOS terminal
python -m venv <virtualenv_name>                     # to create virtualenv on Windows
source <virtualenv_name>/bin/activate                # to activate virtualenv on MacOS
<virtualenv_name>\Scripts\activate                   # to activate virtualenv on Windows

(<virtualenv_name>) <username>@<actual_directory> %  # after above you should see the (<virtualenv_name>). This line appears on MacOS.
```
</details>

<details>
<summary> Flask:</summary>

If you did above tutorials, now you should have schema of your files like:

```
Desktop/
    <directory_name>/
        <virtualenv_name>
```

Now we can install Flask framework. Simply type in your terminal/command prompt:

```
pip3 install flask     # on MacOS
pip install flask      # on Windows
```

</details>

<details>
<summary>All packages included in requirements.txt:</summary>

<details>
<summary>First option (preferred):</summary>

After clone this repo, type command:
```
pip3 install -r requirements.txt        # on MacOS
pip install -r requirements.txt         # on Windows
```

</details>

<details>
<summary>Second option:</summary>

Open file ```requirements.txt``` and type command with every package name:
```
pip3 install <package_name>     # on MacOS
pip install <package_name>      # on Windows
```

</details>

</details>

Perfect! Now, it's time to last episode.

##  Run

We've seen how to run venv. Keep that running!

<details>
<summary>Now we can simply clone this repo, and see if it's working on our machine (in case we did everything above count creating virtualenv):</summary>

```
git init                  # to initialize repository
git clone <repo url>      # to clone this repository into your local machine

python3 market.py    # using MacOS
python market.py     # using Windows
```
</details>

## Useful commands:

<details>
<summary>Setting a FLASK_APP variable and Debug statement:</summary>

```
export FLASK_APP=market.py
export FLASK_DEBUG=1

Than you can run the app using command:
flask run
```

</details>

<details>

<summary>Creating a database:</summary>

```
Write creating script (app.config, db variable) and than type (in projects terminal):
python          # on Windows
python3         # on MacOS

from market import db               # db stands for database variable which I've created (db = SQLAlchemy(app))
db.create_all()

Than db file should appear in your projects directory.
```

</details>

<details>

<summary>Creating items in db:</summary>

```
Keep your Python shell opened (like above) and type:

from <python_file_name> import <model_name>     # Let Python know what model you are going to pass into db. In my case it's going to be like: from market import Item
item1 = <model_name>(<args>)                    # Create variables (as a good practise) , than pass db.Model and args. In my case: item1 = Item(name='IPhone 10', price=500, barcode='123456789012', description='Desc')

db.session.add(item1)                           # Add item into db
db.session.commit()                             # Save the item in database

Verify db content:

<model_name>.query.all()                        # Check if you did it right and you have item in your db. In my case: Item.query.all()
```

</details>

<details>

<summary>Delete (drop) all information from your database:</summary>

```
python3         # on MacOS
python          # on Windows

from <package_name> import db

db.drop_all()
```

</details>

<details>

<summary>Adding items into db using Python shell:</summary>

```
i1 = Item(name='IPhone 11', description='My IPhone 11', barcode='123456789012', price=800)          # Creating item using variable
db.session.add(i1)                                                                                  # Adding item into db,
db.session.commit()                                                                                 # Saving item in db

The same in second case:
i2 = Item(name='MacBook Pro 15"', description='MacBook Pro from 2009', barcode='123456789011', price=1000)
db.session.add(i2)
db.session.commit()
```

</details>

<details>

<summary>Changing items parameters (in this case it's going to be an owner) using Python shell:</summary>

```
item1.owner = User.query.filter_by(username='Wojtek').first().id        # Important: pass into owner param id of the owner (look at Item model)
db.session.add(item1)
db.session.commit()
```

</details>

And that's it! Great job!