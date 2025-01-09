import cv2

# Load the Haar Cascade for full-body detection
cascade_path = "haarcascade_fullbody.xml"  # Ensure this file is in the same folder
body_cascade = cv2.CascadeClassifier(cascade_path)

# Initialize the webcam
cap = cv2.VideoCapture(0)  # 0 is the default webcam

while True:
    # Capture video frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale (Haar Cascades require grayscale)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect full bodies in the frame
    bodies = body_cascade.detectMultiScale(
        gray, 
        scaleFactor=1.1, 
        minNeighbors=5, 
        minSize=(50, 50)
    )

    # Draw rectangles around detected objects
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow("Webcam Feed - Human Detection", frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

