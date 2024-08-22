from flask import Blueprint, request, jsonify,render_template
from shorten_urls.services import ShortenServices
from http import HTTPStatus

shorten_urls_bp = Blueprint('shorten_urls', __name__)

@shorten_urls_bp.route('/shorten-urls-page')
def shorten_url_page():
    return render_template('shorten-urls.html')

@shorten_urls_bp.route('/shorten-urls-services', methods=['POST'])
def shorten_urls_services():
    try:
        if request.method == "POST":
            original_url = request.form.get('original_url')
            redirect_options = request.form.get('redirect_option')
            link_length = int(request.form.get('link_length'))
            if not original_url and redirect_options:
                return jsonify({'error': 'Please fill the required field'}), HTTPStatus.BAD_REQUEST
            
            shorten_urls_object = ShortenServices(original_url, redirect_options, link_length)
            result = shorten_urls_object.shorten_url()
            print("Hello this is result",result)
            return render_template('shorten-urls.html', result=result)
    except Exception as error:
        return jsonify({'error': f'An error occurred: {str(error)}'}), HTTPStatus.INTERNAL_SERVER_ERROR

