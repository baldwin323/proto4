```python
import sys
from PyQt5.QtWidgets import QApplication

# Importing UI pages
from ui.page1 import Page1
from ui.page2 import Page2
from ui.page3 import Page3
from ui.page4 import Page4
from ui.page5 import Page5

# Importing API integration, chatroom and backend modules
from api.api_integration import ApiIntegration
from chatroom.virtual_chatroom import VirtualChatroom
from chatroom.chatbot_training import ChatbotTraining
from backend.backend_integration import BackendIntegration

def main():
    app = QApplication(sys.argv)

    # Initialize API integration, chatroom and backend
    api_integration = ApiIntegration()
    virtual_chatroom = VirtualChatroom()
    chatbot_training = ChatbotTraining()
    backend_integration = BackendIntegration()

    # Initialize UI pages
    page1 = Page1(api_integration, virtual_chatroom, chatbot_training, backend_integration)
    page2 = Page2(api_integration, virtual_chatroom, chatbot_training, backend_integration)
    page3 = Page3(api_integration, virtual_chatroom, chatbot_training, backend_integration)
    page4 = Page4(api_integration, virtual_chatroom, chatbot_training, backend_integration)
    page5 = Page5(api_integration, virtual_chatroom, chatbot_training, backend_integration)

    # Show the first page
    page1.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
```