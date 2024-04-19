import json
import pickle

from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)

## Load the model created
regmodel=pickle.load(open('regmodel.pkl','rb'))
scalar=pickle.load(open('scaling.pkl','rb'))

# Go to home.html
@app.route('/')
def home():
    return render_template('home.html') # render_template will look at the 'template folder'. calling home.html from the folder.

# create an API so you can post the data to the app and get a return on the prediction. 
# This function will capture the data and run it through the model
@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']               # capture the data in a json format and store it in data
    print(data)
    
    # when you get the data from json, it will be in key value pairs.
    # if you return print(data.values()), you will get the dictionary values. 
    # So 
    # 1. we convert this into a list, we will get a single list
    # 2. convert this into an array which we will reshape to (1,-1) as this is a single data point record that i am going to get
    # if we do not reshape to (1,-1) the transformation expect a single record with X number of features (13 in this case) from the dataset 
    print(np.array(list(data.values())).reshape(1,-1))   
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0]) #return the output in json format

@app.route('/predict',methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    final_input=scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=regmodel.predict(final_input)[0]
    return render_template("home.html",prediction_text="The House price prediction is {}".format(output))

if __name__=="__main__":
    app.run(debug=True)
   
     