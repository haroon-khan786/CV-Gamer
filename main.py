import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils


# Screen size
screen_width, screen_height = pyautogui.size()

# Initialize webcam capture
cap = cv2.VideoCapture(0)

# Check if webcam is opened correctly
if not cap.isOpened():
    print("Error: Unable to access the camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break

    # Flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and get hand landmarks
    results = hands.process(rgb_frame)

    # Create a copy of the frame to draw on (so original frame isn't affected)
    drawing_frame = frame.copy()

    # If hand landmarks are detected
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks on the frame
            # mp_drawing.draw_landmarks(drawing_frame, landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the position of the tip of the index finger (landmark 8)
            index_finger_tip = landmarks.landmark[8]
            finger_x = int(index_finger_tip.x * frame.shape[1])  # Normalize x to pixel
            finger_y = int(index_finger_tip.y * frame.shape[0])  # Normalize y to pixel

            # Convert to screen coordinates
            screen_x = np.interp(index_finger_tip.x, [0, 1], [0, screen_width])
            screen_y = np.interp(index_finger_tip.y, [0, 1], [0, screen_height])

             # Move mouse
            pyautogui.moveTo(screen_x, screen_y)


            # Draw a circle on the frame at the finger's position (red circle)
            cv2.circle(drawing_frame, (finger_x, finger_y), 10, (0, 0, 255), -1)  # Red circle

    # Display the frame with the drawing on top
    cv2.imshow("Hand Tracking - Drawing with Finger", drawing_frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close all windows
cap.release()
cv2.destroyAllWindows()
