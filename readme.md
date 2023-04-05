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
    
```
systemctl enable fprintd.service
systemctl start fprintd.service
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


* configure nvm
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
nvm use 18
nvm install 18
npm install --global yarn 
```

* enable docker
```
sudo systemctl enable docker.service
sudo systemctl start docker.service
sudo usermod -aG docker ${USER}
```

* configure zsh plugins
```
sudo chown waleed:waleed -R /usr/share/oh-my-zsh/custom
git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-completions
git clone git@github.com:jscutlery/nx-completion.git ${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/nx-completion
git clone https://github.com/Aloxaf/fzf-tab ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/fzf-tab
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
```

* configure tmux
```
git clone https://github.com/gpakosz/.tmux.git
ln -s -f .tmux/.tmux.conf
cp .tmux/.tmux.conf.local .
```

* configure zsh autocomplete
```
rm -f /home/waleed/.config/zsh/.zcompdump*; compinit
```

* configure tlp
```
sudo systemctl enable tlp.service
sudo systemctl mask systemd-rfkill.service
sudo systemctl mask systemd-rfkill.socket
sudo systemctl start tlp.service
```

* configure font
```
fc-cache -v
```


* configure fstrim
```
sudo systemctl enable fstrim.timer
sudo systemctl start fstrim.timer
```

* fix simplenote
```
# fix simplenote
Exec=/opt/Simplenote/simplenote %U  to Exec=/opt/Simplenote/simplenote --no-sandbox %U in /usr/share/applications/simplenote.desktop
```

* enable slack share
```
sudo nano /usr/share/applications/slack.desktop
Exec=/usr/bin/slack -s --enable-features=WebRTCPipeWireCapturer %U
```