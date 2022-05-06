from . import admin

# Test application for errors
@admin.route('/index')
def index():
    return 'Put some cool code here'