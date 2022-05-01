import cv2
vidcap = cv2.VideoCapture('/Users/lbrown/Documents/JaneFlies/3 f20-d2-6-recovery-best-fall-from-ceiling-transition to forward-flight.avi')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("Frames/frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1