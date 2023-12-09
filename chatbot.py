import time
import openai
import elevenlabs


start_time = time.time()

openai.api_key = "API_KEY"
content = input("How can I help you?\n")

completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": content}],
)
chat_response = completion.choices[0].message.content

# elevenlabs text to speech
elevenlabs.set_api_key("API_KEY")

# Convert the response to audio and play it
audio = elevenlabs.generate(text=chat_response, voice="Bella")

print("\nAI:", chat_response, end="\r\n")
print("--- %s seconds ---" % (time.time() - start_time))

elevenlabs.play(audio)
