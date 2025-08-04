"""
This module is the Flask web server for the EmotionDetection application.
It exposes a web page and an API endpoint to analyze text emotions.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
# Initiate the flask app
app = Flask("EmotionDetector")
# Define the route for the home page
@app.route("/")
def render_index_page():
    ''' Renders the index.html page. '''
    return render_template('index.html')
# Define the route for emotion detection
@app.route("/emotionDetector")
def sent_emotion_detector():
    ''' Detects emotions from the provided text and returns a formatted string. '''
    text_to_analyze = request.args.get('textToAnalyze')

    if text_to_analyze is None or text_to_analyze.strip() == "":
        return "Invalid input. Please provide text to analyze."

    response = emotion_detector(text_to_analyze)

    if response is None:
        return "An error occurred during emotion detection."

    # Extracting the scores and dominant emotion
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text. Please try again."

    # Formatting the output as per the requirements
    return (
    f"For the given statement, the system response is 'anger': {anger_score}, "
    f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} "
    f"and 'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}."
)

if __name__ == "__main__":
    # The application needs to be deployed on localhost:5000
    app.run(host="0.0.0.0", port=5000, debug=True)
