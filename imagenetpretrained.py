from torchvision import models
from torchvision.transforms import ToTensor, Resize, Normalize
from torchvision import transforms

import torch
from PIL import Image

import json


# Download ResNet
resnet18_model = models.resnet18(pretrained=True)
# Init Transforms
preprocess = transforms.Compose([Resize((224, 224)),
                                 ToTensor(),
                                 Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
# convert image to PIL and pass for transforms
img = Image.open("horse.jpg")
img2 = Image.open("duck.jpg")
img3 = Image.open("cat.jpg")
img = preprocess(img)
img2 = preprocess(img2)
img3 = preprocess(img3)
# print(type(img2))

# unsqueeze image
img_sq = torch.unsqueeze(img, 0)
img_sq2 = torch.unsqueeze(img2, 0)
img_sq3 = torch.unsqueeze(img3, 0)

# Set downloaded model in eval mode
resnet18_model = resnet18_model.eval()

probs = resnet18_model(img_sq)
probs_2 = resnet18_model(img_sq2)
probs_3 = resnet18_model(img_sq3)

value, index = torch.max(probs, 1)
value2, index2 = torch.max(probs_2, 1)
value3, index3 = torch.max(probs_3, 1)

print(int(index.numpy()))
print(int(index2.numpy()))
print(int(index3.numpy()))


with open("imagenet_class_index.json", "r") as read_file:
    labels = json.load(read_file)


print(labels[str(int(index.numpy()))])
print(labels[str(int(index2.numpy()))])
print(labels[str(int(index3.numpy()))])
