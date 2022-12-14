import torch
import torch.optim as optim
import torch.nn as nn
import os

from model import Net

class Solver(object):
    """Solver for training and testing."""

    def __init__(self, train_loader, test_loader, device, writer, args):
        """Initialize configurations."""

        self.args = args
        self.model_name = 'cifar_net_{}.pth'.format(self.args.model_name)

        # Define the model
        self.net = Net(self.args).to(device)

        # load a pretrained model
        if self.args.resume_train == True:
            self.load_model()
        
        # Define Loss function
        self.criterion = nn.CrossEntropyLoss()
        
        # Choose optimizer
        if self.args.opt == "SGD":
            self.optimizer = optim.SGD(self.net.parameters(), lr=self.args.lr, momentum=0.9)
        elif self.args.opt == "Adam":
            self.optimizer = optim.Adam(self.net.parameters(), lr=self.args.lr)

        self.epochs = self.args.epochs
        self.train_loader = train_loader
        self.test_loader = test_loader

        self.device = device

        self.writer = writer

    def save_model(self):
        # if you want to save the model
        check_path = os.path.join(self.args.checkpoint_path, self.model_name)
        torch.save(self.net.state_dict(), check_path)
        print("Model saved!")

    def load_model(self):
        # function to load the model
        check_path = os.path.join(self.args.checkpoint_path, self.model_name)
        self.net.load_state_dict(torch.load(check_path))
        print("Model loaded!")
    
    def train(self):
        self.net.train()
        for epoch in range(self.epochs):  # loop over the dataset multiple times

            running_loss = 0.0
            for i, data in enumerate(self.train_loader, 0):
                # get the inputs; data is a list of [inputs, labels]
                inputs, labels = data
                
                # put data on correct device
                inputs, labels = inputs.to(self.device), labels.to(self.device)
                
                # zero the parameter gradients
                self.optimizer.zero_grad()

                # forward + backward + optimize
                outputs = self.net(inputs)
                loss = self.criterion(outputs, labels)
                loss.backward()
                self.optimizer.step()

                # print statistics
                running_loss += loss.item()
                if i % self.args.print_every == self.args.print_every - 1:  
                    
                    print(f'[{epoch + 1}, {i + 1:5d}] loss: {running_loss / self.args.print_every:.3f}')

                    self.writer.add_scalar('training loss',
                        running_loss / self.args.print_every,
                        epoch * len(self.train_loader) + i)
                    
                    running_loss = 0.0

                    # Test model
                    self.test(epoch, i)

            self.save_model()
        
        self.writer.flush()
        self.writer.close()
        print('Finished Training')   
    
    def test(self, epoch, i):
        # now lets evaluate the model on the test set
        correct = 0
        total = 0

        # put net into evaluation mode
        self.net.eval()

        # since we're not training, we don't need to calculate the gradients for our outputs
        with torch.no_grad():
            for data in self.test_loader:
                inputs, labels = data
                # put data on correct device
                inputs, labels = inputs.to(self.device), labels.to(self.device)
                # calculate outputs by running images through the network
                outputs = self.net(inputs)
                # the class with the highest energy is what we choose as prediction
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        self.writer.add_scalar('test accuracy',
            100 * correct / total,
            epoch * len(self.train_loader) + i)

        print(f'Accuracy of the network on the 10000 test images: {100 * correct / total} %')
        self.net.train()