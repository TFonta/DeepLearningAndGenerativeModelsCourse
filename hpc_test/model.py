# Define a CNN to classify the images
import torch
import torch.nn as nn


class Net(nn.Module):
    def __init__(self, args):
        super().__init__()

        if args.use_norm == False:
            # first convolutional block
            self.conv_block1 = nn.Sequential(nn.Conv2d(3, args.feat, kernel_size=5),
                                            nn.ReLU(),
                                            nn.MaxPool2d(2, 2))
            # second convolutional block
            self.conv_block2 = nn.Sequential(nn.Conv2d(args.feat, args.feat*2, kernel_size=5),
                                            nn.ReLU(),
                                            nn.MaxPool2d(2, 2))
        elif args.use_norm == True:
            # first convolutional block
            self.conv_block1 = nn.Sequential(nn.Conv2d(3, args.feat, kernel_size=5),
                                            nn.BatchNorm2d(args.feat),
                                            nn.ReLU(),
                                            nn.MaxPool2d(2, 2))
            # second convolutional block
            self.conv_block2 = nn.Sequential(nn.Conv2d(args.feat, args.feat*2, kernel_size=5),
                                            nn.BatchNorm2d(args.feat*2),
                                            nn.ReLU(),
                                            nn.MaxPool2d(2, 2))            
        # fully connected blocks
        self.fc1 = nn.Sequential(nn.Linear(args.feat*2 * 5 * 5, 120),
                                nn.ReLU())
        self.fc2 = nn.Sequential(nn.Linear(120, 84),
                                 nn.ReLU())
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.conv_block1(x)
        x = self.conv_block2(x) # bs,args.feat*2,5,5
        x = torch.flatten(x, 1) # flatten all dimensions except batch
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
        return x