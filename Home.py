import streamlit as st
import requests
import re
import nltk
import spacy

# Load spaCy English tokenizer
nlp = spacy.load("en_core_web_sm")

nltk.download('words', quiet=True)
from nltk.corpus import words
from nltk.stem import WordNetLemmatizer

def make_prediction(user_input):
    api_url = "http://localhost:5000/predict"
    data = {"input": user_input}
    response = requests.post(api_url, json=data)
    if response.status_code == 200:
        prediction_data = response.json()
        return prediction_data.get('classification')
    else:
        st.error("Failed to get prediction from the API.")
        return "Error"

def load_custom_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def navigate_to(page_name):
    st.session_state.current_page = page_name
    st.rerun()

def validate_input(user_input):
    english_words = set(words.words())
    lemmatizer = WordNetLemmatizer()

    if not user_input.strip():
        return ["Input cannot be empty."]
     
    
    # Semantic check for at least one verb
    doc = nlp(user_input)
    if not any(token.pos_ == "VERB" for token in doc):
        return ["The sentence doesn't seem to contain a verb. Please make sure it's meaningful."]
    
    # Preprocess input: remove punctuation for validation except apostrophes
    cleaned_input = re.sub(r"[,.;?!]", "", user_input)
    input_words = cleaned_input.split()
    # Allow words with apostrophes by skipping them in the non-English words check
    non_english_words = [word for word in input_words 
                         if "'" not in word and 
                         word.lower() not in english_words and 
                         lemmatizer.lemmatize(word.lower()) not in english_words]

    if non_english_words:
        return [f"Non-English or unrecognized words detected: {', '.join(non_english_words)}"]

    if len(user_input) < 10:
        return ["Input is too short."]
    if len(user_input) > 250:
        return ["Input is too long."]
    
    return []

load_custom_css()

if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

st.markdown("<h1 style='text-align: center; margin-bottom: 1rem;'>PolarPulse</h1>", unsafe_allow_html=True)

if st.session_state.current_page == "Home":
    st.header("Welcome !")
    st.subheader("Your privacy, Our promise.")
    st.caption("Your journey to understanding begins here. In a world of words, find the support and clarity you seek with us.")
    if st.button('Start here'):
        navigate_to("Test")

elif st.session_state.current_page == "Test":
    st.markdown("## How do you feel today?")
    user_input = st.text_area("", placeholder="Enter your feelings...", max_chars=250)
    if st.button('Submit', key='submit_test'):
        errors = validate_input(user_input)
        if errors:
            for error in errors:
                st.error(error)
        else:
            st.session_state.prediction = make_prediction(user_input)
            navigate_to("Result")

    if st.button('Go back to Home'):
        navigate_to("Home")

elif st.session_state.current_page == "Result":
    st.markdown("## Results")
    if st.session_state.prediction:
        st.write(f"The prediction based on your input is: {st.session_state.prediction}")
    else:
        st.write("No prediction was made. Please go back to the Test page.")
    if st.button('Try Again'):
        navigate_to("Test")
    if st.button('Go back to Home', key='result_home'):
        navigate_to("Home")
