import streamlit as st

# Price per square foot for each locality (2025 data)
city_price_per_sqft = {
    "Jubilee Hills": 30550,
    "Banjara Hills": 12207,
    "Financial District": 11250,
    "Hitech City": 7800,
    "Somajiguda": 12207,
    "Kachiguda": 12207,
    "Narayanguda": 12207,
    "Yella Reddy Guda": 12207,
    "Kondapur": 8930,
    "Kukatpally": 6387,
    "Maheshwaram": 7382,
    "Patancheru": 5503,
    "Shadnagar": 5780,
    "Gachibowli": 10000,
    "Mazidpur": 1900,
    "Lemoor": 1950,
    "Mehtab Khan Gudem": 2000,
    "Nandigama": 2600,
    "Tupran": 1650,
    "Adibatla": 3394,
    "Saroornagar": 6074,
    "Chengicherla": 8888, 
    "Gurram Guda":8888, 
    "Kistareddypet":8888, 
    "Badangpet": 8888
}

# Constants for additional costs (customize as needed)
price_for_one_bedroom = 400000
price_for_one_washroom = 200000
price_for_one_parking = 150000

st.title("Hyderabad House Price Predictor (2025)")

city = st.selectbox("Select Locality", list(city_price_per_sqft.keys()))
area = st.number_input("Area (in sq. ft.)", min_value=100, step=10)
bedrooms = st.slider("Number of Bedrooms", min_value=1, max_value=5,step = 1)
washrooms = st.slider("Number of Washrooms", min_value=1, max_value=5, step=1)
parking = st.slider("Number of Parking Spaces", min_value=0, max_value=5, step=1)

if st.button("Calculate Price"):
    price_per_sqft = city_price_per_sqft[city]
    price = (area * price_per_sqft +
             bedrooms * price_for_one_bedroom +
             washrooms * price_for_one_washroom +
             parking * price_for_one_parking)
    st.success(f"Estimated Price: ₹{price:,.0f}")