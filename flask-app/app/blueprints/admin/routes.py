from . import admin


@admin.route('/index')
def index():
    return 'hello world'