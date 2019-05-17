# Python and Flask App

**Version 1.0.0**

View, sort, and filter items from existing tables in a database.

A simple web app to explore how Flask can use views in rendering web pages to URLs controlled by Flask routes.

## Get started with Flask Web App locally

Ensure you have Python and Flask installed, then:

``` bash
git clone https://github.com/king-melchizedek/Python-and-Flask-Web-App.git
set FLASK_APP=northwind.py
flask run --reload
```

If you do not have Flask installed, use the virtual environment in the repository:

```
cd venv/Scripts
activate
cd ../..
```

(Note that PowerShell may have trouble activating virtual enviroments. Use cmd.)

### Entry Point

`northwind.py` contains all the routes for the project. Use `set FLASK_APP=northwind.py` to set it as Flask's entry point for the project. Flask serves the application to [localhost:5000](localhost:5000 "Port 5000") by default.

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