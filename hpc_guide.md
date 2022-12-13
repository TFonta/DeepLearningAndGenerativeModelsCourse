# HPC USER GUIDE

https://www.hpc.unipr.it/dokuwiki/doku.php?id=calcoloscientifico:userguide

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
