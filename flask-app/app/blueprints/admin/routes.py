from . import admin

# Test application for errors
@admin.route('/index')
def index():
    return 'hello world'