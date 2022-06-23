# DeepLearningAndGenerativeModelsCourse

## Create Anaconda Environment

- Download Miniconda from https://docs.conda.io/en/latest/miniconda.html
- Remember to select "add to PATH" when installing 
- Create Pytorch environment using the command:
```
conda create -n pytorch
```

- Then install the required packages:

CPU only
```
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```

GPU
```
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
```

## Setting up VS code

- Install VS code from https://code.visualstudio.com/
- Install Python extension from the extension tab or from https://marketplace.visualstudio.com/items?itemName=ms-python.python
- Setting up conda in VS code: 
  - select a Python 3 interpreter by opening the **Command Palette** (Ctrl+Shift+P) or (F1)
  - type **Python: Select Interpreter**
  - select the Conda environment
