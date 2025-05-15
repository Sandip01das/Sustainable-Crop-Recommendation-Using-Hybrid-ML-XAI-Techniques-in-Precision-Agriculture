from flask import Flask, request, render_template
import numpy as np
import pickle

# Load models and scalers
model = pickle.load(open('model1.pkl', 'rb'))
mx = pickle.load(open('minmaxscaler1.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html") 

@app.route("/predict", methods=['POST'])
def predict():
    # Fetch input values from form
    N = float(request.form['Nitrogen'])
    P = float(request.form['Phosphorus'])
    K = float(request.form['Potassium'])
    temperature = float(request.form['Temperature'])
    humidity = float(request.form['Humidity'])
    ph = float(request.form['pH'])
    rainfall = float(request.form['Rainfall'])

    # Combine inputs into a feature list
    feature_list = [
        N, P, K, temperature, humidity, ph, rainfall
    ]
    single_pred = np.array(feature_list).reshape(1, -1)

    # Scale features using MinMaxScaler and StandardScaler
    mx_features = mx.transform(single_pred)
    #sc_mx_features = sc.transform(mx_features)

    # Predict using the model
    prediction = model.predict(mx_features)

    # Map prediction to crop names
    crop_dict = {
        1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
        8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
        14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
        19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
    }

    # Return the result
    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        result = f"{crop} is the best crop to be cultivated right there."
    else:
        result = "Sorry, we could not determine the best crop to be cultivated with the provided data."

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
