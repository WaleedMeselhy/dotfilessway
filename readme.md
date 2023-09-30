yay -S base-devel           \
    wdisplays-git           \
    chezmoi                 \
    notepad++               \
    visual-studio-code-bin  \
    google-chrome           \
    libfprint-tod-git       \
    fprintd                 \
    howdy                   \
    linux-enable-ir-emitter \
    docker docker-compose   \
    1password 1password-cli \
    slack-desktop git-cola  \
    wlr-randr zoxide        \
    p4v exa autojump        \
    tmux meld               \
    tlp tlp-rdw             \
    ttf-fira-code           \
    adobe-source-code-pro-fonts \
    ttf-sourcecodepro-nerd  \
    ttf-meslo-nerd          \
    ttf-ms-fonts            \
    x86_energy_perf_policy  \
    intel-ucode             \
    intel-compute-runtime   \
    vulkan-intel            \
    dbeaver                 \
    postman-bin             \
    telegram-desktop        \
    neovim                  \
    vlc                     \
    vdhcoapp                \
    notion-app-enhanced     \
    gnome-disk-utility      \
    graphviz                \
    zoom                    \
    gtop                    \
    obsidian    \
    syncthing   \
    okular \
    samba smbclient \
    tor-browser     \
    simplenote-electron-bin
```

sudo systemctl enable fprintd.service
sudo systemctl start fprintd.service
sudo fprintd-enroll waleed
```

* configure face lock
```
sudo linux-enable-ir-emitter configure
replace device_path = none with  device_path = /dev/video2  in EDITOR=editor sudo howdy config
```

* edit below files to add 
```
auth sufficient pam_python.so /lib/security/howdy/pam.py
auth sufficient pam_fprintd.so
```
```
sudo nano /etc/pam.d/system-login
sudo nano /etc/pam.d/system-local-login
sudo nano /etc/pam.d/login
sudo nano /etc/pam.d/swaylock
sudo nano /etc/pam.d/polkit-1 
sudo nano /etc/pam.d/sudo
```

* configure kerying
install seahorse and create default password kerying

* configure nvm
```sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
nvm use 18
nvm install 18
npm install --global yarn 
```

* enable docker
```sh
sudo systemctl enable docker.service
sudo systemctl start docker.service
sudo usermod -aG docker ${USER}
```

* configure zsh plugins
```sh
sudo chown waleed:waleed -R /usr/share/oh-my-zsh/custom
git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-completions
git clone https://github.com/jscutlery/nx-completion.git ${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/nx-completion
git clone https://github.com/Aloxaf/fzf-tab ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/fzf-tab
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
```

* configure tmux
```sh
git clone https://github.com/gpakosz/.tmux.git
ln -s -f .tmux/.tmux.conf
cp .tmux/.tmux.conf.local .
```

* configure zsh autocomplete
```sh
rm -f /home/waleed/.config/zsh/.zcompdump*; compinit
```

* configure tlp
```sh
sudo systemctl enable tlp.service
sudo systemctl mask systemd-rfkill.service
sudo systemctl mask systemd-rfkill.socket
sudo systemctl start tlp.service
```

* configure font
```sh
fc-cache -v
```


* configure fstrim
```sh
sudo systemctl enable fstrim.timer
sudo systemctl start fstrim.timer
```

* fix simplenote
```sh
# fix simplenote
Exec=/opt/Simplenote/simplenote %U  to Exec=/opt/Simplenote/simplenote --no-sandbox %U in /usr/share/applications/simplenote.desktop
```

* enable slack share
```sh
sudo nano /usr/share/applications/slack.desktop
Exec=/usr/bin/slack -s --enable-features=WebRTCPipeWireCapturer %U
```

* loging in 1passworf
```sh
op account add --address my.1password.com --email waleedmeselhy@gmail.com
eval $(op signin)
```