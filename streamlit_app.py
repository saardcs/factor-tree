import streamlit as st

st.title("🧮 Interactive Factor Tree Practice")

numbers = [100, 56, 81, 70]

selected = st.selectbox("Choose a number to factor:", numbers)

st.write(f"### Factor tree for {selected}")

# Step 1: First factor pair of selected number
f1 = st.number_input(f"Step 1: Enter first factor of {selected}", min_value=1, max_value=selected, key="f1")
f2 = st.number_input(f"Step 1: Enter second factor of {selected}", min_value=1, max_value=selected, key="f2")

if f1 * f2 == selected:
    st.success("✅ Correct factor pair!")
else:
    st.error("❌ Factors do not multiply to the original number.")

# Step 2: Factor first factor further if not prime
if f1 > 1 and f1 != selected:
    st.write(f"Factor pair for {f1}:")
    f1a = st.number_input(f"Enter factor 1 of {f1}", min_value=1, max_value=f1, key="f1a")
    f1b = st.number_input(f"Enter factor 2 of {f1}", min_value=1, max_value=f1, key="f1b")
    if f1a * f1b == f1:
        st.success("✅ Correct!")
    else:
        st.error("❌ Incorrect factors.")

# Step 3: Factor second factor further if not prime
if f2 > 1 and f2 != selected:
    st.write(f"Factor pair for {f2}:")
    f2a = st.number_input(f"Enter factor 1 of {f2}", min_value=1, max_value=f2, key="f2a")
    f2b = st.number_input(f"Enter factor 2 of {f2}", min_value=1, max_value=f2, key="f2b")
    if f2a * f2b == f2:
        st.success("✅ Correct!")
    else:
        st.error("❌ Incorrect factors.")
