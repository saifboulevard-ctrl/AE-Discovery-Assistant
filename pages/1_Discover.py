import streamlit as st

st.title("Discover AEs")

st.write(
    "Describe the type of Adult Educator you are looking for. "
    "You can include areas of expertise, sector experience, "
    "professional background and training experience."
)

requirement = st.text_area(
    "Describe your training requirement",
    placeholder=(
        "e.g. I am looking for an AE with experience working with "
        "vulnerable youths, a counselling background and experience "
        "facilitating practice-based training for social service practitioners."
    ),
    height=180
)

if st.button("Find Potentially Relevant AEs", type="primary"):
    if requirement.strip():
        st.success("Search submitted.")
    else:
        st.warning("Please describe the type of AE you are looking for.")
