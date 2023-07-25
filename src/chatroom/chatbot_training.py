```python
import os
from src.api import api_integration
from src.backend import backend_integration
from src.chatroom import chatroom_utils, chatbot_config

class ChatbotTraining:
    def __init__(self):
        self.config = chatbot_config.load_config()
        self.api = api_integration.ApiIntegration()
        self.backend = backend_integration.BackendIntegration()

    def load_training_data(self):
        training_data_path = os.path.join(self.config['data_dir'], 'training_data.json')
        with open(training_data_path, 'r') as file:
            training_data = json.load(file)
        return training_data

    def train_chatbot(self):
        training_data = self.load_training_data()
        self.api.post(self.config['training_url'], data=training_data)
        self.backend.save_model(self.config['model_path'])

    def run(self):
        self.train_chatbot()

if __name__ == "__main__":
    chatbot_training = ChatbotTraining()
    chatbot_training.run()
```