from EmotionDetection.emotion_detection import emotion_detector 
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    
     def test_emotion_detector(self):

        # Test case for test to analyze ='I am glad this happened'
        result = emotion_detector('I am glad this happened') 
        self.assertEqual(result['dominant_emotion'], 'joy') 
        
        # Test case for test to analyze = 'I am really mad about this'
        result = emotion_detector('I am really mad about this')  
        self.assertEqual(result['dominant_emotion'], 'anger') 
        
        # Test case for test to analyze = 'I feel disgusted just hearing about this'
        result = emotion_detector('I feel disgusted just hearing about this') 
        self.assertEqual(result['dominant_emotion'], 'disgust')

        # Test case for test to analyze ='I am so sad about this'
        result = emotion_detector('I am so sad about this') 
        self.assertEqual(result['dominant_emotion'], 'sadness')

        # Test case for test to analyze ='I am really afraid that this will happen'
        result = emotion_detector('I am really afraid that this will happen') 
        self.assertEqual(result['dominant_emotion'], 'fear')

unittest.main()
