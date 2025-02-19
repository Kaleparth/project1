import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 210)

detector = HandDetector(detectionCon= 0.7, maxHands= 1)
keyboard = Controller()

while True:
    _, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        finger = detector.fingersUp(hands[0])
        print(finger)
        if finger == [0, 1, 0, 0, 0]:
            keyboard.press(Key.left)
            keyboard.press(Key.up)
            keyboard.release(Key.down)
            keyboard.release(Key.right)

        if finger == [0, 0, 0, 0, 1]:
            keyboard.press(Key.right)
            keyboard.press(Key.up)
            keyboard.release(Key.left)
            keyboard.release(Key.down)


        if finger == [0,0,0,0,0]:
            keyboard.press(Key.up)
            keyboard.release(Key.down)
            keyboard.release(Key.left)
            keyboard.release(Key.right)

        elif finger == [1,1,1,1,1]:
            keyboard.press(Key.down)
            keyboard.release(Key.up)
            keyboard.release(Key.left)
            keyboard.release(Key.right)
         
    else:
        keyboard.release(Key.left)
        keyboard.release(Key.up)
        keyboard.release(Key.down)
        keyboard.release(Key.right)
        
    if cv2.waitKey(1) == ord ("q"):
        break