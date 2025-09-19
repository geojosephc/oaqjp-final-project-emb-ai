''' This is the main app file which receives requests from the 
webpage and does emotion detection for the text received'''
from flask import Flask,request,render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/')
def home():
    '''This function renders the home page'''
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detect():
    '''This function receives the user input text and 
    return the emotion detection result back to the user'''
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    return f"For the given statement the system response is \
    'anger': {result['anger']}, 'disgust': {result['disgust']}, \
    'fear': {result['fear']}, 'joy': {result['joy']}, \
    'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
