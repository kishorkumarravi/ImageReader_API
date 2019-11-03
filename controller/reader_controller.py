import os
import logging
import pytesseract
from PIL import Image

from flask import Flask, jsonify, request

UPLOAD_FOLDER = '/path/to/the/uploads'
app = Flask(__name__)


@app.route('/', methods=['GET'])
def about():
    """About route for Image reader API
    """
    logging.info("About Page")
    return jsonify(success=True, message='Image Reader API')


@app.route('/upload', methods=['POST'])
def upload():
    response_message = None
    response_status = False
    try:
        if 'file' not in request.files:
            response_message = 'File not found'
        else:

            file = request.files['file']
            file.save(os.path.join(os.getcwd(), file.filename))

            # Can be used to convert the file to image format
            # path = os.path.join(os.getcwd(),  file.filename)
            # img = Image.open(path)
            # img = img.convert('RGB')
            # pix = img.load()
            # for y in range(img.size[1]):
            #     for x in range(img.size[0]):
            #         if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
            #             pix[x, y] = (0, 0, 0, 255)
            # else:
            #     pix[x, y] = (255, 255, 255, 255)
            # img.save('temp.jpg')
            text = pytesseract.image_to_string(Image.open(file.filename))

            response_status = True
            response_message = text

    except Exception as err:
        response_status = False
        response_message = str(err)
    return jsonify(success=response_status, message=response_message)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False, threaded=True)
