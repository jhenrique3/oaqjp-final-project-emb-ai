import json,requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }
    try:
        response = requests.post(url,json=obj,headers=headers)
        response.raise_for_status()
    except:
        return "An error occurred"

    emotion = {
        'anger': response.json()['emotionPredictions'][0]['emotion']['anger'],
        'disgust': response.json()['emotionPredictions'][0]['emotion']['disgust'],
        'fear': response.json()['emotionPredictions'][0]['emotion']['fear'],
        'joy': response.json()['emotionPredictions'][0]['emotion']['joy'],
        'sadness': response.json()['emotionPredictions'][0]['emotion']['sadness']
    }
    emotion['dominant_emotion'] = max(emotion, key=emotion.get)

    return emotion
