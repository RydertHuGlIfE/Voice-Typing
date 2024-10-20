# Voice-Typing
This is an old speech recognition project that I modified so that it could Type as well 


How it works 
Well it uses three main modules 

pyttsx3                 |
speech_recognition      |   REQUIRED
pyautogui               |

time and sys  [optional]


Speech Recognizer and Typing Bot
This Python script integrates speech recognition and text-to-speech functionalities to create a simple voice-activated typing bot. The script uses the pyautogui library to type out recognized speech and pyttsx3 for text-to-speech feedback.

Features
Speech Recognition: Listens for user speech and converts it into text using Google's speech recognition API.

Typing Automation: Types out the recognized speech using the pyautogui library.

Text-to-Speech: Provides audio feedback indicating the bot is listening and ready to type.

How It Works
Initialization:

Imports necessary libraries: pyautogui, speech_recognition, pyttsx3, sleep from time, and sys.

Initializes the text-to-speech engine with a specified voice.

Main Loop:

Continuously listens for user speech using the sr.Recognizer() object.

Provides audio feedback indicating it is listening and ready to type.

Adjusts for ambient noise and listens through the microphone.

Recognizes the speech and converts it to text using Google's API.

Types the recognized text using pyautogui.write().

Exits the loop if a termination condition is met.



Example Usage
Listening: "Listening and Ready to type"

Recognizing: Converts speech to text.

Typing: Automatically types the recognized text.

This script is useful for hands-free typing and simple voice-activated commands. Enjoy enhancing your productivity with voice commands!

Let me know if there's anything else you want to add or modify. 🎤👨‍💻
