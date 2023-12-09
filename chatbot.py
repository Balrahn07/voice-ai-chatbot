import os
import time
import openai
import elevenlabs


timestamp = time.strftime("%Y_%m_%d-%H_%M_%S", time.gmtime())
filename = "ai_chatbot_conversation" + timestamp + ".txt"

# openai chatgpt
openai.api_key = "OPENAI_API_KEY"
# elevenlabs text to speech
elevenlabs.set_api_key("ELEVENLABS_API_KEY")

conversation = []

while True:
    
    content = input("Message chatbot: \n")
    start_time = time.time()
    if (content=="quit"):
        break
    
    conversation.append({"role": "user", "content":content})

    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation,
    )

    chat_response = completion.choices[0].message.content
    conversation.append({"role": "assistant", "content": chat_response})
    
    # Convert the response to audio and play it
    audio = elevenlabs.generate(text=chat_response, voice="Bella")

    print("\nChatbot:", chat_response, end="\r\n")
    print("--- %s seconds ---" % (time.time() - start_time))

    with open(filename, 'a') as f:
        f.write("User: " + content + "\n")
        f.write("Chatbot: " + chat_response + "\n")

    elevenlabs.play(audio)

print("Chat session is terminated.")