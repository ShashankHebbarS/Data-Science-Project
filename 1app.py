from flask import * 
import numpy as np
import os
import pickle
  
app = Flask(__name__)
 
@app.route('/')   
def home():  
    return render_template("Home.html")



@app.route('/IrisClass')
def IrisClass():
    return render_template('Iris.html')

def irispred(inp):
    arr = np.array(inp).reshape(1, 4)
    iris_model = pickle.load(open('iris.pkl', 'rb'))
    result = iris_model.predict(arr)
    return result[0]

@app.route('/IrisClass', methods=['POST'])
def IrisResult():
    if request.method == 'POST':
        inp = request.form.values()

        inp = list(map(float, inp))
        result = irispred(inp)

        return render_template('Iris.html', predictions=result)



@app.route('/TitanicPred')
def TitanicPred():
    return render_template('Titanic.html')

def titanicpred(inp):
    arr = np.array(inp).reshape(1, 6)
    titanic_model = pickle.load(open('titanic.pkl', 'rb'))
    result = titanic_model.predict(arr)
    return result[0]

@app.route('/TitanicPred', methods=['POST'])
def titanicresult():
    if request.method == 'POST':
        inp = request.form.values()
        inp = list(map(float, inp))
        result = titanicpred(inp)

        if result == 0:
            return render_template('Titanic.html', predictions='The Passenger Died')

        else:
            return render_template('Titanic.html', predictions='The Passenger Survived')


if __name__ =='__main__':  
    app.run(debug = True)
 