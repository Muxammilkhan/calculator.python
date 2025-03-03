import streamlit as st
import numpy as np
import math

def custom_css():
    st.markdown(
        """
       <style>
    body {
        background-color: rgba(0, 0, 0, 0.8);
        color: #ffffff;
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: linear-gradient(#e66465, #9198e5);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 15px rgba();
    }

    .stButton>button {
        width: 100%;
        background: linear-gradient(45deg, rgba(255, 0, 255, 0.8), rgba(98, 0, 234, 0.8), rgba(0, 212, 255, 0.8));
        color: white;
        border: none;
        padding: 12px;
        border-radius: 8px;
        transition:  0.2s ease-in-out, background 0.3s ease;
        font-size: 18px;
        font-weight: bold;
    }

    .stButton>button:hover {
    background: linear-gradient(45deg, rgba(255, 20, 147, 0.8), rgba(255, 69, 0, 0.8), rgba(255, 204, 0, 0.8));
    transform: scale(1.05);
    color: white; /* Button text color */
    text-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); /* Button text shadow *        transform: scale(1.05);
    }

    .stSelectbox, .stNumberInput {
        color: black;
        font-size: 18px;
    }
</style>

        """,
        unsafe_allow_html=True,
    )

def calculate(operation, num1, num2=None):
    if operation == "Add (+)":
        return num1 + num2
    elif operation == "Subtract (-)":
        return num1 - num2
    elif operation == "Multiply (×)":
        return num1 * num2
    elif operation == "Divide (÷)":
        return num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == "Power (^)":
        return np.power(num1, num2)
    elif operation == "Modulus (%)":
        return num1 % num2
    elif operation == "Square Root (√)":
        return np.sqrt(num1)
    elif operation == "Logarithm (log)":
        return np.log(num1) if num1 > 0 else "Error: Logarithm undefined"
    elif operation == "Exponential (e^x)":
        return np.exp(num1)
    elif operation == "Factorial (!)":
        return math.factorial(int(num1)) if num1 >= 0 and num1 == int(num1) else "Error: Factorial only for non-negative integers"
    elif operation == "Sine (sin)":
        return np.sin(np.radians(num1))
    elif operation == "Cosine (cos)":
        return np.cos(np.radians(num1))
    elif operation == "Tangent (tan)":
        return np.tan(np.radians(num1))
    else:
        return "Invalid Operation"

st.title  ("EquationLab ⚙️")
custom_css()

operation = st.selectbox("Choose an operation", [
    "Add (+)", "Subtract (-)", "Multiply (×)", "Divide (÷)", "Power (^)",
    "Modulus (%)", "Square Root (√)", "Logarithm (log)", "Exponential (e^x)",
    "Factorial (!)", "Sine (sin)", "Cosine (cos)", "Tangent (tan)"
])

if operation in ["Square Root (√)", "Logarithm (log)", "Exponential (e^x)", "Factorial (!)", "Sine (sin)", "Cosine (cos)", "Tangent (tan)"]:
    num1 = st.number_input("Enter number", value=0.0, step=0.1)
    num2 = None
else:
    num1 = st.number_input("Enter first number", value=0.0, step=0.1)
    num2 = st.number_input("Enter second number", value=0.0, step=0.1)

if st.button("🚀 Calculate"):
    result = calculate(operation, num1, num2)
    st.success(f"✅ Result: {result}")

st.markdown("---")
st.markdown("<p style='text-align: center;'>🌍 Made with ❤ by Muzammil </p>", unsafe_allow_html=True)    