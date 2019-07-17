# Northwind Traders

**Version 1.0.0**

View, sort, and filter items from existing tables in a database.

A simple web app to explore how Flask uses html/Jinja2 templates in rendering web pages to HTTP requests controlled by Flask routes.

## Demo

Visit [northwindtraders.herokuapp.com](https://northwindtraders.herokuapp.com/) for a demonstration of the Northwind Traders web application.

## Get started with Flask Web App locally

Ensure you have Python and Flask installed, then:

``` bash
# Clone repository
$ git clone https://github.com/ethanmiller1/Python-and-Flask-Web-App.git
# Install a virtual environment
$ cmd
$ python –m venv venv
# Activate the virtual environment
$ cd venv/Scripts && activate && cd ../..
# Install dependencies in the virtual environment
$ pip install -r requirements.txt
# Run app
$ python northwind.py
# Or run with flask
$ set FLASK_APP=northwind.py && set FLASK_DEBUG=1 && flask run --reload
```

(Note: Powershell is known to have problems with `set FLASK_APP=northwind.py`. Activate cmd with `cmd`.)

### Entry Point

`northwind.py` contains all the routes for the project. Use `set FLASK_APP=northwind.py` to set it as Flask's entry point for the project. Flask serves the application to [localhost:5000](localhost:5000 "Port 5000") by default.

## Deploy to Heroku

1. Download the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) and [login from your terminal](https://devcenter.heroku.com/articles/heroku-cli#getting-started).
1. Install gunicorn with `pip install gunicorn` and add to `requirements.txt`.
1. Create a `Procfile` containing the following code:

``` Procfile
web: gunicorn northwind:app
```

4. Create a [Heroku app](https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app) with `heroku create`.
1. Commit changes to git and push to the created heroku remote:

``` bash
$ git push heroku master
```

## Deploy to Netlify

1. Download Frozen Flask with `pip install Frozen-Flask`, then create a file called `freeze`:

``` python
from flask_frozen import Freezer
from northwind import app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
```

2. Be sure to render a `requirements.txt` with `pip freeze > requirements.txt` and create a `runtime.txt` to specify the Python version your app is built in (`3.7` for this app).
1. Link to your GitHub repository on [Netlify](https://app.netlify.com) and insert the following commands:

* Build command: `python freeze.py`.
* Public directory: `build`.

![](https://miro.medium.com/max/700/1*kPMjcU3kUaoJ9DmamhlcRA.png)

Freezer basically renders all of your possible HTML pages into a "build" folder and Netlify runs the website from there. This provides certain limitations and is not ideal for websites that interact with client POST requests, but will be fine for a static database as we have here.

### uwsgi

To keep your app MVC in production, create a uwsgi configuration file named `uwsgi.ini`.

## Technologies

There are 7 technologies used in this project:

 - Python
 - Flask
 - sqlite
 - HTML
 - CSS
 - Jinja2
 - jQuery

## Contributors

---

- Ethan Miller <ethan.romans5.8@gmail.com>

---

## License & copyright

© Ethan Miller