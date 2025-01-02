"""
This module sets up a Flask web server for an emotion detection application.

The server exposes an endpoint `/emotionDetector` which accepts a text input
and returns the detected dominant emotion using the `emotion_detector` function
from the `EmotionDetection` module.

Routes:
    /emotionDetector: Accepts a GET request with a `textToAnalyze` parameter and
                      returns the detected dominant emotion.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """
    Endpoint to detect the dominant emotion in the provided text.

    This function handles GET requests to the `/emotionDetector` endpoint.
    It expects a query parameter `textToAnalyze` containing the text to be analyzed.
    The function uses the `emotion_detector` to determine the dominant emotion
    in the text and returns the result.

    Returns:
        str: The dominant emotion detected in the text or an error message if the text is invalid.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    print(text_to_analyze)
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"""For the given statement, the system response is
            'anger': {response['anger']},
            'disgust': {response['disgust']},
            'fear': {response['fear']},
            'joy': {response['joy']} and
            'sadness': {response['sadness']}.
            The dominant emotion is <b>{response['dominant_emotion']}</b>."""

@app.route("/")
def render_index_page():
    """
    Route for the index page.

    This function handles the root URL ("/") of the Flask application and 
    renders the 'index.html' template.

    Returns:
        Response: The rendered 'index.html' template.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
