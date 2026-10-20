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
        st.session_state.search_done = True
    else:
        st.session_state.search_done = False

if st.session_state.search_done:

        st.success("Search submitted.")

        st.subheader("Potentially Relevant AEs")

        st.caption(
            "These are sample results for testing. "
            "AI search is not connected yet."
        )

        st.markdown("### AE001 - Alex Tan")

        select_ae001 = st.checkbox(
            "Select Alex Tan for comparison",
            key="ae001"
        )
        st.write("**Sub-sector:** Children & Youth")
        st.write("**Expertise:** Youth Work, Counselling")
        st.write("**Training Experience:** 12 years")
        st.write("**AE Effectiveness:** 95%")

        st.divider()

        st.markdown("### AE002 - Jamie Lim")

        select_ae002 = st.checkbox(
            "Select Jamie Lim for comparison",
            key="ae002"
        )
        st.write("**Sub-sector:** Children & Youth")
        st.write("**Expertise:** Trauma-Informed Practice")
        st.write("**Training Experience:** 8 years")
        st.write("**AE Effectiveness:** 93%")

        st.divider()

        st.markdown("### AE003 - Taylor Lee")
        select_ae003 = st.checkbox(
            "Select Taylor Lee for comparison",
            key="ae003"
        )
        st.write("**Sub-sector:** Family")
        st.write("**Expertise:** Family Violence, Case Management")
        st.write("**Training Experience:** 10 years")
        st.write("**AE Effectiveness:** 96%")


