from torchvision import transforms
from torch.utils.data import DataLoader
# Imports PIL module
from PIL import Image

# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np


# Image transformations
image_transforms = {
    # Train uses data augmentation
    'train':
    transforms.Compose([
        transforms.RandomResizedCrop(size=256, scale=(0.8, 1.0)),
        transforms.RandomRotation(degrees=15),
        transforms.ColorJitter(),
        transforms.RandomHorizontalFlip(),
        transforms.CenterCrop(size=224),  # Image net standards
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225])  # Imagenet standards
    ]),
    # Validation does not use augmentation
    'valid':
    transforms.Compose([
        transforms.Resize(size=256),
        transforms.CenterCrop(size=224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}

# # Datasets from folders
# data = {
#     'train':
#     datasets.ImageFolder(root=traindir, transform=image_transforms['train']),
#     'valid':
#     datasets.ImageFolder(root=validdir, transform=image_transforms['valid']),
# }

# # Dataloader iterators, make sure to shuffle
# dataloaders = {
#     'train': DataLoader(data['train'], batch_size=batch_size, shuffle=True),
#     'val': DataLoader(data['valid'], batch_size=batch_size, shuffle=True)
# }





# open method used to open different extension image file
im = Image.open(r"root/dog/0-0.jpg")
x = image_transforms["train"](im)

# x = preprocess(img)
print(x.shape)

# This method will show image in any image viewer
# im.show()

reverse_preprocess = transforms.Compose([
    transforms.ToPILImage(),
    np.array,
])

plt.imshow(reverse_preprocess(x))