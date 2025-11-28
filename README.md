# 🏨 Pride Of Bengal Hotel Booking Chatbot

A fully functional AI-powered chatbot for automated hotel room bookings at Pride Of Bengal Hotel.

## 🌟 Features
- Complete natural language booking flow
- Date selection and guest management
- Breakfast preferences
- Multiple payment options
- Professional web interface with Flask
- Real-time booking confirmation

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation & Setup
```bash
# 1. Clone the repository
git clone https://github.com/Arijeet9876/Hotel-Chatbot.git
cd Hotel-Chatbot

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate  
# On Windows: venv\Scripts\activate
# On Mac: source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Train the AI model
rasa train

# 5. Run the complete system
# Terminal 1: Action server
rasa run actions

# Terminal 2: Rasa server  
rasa run --cors "*" --port 5005

# Terminal 3: Web interface
python app.py

# 6.run the chatbot  
http://127.0.0.1:5000

# 7. Repository
https://github.com/Arijeet9876/Hotel-Chatbot
