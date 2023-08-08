import torch
import torchvision



MobileNet = torchvision.models.mobilenet_v2()

class TrashModel(torch.nn.Module):
    def __init__(self, gpu):
        super(MobileNet, self).__init__()
        self.to(gpu)
        
    def build(self):
        pass

    def train(self):
        pass
