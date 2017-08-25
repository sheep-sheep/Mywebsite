import os
from flask import Flask, render_template
from flask import send_from_directory
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')
APP_DOCS = os.path.join(APP_STATIC, 'docs')
@app.route('/docs', defaults = {'filename': 'index.html'})
@app.route('/docs/<path:filename>')
def render(filename):
    path = os.path.join(os.sep, 'docs', 'html')
    print filename
    print path
    path2 = os.path.join(os.sep, APP_DOCS, 'html')
    print path2
    return send_from_directory(path2, filename)