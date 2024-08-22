from flask import render_template,request,Blueprint,jsonify,abort
from .services import PasteLockly


pastelockly_bp = Blueprint('pastelockly', __name__)

@pastelockly_bp.route('/paste-lockly-page')
def paste_lockly_page():
    return render_template('paste-lockly.html')

@pastelockly_bp.route('/paste-lockly-get-snippet/<int:id>', methods=['GET'])
def paste_lockly_get_snippet(id):
    obj = PasteLockly()
    snippet = obj.get_snippet(id)
    if snippet:
        return render_template('view-only-snippet.html',snippet = snippet)
    else:
        abort(404, description="Snippet not found")

@pastelockly_bp.route('/paste-lockly-encrpyt', methods=['POST'])
def paste_lockly_encrpyt():
    if request.method == 'POST':
        text = request.form.get('text')
        encrpyt_key = request.form.get('encrpytKey')
        obj = PasteLockly(text,encrpyt_key)
        obj = obj.create_sharable_link()
        return render_template('paste-lockly.html',obj=obj)
