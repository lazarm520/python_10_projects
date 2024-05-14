import cv2
import numpy as np
from PIL import ImageGrab

def screanRecorder():
  fourcc = cv2.VideoWriter.fourcc(*'XVID')
  out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1366, 768))

  while True:
    img = ImageGrab.grab()
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2BGRA)
    cv2.imshow("Screan Recorder", frame)
    out.write(frame)

    if cv2.waitKey(1) == 27:
      break
  
  out.release()
  cv2.destroyAllWindows()


screanRecorder()

