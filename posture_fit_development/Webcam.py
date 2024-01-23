import cv2
import time

cap = cv2.VideoCapture(0)
class CameraModule():
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(CameraModule, cls).__new__(cls)
        return cls.instance
    
    def __init__(self) -> None:
        self.webcam =  False
        self.required = True
        self.frame = None
        pass
    
    def open_camera(self) -> None:
        self.webcam = True
        cap = cv2.VideoCapture(0)
        time_previous = 0
        time_current = 0

        while cap.isOpened():
            
            _, frame = cap.read()
            _ = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            frame = cv2.flip(frame,1)    

            time_current = time.time()
            fps = 1 / (time_current - time_previous)
            time_previous = time_current
            cv2.putText(frame,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),3)

            self.fps = fps
            self.frame = cv2.imshow('Frame',frame)
            self.requried = True
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
    def camera_stats(self) -> [list[str]]:
        return [self.required, self.fps, self.frame]
