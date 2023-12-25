import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="AI_Assistant | Chat-Bot 🤖")

st.balloons()

#Contact
with st.sidebar.expander("📬 Contact"):

    st.write("**GitHub:**",
"[Vineeth](https://github.com/vineeth2281)")


    st.write("**Mail** : vineethramesh@outlook.in")
    st.write("**Created by Vineeth Ramesh**")


#Title
st.markdown(
    """a
    <h2 style='text-align: center;'>AI Wizard, Your Data Guru</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>Vineeth Ramesh</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#AI_Assistant's Pages
st.subheader("🚀 Wiziard's Super Powers")
st.write("""
- **DocsQWizard**: General Chat on data (PDF, TXT,CSV) 


""")
st.markdown("---")







