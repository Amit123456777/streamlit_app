import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords

# Download NLTK resources (if not already downloaded)
nltk.download('punkt')
nltk.download('stopwords')

# Set page title and favicon
st.set_page_config(page_title="Stop Words Removal", page_icon="✨", layout="wide")

# Header Section with the updated image path
st.image(
    "https://github.com/Amit123456777/streamlit_website-stopword-punctuation-removal-/blob/main/Screenshot%202024-11-29%20234452.png",
)

st.markdown("""
<h1 style='text-align: center; color: #FF5733;'>📝 Stop Words Removal App</h1>
<p style='text-align: center;'>Effortlessly clean your text by removing stop words and punctuation for better insights! ✨</p>
""", unsafe_allow_html=True)

# Input Section
st.markdown("### 🚀 **Enter Your Text Below:**")
text = st.text_area("Type or paste your text here:", placeholder="e.g., Hello, how are you?")

# Create columns for layout
col1, col2 = st.columns([1, 1])

with col1:
    if st.button("✨ Clean Text"):
        if text.strip():  # Check if text is not empty
            # Tokenize text
            words = word_tokenize(text)

            # Stop words and punctuation
            stop_words = set(stopwords.words("english"))
            punctuation_set = set(punctuation)

            # Filtered words
            filtered_words = [word for word in words if word.lower() not in stop_words and word not in punctuation_set]

            # Display results
            st.markdown("### 🎉 **Filtered Text**")
            st.success(" ".join(filtered_words))
        else:
            st.error("Please enter some text to process.")

with col2:
    st.markdown("### 🌟 **Features**")
    st.markdown("""
    - **Easy to Use:** Paste your text and click a button!
    - **Stop Words Removal:** Removes common stop words (e.g., *is, the, and*).
    - **Punctuation Cleaning:** Cleans up symbols like commas and periods.
    - **Instant Results:** View cleaned text immediately.
    """)

# Footer Section
st.markdown("---")
st.markdown("""
<div style='text-align: center;'>
    <p>Made with ❤️ by Amit Sharma</p>
    <p>🌐 <a href="https://www.linkedin.com/in/amit-sharma-868b3a23a/" target="_blank">Visit My Website</a> | 📧 <a href="amsharma@gmail.com">Contact Me</a></p>
</div>
""", unsafe_allow_html=True)
