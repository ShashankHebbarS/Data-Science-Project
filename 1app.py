from flask import Flask, render_template, request
import numpy as np
import pickle
  
app = Flask(__name__)
 
@app.route('/')   
def home():  
    return render_template("Home.html")



@app.route('/IrisClass', methods=['GET', 'POST'])
def IrisClass():
    if request.method == 'POST':
        inp = request.form.values()

        inp = list(map(float, inp))
        result = irispred(inp)

        return render_template('Iris.html', predictions=result)

    return render_template('Iris.html')

def irispred(inp):
    arr = np.array(inp).reshape(1, 4)
    iris_model = pickle.load(open('iris.pkl', 'rb'))
    result = iris_model.predict(arr)
    return result[0]

@app.route('/TitanicPred', methods=['GET', 'POST'])
def TitanicPred():
    if request.method == 'POST':
        inp = list(map(float, request.form.values()))
        result = titanicpred(inp)

        if result == 0:
            pred='The Passenger Died'

        else:
            pred='The Passenger Survived'

        return render_template('Titanic.html', predictions=pred)
        
    return render_template('Titanic.html')

def titanicpred(inp):
    arr = np.array(inp).reshape(1, 6)
    titanic_model = pickle.load(open('titanic.pkl', 'rb'))
    result = titanic_model.predict(arr)
    return result[0]

if __name__ =='__main__':  
    app.run(debug = False)