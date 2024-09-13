import cv2
import HandTrackingModule as htm  # Ensure HandTrackingModule.py is correctly imported

# Initialize video capture
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

print("Camera opened successfully.")

# Initialize hand detector
try:
    detector = htm.handDetector()
    print("Hand detector initialized successfully.")
except AttributeError as e:
    print("Error initializing hand detector:", e)
    exit()

# Capture a single frame to test
success, img = cap.read()

if not success:
    print("Failed to capture image.")
    cap.release()
    exit()

print("Captured image successfully.")

# Test findHands function
try:
    img = detector.findHands(img)  # Process the image to detect hands
    print("findHands executed successfully.")
except Exception as e:
    print("Error during findHands execution:", e)

# Test findPosition function
try:
    lmList = detector.findPosition(img)
    print("findPosition executed successfully.")
    if lmList:
        print("Landmarks detected:", lmList)
    else:
        print("No landmarks detected.")
except Exception as e:
    print("Error during findPosition execution:", e)

# Display the image to check if imshow works
try:
    cv2.imshow("Hand Tracking Test", img)
    print("Image window updated. Press 'q' to exit.")
    cv2.waitKey(0)  # Wait for a key press indefinitely
except Exception as e:
    print("Error displaying the image:", e)

# Release resources
cap.release()
cv2.destroyAllWindows()
print("Video capture released and all windows closed.")
