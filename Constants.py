import os
import torch
# Path to your test directory
test_dir = './TrashData/val/'

# Get a list of subdirectories (labels)
labels = [label for label in os.listdir(test_dir) if os.path.isdir(os.path.join(test_dir, label))]

CATEGORIES = labels[::-1]

GPU = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

if __name__ == "__main__":
    pass