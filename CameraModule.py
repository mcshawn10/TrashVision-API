import cv2


class CameraModule:

    def __init__(self) -> None:
        pass

    def run_camera(self):

        cap = cv2.VideoCapture(self.path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        print(total_frames)
        # if not cap.isOpened():
        #     cap = cv2.VideoCapture(0)
        # if not cap.isOpened():
        #     raise IOError("cannot open webcam")

    

        while cap.isOpened():
            current_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
            success, frame = cap.read()

            if not success: break
            #assert(success)
            frame = rescale_frame(frame, 30)
            result = DeepFace.analyze(frame, enforce_detection=False, actions=['emotion'])

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            

            #draw rectangles around Trash
            # for(x,y,w,h) in Trash:
            #     cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

            font = cv2.FONT_HERSHEY_SIMPLEX
            
            cv2.putText(frame, 
                        result["dominant_emotion"], 
                        (50,50),
                        font, 2,
                        (0,0,255),
                        2,
                        cv2.LINE_4)
            cv2.imshow('original video', frame)   
            if cv2.waitKey(5) & 0xFF == 27:
                break


        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    pass