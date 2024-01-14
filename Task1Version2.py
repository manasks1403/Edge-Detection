import numpy as np
import cv2

vid = cv2.VideoCapture(r'C:\Users\Manas Kumar Sinha\Desktop\Coding New\OpenCV\Task_1_test_video.mp4')

while True:
    ret, frame = vid.read()

    if not ret:
        break

    height, width, _ = frame.shape

    # Define the region of interest (ROI) based on the video dimensions
    roi_top_left = (int(width * 0.2), int(height * 0.5))
    roi_bottom_right = (int(width * 0.8), int(height * 0.9))
    roi = frame[roi_top_left[1]:roi_bottom_right[1], roi_top_left[0]:roi_bottom_right[0]]

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 125, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, maxLineGap=75, minLineLength=25)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1 + roi_top_left[0], y1 + roi_top_left[1]),
                     (x2 + roi_top_left[0], y2 + roi_top_left[1]), (0, 0, 255), 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
