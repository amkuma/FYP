# PolarPulse: Bipolar Disorder Detection Using NLP

## Overview
PolarPulse is a final year project that leverages advanced Natural Language Processing (NLP) techniques to detect potential signs of bipolar disorder from textual data. Developed as part of a BEng in Software Engineering thesis, it employs a Bidirectional Long Short-Term Memory (Bi-LSTM) network architecture to analyze tweets that reflect various moods indicative of bipolar disorder diagnoses. Through the identification of linguistic patterns and emotional cues, PolarPulse strives to advance the field of mental health by contributing to early, accurate, and non-invasive diagnostic methodologies.


## Installation

### Prerequisites
- Python 3.9 - 3.11
- pip


## Usage

This project consists of two main components: the backend API developed using Flask, and the frontend developed using Streamlit.

### Running the Backend
Navigate to the terminal and run the following command:
```bash
flask run
```
This starts the Flask server that acts as the backend and API for the application.

### Running the Frontend
In a separate terminal, run:
```bash
streamlit run Home.py
```
This command starts the Streamlit server and launches the frontend interface, which communicates with the Flask backend.


## Project Structure
- `Home.py` - The main entry point for the Streamlit frontend interface.
- `app.py` - Initializes the Flask server and includes the main application logic.
- `RNNModel.h5` - The pre-trained Bi-LSTM model used for making predictions.
- `prediction.py` - Contains functions to perform predictions using the model.
- `test_app.py` - Includes tests for the Flask application.
- `test_prediction.py` - Includes tests for the prediction logic.
- `tokenizer.json` - The tokenizer used for converting text inputs into a format suitable for model prediction.
- `fyp2.py` - The source file containing the model training.
- `style.css` - Frontend styling.
- `scripts.js` - Scripts enhancing the user interface.


## Contact
- Manickavasaga Kumaran Arunasalam - arunasalam.20201005@iit.ac.lk
- Project Link: https://github.com/amkuma/FYP

