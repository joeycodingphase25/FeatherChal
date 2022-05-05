from app import app
from flask import redirect, url_for

# Creation of immediate redirect to the admin blueprint
@app.route('/')
def index():
    return redirect(url_for('admin.index'))