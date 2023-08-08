#import torch
import torchvision
import torch.nn as nn
import torchvision.models as models



class TrashModel(nn.Module):
    def __init__(self, gpu):
        super(TrashModel, self).__init__()
        self.to(gpu)
        self.NUM_CLASSES = 12

        self.mobilenet = models.mobilenet_v2(pretrained=False)  
        in_features = self.mobilenet.classifier[1].in_features
        self.mobilenet.classifier = nn.Sequential(nn.Linear(in_features, self.NUM_CLASSES))
    
    def forward(self, x):
        return self.mobilenet(x)   
    
    def build(self):
        pass

    def train(self):
        pass


if __name__ ==  "__main__":
    pass