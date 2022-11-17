#  library - by Or Smadga

project by Or Smadga
John Bryce full stack
course 7731/12
project uses Flask as a web framwork,
uses Jinja2 engine as a view engine,
uses SQLAlchemy as an ORM,
uses SQlite3 as a DB.


**Key parts**

app.py is now just the entry point to the app, and all code related to making the app is placed in a project directory. Because we no longer configure everything at top level, Flask will look for an `__init__.py` file inside project directory. We'll place all the configurations for our app there.


### Setup

If you have not installed Python3, [please do](https://www.python.org/downloads/).

First create and activate some form of environment to store your dependencies. I like [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html):

```
$ conda create -n myenv python=3.7

$ conda activate myenv
```

**Or** just use Pythons built in environments:

```
$ python3 -m venv venv

$ .venv/bin/activate
```
**Or** install virtualenvs:
```

$ pip install virtualenv
$ python -m virtualenv myenv
$ myenv\Scripts\activate
```

then, install the requierments 

`$ pip install -r requirements.txt`
```
DB under instance folder should come with data.
to add data  run

$ py .\init_db.py

```

### Run the app

`$ flask run`

You should now be able to see the output in your browser window (at http://127.0.0.1:5000) 


