<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>SmartBot Assistant</title>
  <link href="https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@300;500;700&family=Dancing+Script&display=swap" rel="stylesheet" />
  <style>
    body, html {
      margin: 0; padding: 0; height: 100%;
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(135deg, #833ab4, #fd1d1d, #fcb045);
      color: #f0f0f0;
    }
    .front-page {
      height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 20px;
    }
    .front-page img {
      width: 400px;
      margin-bottom: 25px;
    }
    .front-page h1 {
      font-family: 'Pacifico', cursive;
      font-size: 3em;
      margin-bottom: 10px;
      color: #ffffff;
      text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
    }
    .front-page p {
      font-family: 'Dancing Script', cursive;
      font-size: 1.8em;
      margin-bottom: 30px;
      color: #f0f0f0;
    }
    .front-page button {
      padding: 15px 40px;
      font-size: 24px;
      font-family: 'Pacifico', cursive;
      background-color: #9b59b6;
      border: none;
      border-radius: 30px;
      color: white;
      cursor: pointer;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .front-page button:hover {
      transform: scale(1.05);
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
    }
    .chat-container {
      display: none;
      max-width: 600px;
      margin: 30px auto;
      background: rgba(255, 255, 255, 0.1);
      backdrop-filter: blur(15px);
      color: white;
      padding: 20px;
      border-radius: 15px;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.25);
    }
    #chat {
      height: 300px;
      overflow-y: auto;
      border: 1px solid #ccc;
      padding: 10px;
      margin-bottom: 20px;
      background-color: rgba(0, 0, 0, 0.3);
      border-radius: 10px;
      backdrop-filter: blur(10px);
      color: #f0f0f0;
    }
    .bot {
      color: #ffffff;
    }
    .user {
      font-weight: bold;
      color: #87ceeb;
    }
    .buttons {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      justify-content: center;
    }
    button.ask-btn {
      padding: 10px 15px;
      background-color: #9b59b6;
      color: white;
      border: none;
      border-radius: 30px;
      font-weight: 500;
      cursor: pointer;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    button.ask-btn:hover {
      transform: scale(1.05);
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
  </style>
</head>
<body>

  <div class="front-page" id="welcome">
    <img src="https://cdnl.iconscout.com/lottie/premium/thumb/chatbot-virtual-assistant-on-ai-messaging-and-conversation-apps-animation-download-in-lottie-json-gif-static-svg-file-formats--bot-robotics-automation-pack-science-technology-animations-3378318.gif" alt="SmartBot Animation" />
    <h1>I'm SmartBot</h1>
    <p>your cute assistant. Ready to help you out!</p>
    <button onclick="startChat()">Let's Chat!</button>
  </div>

  <div class="chat-container" id="chatContainer">
    <h2 id="botHeading" style="text-align:center; color:#f0f0f0;">&nbsp;</h2>
    <div id="chat"></div>
    <div class="buttons">
      <button class="ask-btn" onclick="ask('Hello')">Hello</button>
      <button class="ask-btn" onclick="ask('Tell me a joke')">Tell me a joke</button>
      <button class="ask-btn" onclick="ask('Track my order')">Track my order</button>
      <button class="ask-btn" onclick="ask('Return my order')">Return order</button>
      <button class="ask-btn" onclick="ask('Cancel my order')">Cancel order</button>
      <button class="ask-btn" onclick="ask('Talk to human')">Talk to human</button>
      <button class="ask-btn" onclick="ask('Where is my refund?')">Where is my refund?</button>
      <button class="ask-btn" onclick="ask('Do you support voice input?')">Voice input?</button>
      <button class="ask-btn" onclick="ask('What NLP models do you use?')">What NLP models?</button>
      <button class="ask-btn" onclick="ask('How do I update my address?')">Update address</button>
      <button class="ask-btn" onclick="ask('Can I change delivery date?')">Change delivery date</button>
      <button class="ask-btn" onclick="ask('What is your return policy?')">Return policy</button>
      <button class="ask-btn" onclick="ask('Is SmartBot secure?')">SmartBot secure?</button>
      <button class="ask-btn" onclick="ask('Can you translate languages?')">Translate languages</button>
      <button class="ask-btn" onclick="ask('Bye')">Bye</button>
    </div>
  </div>

  <script>
    function startChat() {
      document.getElementById("welcome").style.display = "none";
      document.getElementById("chatContainer").style.display = "block";
      typeWriter("SmartBot Assistant", "botHeading", 100, () => {
        typeChatMessage("Hello! Ask me anything about orders, returns, or more.");
      });
    }

    function typeWriter(text, elementId, delay = 100, callback = null) {
      let i = 0;
      const element = document.getElementById(elementId);
      element.innerHTML = '';

      function type() {
        if (i < text.length) {
          element.innerHTML += text.charAt(i);
          i++;
          setTimeout(type, delay);
        } else if (callback) {
          callback();
        }
      }

      type();
    }

    function typeChatMessage(message, delay = 40) {
      const chat = document.getElementById("chat");
      const p = document.createElement("p");
      p.classList.add("bot");
      p.innerHTML = '<strong>SmartBot:</strong> ';
      chat.appendChild(p);

      let i = 0;
      function type() {
        if (i < message.length) {
          p.innerHTML += message.charAt(i);
          i++;
          setTimeout(type, delay);
        }
      }

      type();
    }

    const responses = {
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
    };

    function ask(question) {
      const chat = document.getElementById("chat");
      const userMsg = document.createElement("p");
      userMsg.classList.add("user");
      userMsg.innerHTML = `<strong>You:</strong> ${question}`;
      chat.appendChild(userMsg);

      const lower = question.toLowerCase().trim();
      const answer = responses[lower] || "Sorry, I didn't get that. Try asking differently.";
      typeChatMessage(answer);
      chat.scrollTop = chat.scrollHeight;
    }
  </script>

</body>
</html>
