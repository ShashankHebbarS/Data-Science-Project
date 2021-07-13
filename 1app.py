from flask import Flask, render_template, request
import predictor
  
app = Flask(__name__)
 
@app.route('/')   
def home():  
    return render_template("Home.html")

@app.route('/IrisClass', methods=['GET', 'POST'])
def IrisClass():
    if request.method == 'POST':
        inp = request.form.values()

        inp = list(map(float, inp))
        result = predictor.irispred(inp)

        return render_template('Iris.html', predictions=result)

    return render_template('Iris.html')    

@app.route('/TitanicPred', methods=['GET', 'POST'])
def TitanicPred():
    if request.method == 'POST':
        inp = list(map(float, request.form.values()))
        result = predictor.titanicpred(inp)

        if result == 0:
            pred='The Passenger Died'

        else:
            pred='The Passenger Survived'

        return render_template('Titanic.html', predictions=pred)

    return render_template('Titanic.html')

if __name__ =='__main__':  
    app.run(debug = True)