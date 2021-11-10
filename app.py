# Importing Libraries
import ast
import requests
from DataGeneratorTransformer import TransformerDataGenerator
from flask import Flask, jsonify

# Flask App
app = Flask(__name__)

# Default Route
@app.route("/")
def transformer_output():
    '''
    Function to respond to API Request.
    '''

    # Power BI URL
    REST_API_URL = 'https://api.powerbi.com/beta/e4e34038-ea1f-4882-b6e8-ccd776459ca0/datasets/9f0c52af-55e6-4742-9b1c-9f7d999901ca/rows?key=hgrgOr9z%2FzDWNkbKuZyVc2d4xFQeLmtG4CJIOitR93xS6GFHCIpstEwUxlMbLf4NK4ZGjzwJ7N1g%2FRQW8TRjhA%3D%3D'
    
    # Data Generator
    tf = TransformerDataGenerator()
    tf_json = tf.data_generator()[0]

    # JSON Response
    data_json = bytes(tf_json, encoding='utf-8')

    # Posting Data to Power BI API
    req = requests.post(REST_API_URL, data_json)
    
    # Generating Output
    tf_dict = ast.literal_eval(tf_json[1:len(tf_json) - 1])
    return jsonify(tf_dict)