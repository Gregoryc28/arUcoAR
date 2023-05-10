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