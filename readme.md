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




```
systemctl enable fprintd.service
systemctl start fprintd.service
sudo fprintd-enroll waleed
```


sudo linux-enable-ir-emitter configure
EDITOR=editor sudo howdy config # edit device_path to what we get from "v4l2-ctl --list-devices"


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

* enable docker
```
sudo systemctl start docker.service
sudo systemctl enable docker.service
sudo usermod -aG docker ${USER}
```