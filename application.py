from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)  
app = application

# Import ridge regressor and Standard Scaler
ridge_model = pickle.load(open('models/Ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('models/Scaler.pkl', 'rb'))  # Fixed incorrect file path

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method == "POST":
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        WS = float(request.form.get('WS'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        new_scaled_data = standard_scaler.transform([[Temperature,RH,WS,Rain,FFMC,DMC,ISI,Classes,Region]])
        result = ridge_model.predict(new_scaled_data)

        return render_template('home.html',result=result[0])

    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)