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
yay -S notion-app-electron libreoffice-still \
vlc vlc-plugin-ffmpeg samba smbclient\
gnome-keyring libsecret libgnome-keyring seahorse \
xdg-desktop-portal-wlr xdg-desktop-portal-gtk pipewire wireplumber \
fortune-mod cowsay gtop \
1password 1password-cli chezmoi wlr-randr  ttf-roboto-mono-nerd \
ttf-fira-code           \
intel-ucode    intel-compute-runtime \
adobe-source-code-pro-fonts \
ttf-sourcecodepro-nerd  \
ttf-meslo-nerd          \
ttf-ms-fonts      \
visual-studio-code-bin qownnotes \
google-chrome nvim tmux meld geany\
autojump zoxide fzf eza yazi \
kubectl aws-cli \
zoom slack-desktop \
docker docker-compose postman-bin ngrok postgresql redis \
git-cola nemo dbeaver zip k9s htop \
electron25-bin chatgpt-desktop-bin \
solaar  psensor obsidian ncdu simplenote-electron-bin
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
## config keyring
* Configure PAM for Automatic Unlock

    Edit the PAM configuration to unlock the keyring on login:
    ```sh
    sudo nano /etc/pam.d/login
    ```
    Add these lines if not present:
    ```
    auth       optional     pam_gnome_keyring.so
    session    optional     pam_gnome_keyring.so auto_start
    ```
## fix zoom sharing
```sh
systemctl --user restart pipewire wireplumber xdg-desktop-portal
```

## enable docker
```sh
sudo systemctl enable docker.service
sudo systemctl start docker.service
sudo usermod -aG docker ${USER}
```

## fix simplenote
```sh
cp /usr/share/applications/simplenote.desktop ~/.local/share/applications/simplenote.desktop
sed -i 's|^Exec=.*|Exec=/opt/Simplenote/simplenote --ozone-platform=x11 %U|' ~/.local/share/applications/simplenote.desktop

```

* configure font
```sh
fc-cache -v
```



## make chezmoi repo use shh
```sh
git remote set-url origin git@github.com:waleedmeselhy/dotfilessway
```
















#@plugin 'omerxx/tmux-floax