from flask import Flask, send_file, request
import argparse
import os
app = Flask(__name__)
parser = argparse.ArgumentParser()
parser.add_argument('-a', '--arg', default="c", help="The argument to get from the request (default is 'c').")
parser.add_argument('-f', '--path', default="image.jpg", help="The path to the image file to serve (default is 'image.jpg').")
parser.add_argument('-p', '--port', default="80", help="The port to run the server on (default is '80').")
parser.add_argument('-r', '--route', default="/", help="The route to serve the image on (default is '/').")
parser.add_argument('-s', '--serve_image', action='store_true', help="A flag to determine whether to serve the image or not (default is False).")

args, unknown = parser.parse_known_args()
if not os.path.exists(args.path):
    print("No such file")
    exit(0)
@app.route(str(args.route))
def serve_image():
    try:
        cookie_value = request.args.get(str(args.arg))
        print("Cookie Value: ", cookie_value)
        if args.serve_image:
            return send_file(str(args.path), mimetype='image/jpg/png')
        else:
            return "Not Found", 404
    except:
        return "Not Found", 404

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')