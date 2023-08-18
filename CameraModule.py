import cv2
import torch
from torchvision.transforms import ToTensor
from Constants import *
from TrashModel import TrashModel
from Producer import KafkaProducer
# import torch.nn.functional as F

class CameraModule:

    def __init__(self) -> None:
        self.producer = KafkaProducer()

    def CameraCapture(self):
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
            
            #frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            
            #current_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (128,128), interpolation=cv2.INTER_AREA)

            tensor_frame = ToTensor()(frame).unsqueeze(0)  # Convert to tensor
            
            # Perform inference
            with torch.no_grad():
                predictions = trashModel(tensor_frame)
            # probabilities = F.softmax(predictions, dim=0)
            
            predicted_class_index = predictions.argmax().item()
            predicted_label = categories[predicted_class_index]
            confidence = predictions[predicted_label].item()
            # Process predictions and draw on the frame
            # ...
            if confidence > 0.5:
                cv2.putText(frame, 
                            predicted_label, 
                            (5,25),
                            font, 1,
                            (0,0,255),
                            1,
                            cv2.LINE_4)
            else: 
                cv2.putText(frame, 
                            "UNKNOWN", 
                            (5,25),
                            font, 1,
                            (0,0,255),
                            1,
                            cv2.LINE_4)
            
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            cv2.imshow('TrashVision', frame)
        


            if cv2.waitKey(5) & 0xFF == 27:
                
                break
            
        cv2.waitKey(0)
        cap.release()
        cv2.destroyAllWindows()
        cv2.waitKey(1)
        

    def ProduceTopic(self, detectedObject):
         # Your object detection logic here
        #
        # If an object is detected
        # if object_detected:
            # Send Kafka message
        self.producer.produce('object_detection_topic', value=detected_object_info)
        self.producer.flush()
        

if __name__ == "__main__":
    pass