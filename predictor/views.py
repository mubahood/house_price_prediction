# predictor/views.py

from django.shortcuts import render
from .forms import HousePriceForm
import joblib
import numpy as np

# Load the trained model and scaler
ridge_model = joblib.load('predictor/ridge_model.pkl')
scaler = joblib.load('predictor/scaler.pkl')

def predict_price(request):
    if request.method == 'POST':
        form = HousePriceForm(request.POST)
        if form.is_valid():
            # Extract data from form
            num_rooms = form.cleaned_data['num_rooms']
            house_age = form.cleaned_data['house_age']
            distance_to_city = form.cleaned_data['distance_to_city']
            
            # Prepare data for prediction
            input_data = np.array([[num_rooms, house_age, distance_to_city]])
            input_data_scaled = scaler.transform(input_data)
            
            # Make prediction
            predicted_price = ridge_model.predict(input_data_scaled)[0]
            
            # Render the result
            return render(request, 'predictor/result.html', {
                'predicted_price': int(predicted_price),
                'form': form
            })
    else:
        form = HousePriceForm()

    return render(request, 'predictor/predict.html', {'form': form})
