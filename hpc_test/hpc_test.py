import torch
import torchvision
import torchvision.transforms as transforms
import argparse
from torch.utils.tensorboard import SummaryWriter

from solver import Solver

def get_args():
    parser = argparse.ArgumentParser()   

    parser.add_argument('--run_name', type=str, default="run_1", help='name of current run')
    parser.add_argument('--model_name', type=str, default="first_train", help='name of the model to be saved/loaded')

    parser.add_argument('--epochs', type=int, default=2, help='number of epochs')
    parser.add_argument('--batch_size', type=int, default=16, help='number of elements in batch size')
    parser.add_argument('--workers', type=int, default=2, help='number of workers in data loader')
    parser.add_argument('--print_every', type=int, default=500, help='print losses every N iteration')

    parser.add_argument('--lr', type=float, default=0.001, help='learning rate')
    parser.add_argument('--opt', type=str, default='SGD', choices=['SGD', 'Adam'], help = 'optimizer used for training')
    parser.add_argument('--use_norm', action='store_true', help='use normalization layers in model')
    parser.add_argument('--feat', type=int, default=16, help='number of features in model')

    parser.add_argument('--dataset_path', type=str, default='./data', help='path were to save/get the dataset')
    parser.add_argument('--checkpoint_path', type=str, default='./', help='path were to save the trained model')

    parser.add_argument('--resume_train', action='store_true', help='load the model from checkpoint before training')

    return parser.parse_args()

def main(args):
    writer = SummaryWriter('./runs/' + args.run_name)

    # define transforms
    transform = transforms.Compose(
        [transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

    # load train ds
    trainset = torchvision.datasets.CIFAR10(root=args.dataset_path, train=True,
                                            download=True, transform=transform)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=args.batch_size,
                                            shuffle=True, num_workers=args.workers)
    # load test ds
    testset = torchvision.datasets.CIFAR10(root=args.dataset_path, train=False,
                                        download=True, transform=transform)
    testloader = torch.utils.data.DataLoader(testset, batch_size=args.batch_size,
                                            shuffle=False, num_workers=args.workers)

    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print("Device: ", device)

    # define solver class
    solver = Solver(train_loader=trainloader,
            test_loader=testloader,
            device=device,
            writer=writer,
            args=args)

    # TRAIN model
    solver.train()

if __name__ == "__main__":
    args = get_args()
    print(args)
    main(args)