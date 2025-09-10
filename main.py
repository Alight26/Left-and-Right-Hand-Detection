import cv2 as cv
import mediapipe as mp 

# initializes the hand 
mp_hands = mp.solutions.hands 
# initializes drawing the points on the hand
mp_drawing = mp.solutions.drawing_utils 

hands = mp_hands.Hands(min_detections_confidence = 0.5,
                       min_tracking_confidence = 0.5,
                       )

cap = cv.VideoCapture(1)


cap.release()
cv.destroyAllWindows()