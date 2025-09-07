Voice-to-Text Converter

A simple desktop application that converts spoken words from your microphone to text in real time. Built using Python, Tkinter for the GUI, and the SpeechRecognition library with Google's speech-to-text API.
Features

    User-friendly interface with Start and Stop recording buttons

    Continuously listens to your microphone input and transcribes speech to text

    Displays recognized text live in a scrollable text area

    Uses Google’s free speech recognition service via the speech_recognition Python library

    Runs locally, simple setup on Ubuntu and other platforms with Python support

Requirements

    Python 3.x

    Tkinter (usually pre-installed with Python)

    SpeechRecognition

    PyAudio (for microphone access)

Installation

    Clone the repository:

bash
git clone https://github.com/yourusername/voice-to-text-converter.git

Change to the project directory:

bash
cd voice-to-text-converter

(Optional) Create and activate a virtual environment:

bash
python3 -m venv venv
source venv/bin/activate

Install required dependencies:

bash
pip install -r requirements.txt

If requirements.txt is not present, install packages manually:

bash
pip install SpeechRecognition pyaudio

Note: On Ubuntu, you may need to install system dependencies before PyAudio:

bash
sudo apt-get install portaudio19-dev python3-pyaudio

Run the application:

    bash
    python3 voice_to_text.py

Usage

    Click Start Rec button to begin voice recording.

    Speak into your microphone.

    Click Stop Rec to end recording and stop transcription.

    The transcribed text will appear in the text area for review, editing, or saving.

Troubleshooting

    If PyAudio installation fails, ensure you have the required development headers installed (portaudio19-dev on Ubuntu).

    Make sure your microphone is connected and accessible.

    Internet connection is required for Google's speech recognition API to work.

Contributing

Contributions, bug reports, and feature requests are welcome! Feel free to submit issues or pull requests.
License

This project is licensed under the MIT License. See the LICENSE file for details.

Author

Neeraj
neerajpm95@gmail.com
