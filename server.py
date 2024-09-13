"""
Entry point for the Emotion Detection web app
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def get_index():
    """
    Home page endpoint
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def get_emotion_detector():
    """
    API endpoint for emotion detection functionality
    """
    if not request.args or not request.args.get("textToAnalyze"):
        return "Missing query parameter textToAnalyze", 400

    prediction = emotion_detector(request.args["textToAnalyze"])

    if not prediction:
        return "Internal server error", 500

    return (
        "For the given statement, the system response is "
        f"'anger': {prediction['anger']}, "
        f"'disgust': {prediction['disgust']}, "
        f"'fear': {prediction['fear']}, "
        f"'joy': {prediction['joy']}, "
        f"'sadness': {prediction['sadness']}. "
        f"The dominant emotion is <b>{prediction['dominant_emotion']}</b>."
    )

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
