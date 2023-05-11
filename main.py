import cv2
import numpy as np

import data

# Generate a marker
# name = "dog"
# marker = data.genMarker(name, data.convIDtoInt(name), 100)

cap = cv2.VideoCapture(0)

while True:
    # Capture the next frame.
    ret, frame = cap.read()

    # Overlay the image file over the arUco marker.
    frame = data.overlay_2D(frame, 147, "dogInSpace3.jpg")

    # Display the frame.
    cv2.imshow("Frame", frame)

    # If the user presses the `q` key, stop the loop.
    if cv2.waitKey(1) == ord("q"):
        break

# Close all open windows.
cv2.destroyAllWindows()