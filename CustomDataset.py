import os
from PIL import Image
import torch
import torchvision.transforms as transforms

# Define the target size for resizing
target_size = (224, 224)  # Specify the width and height

# Define transformations to resize images
transform = transforms.Compose([
    transforms.Resize(target_size),
    transforms.ToTensor(),  # Convert to tensor
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])  # Normalize
])

# Example directory containing images
image_dir = "./TrashData/train" #path/to/your/images

# List all image file names
image_files = [file for file in os.listdir(image_dir) if file.endswith('.jpg')]

# Load and preprocess images
for image_file in image_files:
    image_path = os.path.join(image_dir, image_file)
    image = Image.open(image_path)
    processed_image = transform(image)  # Apply transformations

    # Process the processed_image further (e.g., feed it to your model)

# If you are using a DataLoader:
from torch.utils.data import DataLoader, Dataset

class CustomDataset(Dataset):
    def __init__(self, image_paths, transform=None):
        self.image_paths = image_paths
        self.transform = transform

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        image_path = self.image_paths[idx]
        image = Image.open(image_path)
        
        if self.transform:
            image = self.transform(image)

        return image

# Create a DataLoader
train_image_paths = [os.path.join(image_dir, file) for file in image_files]
trainingDataset = CustomDataset(train_image_paths, transform=transform)
trainingDataloader = DataLoader(trainingDataset, batch_size=16, shuffle=True)


if __name__ == "__main__":
    pass