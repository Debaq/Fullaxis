import os
import time

import cv2
import numpy as np
from lib.video.BlobDetector import BlobDetector
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QImage
from base import context
import os



class OpenCVProcessingThread(QThread):
    change_pixmap_signal = Signal(QImage)
    signal_frame_states = Signal(dict)

    def __init__(self, parent=None, cam_n=2):
        super().__init__(parent)
        self._running = True
        self._flip_horizontal = False
        self.blob_detector_left = BlobDetector()
        self.blob_detector_rigth = BlobDetector()
        self.record = [False, 0, False]
        self.cam_n = cam_n

    def run(self):
        """Main loop for processing video frames."""
        self.open_cap()
        while self._running:
            ret, frame = self.cap.read()
            if ret:
                self.process_frame(frame)

    def process_frame(self, frame):
        """Process a single frame and emit the result."""
        if self.record[0]:
            im_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            self.out.write(im_bgr)

        left_half, right_half = self.split_frame(frame)
        left_half = self.blob_detector_left.detect(
            left_half, "left", self.get_color("left"))
        right_half = self.blob_detector_rigth.detect(
            right_half, "right", self.get_color("right"))

        result = np.hstack((left_half, right_half))
        self.emit_frame(result)

    def split_frame(self, frame):
        """Split the frame into left and right halves."""
        height, width = frame.shape[:2]
        left_half = frame[:, :width//2]
        right_half = frame[:, width//2:]
        return left_half, right_half

    def get_color(self, side):
        """Get color based on the side and flip setting."""
        if side == "left":
            return (0, 0, 255) if not self._flip_horizontal else (255, 0, 0)
        else:
            return (255, 0, 0) if not self._flip_horizontal else (0, 0, 255)

    def emit_frame(self, frame):
        """Convert and emit the frame as QImage."""
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(
            rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(640, 480, Qt.KeepAspectRatio)
        self.change_pixmap_signal.emit(p)

    def update_config_video(self, slides_values):
        """Update video settings based on provided values."""
        settings_map = {
            'contrast': cv2.CAP_PROP_CONTRAST,
            'blackligth': cv2.CAP_PROP_BACKLIGHT,
            'whitebalance': cv2.CAP_PROP_WB_TEMPERATURE,
            'brightness': cv2.CAP_PROP_BRIGHTNESS,
            'gamma': cv2.CAP_PROP_GAMMA,
            'sharpness': cv2.CAP_PROP_SHARPNESS,
            'hue': cv2.CAP_PROP_HUE,
            'saturation': cv2.CAP_PROP_SATURATION
        }
        for setting, value in slides_values.items():
            self.cap.set(settings_map[setting], value)

    def open_cap(self):
        """Open the video capture."""
        if os.name == 'nt':
            self.cap = cv2.VideoCapture(self.cam_n, cv2.CAP_DSHOW)
        else:
            self.cap = self.open_camera(self.cam_n)
        self.setup_video_writer()

    def setup_video_writer(self):
        """Setup the video writer for recording."""
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
        size_frame = (int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                      int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        FPS = self.cap.get(cv2.CAP_PROP_FPS)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter('output.avi', fourcc, FPS, size_frame)

    def open_camera(self, index):
        """Open the camera and handle any failures."""
        while True:
            cap = cv2.VideoCapture(index)
            if cap.isOpened():
                self.record[2] = True
                self.signal_frame_states.emit(self.record)
                self._running = True
                return cap
            else:
                time.sleep(1)

    def close_cap(self, close_out=False):
        """Close the video capture."""
        self._running = False
        self.cap.release()
        self.record[2] = False
        self.signal_frame_states.emit(self.record)
        self.out.release()

    def stop(self, save, name):
        """Stop the video processing and optionally save the recording."""
        self._running = False
        self.close_cap(True)
        self.record[0] = False
        if save:
            time_str = str(time.time()).replace('.', '-')
            name = f"{name}_{time_str}"
            os.rename('output.avi', name)

    def state_record(self):
        """Set the recording state."""
        self.record = True

        

