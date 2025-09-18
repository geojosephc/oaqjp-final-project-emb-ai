from flask import Flask,request,render_template

app = Flask("Emotion Detection")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detect():
    text_to_analyze = request.args.get('textToAnalyze')

    return emotion_detector(text_to_analyze)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000)