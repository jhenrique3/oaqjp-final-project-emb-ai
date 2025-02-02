'''
App "Emotion Analyzer"
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Analyzer")

@app.route("/emotionDetector")
def emotion_analyzer():
    '''
    This function gets the text from the form and sends
    to the Watson's API
    '''

    text = request.args.get('textToAnalyze')
    response = emotion_detector(text)
    if response['dominant_emotion'] is None:
        answer = "Invalid text! Please try again!"
    else:
        answer = f"""
            For the given statement, the system response is 'anger': {response['anger']},
            'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']}
            and 'sadness': {response['sadness']}. The dominant emotion is <b>{response['dominant_emotion']}</b>
        """
    return answer

@app.route("/")
def render_index_page():
    '''
    Function rendering the Index file
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
