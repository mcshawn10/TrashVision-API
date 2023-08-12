import cv2
import torch
from torchvision.transforms import ToTensor
from Constants import *
from TrashModel import TrashModel

class CameraModule:

    def __init__(self) -> None:
        pass

    def RunCamera(self):

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


    def DetectTrash(self):
        
        trashModel = TrashModel(GPU)
        trashModel.load_state_dict(torch.load('./TrainingAccuracyWeights/model1_weights'))
        trashModel.eval()


        font = cv2.FONT_HERSHEY_SIMPLEX
        categories = CATEGORIES
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            raise IOError("cannot open webcam")

        while cap.isOpened():

            success, frame = cap.read()
            
            frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            current_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)

            #input_arr = frame.astype("float32") / 255
            tensor_frame = ToTensor()(frame).unsqueeze(0)  # Convert to tensor
            #prediction = EffNet.predict(np.expand_dims(input_arr, axis=0))
            prediction = trashModel.evaluate()

            i = 0

            if prediction[0][0] <= 0.5:
                i = 0
            else: i = 1

            # Perform inference
            with torch.no_grad():
                predictions = trashModel(tensor_frame)
            
            # Process predictions and draw on the frame
            # ...
            # cv2.putText(frame, 
            #             categories[i], 
            #             (5,25),
            #             font, 1,
            #             (0,0,255),
            #             1,
            #             cv2.LINE_4)
            

            cv2.imshow('original video', frame)
        

            

                    #preds = EffNet.predict(np.expand_dims(frame, axis=0))[0]


            if cv2.waitKey(5) & 0xFF == 27:
                
                break
            
        cv2.waitKey(0)
        cap.release()
        cv2.destroyAllWindows()
        cv2.waitKey(1)

if __name__ == "__main__":
    pass