"""import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
#fingerCoordinates = [(8, 6), (12, 10), (16, 14), (20, 18)]
littlefin=(20,18)
ringfin=(16,14)
middlefin=(12,10)
indexfin=(8,6)
thumbCoordinate = (4,2)



while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    multiLandMarks = results.multi_hand_landmarks
    sentance=""
    if multiLandMarks:
        handPoints = []
        for handLms in multiLandMarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            for idx, lm in enumerate(handLms.landmark):
                print(idx,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                handPoints.append((cx, cy))

        for point in handPoints:
            cv2.circle(img, point, 10, (0, 0, 255), cv2.FILLED)
        thumb_tip = landmarks[4]
        index_tip = landmarks[8]
        middle_tip = landmarks[12]
        ring_tip = landmarks[16]
        pinky_tip = landmarks[20]
        thumb_ip = landmarks[3]
        index_ip = landmarks[7]
        middle_ip = landmarks[11]
        ring_ip = landmarks[15]
        pinky_ip = landmarks[19]
        thumb_mcp = landmarks[2]  # MCP joint of the thumb
        index_mcp = landmarks[5]  # MCP joint of the index finger
        #if not handPoints[thumbCoordinate[0]][0] > handPoints[thumbCoordinate[1]][0]:
         #   cv2.putText(img, "A", (150,150), cv2.FONT_HERSHEY_PLAIN, 12, (255,0,0), 12)
        # Example logic for "A" (fist-like gesture)
        if (thumb_tip.x < thumb_ip.x and
            index_tip.y > index_ip.y and
            middle_tip.y > middle_ip.y and
            ring_tip.y > ring_ip.y and
            pinky_tip.y > pinky_ip.y):
            cv2.putText(img, "A", (150,150), cv2.FONT_HERSHEY_PLAIN, 12, (255,0,0), 12)
        #return "A"

    # Example logic for "B" (all fingers extended straight)
        if (index_tip.y < index_ip.y and
            middle_tip.y < middle_ip.y and
            ring_tip.y < ring_ip.y and
            pinky_tip.y < pinky_ip.y):
            cv2.putText(img, "B", (150,150), cv2.FONT_HERSHEY_PLAIN, 12, (255,0,0), 12)
        #return "B"

    # Example logic for "C" (forming a "C" with thumb and index)
        if (thumb_tip.x < index_tip.x and
            0 < (thumb_tip.y - index_tip.y) < 0.2 and
            middle_tip.y < landmarks[9].y and
            ring_tip.y < landmarks[13].y and
            pinky_tip.y < landmarks[17].y):
            cv2.putText(img, "C", (150,150), cv2.FONT_HERSHEY_PLAIN, 12, (255,0,0), 12)
        #return "C"

    # Example logic for "D" (index finger pointing up, others curled in)
        if (index_tip.y < index_mcp.y and
            middle_tip.y > middle_ip.y and
            ring_tip.y > ring_ip.y and
            pinky_tip.y > pinky_ip.y and
            thumb_tip.x > thumb_mcp.x):
            cv2.putText(img, "D", (150,150), cv2.FONT_HERSHEY_PLAIN, 12, (255,0,0), 12)
        #return "D"

    # Example logic for "E" (fingers curled in, thumb across palm)
        if (thumb_tip.x > thumb_mcp.x and
            index_tip.y > index_ip.y and
            middle_tip.y > middle_ip.y and
            ring_tip.y > ring_ip.y and
            pinky_tip.y > pinky_ip.y):
            cv2.putText(img, "E", (150,150), cv2.FONT_HERSHEY_PLAIN, 12, (255,0,0), 12)
        #return "E"

    # Example logic for "F" (thumb and index forming a circle, others straight)
        if (thumb_tip.x > index_tip.x and
            index_tip.y < index_ip.y and
            middle_tip.y < middle_ip.y and
            ring_tip.y < ring_ip.y and
            pinky_tip.y < pinky_ip.y):
            cv2.putText(img, "F", (150,150), cv2.FONT_HERSHEY_PLAIN, 12, (255,0,0), 12)
        #return "F"

    # Example logic for "G" (thumb and index parallel, others closed)
        if (thumb_tip.y > thumb_mcp.y and
            index_tip.y < index_mcp.y and
            middle_tip.y > middle_ip.y and
            ring_tip.y > ring_ip.y and
            pinky_tip.y > pinky_ip.y):
            cv2.putText(img, "G", (150,150), cv2.FONT_HERSHEY_PLAIN, 12, (255,0,0), 12)
        #return "G"

      
    
    cv2.imshow("Finger Counter", img)
    cv2.waitKey(1)"""
import cv2
import mediapipe as mp

# Initialize MediaPipe hands and drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Open the webcam
cap = cv2.VideoCapture(0)

