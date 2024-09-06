# predictor/forms.py
from django import forms

class HousePriceForm(forms.Form):
    num_rooms = forms.IntegerField(label='Number of Rooms', min_value=1)
    house_age = forms.IntegerField(label='House Age (in years)', min_value=0)
    distance_to_city = forms.IntegerField(label='Distance to City (in km)', min_value=0)