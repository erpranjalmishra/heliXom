import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import time
from tkinter import *
from PIL import Image, ImageTk
from gtts import gTTS
import pygame
import time

# Initialize the webcam and the hand detector
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

# Set constants for cropping and resizing
offset = 20
imgSize = 300
sen = ""  # Sentence string
labels = ['Hungry', 'Love', 'Namaste', 'Namaste', 'Yes']  # Update this with the full list

# Initialize Pygame mixer for playing audio
pygame.mixer.init()

# Word suggestions (based on the first letter, for simplicity)
word_suggestions = {
    'A': ['Apple', 'Ant', 'Axe'],
    'B': ['Ball', 'Boy', 'Bat'],
    'C': ['Cat', 'Cup', 'Car'],
    'D': ['Dog', 'Door', 'Duck'],
    'E': ['Elephant', 'Egg', 'Ear'],
    'F': ['Fish', 'Fan', 'Fox'],
    'G': ['Goat', 'Girl', 'Gum']
    # Add more suggestions for other letters
}

def text_to_speech_gtts(text, filename="output.mp3"):
    """
    Convert text to speech using gTTS and save it to a file.
    """
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    print(f"Audio saved as {filename}")
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def update_sentence(char):
    """
    Update the sentence based on recognized character and display it in the GUI.
    """
    global sen
    sen += char
    sentence_label.config(text="Sentence: " + sen)
    update_suggestions(char)

def clear_text():
    """
    Clear the sentence in the GUI.
    """
    global sen
    sen = ""
    sentence_label.config(text="Sentence: ")
    update_suggestions('')  # Clear suggestions

def speak_text():
    """
    Convert the current sentence to speech.
    """
    if sen:
        text_to_speech_gtts(sen)

def update_suggestions(char):
    """
    Update word suggestions based on the current character.
    """
    if char in word_suggestions:
        for i, word in enumerate(word_suggestions[char]):
            suggestion_buttons[i].config(text=word, state=NORMAL)
    else:
        for btn in suggestion_buttons:
            btn.config(text="", state=DISABLED)

def add_suggestion_word(word):
    """
    Add the suggested word to the sentence when clicked.
    """
    global sen
    sen += " " + word
    sentence_label.config(text="Sentence: " + sen)

def update_gui():
    """
    Update the GUI with the latest camera frame and hand gesture predictions.
    """
    global sen
    success, img = cap.read()
    imgOutput = img.copy()
    hands, img = detector.findHands(img)
    
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]
        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw=False)
        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw=False)

        char = labels[index]
        update_sentence(char)
        
        # Display the character detected on the frame
        cv2.rectangle(imgOutput, (x-offset, y-offset-50), (x + w+offset, y - offset), (255, 0, 255), cv2.FILLED)
        cv2.putText(imgOutput, char, (x, y - 26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
        cv2.rectangle(imgOutput, (x-offset, y-offset), (x + w+offset, y + h+offset), (255, 0, 255), 4)
        
    # Convert the OpenCV image (BGR) to a format suitable for Tkinter (RGB)
    imgRGB = cv2.cvtColor(imgOutput, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(imgRGB)
    img_tk = ImageTk.PhotoImage(image=img_pil)

    # Update the Tkinter label with the new frame
    video_label.imgtk = img_tk
    video_label.config(image=img_tk)

    # Call this function again after 10ms to keep updating the GUI
    root.after(10, update_gui)

# Initialize the GUI
root = Tk()
root.title("Sign Language to Text Conversion")
root.geometry("900x700")

# Add GUI components
title_label = Label(root, text="Sign Language To Text Conversion", font=("Helvetica", 16))
title_label.pack()

# Image display section (Video Frame)
image_frame = Frame(root)
image_frame.pack()

video_label = Label(image_frame)
video_label.pack()

# Sentence label
sentence_label = Label(root, text="Sentence: ", font=("Helvetica", 14))
sentence_label.pack()

# Suggestion buttons
suggestion_frame = Frame(root)
suggestion_frame.pack()

suggestion_buttons = []
for i in range(3):  # Display up to 3 suggestions
    btn = Button(suggestion_frame, text="", font=("Helvetica", 12), width=20, state=DISABLED, command=lambda i=i: add_suggestion_word(suggestion_buttons[i].cget("text")))
    btn.pack(side=LEFT)
    suggestion_buttons.append(btn)

# Control buttons
control_frame = Frame(root)
control_frame.pack()

clear_button = Button(control_frame, text="Clear Text", command=clear_text)
clear_button.pack(side=LEFT)

speak_button = Button(control_frame, text="Speak Text", command=speak_text)
speak_button.pack(side=LEFT)

# Start updating the GUI
update_gui()

# Start the Tkinter main loop
root.mainloop()
