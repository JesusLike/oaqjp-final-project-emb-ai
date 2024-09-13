"""
Emotion detection using Watson NLP Library
"""

from functools import reduce
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Calls the Emotion Predict function via Watson web API
    """
    print("!!! " + text_to_analyze + " !!!")

    url = ('https://sn-watson-emotion.labs.skills.network/'
           'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    json_body = {
        "raw_document": {
            "text": text_to_analyze 
        }
    }
    response = requests.post(url, headers=headers, json=json_body, timeout=5000)

    if response.status_code == 400:
        # Redundant data for error handling
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    if response.status_code != 200:
        return None

    return formatted_response(response.text)

def formatted_response(response_text):
    """
    Format retrieved emotion predictions
    """
    parsed_json = json.loads(response_text)
    emotions = parsed_json["emotionPredictions"][0]["emotion"]
    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness']
    }
    result['dominant_emotion'] = reduce(
        lambda a, b: a if emotions[a] > emotions[b] else b,
        emotions.keys()
    )
    return result
