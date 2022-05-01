# FlyTracker

installation:
  -pip install opencv-python
  -pip install numpy

-create images from video using GetFramesFromVideo.py
  change video name and output directories accordingly
-create tracked frames from video image frames using TrackFly.py
  output is one mask frame per video frame with object (fly) at 255 and background at 0
  Note: I hard-wired a cropping to remove the ruler on the left side and some noise at the top
  
Example outputs for video: 3 f20-d2-6-recovery-best-fall-from-ceiling-transition to forward-flight.avi
are in OutFrames
