from flask import Flask, request,jsonify
# from flask_cors import CORS  --> MIDDLEWARE NOT NEEDED FOR  NOW
import datetime
from console_engine_deploy import *
from console_engine_deploy import puzzle, grid, row_hints, col_hints
import os


app = Flask(__name__)
# CORS(app)     

  
x = datetime.datetime.now()
@app.route("/")
def sayHi():
    return "Hello World! GO to /data for more data :)"


@app.route("/data", methods=['GET', 'POST'])
def nonogram_data():
    rows, columns, max_sequential_val = 5, 5, 2
    puzzle = create_nonogram(rows, columns, max_sequential_val)
    grid, row_hints, col_hints = puzzle
    matrix = grid
    

    if request.method == 'POST':
    # # Compare the updated state with the matrix
    #     data = request.get_json()

    #     if matrix == data['player_grid']:
    #         return 'WIN!'
    #         # return jsonify({'success': True, 'message': f"Received data: {data['player_grid']}"})
    #     else:
    #       return 'Not a winner yet!'
        return "POST request"

    else:
        for row in grid:
            print(row)
        return {
        "Grid":grid,
        "Row_hints":row_hints,
        "Col_hints":col_hints
        }

@app.route("/grid", methods=['GET'])
def display_grid():
    
        return grid

   
@app.route("/post", methods=['POST'])
def post_method():
    return "POST request"


    
# The error message you're seeing indicates that the CORS policy is blocking your request from the origin http://localhost:3001 to the URL http://localhost:5000/data.
# CORS, or Cross-Origin Resource Sharing, is a security feature implemented in web browsers that restricts web pages from making requests to a different domain than the one that served the page. This security feature is in place to prevent malicious websites from stealing data from other websites.
# In order to allow your frontend application hosted at http://localhost:3001 to make requests to your backend API hosted at http://localhost:5000, you will need to configure your backend API to add the Access-Control-Allow-Origin header to its response. This header allows the browser to make cross-origin requests to the server.
# To fix the error, you can add the cors middleware to your Node.js backend API. 

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == '__main__':
    app.run()
    # confid:
    # app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), debug=True)
