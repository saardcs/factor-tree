import streamlit as st

st.title("Simple Factor Tree Practice")

number = 100
st.write(f"Find the factors step-by-step for: **{number}**")

# Step 1
f1 = st.number_input("Step 1: Enter a factor of 100", min_value=1, max_value=number, key="f1")
if f1 != 0 and number % f1 == 0:
    f2 = number // f1
    st.write(f"Good! The other factor is **{f2}**.")
else:
    st.error("That is not a factor of 100.")

# Step 2: Factor f1 if not prime and >1
if f1 > 1 and not st.button("f1 is prime"):
    st.write(f"Now, factor **{f1}**:")
    f1a = st.number_input(f"Enter a factor of {f1}", min_value=1, max_value=f1, key="f1a")
    if f1a != 0 and f1 % f1a == 0:
        f1b = f1 // f1a
        st.write(f"The other factor is **{f1b}**.")
    else:
        st.error(f"{f1a} is not a factor of {f1}.")

# Step 3: Factor f2 if not prime and >1
if 'f2' in locals() and f2 > 1 and not st.button("f2 is prime"):
    st.write(f"Now, factor **{f2}**:")
    f2a = st.number_input(f"Enter a factor of {f2}", min_value=1, max_value=f2, key="f2a")
    if f2a != 0 and f2 % f2a == 0:
        f2b = f2 // f2a
        st.write(f"The other factor is **{f2b}**.")
    else:
        st.error(f"{f2a} is not a factor of {f2}.")
