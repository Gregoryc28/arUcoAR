import cv2
import numpy as np

import data

# Generate a marker
name = "dog"
marker = data.genMarker(name, data.convIDtoInt(name), 100)