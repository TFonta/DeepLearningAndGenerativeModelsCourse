# Deep Learning And Generative Models Course

## Setting up Pytorch environment

### Create Conda Environment

- Download Miniconda from https://www.anaconda.com/download/success?reg=skipped-miniconda
- On Windows, open **Miniconda Prompt** as administrator to run the commands below (no need to add Conda to PATH).
- Create the Pytorch environment:

  ```bash
  conda create -n pytorch python=3.12
  ```

- To activate the environment:

  ```bash
  conda activate pytorch
  ```

- To deactivate it:

  ```bash
  conda deactivate
  ```

### Install Pytorch

With the `pytorch` environment activated, install PyTorch. The official installation commands are available here: https://pytorch.org/get-started/locally/

**CPU (Windows/Linux)**

```bash
python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

**NVIDIA GPU**

Check your GPU driver with `nvidia-smi`, then select the appropriate CUDA option on the [PyTorch installation page](https://pytorch.org/get-started/locally/) and run the suggested command.

Example:

```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu126
```


**Mac (Intel / Apple Silicon)**

```bash
python -m pip install torch torchvision
```

For Apple Silicon GPU support, see https://developer.apple.com/metal/pytorch/

A GPU is not required for the first exercises.

### Check the installation

Open Python in your terminal:

```bash
python
```

Then run:

```python
import torch

print(torch.__version__)
print("CUDA:", torch.cuda.is_available()) # for Windows/Linux
print("MPS:", torch.backends.mps.is_available()) # for Mac
print(torch.rand(2, 3))
```

If the tensor is printed without errors, PyTorch is working. `False` for CUDA or MPS is normal if your computer does not support them.

### Enabling Conda on PowerShell

If PowerShell does not recognize `conda`, open Miniconda Prompt and run:

```bash
conda init powershell
```

Then restart PowerShell. You can also continue using Miniconda Prompt.

### Setting up VS Code

- Install VS Code from https://code.visualstudio.com/
- Install the **Python** and **Jupyter** extensions.
- Open the Command Palette (`Ctrl+Shift+P` or `F1`), type **Python: Select Interpreter**, and select the `pytorch` Conda environment.
- When opening a notebook (`.ipynb`), select the same environment as the notebook kernel.

### Google Colab

Alternatively, you can use Google Colab: https://colab.research.google.com/

To use a GPU, go to **Runtime > Change runtime type** and select a GPU if one is available.

### Install additional packages

With the environment activated:

```bash
python -m pip install jupyterlab ipykernel numpy matplotlib tqdm
```

Usually, if some package is missing, it can be installed with:

```bash
python -m pip install PACKAGE_NAME
```

### Final Test

Now you can start with [ex0.ipynb](ex0.ipynb)!

### Honorable Mentions

Some code borrowed from the excellent repo: https://github.com/Atcold/NYU-DLSP20/tree/master
