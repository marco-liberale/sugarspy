from flask import Flask, send_file, request
import argparse
import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Set up logging
logger = logging.getLogger('flask.app')
logger.setLevel(logging.INFO)

# File logging
file_handler = RotatingFileHandler('flask_app.log', maxBytes=10000, backupCount=1)
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)

# Stream (console) logging
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
logger.addHandler(stream_handler)

# Argument Parsing with validation
parser = argparse.ArgumentParser()
parser.add_argument('-a', '--arg', default="c", help="The name of the cookie to get (default is 'c').")
parser.add_argument('-f', '--path', default="image.jpg", help="The path to the image file to serve (default is 'image.jpg').")
parser.add_argument('-p', '--port', default=os.environ.get('PORT', 80), help="The port to run the server on (default is '80').")
parser.add_argument('-r', '--route', default="/", help="The route to serve the image on (default is '/').")
parser.add_argument('-s', '--serve_image', action='store_true', help="A flag to determine whether to serve the image or not (default is False).")

args = parser.parse_args()

# File Existence Check
if not os.path.exists(args.path):
    logger.error("No such file: %s", args.path)
    exit(0)

@app.route(str(args.route))
def serve_image():
    try:
        # Direct cookie handling
        cookie_value = request.cookies.get(str(args.arg))
        if cookie_value:
            logger.info("Cookie Value: %s", cookie_value)
            print("Cookie Value: ", cookie_value)
        else:
            logger.info("Cookie not found.")

        if args.serve_image:
            return send_file(str(args.path), mimetype='image/jpg/png')
        else:
            return "Not Found", 404
    except FileNotFoundError:
        logger.error("File not found error.")
        return "Not Found", 404
    except Exception as e:
        logger.error("An error occurred: %s", e)
        return "Internal Server Error", 500

if __name__ == '__main__':
    # Disclaimer for educational use
    logger.warning("This application is for educational purposes only and should not be used in production.")
    app.run(debug=False, port=args.port, host='0.0.0.0')
