# HPC USER GUIDE

https://www.hpc.unipr.it/dokuwiki/doku.php?id=calcoloscientifico:userguide

To login to hpc use the following command (while in VPN):
```
ssh <name.surname>@login.hpc.unipr.it 
```

## Generate Key for ssh 

In order to use the cluster it is necessary to eliminate the need to use the password among nodes, using public key authentication. It is necessary to generate on login.hpc.unipr.it the pair of keys, without passphrase, and add the public key in the authorization file (authorized_keys):

Key generation. Accept the defaults by pressing enter:
```
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
```

Copy of the public key into authorized_keys:
```
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```
Change the authorized_keys file permission:
```
chmod 0600 ~/.ssh/authorized_keys
```

## Launch a script in hpc

Once logged you will need to create a bash file to launch the job that will execute your code. An example can be seen below:
```
#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --qos=gpu
#SBATCH --time 00:10:00
#SBATCH --mem=32gb
#SBATCH --ntasks-per-node 10


#< Charge resources to account 
#SBATCH --account T_2022_dlagm

echo $SLURM_JOB_NODELIST

echo  #OMP_NUM_THREADS : $OMP_NUM_THREADS

module load miniconda3
source "$CONDA_PREFIX/etc/profile.d/conda.sh"
conda activate pytorch-cuda-11.1

python ./hpc_test/hpc_test.py --dataset_path /hpc/archive/T_2022_DLAGM/tomaso.fontanini/cifar10 \
--checkpoint_path /hpc/group/T_2022_DLAGM/tomaso.fontanini/hpc_exp

conda deactivate
```
To put your job in queue do:
```
sbatch <filename>.bash
```
In order to see the status of your job:
```
squeue
```
or
```
squeue --user=<name.surname>
```

To cancel a job:
```
scancel <jobID>
```
