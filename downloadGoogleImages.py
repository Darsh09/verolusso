from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# search_query = input('Enter search query')
# numberOfImages  = int(input('Number of Images'))

from google_images_download import google_images_download

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/google', methods=['GET'])
def google():
    return render_template('google.html')

@app.route('/instagram', methods=['GET'])
def instagram():
    return render_template('instagram.html')

@app.route('/website', methods=['GET'])
def website():
    return render_template('website.html')

@app.route('/classes', methods=['GET'])
def classes():
    return render_template('classes.html')

@app.route('/search', methods=['POST'])
def main():
    
    search_query=request.json['search']
    numberOfImages=request.json['number']
    
    response = google_images_download.googleimagesdownload()
    
    # def downloadimages(query):
        
    arguments = {"keywords": search_query,
                "format": "jpg",
                "limit":numberOfImages,
                "print_urls":True,
                "size": "medium",
                "aspect_ratio":"panoramic",
                "output_directory": os.path.join(os.path.join(os.environ['HOME']), 'Desktop')}
    # try:
    response.download(arguments)
    return render_template('google.html')

        # # Handling File NotFound Error	
        # except FileNotFoundError:
        #     arguments = {"keywords": query,
        #                 "format": "jpg",
        #                 "limit":4,
        #                 "print_urls":True,
        #                 "size": "medium"}
                        
        #     # Providing arguments for the searched query
        #     try:
        #         # Downloading the photos based
        #         # on the given arguments
        #         response.download(arguments)
        #         return 200
        #     except:
        #         pass
        #         return 500

            
    # Driver Code

    # downloadimages(search_query)
    # print()
    
# @app.route('/instasearch', methods=['POST'])
# def instasearch():
    
#     return NoneType

if __name__ == '__main__':
    app.run(debug=False)
