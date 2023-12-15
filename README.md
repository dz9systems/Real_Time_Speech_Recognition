# Real-time Audio Transcription using AssemblyAI WebSocket
https://github.com/dz9systems/Real_Time_Speech_Recognition/assets/77218260/86db39ca-05fb-4689-8a52-c169201ed926

## Project Overview
This project focuses on implementing a real-time audio transcription system using the AssemblyAI WebSocket API. The application captures audio data from a microphone, encodes it in base64, and sends it to the AssemblyAI endpoint for transcription in real-time. The transcription results are then processed and printed to the console.

## Key Features
- Real-time Audio Streaming: The application captures audio in real-time using PyAudio and sends it to the AssemblyAI WebSocket for transcription.

- WebSocket Communication: Utilizes the websockets library to establish a WebSocket connection with the AssemblyAI API.

- Authentication: The application uses an authentication key from an external configuration file (configure.py) to authenticate with the AssemblyAI API.

- Error Handling: Implements error handling for connection issues, ensuring the application gracefully handles exceptions such as ConnectionClosedError.

- Transcription Display: Displays the transcribed text on the console in real-time as it becomes available from the AssemblyAI API.

## Dependencies
- websockets: Used for WebSocket communication with the AssemblyAI API.
- pyaudio: Enables audio capture and streaming functionalities.
- base64: Used to encode the audio data before sending it to AssemblyAI.
- json: Handles the serialization and deserialization of JSON data for communication with the AssemblyAI API.
- configure: External configuration file containing the authentication key (auth_key).

## Getting Started

### Prerequisites
- Python 3.x
- Pip (Python package installer)
- Virtual environment (recommended)

### Installation

- **Clone the repository**
   ```bash
        git clone https://github.com/dz9systems/Real_Time_Speech_Recognition.git


### Start Virtual Environment
- ***Execute the following script:***
  ```bash
        python3 -m venv venv
        source venv/bin/activate

### Install Dependencies
- ***Execute the following script:***
  ```bash
        pip install -r requirements.txt

###  Running the Application

- ***Execute the code in speech_recognition.py file:***
  ```bash
        python3 speech_recognition.py
        
- ***Execute the code in rtsr_in_streamlit.pyfile:***
  ```bash
        streamlit run rtsr_in_streamlit.py


