"""
This module initiates the Flask app for emotion analysis.
The app listens on localhost:5000 and processes text input
to detect emotions using the emotion_detector function.
"""
from flask import Flask, render_template, request
import requests
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the Flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Receive text input from query parameters, run emotion detection,
    and return the emotion scores and dominant emotion.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response

    url = 'https://sn-watson-emotion.labs.skills.network/v1/wa\
        tson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=myobj, headers=headers, timeout=1400)
    emotion_output = emotion_detector(text_to_analyze)

    # Check if the label is None, indicating an error or invalid input
    if response.status_code == 400 or emotion_output is None:
        #return "Invalid input! Try again."
        message = (
           "Inalid tex! Pleaset, try again. "
        )
    else:
        #Return a formatted string with the emotion predictions and score
        message = (
            f"For the given statement, the system response is "
            f"'anger': {emotion_output['anger']}, "
            f"'disgust': {emotion_output['disgust']}, "
            f"'fear': {emotion_output['fear']}, "
            f"'joy': {emotion_output['joy']} and "
            f"'sadness': {emotion_output['sadness']}. "
            f"The dominant emotion is {emotion_output['dominant_emotion']}."
        )
    #return message as the output in the required format
    return message

@app.route("/")
def render_index_page():
    """
    Render the index.html template as the home page.
    """
    return render_template('index.html')

#For deployment to localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
