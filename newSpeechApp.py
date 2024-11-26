# newSpeechApp.py
from dotenv import load_dotenv
from threading import Thread
import websocket
import pyaudio
import streamlit as st
from openai import OpenAI
import json
import os

# Load environment variables
load_dotenv()
AUTH_KEY = os.getenv("AUTH_KEY")
OPEN_API_KEY = os.getenv("OPEN_API_KEY")

# Set OpenAI API key


client = OpenAI()

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
SAMPLE_RATE = 16000
p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=SAMPLE_RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

# Disable WebSocket trace
websocket.enableTrace(False)
# Set the Authorization header
auth_header = {"Authorization": AUTH_KEY}

transcript_file = "transcripts.txt"

def summarize_text(file_path):
    """
    Summarizes the content of the provided text file using OpenAI.
    """
    with open(file_path, "r") as file:
        content = file.read()
    if not content.strip():
        st.warning("No content available to summarize.")
        return

    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Summarize the following Scrum meeting notes:\n\n{content}"
                }
            ]
        )

        summary = completion.choices[0].message.content
        st.success("Summary:")
        st.write(summary)
    except Exception as e:
        st.error(f"Error summarizing: {e}")



def on_message(ws, message):
    """
    is being called on every message
    """
    transcript = json.loads(message)
    text = transcript['text']

    if transcript["message_type"] == "PartialTranscript":
        print(f"Partial transcript received: {text}")
    elif transcript['message_type'] == 'FinalTranscript':
        print(f"Final transcript received: {text}")
        st.write(text)
        with open(transcript_file, "a") as file:
            file.write(text + "\n")  # Save the transcript



def on_open(ws):
    """
    is being called on session begin
    """
    def send_data():
        while True:
            # read from the microphone
            data = stream.read(FRAMES_PER_BUFFER)

            # binary data can be sent directly
            ws.send(data, opcode=websocket.ABNF.OPCODE_BINARY)


    # Start a thread where we send data to avoid blocking the 'read' thread
    Thread(target=send_data).start()



def on_error(ws, error):
    """
    is being called in case of errors
    """
    print(error)


def on_close(ws):
    """
    is being called on session end
    """
    print("WebSocket closed")

ws = websocket.WebSocketApp(
    f"wss://api.assemblyai.com/v2/realtime/ws?sample_rate={SAMPLE_RATE}",
    header=auth_header,
    on_message=on_message,
    on_open=on_open,
    on_error=on_error,
    on_close=on_close

)

st.header("Real-time Speech Recognition")

if st.button("Summarize Meeting"):
   summarize_text(transcript_file)

if st.button("Stop listening"):
  # Close the WebSocket connection
  ws.close()
  st.write("Stopped listening")

if st.button("Start listening"):
   # Clear the transcript file
   with open(transcript_file, "w") as file:
        file.write("")
   # Start the WebSocket connection
   ws.run_forever()


