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
