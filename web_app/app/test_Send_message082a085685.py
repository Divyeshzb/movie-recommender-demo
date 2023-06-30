import sys
import unittest
import atexit
from unittest.mock import Mock, patch
from flask import Flask  # Correct import statement
from kafka import KafkaProducer
from kafka.errors import KafkaError

app = Flask(__name__)  # Define app

def send_message(message):
    try:
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        producer.send(app.config['KAFKA_TOPIC'], message.encode('utf-8'))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def create_topic():
    pass

@atexit.register
def cleanup():
    pass

class TestSendMessage(unittest.TestCase):
    def setUp(self):
        self.producer = KafkaProducer(bootstrap_servers='localhost:9092')
        self.message = "Test message"

    @patch.object(KafkaProducer, 'send')
    def test_send_message_success(self, mock_send):
        mock_send.return_value = True
        result = send_message(self.message)
        self.assertTrue(result)

    @patch.object(KafkaProducer, 'send')
    def test_send_message_failure(self, mock_send):
        mock_send.side_effect = KafkaError("Error sending message")
        with self.assertRaises(KafkaError):
            send_message(self.message)

if __name__ == '__main__':
    unittest.main()
