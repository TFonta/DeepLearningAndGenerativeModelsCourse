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

CPU
```
pip3 install torch torchvision torchaudio
```

GPU
```
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
```
### Enabling Conda on powershell

Follow the instruction on this link: https://gist.github.com/martinsotir/2bd2e16332dff71e0fa5be3ed3468a6c

### Setting up VS code

- Install VS code from https://code.visualstudio.com/
- Install Python extension from the extension tab or from https://marketplace.visualstudio.com/items?itemName=ms-python.python
- Setting up conda in VS code: 
  - select a Python 3 interpreter by opening the **Command Palette** (Ctrl+Shift+P) or (F1)
  - type **Python: Select Interpreter**
  - select the 'pytorch' Conda environment
- Now you can code with Pytorch :)

### Google Colab

Alternatively, you can also use Google Colab: https://www.marktechpost.com/2021/01/09/getting-started-with-pytorch-in-google-collab-with-free-gpu/

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
