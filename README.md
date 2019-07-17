# Python and Flask App

**Version 1.0.0**

View, sort, and filter items from existing tables in a database.

A simple web app to explore how Flask can use views in rendering web pages to URLs controlled by Flask routes.

## Get started with Flask Web App locally

Ensure you have Python and Flask installed, then:

``` bash
git clone https://github.com/ethanmiller1/Python-and-Flask-Web-App.git
cmd
python –m venv venv
cd venv/Scripts && activate && cd ../..
pip install -r requirements.txt
set FLASK_APP=northwind.py && set FLASK_DEBUG=1 && flask run --reload
```

(Note: Powershell is known to have problems with `set FLASK_APP=northwind.py`. Activate cmd with `cmd`.)

### Entry Point

`northwind.py` contains all the routes for the project. Use `set FLASK_APP=northwind.py` to set it as Flask's entry point for the project. Flask serves the application to [localhost:5000](localhost:5000 "Port 5000") by default.

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