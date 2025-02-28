# Project 01: Unit Convertor
# Build a Google Unit Convertor using Python and Streamlit:

import streamlit as st

# CSS Styling
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5; /* Light Gray Background */
    }
    
    @keyframes textGlow {
        0% { text-shadow: 0 0 10px #92fe9d; }
        50% { text-shadow: 0 0 20px #00c9ff; }
        100% { text-shadow: 0 0 10px #92fe9d; }
    }

    .custom-heading {
        text-align: center;
        font-size: 45px;
        font-weight: 900;
        padding: 25px;
        margin-top: -20px;
        border-radius: 12px;
        background: linear-gradient(45deg, rgb(148, 11, 98), #351c75, rgba(0, 201, 255, 0.4));
        color: white;
        animation: textGlow 2s infinite alternate;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }

    .stButton>button {
        background: linear-gradient(45deg, rgb(148, 11, 98), #351c75);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px rgba(0, 201, 255, 0.4);
    }

    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }

    .result-box {
        text-align: center;
        font-size: 22px; /* Bigger Font */
        font-weight: bold;
        margin-top: 20px;
        padding: 15px;
        border-radius: 12px;
        background: rgba(0, 201, 255, 0.1);
        box-shadow: 0px 4px 10px rgba(0, 201, 255, 0.3);
    }

    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        font-size: 18px;
        font-weight: 900;
    }

    .footer b {
        display: inline-block;
        font-size: 20px;
        font-weight: 900;
        animation: gradientText 2s infinite alternate;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Description
st.markdown("<div class='custom-heading'>🚀 Universal Unit Convertor</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Easily convert between different units of Length, Weight, and Temperature.</p>", unsafe_allow_html=True)

# Sidebar Menu
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion Functions
def length_conversion(value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28084, 'Inches': 39.3701,
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'Kilograms': 1, 'Grams': 1000, 'Milligrams': 1000000,
        'Pounds': 2.20462, 'Ounces': 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temp_converter(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else (value + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return ((value - 32) * 5/9) if to_unit == "Celsius" else ((value - 32) * 5/9 + 273.15) if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return (value - 273.15) if to_unit == "Celsius" else ((value - 273.15) * 9/5 + 32) if to_unit == "Fahrenheit" else value
    return value

# Button for conversion
if st.button("🔄 Convert"):
    if conversion_type == "Length":
        result = length_conversion(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_converter(value, from_unit, to_unit)

    # Show Result in a bigger box
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <style>
    @keyframes gradientText {
        0% { color: rgb(148, 11, 98); }
        100% { color: #00c9ff; }
    }
    
    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        font-size: 18px; /* Bigger Font */
        font-weight: 900; /* Maximum Bold */
    }
    
    .footer b {
        display: inline-block;
        font-size: 20px;
        font-weight: 900;
        animation: gradientText 2s infinite alternate; /* Automatic Animation */
    }
    </style>
    <div class='footer'><b>Developed by ©️ Code With Ammar</b></div>
    """,
    unsafe_allow_html=True
)