from flask import Flask, redirect, url_for, jsonify, request,render_template
import pickle
import numpy as np
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
   return render_template("index.html")
   

@app.route('/ff',methods = ['POST', 'GET'])
def ff():
   return render_template("form.html")
  

@app.route('/predict',methods = ['POST'])
def predict():

   values=[]
   name=request.form['name']

   Pregnancies=request.form['Pregnancies']
   values.append(Pregnancies)
   
   Glucose=request.form['Glucose']
   values.append(Glucose)
   
   BloodPressure=request.form['BloodPressure']
   values.append(BloodPressure)

   SkinThickness=request.form['SkinThickness']
   values.append(SkinThickness)

   Insulin=request.form['Insulin']
   values.append(Insulin)
   
   BMI=request.form['BMI']
   values.append(BMI)
   
   DiabetesPedigreeFunction=request.form['DiabetesPedigreeFunction']
   values.append(DiabetesPedigreeFunction)

   Age=request.form['Age']
   values.append(Age)  
   
   
   final_values=[np.array(values)]
   print(final_values)
   

   prediction=model.predict(final_values)
   print(prediction)
   
   result=prediction
   print(result)
   
   if result==0:
       return {'message':'you are not diagnised'}
       
   else:
       return {'message':'you are  diagnised'}
       


if __name__ == '__main__':
   app.run(debug=True,use_reloader=False)
