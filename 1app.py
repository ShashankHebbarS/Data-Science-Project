from flask import * 
import numpy as np
import os
import pickle
  
app = Flask(__name__)
 
@app.route('/')   
def home():  
    return render_template("Home.html"); 

@app.route('/IrisClass')
def IrisClass():
    return render_template('Iris.html')

def predictor(inp):
    arr = np.array(inp).reshape(1, 4)
    mod = pickle.load(open('iris.pkl', 'rb'))
    result = mod.predict(arr)
    return result[0]

@app.route('/results', methods=['POST'])
def result():
    if request.method == 'POST':
        inp = request.form.values()
        inp = list(map(float, inp))
        result = predictor(inp)

        return render_template('Iris.html', predictions=result)


if __name__ =='__main__':  
    app.run(debug = True)
 