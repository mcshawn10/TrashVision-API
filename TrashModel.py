import torch
import torchvision
import torch.nn as nn
import torchvision.models as models
import torch.optim as optim



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
    
    

    def train_custom_model(self, train_loader):
        criterion = nn.CrossEntropyLoss()
        
        optimizer = optim.Adam(self.parameters(), lr=0.001)
        num_epochs = 50
        for epoch in range(num_epochs):
            
            self.train()  # Set the model to training mode
            for inputs, labels in train_loader:
                optimizer.zero_grad()  # Zero the gradients
                outputs = self(inputs)  # Forward pass
                loss = criterion(outputs, labels)  # Calculate loss
                loss.backward()  # Backpropagation
                optimizer.step()  # Update model parameters
            
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