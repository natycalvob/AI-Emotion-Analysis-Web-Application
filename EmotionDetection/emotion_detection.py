import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)
    
    # Response text into dict
    formatted_response = json.loads(response.text)
    
    # Extract the set of emotions and their scores
    emotion_scores = formatted_response['emotionPredictions'][0]['emotion']

    # Dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Define output_dict
    result_dict = {
        'anger': emotion_scores.get('anger', 0),
        'disgust': emotion_scores.get('disgust', 0),
        'fear': emotion_scores.get('fear', 0),
        'joy': emotion_scores.get('joy', 0),
        'sadness': emotion_scores.get('sadness', 0),
        'dominant_emotion': dominant_emotion
    }

    return result_dict

