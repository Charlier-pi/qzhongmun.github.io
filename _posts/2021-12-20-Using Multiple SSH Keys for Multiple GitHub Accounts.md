## Using Multiple SSH Keys for Multiple GitHub Accounts
###  How to manage SSH keys on GitHub accounts


#### 1. Generating the SSH keys

```tsql
ssh-keygen -t rsa -C "your-github-mail"
ssh-keygen -t rsa -C "your-another-github-mail"
```

The key generator will prompt you for a file name.

Enter a unique name like:

```tsql
id_rsa_personal
id_rsa_work
```
```tsql
ls ~/.ssh
```
you will see below documents: 

```tsql
id_rsa_personal   id_rsa_personal.pub	  id_rsa_work   id_rsa_work.pub 
```  


#### 2. Adding a new SSH key to your GitHub account

Now that we have the SSH keys let us link them with the Github account.

To obtain the SSH key execute this command:

```powershell
cat id_rsa_personal.pub
```
Follow the steps below to add an SSH key to your GitHub account:

1. On your GitHub, navigate to Settings.
2. Hit on the New SSH Key button, give it a significant Title and paste the Key.
3. Finally, click the Add SSH key button.


#### 3. Creating and updating the SSH config file
Next, let us bring it all together in a config file. There are two GitHub accounts - the personal and work accounts. The personal account is the local account, and work is the global account.

The SSH config file is accessed by running this command:

```powershell
~/.ssh/config
```

If it exists, you can edit it, or else it can be created using this command:

```powershell
touch config
nano config
```

Update the config file by adding the following rules:

```powershell
# Default github account: personal
Host github-username1
   HostName github.com
   User git
   AddKeysToAgent yes
   UseKeychain yes
   IdentityFile  ~/.ssh/id_rsa_personal
   
# Other github account: work
Host github-username2
   HostName github.com
   User git
   AddKeysToAgent yes
   UseKeychain yes
   IdentityFile ~/.ssh/id_rsa_work
```


#### 4. Add ssh private keys to your agent:
```powershell
$ ssh-add ~/.ssh/oanhnn_private_key
$ ssh-add ~/.ssh/superman_private_key
```


#### 5. Test your connection
```powershell
$ ssh -T git@github.com
$ ssh -T git@github-superman
```
With each command, you may see this kind of warning, type yes:

```powershell
The authenticity of host 'github.com (192.30.252.1)' can't be established.
RSA key fingerprint is xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:
Are you sure you want to continue connecting (yes/no)?
```

If everything is OK, you will see these messages:

```powershell
Hi oanhnn! You've successfully authenticated, but GitHub does not provide shell access.
Hi superman! You've successfully authenticated, but GitHub does not provide shell access.
```


#### 6. Now all are set, just clone your repositories

Here we need to use SSH link and change this link like below:
```powershell
$ git clone git@username:programname.git 
```


***
```powershell
https://gist.github.com/oanhnn/80a89405ab9023894df7
https://www.section.io/engineering-education/using-multiple-ssh-keys-for-multiple-github-accounts/
```