# Define the hand gesture mappings based on the landmarks
def detect_gesture(landmarks):
    # Extract landmark positions
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    pinky_tip = landmarks[20]

    thumb_ip = landmarks[3]
    index_ip = landmarks[7]
    middle_ip = landmarks[11]
    ring_ip = landmarks[15]
    pinky_ip = landmarks[19]

    thumb_mcp = landmarks[2]
    index_mcp = landmarks[5]
    middle_mcp = landmarks[9]
    ring_mcp = landmarks[13]
    pinky_mcp = landmarks[17]

    sentance = ""

    # Logic for "A" (fist-like gesture)
    if (thumb_tip.x < thumb_ip.x and
        index_tip.y > index_ip.y and
        middle_tip.y > middle_ip.y and
        ring_tip.y > ring_ip.y and
        pinky_tip.y > pinky_ip.y):
        sentance += "A"
        return "A"

    # Logic for "B" (all fingers extended straight)
    if (index_tip.y < index_ip.y and
        middle_tip.y < middle_ip.y and
        ring_tip.y < ring_ip.y and
        pinky_tip.y < pinky_ip.y):
        sentance += "B"
        return "B"

    # Logic for "C" (forming a "C" with thumb and index)
    if (thumb_tip.x < index_tip.x and
        0 < (thumb_tip.y - index_tip.y) < 0.2 and
        middle_tip.y < middle_mcp.y and
        ring_tip.y < ring_mcp.y and
        pinky_tip.y < pinky_mcp.y):
        sentance += "C"
        return "C"

    # Logic for "D" (index finger pointing up, others curled in)
    if (index_tip.y < index_mcp.y and
        middle_tip.y > middle_ip.y and
        ring_tip.y > ring_ip.y and
        pinky_tip.y > pinky_ip.y and
        thumb_tip.x > thumb_mcp.x):
        sentance += "D"
        return "D"

    # Logic for "E" (fingers curled in, thumb across palm)
    if (thumb_tip.x > thumb_mcp.x and
        index_tip.y > index_ip.y and
        middle_tip.y > middle_ip.y and
        ring_tip.y > ring_ip.y and
        pinky_tip.y > pinky_ip.y):
        sentance += "E"
        return "E"

    # Logic for "F" (thumb and index forming a circle, others straight)
    if (thumb_tip.x > index_tip.x and
        index_tip.y < index_ip.y and
        middle_tip.y < middle_ip.y and
        ring_tip.y < ring_ip.y and
        pinky_tip.y < pinky_ip.y):
        sentance += "F"
        return "F"

    # Logic for "G" (thumb and index parallel, others closed)
    if (thumb_tip.y > thumb_mcp.y and
        index_tip.y < index_mcp.y and
        middle_tip.y > middle_ip.y and
        ring_tip.y > ring_ip.y and
        pinky_tip.y > pinky_ip.y):
        sentance += "G"
        return "G"

    # Logic for "H" (index and middle finger extended, others curled)
    if (index_tip.y < index_ip.y and
        middle_tip.y < middle_ip.y and
        ring_tip.y > ring_ip.y and
        pinky_tip.y > pinky_ip.y and
        thumb_tip.x < thumb_ip.x):
        sentance += "H"
        return "H"

    # Logic for "I" (pinky extended, others curled)
    if (pinky_tip.y < pinky_ip.y and
        index_tip.y > index_ip.y and
        middle_tip.y > middle_ip.y and
        ring_tip.y > ring_ip.y and
        thumb_tip.x < thumb_ip.x):
        sentance += "I"
        return "I"

    # Logic for "J" (pinky draws a "J" shape, others curled)
    if (pinky_tip.y < pinky_ip.y and
        index_tip.y > index_ip.y and
        middle_tip.y > middle_ip.y and
        ring_tip.y > ring_ip.y and
        thumb_tip.x < thumb_ip.x):
        sentance += "J"
        return "J"

    # Logic for "K" (thumb, index, and middle finger extended, others curled)
    if (thumb_tip.x > thumb_mcp.x and
        index_tip.y < index_ip.y and
        middle_tip.y < middle_ip.y and
        ring_tip.y > ring_ip.y and
        pinky_tip.y > pinky_ip.y):
        sentance += "K"
        return "K"

    # Logic for "L" (thumb and index extended, others curled)
    if (thumb_tip.x > thumb_ip.x and
        index_tip.y < index_ip.y and
        middle_tip.y > middle_ip.y and
        ring_tip.y > ring_ip.y and
        pinky_tip.y > pinky_ip.y):
        sentance += "L"
        return "L"

    # Logic for "M" (thumb tucked under index, middle, and ring fingers)
    if (thumb_tip.x > thumb_ip.x and
        index_tip.x > thumb_tip.x and
        middle_tip.x > thumb_tip.x and
        ring_tip.x > thumb_tip.x and
        pinky_tip.y > pinky_ip.y):
        sentance += "M"
        return "M"

    # Logic for "N" (thumb tucked under index and middle fingers)
    if (thumb_tip.x > thumb_ip.x and
        index_tip.x > thumb_tip.x and
        middle_tip.x > thumb_tip.x and
        ring_tip.x < thumb_tip.x and
        pinky_tip.y > pinky_ip.y):
        sentance += "N"
        return "N"

    # Logic for "O" (fingers form an "O" shape)
    if (thumb_tip.x < index_tip.x and
        index_tip.y < middle_tip.y and
        middle_tip.y < ring_tip.y and
        ring_tip.y < pinky_tip.y):
        sentance += "O"
        return "O"

    # Logic for "P" (similar to "K" but tilted down)
    if (thumb_tip.x > thumb_ip.x and
        index_tip.y < index_ip.y and
        middle_tip.y < middle_ip.y and
        ring_tip.y > ring_ip.y and
        pinky_tip.y > pinky_ip.y and
        thumb_tip.y > thumb_mcp.y):
        sentance += "P"
        return "P"

    # Logic for "Q" (thumb and index form a "Q" shape, others curled)
    if (thumb_tip.x < index_tip.x and
        index_tip.y < index_ip.y and
        middle_tip.y > middle_ip.y and
        ring_tip.y > ring_ip.y and
        pinky_tip.y > pinky_ip.y):
        sentance += "Q"
        return "Q"

    # Logic for "R" (index and middle fingers crossed, others curled)
    if (index_tip.x < middle_tip.x and
        middle_tip.y < middle_ip.y and
        ring_tip.y > ring_ip.y and
        pinky_tip.y > pinky_ip.y):
        sentance += "R"
        return "R"

    # Logic for "S" (fist with thumb across the fingers)
    if (thumb_tip.x > thumb_mcp.x and
        index_tip.y > index_ip.y and
        middle_tip.y > middle_ip.y and
        ring_tip.y > ring_ip.y and
        pinky_tip.y > pinky_ip.y):
        sentance += "S"
        return "S"

    # Logic for "T" (thumb tucked under index finger)
    if (thumb_tip.x < index_mcp.x and
        index_tip.y > thumb_tip.y and
        middle_tip.y > middle_ip.y and
        ring_tip.y > ring_ip.y and
        pinky_tip.y > pinky_ip.y):
        sentance += "T"
        return "T"

    # Logic for "U" (index and middle fingers extended together)
    if (index_tip.y < index_ip.y and
        middle_tip.y < middle_ip.y and
        ring_tip.y > ring_ip.y and
        pinky_tip.y > pinky_ip.y):
        sentance += "U"
        return "U"

    # Logic for "V" (index and middle fingers extended apart)
    if (index_tip.y < index_ip.y and
        middle_tip.y < middle_ip.y and
        ring_tip.y > ring_ip.y and
        pinky_tip.y > pinky_ip.y and
        (index_tip.x - middle_tip.x) > 0.1):
        sentance += "V"
        return "V"

    # Logic for "W" (index, middle, and ring fingers extended)
    if (index_tip.y < index_ip.y and
        middle_tip.y < middle_ip.y and
        ring_tip.y < ring_ip.y and
        pinky_tip.y > pinky_ip.y):
        sentance += "W"
        return "W"

    # Logic for "X" (index finger curled, others curled)
    if (index_tip.y > index_ip.y and
        middle_tip.y > middle_ip.y and
        ring_tip.y > ring_ip.y and
        pinky_tip.y > pinky_ip.y and
        thumb_tip.x < thumb_ip.x):
        sentance += "X"
        return "X"

    # Logic for "Y" (thumb and pinky extended, others curled)
    if (thumb_tip.x > thumb_mcp.x and
        pinky_tip.y < pinky_ip.y and
        index_tip.y > index_ip.y and
        middle_tip.y > middle_ip.y and
        ring_tip.y > ring_ip.y):
        sentance += "Y"
        return "Y"

    # Logic for "Z" (index finger traces a "Z" shape)
    if (index_tip.y < index_ip.y and
        middle_tip.y > middle_ip.y and
        ring_tip.y > ring_ip.y and
        pinky_tip.y > pinky_ip.y and
        thumb_tip.x < thumb_ip.x):
        sentance += "Z"
        return "Z"

    return None  # No gesture detected

    print(sentance)

   

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert the frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process the frame and detect hands
        result = hands.process(rgb_frame)
        
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                # Draw landmarks on the frame
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                # Get landmarks as a list of normalized coordinates
                landmarks = hand_landmarks.landmark
                
                # Detect the gesture based on landmarks
                detected_gesture = detect_gesture(landmarks)
                
                # Display the corresponding letter
                if detected_gesture:
                    cv2.putText(frame, detected_gesture, (50, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
                            
        # Show the frame
        cv2.imshow('Hand Gesture Recognition',frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

print(sentance)

cap.release()
cv2.destroyAllWindows()
