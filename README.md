# Deep Learning And Generative Models Course

## Setting up Pytorch environment

### Create Anaconda Environment

- Download Miniconda from https://docs.conda.io/en/latest/miniconda.html
- Remember to select "add to PATH" when installing 
- Create Pytorch environment using the command:
```
conda create -n pytorch
```
- To activate env:
```
conda activate pytorch
```
- To deactivate env:
```
conda deactivate
```
- With the 'pytorch' env activated install the required packages:

CPU only
```
conda install pytorch torchvision torchaudio cpuonly -c pytorch
```

GPU
```
conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch
```

Alternatively, you can also install torch via pip
```
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
```

### Setting up VS code

- Install VS code from https://code.visualstudio.com/
- Install Python extension from the extension tab or from https://marketplace.visualstudio.com/items?itemName=ms-python.python
- Setting up conda in VS code: 
  - select a Python 3 interpreter by opening the **Command Palette** (Ctrl+Shift+P) or (F1)
  - type **Python: Select Interpreter**
  - select the 'pytorch' Conda environment
- Now you can code with Pytorch :)

### Install additional packages
Jupyter-lab:
```
pip install jupyterlab
```
Usually if some package is missing it can be installed with:
```
pip install [PACKAGE_NAME]
```

### Honorable Mentions
Some code borrowed from the excellent repo: https://atcold.github.io/pytorch-Deep-Learning/
