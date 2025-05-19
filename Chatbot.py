from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Frontend-inu allow panradhuku

responses = {
    "hello": "Hi there! I'm here to help you with anything you need!",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "track my order": "You can track your order via our integrated WhatsApp API or webhooks.",
    "return my order": "To return your order, connect with our Dialogflow-based return bot.",
    "cancel my order": "Please use our Rasa-based assistant to cancel if it's not yet shipped.",
    "talk to human": "Sure! Routing your request through Twilio. Please wait...",
    "where is my refund?": "Refunds are processed within 5-7 business days. Check your bank notifications.",
    "do you support voice input?": "Voice support is in beta using Web Speech API and AssemblyAI.",
    "what nlp models do you use?": "I leverage smart language models to help you understand and solve problems efficiently.",
    "how do i update my address?": "You can update your address from your profile settings or by contacting support.",
    "can i change delivery date?": "Yes, go to your order details and select 'Reschedule Delivery'.",
    "what is your return policy?": "Items can be returned within 30 days. Refer to our return policy page.",
    "is smartbot secure?": "Absolutely! I follow industry standards and encrypt all sensitive data.",
    "can you translate languages?": "Yes! I support real-time translation in over 20 languages.",
    "bye": "Thank you! Have a great day. Feel free to chat with me anytime!"
}

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "").lower().strip()
    reply = responses.get(user_msg, "Sorry, I didn't get that. Try asking differently.")
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
