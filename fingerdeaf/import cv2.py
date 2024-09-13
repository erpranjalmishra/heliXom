import cv2
import HandTrackingModule as htm  # Ensure this module is correctly placed in the same directory

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

while True:
    # Capture frame-by-frame
    success, img = cap.read()
    
    if not success:
        print("Failed to capture image.")
        break

    # Process the image to detect hands
    try:
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
    except Exception as e:
        print("Error during hand detection:", e)
        break

    # Check and print detected landmarks if any
    if len(lmList) != 0:
        print("Landmarks detected:", lmList)
        if len(lmList) > 4:
            print("Thumb tip position:", lmList[4])  # Example: Print the position of the thumb tip.
    else:
        print("No landmarks detected")

    # Display the image
    try:
        cv2.imshow("Hand Tracking", img)
        print("Image window updated.")  # Debugging statement to ensure imshow is called
    except Exception as e:
        print("Error displaying the image:", e)
        break

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting...")
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
print("Video capture released and all windows closed.")
