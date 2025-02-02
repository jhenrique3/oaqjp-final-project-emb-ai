from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Analyzer")

@app.route("/emotionDetector")
def emotion_analyzer():
    textToAnalyze = request.args.get('textToAnalyze')
    response = emotion_detector(textToAnalyze)
    if response['dominant_emotion'] == None:
        return "Invalid text! Please try again!"
    else:
        return f"For the given statement, the system response is 'anger': {response['anger']}, 'disgust': {response['disgust']}, \
        'fear': {response['fear']}, 'joy': {response['joy']} and 'sadness': {response['sadness']}. The dominant emotion is <b>{response['dominant_emotion']}</b>"

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
