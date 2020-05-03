
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            age = int(request.form['age'])
            y_sex = (request.form['sex'])
            if(y_sex=='female'):
                sex=1
            else:
                sex=0
            bmi = float(request.form['bmi'])
            children = int(request.form['children'])
            is_smoker = (request.form['smoker'])
            if(is_smoker=='yes'):
                smoker=1
            else:
                smoker=0
            y_region = (request.form['region'])
            if(y_region=='southwest'):
                region=1
            elif(y_region=='southeast'):
                region=2
            elif(y_region=='northwest'):
                region=3
            else:
                region=4

            filename = 'finalized_model5.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction = loaded_model.predict([[age, sex, bmi, children, smoker, region]])
            print('your annual insurance premium is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html', prediction='{:.2f}'.format(prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=8001, debug=True)
	app.run(debug=True) # running the app