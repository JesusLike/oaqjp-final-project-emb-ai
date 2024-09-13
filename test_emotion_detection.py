import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector_joy(self):
        prediction = emotion_detector("I am glad this happened")
        self.assertEqual(prediction["dominant_emotion"], "joy")

    def test_emotion_detector_anger(self):
        prediction = emotion_detector("I am really mad about this")
        self.assertEqual(prediction["dominant_emotion"], "anger")

    def test_emotion_detector_disgust(self):
        prediction = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(prediction["dominant_emotion"], "disgust")

    def test_emotion_detector_sadness(self):
        prediction = emotion_detector("I am so sad about this")
        self.assertEqual(prediction["dominant_emotion"], "sadness")

    def test_emotion_detector_fear(self):
        prediction = emotion_detector("I am really afraid this will happen")
        self.assertEqual(prediction["dominant_emotion"], "fear")