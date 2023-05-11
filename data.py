import cv2
import numpy as np


def genMarker(name, id, size):
    """Generates an ArUco marker with the given ID, size, and color.

  Args:
    id: The ID of the marker.
    size: The size of the marker in pixels.
    color: The color of the marker.

  Returns:
    The generated marker image.
  """

    # Create the ArUco dictionary.
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)

    # Check if the ID has already been used.
    # if id in used_ids:
    #  return "ERROR: This ID has already been used!"

    # Generate the marker.
    marker = cv2.aruco.generateImageMarker(dictionary, id, size)

    # Save the marker to an image file.
    cv2.imwrite(f"marker_{id}_{name}.png", marker)

    # Add the ID to the list of used IDs.
    # used_ids.append(id)

    return marker


def convIDtoInt(id):
    """Converts an ArUco marker ID from a string to an integer.

  Args:
    id: The ID of the marker as a string.

  Returns:
    The ID of the marker as an integer.
  """

    # Convert the ID to an integer.
    try:
        id = int(id)
    except:
        # Convert the string to their ascii values.
        id = [ord(c) for c in id]
        # Convert the ascii values to a single integer.
        id = int("".join(str(c) for c in id))
        # Ensure that the number is not over 250, and if it is, reduce it until it is not.
        while id > 250:
            id = id // 2

    return id


def overlay_2D(image, marker_id, image_file):
    """Overlays an image file over an arUco marker in a video frame.

  Args:
    image: The video frame.
    marker_id: The id of the arUco marker.
    image_file: The path to the image file to overlay.

  Returns:
    The video frame with the image overlayed.
  """

    # Load the arUco dictionary.
    dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)

    parameters = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(dictionary, parameters)

    # Find the arUco markers in the image.
    corners, ids, rejected_img_points = detector.detectMarkers(image)

    # If a marker with the specified id is found, overlay the image file.
    if ids is not None and ids[0] == marker_id:
        # Draw the image_file over the arUco marker.

        top_left = (int(corners[0][0][0][0]), int(corners[0][0][0][1]))
        top_right = (int(corners[0][0][1][0]), int(corners[0][0][1][1]))
        bottom_left = (int(corners[0][0][3][0]), int(corners[0][0][3][1]))
        bottom_right = (int(corners[0][0][2][0]), int(corners[0][0][2][1]))

        cv2.circle(image, top_left, 5, (0, 0, 255), -1)
        cv2.circle(image, top_right, 5, (0, 0, 255), -1)
        cv2.circle(image, bottom_left, 5, (0, 0, 255), -1)
        cv2.circle(image, bottom_right, 5, (0, 0, 255), -1)

        # Overlay the image file over the arUco marker.
        overlay = cv2.imread(image_file)

        # Resize the overlay to fit the arUco marker.
        overlay = cv2.resize(overlay, (int(corners[0][0][1][0]) - int(corners[0][0][0][0]), int(corners[0][0][3][1]) - int(corners[0][0][0][1])))

        # Overlay the image file over the arUco marker.
        #image[int(corners[0][0][0][1]):int(corners[0][0][3][1]), int(corners[0][0][0][0]):int(corners[0][0][1][0])] = overlay

        # Overlay the image file over the arUco marker but use our defined corners
        image[top_left[1]:bottom_left[1], top_left[0]:top_right[0]] = overlay

        # Draw the bounding box around the arUco marker.
        cv2.line(image, top_left, top_right, (0, 255, 0), 2)
        cv2.line(image, top_right, bottom_right, (0, 255, 0), 2)
        cv2.line(image, bottom_right, bottom_left, (0, 255, 0), 2)
        cv2.line(image, bottom_left, top_left, (0, 255, 0), 2)

        # Draw the ID of the arUco marker.
        cv2.putText(image, str(ids[0]), (int(corners[0][0][0][0]), int(corners[0][0][0][1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return image