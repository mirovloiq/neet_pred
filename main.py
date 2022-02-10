from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
loaded_model = pickle.load(open("UZ.sav", "rb"))
@app.route('/')
def index():
    return render_template('UNICEF_ZYPL.html')
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        if(request.form.get('childexist') == "No 1st child"):
            childexist = 0
        if(request.form.get('childexist') == "1st child exists"):
            childexist = 1
        if(request.form.get('Urban') == "Urban"):
            Urban = 1
        else:
            Urban = 2
        if(request.form.get('isFemale') == "Male"):
            isFemale = 1
        if(request.form.get('isFemale') == "Female"):
            isFemale = 2
        if(request.form.get('BeenAbroad') == "Yes"):
            BeenAbroad = 1
        else:
            BeenAbroad = 0
        if(request.form.get('edlevel') == "General education"):
            edlevel = 1
        if(request.form.get('edlevel') == "VET"):
            edlevel = 2
        if(request.form.get('edlevel') == "Tertury"):
            edlevel = 3
        if(request.form.get('healthy') == "Bad"):
            healthy = 0
        if(request.form.get('healthy') == "Very good"):
            healthy = 1
        if(request.form.get('fjobexist') == "No 1st job"):
            fjobexist = 0
        if(request.form.get('fjobexist') == "1st job exists"):
            fjobexist = 1
        if(request.form.get('married') == "Single, never married and never cohabitated"):
            married = 0
        if(request.form.get('married') == "Married"):
            married = 1
        q1 = int(childexist)
        q2 = int(Urban)
        q3 = int(isFemale)
        q4 = int(BeenAbroad)
        q5 = int(edlevel)
        q8 = int(healthy)
        q9 = int(request.form.get('ageYr'))
        q10 = int(fjobexist)
        q11 = int(married)

        result = [q1, q2, q3, q4, q5, q8, q9, q10, q11]
        pr = loaded_model.predict([result])
        if(pr == 0):
            result = "Работает"
        else:
            result = "Не работает"
        
    return render_template("UNICEF_ZYPL.html", result_text = result)


if __name__ == "__main__":
    
    app.run()
