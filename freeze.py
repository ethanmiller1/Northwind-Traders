from flask_frozen import Freezer
from northwind import app

freezer = Freezer(app)

freezer.freeze()
