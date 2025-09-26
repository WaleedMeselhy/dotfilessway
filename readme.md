# Manjaro Installation
=================================
## Required Packages
```sh
yay -S  qt6-tools qt6-websockets python-pipx
pipx ensurepath
```

## Packages
```sh
pipx install linak-controller 
yay -S gnome-keyring libsecret libgnome-keyring seahorse \
fortune-mod cowsay gtop \
1password 1password-cli chezmoi wlr-randr  ttf-roboto-mono-nerd \
visual-studio-code-bin qownnotes \
google-chrome nvim tmux meld geany\
autojump zoxide fzf eza yazi \
kubectl
curl -fsSL https://pyenv.run | bash
curl -fsSL "https://github.com/gpakosz/.tmux/raw/refs/heads/master/install.sh#$(date +%s)" | bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
```

## config zsh plugins
```sh
sudo chown waleed:waleed -R /usr/share/oh-my-zsh/custom
git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-completions
git clone https://github.com/jscutlery/nx-completion.git ${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/nx-completion
git clone https://github.com/Aloxaf/fzf-tab ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/fzf-tab
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
```

## Load config
```sh
sh -c "$(curl -fsLS get.chezmoi.io)" -- init  https://github.com/WaleedMeselhy/dotfilessway.git
```






































#@plugin 'omerxx/tmux-floax