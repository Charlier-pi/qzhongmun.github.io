## Shell & Github action (CI)

### autojump

```
vim .zshrc
source .zshrc
cd .oh-my-zsh
vim -p .zshrc .zshrc.pre-oh-my-zsh
ls .oh-my-zsh/plugins
ls .oh-my-zsh/plugins/autojump
echo $SHELL
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
brew install autojump
git status
vim .gitignore
git branch
git pull
git add -A .
git status
git commit -m "backend python"
git checkout -b dev
git checkout main
git checkout -b actions
mkdir -p .github/workflows
cd .github/workflows
touch github-actions-demo.yml
vim github-actions-demo.yml
pwd
cd ../..
git add .github/
git status
git commit -m "github actions demo"
git remote -v
git push origin
git push --set-upstream origin actions
git remote -v
vim .github/workflows/github-actions-demo.yml
cd .github/workflows/
ls
cat id_ssh_key.pub
cat id_ssh_key
ssh qzdocker
docker images
vim .zshrc
source .zshrc
docker images
docker run -it ubuntu
ls
docker ps
docker images
pyenv shell venv395
pwd
j exx
j deplo

```

### Github action

```

```
