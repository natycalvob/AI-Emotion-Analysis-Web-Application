from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detection()
        function. The output returned shows the emotions and their 
        confidence score for the provided text, as well as the 
        dominant emotion. 
    '''
    text_to_analyze = request.args["textToAnalyze"]
    response = emotion_detector(text_to_analyze)

    # Format the emotion scores
    emotion_scores_str = ', '.join([
        f"'{emotion}': {score}" 
        for emotion, score in response.items() 
        if emotion != 'dominant_emotion'])
    
    # Get the dominant emotion from the response
    dominant_emotion = response['dominant_emotion']
    
    # Print the formatted response
    return (f"For the given statement, the system response is {emotion_scores_str}. "
            f"The dominant emotion is <b>{dominant_emotion}</b>.")

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
