import streamlit as st

st.title("Simple Factor Tree Input")

st.write("Factor tree for 36")

st.write("        36")

col1, col2, col3 = st.columns([1, 0.2, 1])
with col1:
    f1 = st.number_input(" ", key="f1", label_visibility="collapsed", min_value=1)
with col2:
    st.write("×")
with col3:
    f2 = st.number_input(" ", key="f2", label_visibility="collapsed", min_value=1)

if f1 and f2:
    if f1 * f2 == 36:
        st.success("✅ Correct factor pair!")
    else:
        st.error("❌ Try again.")

st.write("Factor further:")

col4, col5, col6 = st.columns([1, 0.2, 1])
with col4:
    f1a = st.number_input(" ", key="f1a", label_visibility="collapsed", min_value=1)
with col5:
    st.write("×")
with col6:
    f1b = st.number_input(" ", key="f1b", label_visibility="collapsed", min_value=1)

if f1a and f1b and f1:
    if f1a * f1b == f1:
        st.success(f"✅ Correct! Factors of {f1}")
    else:
        st.error(f"❌ Try again for {f1}")

col7, col8, col9 = st.columns([1, 0.2, 1])
with col7:
    f2a = st.number_input(" ", key="f2a", label_visibility="collapsed", min_value=1)
with col8:
    st.write("×")
with col9:
    f2b = st.number_input(" ", key="f2b", label_visibility="collapsed", min_value=1)

if f2a and f2b and f2:
    if f2a * f2b == f2:
        st.success(f"✅ Correct! Factors of {f2}")
    else:
        st.error(f"❌ Try again for {f2}")
