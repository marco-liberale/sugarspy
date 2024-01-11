# Sugarspy

Sugarspy is a demo tool for the backend of an image-based XSS cookie stealer. It is built using Flask, a lightweight WSGI web application framework.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of Python.
- You have a Windows/Linux/Mac machine.
- If using Docker, you have Docker installed on your machine.

## Installing Sugarspy

Using Git

To install Sugarspy, follow these steps:

1. Clone the git repository:
   ```
   git clone https://github.com/marco-liberale/sugarspy
   ```
3. Navigate to the cloned repository:
   ```
   cd sugarspy
   ```
5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```


## Usage

To use Sugarspy, you need to run the main Python script if not using Docker. The script accepts several command-line arguments:

- `-a, --arg`: The cookie argument to get from the request (default is "c" e.g https://URL/c=Cookieinfo).
- `-f, --path`: The path to the image file to serve (default is "image.jpg").
- `-p, --port`: The port to run the server on (default is "80").
- `-r, --route`: The route to serve the image on (default is "/").
- `-s, --serve_image`: A flag to determine whether to serve the image or not, if disabled it will grab the cookie and return 404: not found (default is Disabled).

Here is an example of how to run the script:
```
python3 main.py -a cookie -f /path/to/image.jpg -p 8080 -r /image -s
```
## Legal Disclamer
By using the repository, you acknowledge that you have read this [Disclaimer](https://github.com/marco-liberale/sugarspy/blob/main/legal_disclamer.md) and agree to be bound by the terms hereof.
If you do not agree to abide by the above, please do not use the repository.

Enjoy :)

