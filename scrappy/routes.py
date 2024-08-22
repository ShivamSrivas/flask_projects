from flask import Blueprint, request, jsonify,render_template
from scrappy.services import Scrappy
from http import HTTPStatus


scrappy_bp = Blueprint('scrappy_bp', __name__)

@scrappy_bp.route('/scrappy-page')
def shorten_url_page():
    return render_template('scrappy.html')

@scrappy_bp.route('/scrappy-scrape', methods=['POST'])
def shorten_urls_services():
    try:
        if request.method == "POST":
            import os
            image_dir = 'static/images'
            [os.unlink(os.path.join(image_dir, f)) for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
            scrapeQuery = request.form.get('scrapeQuery')
            scrapeCount = int(request.form.get('scrapeCount'))
            print(scrapeQuery,scrapeCount)
            obj = Scrappy(scrapeQuery,scrapeCount)
            response = obj.download_images()
            image_list = os.listdir(r'static/images')
            return render_template('scrappy.html', flag=True,image_list=image_list)
    except Exception as error:
        return jsonify({'error': f'An error occurred: {str(error)}'}), HTTPStatus.INTERNAL_SERVER_ERROR

