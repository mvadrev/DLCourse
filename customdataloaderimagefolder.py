from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
from torchvision.transforms import ToTensor, Resize, Normalize
from torchvision import transforms
import os
import matplotlib.pyplot as plt
import numpy as np

root_dir = "main_dir"
print(os.listdir(root_dir))

transforms = transforms.Compose([Resize((224, 224)),
                                 ToTensor(),
                                 Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

train_data = ImageFolder(root=os.path.join(
    root_dir, "train"), transform=transforms)

val_data = ImageFolder(root=os.path.join(
    root_dir, "val"), transform=transforms)

train_loader = DataLoader(train_data, batch_size=4,
                          shuffle=True, num_workers=1)

train_loader_iter = iter(train_loader)
x, y = next(train_loader_iter)
print(x.shape, y.shape)
