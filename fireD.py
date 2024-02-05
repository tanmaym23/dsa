import cv2
import numpy as np
from tensorflow import keras
from google.cloud import texttospeech

# Set up Google Text-to-Speech client
client = texttospeech.TextToSpeechClient()

# Load ANN model
model = keras.models.load_model('fire_detection_model.h5')

# Define ROI coordinates
x1, y1, x2, y2 = 100, 100, 300, 300

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Extract ROI from frame
    roi = frame[y1:y2, x1:x2]
    
    # Resize ROI to fit ANN input shape
    roi = cv2.resize(roi, (64, 64))
    
    # Normalize pixel values to [0, 1]
    roi = roi.astype('float32') / 255.0
    
    # Reshape ROI to match ANN input shape
    roi = np.reshape(roi, (1, 64, 64, 3))
    
    # Make prediction using ANN model
    prediction = model.predict(roi)
    
    # Threshold prediction probability
    threshold = 0.5
    
    # Check if prediction probability exceeds threshold
    if prediction[0][0] > threshold:
        # Display warning message on frame
        cv2.putText(frame, 'FIRE DETECTED', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
        
        # Convert text to speech using Google Text-to-Speech API
        synthesis_input = texttospeech.SynthesisInput(text='Fire detected')
        voice = texttospeech.VoiceSelectionParams(
            language_code='en-US', 
            ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)
        audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
        response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
        
        # Write speech output to file
        with open('output.mp3', 'wb') as out:
            out.write(response.audio_content)
        
        # Play speech output
        os.system('mpg321 output.mp3')
        
    # Display ROI on frame
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    # Display frame
    cv2.imshow('Fire Detection System', frame)
    
    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and destroy windows
cap.release()
cv2.destroyAllWindows()
