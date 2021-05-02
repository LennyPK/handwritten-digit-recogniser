'''code for AI model acquired from https://colab.research.google.com/drive/1EGMH2qYQydshkOCXpciKhI2NXNJDfcyQ?usp=sharing Lab 5 COMPSYS 302, University of Auckland'''

from __future__ import print_function
import sys
import torch
from torch import nn, optim, cuda
from torch.utils import data
from torch.autograd import Variable
from torchvision import datasets, transforms
import torch.nn.functional as F
import time
import numpy
import random
from PIL import Image, ImageOps
import canvas_file

# import matplotlib
# import matplotlib.pyplot as plt

global First
global Last
global last_epoch
global total_batches
global train_finish
global test_loss
global correct

correct = 0

# Training settings
batch_size = 64
device = 'cuda' if cuda.is_available() else 'cpu'
print(f'Training MNIST Model on {device}\n{"=" * 44}')

# MNIST Dataset
train_dataset = datasets.MNIST(root='mnist_data/',
                               train=True,
                               transform=transforms.ToTensor(),
                               download=True)

test_dataset = datasets.MNIST(root='mnist_data/',
                              train=False,
                              transform=transforms.ToTensor())

# Data Loader (Input Pipeline)
train_loader = data.DataLoader(dataset=train_dataset,
                                           batch_size=batch_size,
                                           shuffle=True)

test_loader = data.DataLoader(dataset=test_dataset,
                                          batch_size=batch_size,
                                          shuffle=False)


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.l1 = nn.Linear(784, 520)
        self.l2 = nn.Linear(520, 320)
        self.l3 = nn.Linear(320, 240)
        self.l4 = nn.Linear(240, 120)
        self.l5 = nn.Linear(120, 10)

    def forward(self, x):
        x = x.view(-1, 784)  # Flatten the data (n, 1, 28, 28)-> (n, 784)
        x = F.relu(self.l1(x))
        x = F.relu(self.l2(x))
        x = F.relu(self.l3(x))
        x = F.relu(self.l4(x))
        return self.l5(x)


model = Net()
model.to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)


def train(epoch):
    global percentage
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()

        '''arbitrary if statement, just making sure the functions runs'''
        if batch_idx:
            train_progress(batch_idx * len(data), epoch)
            # display_percentage()

        if batch_idx % 10 == 0:
            print('Train Epoch: {} | Batch Status: {}/{} ({:.0f}%) | Loss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))

def test():
    global correct

    model.eval()
    test_loss = 0
    correct = 0
    for data, target in test_loader:
        data, target = data.to(device), target.to(device)
        output = model(data)
        # sum up batch loss
        test_loss += criterion(output, target).item()
        # get the index of the max
        pred = output.data.max(1, keepdim=True)[1]
        correct += pred.eq(target.data.view_as(pred)).cpu().sum()

    test_loss /= len(test_loader.dataset)
    print(f'===========================\nTest set: Average loss: {test_loss:.4f}, Accuracy: {correct}/{len(test_loader.dataset)} '
          f'({100. * correct / len(test_loader.dataset):.0f}%)')

def evaluate():
    model.eval()
    loss = 0
    correct = 0
    
    for data, target in test_loader:
        data = data.unsqueeze(1)
        data, target = data, target
        
        if torch.cuda.is_available():
            data = data.cuda()
            target = target.cuda()
        
        output = model(data)
        
        loss += F.cross_entropy(output, target, size_average=False).data[0]

        pred = output.data.max(1, keepdim=True)[1]
        correct += pred.eq(target.data.view_as(pred)).cpu().sum()
        
    loss /= len(test_loader.dataset)
        
    print('\nAverage Val Loss: {:.4f}, Val Accuracy: {}/{} ({:.3f}%)\n'.format(
        loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))

'''specifying number of epochs to be inputted'''
def test_input(first, last):
    global First
    global Last
    global last_epoch
    global total_batches
    global train_finish

    First = first
    Last = last
    total_batches = []
    last_epoch = 0
    train_finish = 0

    since = time.time()
    for epoch in range(first, last):
        epoch_start = time.time()
        train(epoch)
        m, s = divmod(time.time() - epoch_start, 60)
        print(f'Training time: {m:.0f}m {s:.0f}s')
        test()
        m, s = divmod(time.time() - epoch_start, 60)
        print(f'Testing time: {m:.0f}m {s:.0f}s')

    m, s = divmod(time.time() - since, 60)
    
    print(f'Total Time: {m:.0f}m {s:.0f}s\nModel was trained on {device}!')
    train_finish = 1
    
'''kees track of how far through each epoch the AI has trained through'''
def train_progress(batch, epoch):
    global last_epoch
    global total_batches
    
    '''stores all the batches'''
    if epoch > last_epoch:
        last_epoch = epoch
        total_batches.append(batch)
    else:
        '''new epoch'''
        if total_batches[epoch - 1] < batch:
            total_batches[epoch - 1] = batch
    
'''displays total percentage'''
def display_percentage():
    global First
    global Last
    global total_batches
    completed = 0
    for total in total_batches:
        completed += total
    return (100. * completed / (len(train_loader.dataset) * (Last - First)))

'''checks if training has been finished or not'''
def train_status():
    global train_finish
    if train_finish == 0:
        return False
    else:
        return True

'''returns number probability'''
def make_predictions():

    output = model(preprocess())

    '''converting tensor weights into probabilities'''
    probabilities = torch.nn.functional.softmax(output[1], dim = 0)
    probabilities = probabilities.detach().numpy()

    print(probabilities)
    return(probabilities)

'''resizes the image to match the image type of the MNIST dataset'''
def preprocess():
    saved_image = Image.open('saved_canvas.png')
    saved_image_invert = ImageOps.invert(saved_image)

    '''Crop the image'''
    cropped_image = saved_image_invert.getbbox()
    
    if cropped_image:
        saved_image_invert = saved_image_invert.crop(cropped_image)
    '''Resize image'''
    centered_image = saved_image_invert.resize((20,20))
    '''Add padding'''
    final_image = Image.new(centered_image.mode, (28, 28), (0, 0, 0))
    final_image.paste(centered_image, (4, 4))

    final_image.save('saved_canvas.png')
        
    '''converts the processed image into a tensor'''
    tensor_converter = transforms.Compose([
        transforms.ToTensor(),
    ])

    tensor_of_canvas = tensor_converter(final_image)
    tensor_of_canvas = tensor_of_canvas.unsqueeze_(1)
    
    return tensor_of_canvas

def get_accuracy():
    return (100. * correct / len(test_loader.dataset))