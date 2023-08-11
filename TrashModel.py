import torch
import torchvision
import torch.nn as nn
import torchvision.models as models
import torch.optim as optim
from tqdm import tqdm



class TrashModel(nn.Module):
    def __init__(self, gpu):
        super(TrashModel, self).__init__()
        self.gpu = gpu
        self.to(self.gpu)
        self.NUM_CLASSES = 12

        self.mobilenet = models.mobilenet_v2(pretrained=False)  
        in_features = self.mobilenet.classifier[1].in_features
        self.mobilenet.classifier = nn.Sequential(nn.Linear(in_features, self.NUM_CLASSES))
    
    def forward(self, x):
        
        return self.mobilenet(x)   
    
    def calc_training_accuracy(self, outputs, labels):
        
        _, predicted = torch.max(outputs, 1)  # Get class predictions
        total = labels.size(0)  # Total number of samples
        correct = (predicted == labels).sum().item()  # Count correct predictions
        accuracy = correct / total
        return accuracy

    def train_custom_model(self, train_loader:torch.utils.data.dataloader.DataLoader):
        criterion = nn.CrossEntropyLoss()
        
        optimizer = optim.Adam(self.parameters(), lr=0.001)
        num_epochs = 11
        
        for epoch in range(num_epochs):
            self.train()  # Set the model to training mode
            loop = tqdm(enumerate(train_loader), total=len(train_loader), leave = False)
            accuracy = 0
            for batchIndex , (inputs, labels) in loop:
                inputs = inputs.to(device=self.gpu)
                labels= labels.to(device=self.gpu)
                optimizer.zero_grad()  # Zero the gradients
                outputs = self(inputs)  # Forward pass
                loss = criterion(outputs, labels)  # Calculate loss
                loss.backward()  # Backpropagation
                optimizer.step()  # Update model parameters
                
                accuracy += self.calc_training_accuracy(outputs, labels)
                epoch_accuracy = accuracy / len(train_loader)
                loop.set_description(f"Epoch [{epoch}/{num_epochs}]")
                loop.set_postfix(loss = loss.item(), acc=epoch_accuracy)  


    def evaluate(self, test_loader):
        # Validation
        self.eval()  # Set the model to evaluation mode
        with torch.no_grad():
            # Evaluate on validation dataset and calculate metrics
            pass       

    def SaveModel(self, savePath):
        torch.save(self.state_dict(), savePath)

if __name__ ==  "__main__":
    pass