import argparse

import torchvision
from torchvision import transforms
from torch.utils.data import DataLoader
from model import *
from train import *

#==============================================================================
# Training settings
#==============================================================================
parser = argparse.ArgumentParser()
#
parser.add_argument('--seed', type=int, default=1, help='seed value')
#
parser.add_argument('--num_inputs', type=int, default=784, metavar='N', help='number of input features')
#
parser.add_argument('--num_outputs', type=int, default=10, metavar='N', help='number of output claases')
#
parser.add_argument('--num_epochs', type=int, default=5, metavar='N', help='number of epochs to train (default: 5)')
#
args = parser.parse_args()

torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
set_seed(args.seed)
device = get_device()

#******************************************************************************
# Download Datasets
#******************************************************************************
mnist_train = torchvision.datasets.FashionMNIST(root='~/Datasets/FashionMNIST', train=True, download=False, transform=transforms.ToTensor())
mnist_test = torchvision.datasets.FashionMNIST(root='~/Datasets/FashionMNIST', train=False, download=True, transform=transforms.ToTensor())

#******************************************************************************
# Create Dataloader objects
#******************************************************************************
train_loader = DataLoader(mnist_train, batch_size=100, shuffle=True)
test_loader = DataLoader(mnist_test, batch_size=100, shuffle=False)

#==============================================================================
# Model
#==============================================================================
model = SoftmaxGST(args.num_inputs, args.num_outputs)
model = model.to(device)

#==============================================================================
# Start training
#==============================================================================
train(model, train_loader, test_loader, args.num_epochs)
