# ============================================
# 🧮 Streamlit Calculator (Advanced Version)
# ============================================
import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="🧮 Advanced Calculator", page_icon="🧮", layout="centered")
st.title("🧮 Streamlit Calculator")
st.caption("Perform basic arithmetic operations easily")

# --- Initialize history ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- User Inputs ---
num1 = st.number_input("Enter first number:", step=1.0, format="%.6f")
num2 = st.number_input("Enter second number:", step=1.0, format="%.6f")
operation = st.selectbox("Select Operation:", ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"])

# --- Calculate Result ---
result = None
if st.button("Calculate"):
    try:
        if operation == "Addition (+)":
            result = num1 + num2
        elif operation == "Subtraction (-)":
            result = num1 - num2
        elif operation == "Multiplication (×)":
            result = num1 * num2
        elif operation == "Division (÷)":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("❌ Cannot divide by zero!")
                result =
