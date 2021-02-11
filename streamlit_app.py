import streamlit as st
import base64

# Display some header text
"""
# Upload and Download

This little program tests Streamlit's upload and download 
functionality. Note: Your file is not stored anywhere other than in
the Streamlit server's memory.
"""

# Allow the user to browse the source code.
with st.beta_expander("See source code"):
    source = open(__file__).read()
    start_sentinal = source.find('#>')
    end_sentinal = source.find('#<')
    st.code(source[start_sentinal + 2 : end_sentinal])

# Source code starts below
#>

st.markdown("""
## Upload

Upload any file. We'll give you the chance to download it
afterwards.
""")

my_file = st.file_uploader("Upload any file.")
if my_file == None:
    st.stop()

b64 = base64.b64encode(my_file.read()).decode()

st.markdown(f"""
## Download

Click 
<a href="data:file/kml;base64,{b64}" download={my_file.name}>
    this link
</a>
to download `{my_file.name}`.
""", unsafe_allow_html=True)

#<
# Source code ends above

