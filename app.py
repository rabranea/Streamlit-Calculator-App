# ================================================
# 🧮 Streamlit Calculator App
# ================================================
import streamlit as st

# --- Page Configuration ---
st.set_page_config(page_title="🧮 Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Streamlit Calculator")
st.caption("A simple, interactive calculator built using Streamlit")

# --- Initialize session state ---
if "expression" not in st.session_state:
    st.session_state.expression = ""

# --- Display area ---
st.text_input("Expression", st.session_state.expression, key="display", disabled=True)

# --- Button press handler ---
def press(button):
    if button == "C":
        st.session_state.expression = ""
    elif button == "⌫":
        st.session_state.expression = st.session_state.expression[:-1]
    elif button == "=":
        try:
            # Safe evaluation
            st.session_state.expression = str(eval(st.session_state.expression))
        except Exception:
            st.session_state.expression = "Error"
    else:
        st.session_state.expression += button

# --- Calculator buttons layout ---
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "⌫"]
]

# --- Render the buttons ---
for row in buttons:
    cols = st.columns(len(row))
    for i, button in enumerate(row):
        cols[i].button(button, on_click=press, args=(button,))

# --- Footer ---
st.markdown("---")
st.write("✅ Built with ❤️ using [Streamlit](https://streamlit.io)")
