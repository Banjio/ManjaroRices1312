# From Zero to Manjaro Hero

# Installation Guide

* Use balena etcher to burn the iso on an usb
* If you do not want to use UEFI you have to disable safe boot or otherwise after installation manjaro wont boot
* On my Asus Laptop i cannot find the disabling option

## 1 KDE

Guide for setting up a nice Manjaro KDE Plasma environment.

### 1.1 Package Manager

For starters we use the standard pacman cli tool. The following will select the fastest mirros and do a full system update so that our system is updated.
    ```
    sudo pacman --fasttrack && sudo pacman -Syyu
    ```

Pacman can only install from the official arch repository. If you want to install from unoficial sources use either pamac or download directly from AUR and do `makepkg -si`

#### yay 

Install packages from AUR using yay `sudo pacman -Sy yay`

### 1.2 Install needed packages

#### Ricing (optional)

Make your os look nice. We will install the following packages

* latte-dock: A mac like dock for KDE


```
sudo pacman -S latte-dock konsole
```

#### Developing

#### Editors/IDES
* VSCODE: `pacman -S code`
* Pycharm: `pacman -S pycharm-community-edition` or from snap https://snapcraft.io/install/pycharm-community/arch
* typora: m


### 1.3 Standard Settings

* Change do dark desing, change shortcuts (TODO: Find shortcut for swithcing between workspaces)

## 2 Community Edition XFCE with i3

### 2.1 Ricing

This tutorial has some nice additional ressources for i3 additionally for ubuntu, but should also work on arch https://github.com/alec-kr/i3-rice or https://github.com/steelvelveteen/i3_dotfiles (which is more targeted on arch)

* Polybar: A nicer status bar than i3-status (yay install polybar from AUR)
  * For some icons font-awesome needs to be downloaded: `yay ttf-font-awesome`
* i3-gaps -> Not needed on manjaro-i3 (already installed)
* kitty: Terminal emulator `sudo pacman -S kitty` -> Use the kitty.conf from the first rice
* rofi: Replacement for dmenu (Application Launcher i.e. mod+d) `sudo pacman -S rofi` &Rightarrow; https://wiki.archlinux.org/title/Rofi (Then copy the config files from the second rice) &Rightarrow; Binding does not work right now need to find error -> Error was double binding of mod+d
  * Exec command: `rofi -show drun -theme sidebar -show-icons`
  * Exec command windows switcher:`rofi -show window -theme sidebar -show-icons`

#### ZSH
* zsh/ oh-my-zsh (Manjaro comes preinstalled with zsh you just have to set it as default )
* Set as default `sudo chsh -s zsh`
* Install oh-my-zsh for arch https://github.com/ohmyzsh/ohmyzsh
* Many themes require the powerline fonts to be installed https://github.com/powerline/fonts  (which is already installed on manjaro)

#### Additional Information
__Multi Monitor setup__
* In my current setup there is a bug with xserver and startx with prevents the xrandr code needed for dual Monitor setup to be executed correctly. A quick fix was to write this code into .bashrc or .zshrc. Does after startup a console can be opened and the xrandr command is called. The command used is  
```
con=$(xrandr -q | grep HDMI2 | grep -w -o connected)
if [ $con = 'connected' ]; then
    xrandr --output eDP1 --primary --mode 1920x1080 --rate 120.00 --output HDMI2 --mode 1920x1080 --right-of eDP1
else
    xrandr --output eDP1 --primary --mode 1920x1080 --rate 120.00
fi
```
* You have to change the outputs if you have another device 
### 2.2 Needed Packages

#### Developing

__Editors/IDES__:
* **VSCODE**: `pacman -S code` Because i use setting sync we need to use the AUR binary https://aur.archlinux.org/packages/visual-studio-code-bin/
* **Pycharm**: `pacman -S pycharm-community-edition` or from snap https://snapcraft.io/install/pycharm-community/arch

__Languages__: 

* Rust: `curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh`

### Multimedia

* **Spotify**: AUR only for arch. Because of a wrong GPA key consider using makepkg -si --skip-checksums
* **Telegram**: 

#### Browsers

I prefer chromium based browser because of the working netflix 1080

* **Vivaldi** `pacman -S vivaldi vivaldi-ffmpeg-codecs`
* **Firefox** `pacman -S firefox`
* **Chromium** `pacman -S chromium`

#### File Management

* Doublecommander `pacman -S doublecmd-gtk`
  * Activate show hidden files in Dateiansicht extras

### 2.3 Configuration

### 2.4 Problems

#### Bluemann

__Problem__: Not working by default -> Ressource not available Error message
__Solution__: 

### 2.X Misc  

#### Nvidia Drivers

I have an older graphic card and thus had to downgrad the driver for a more stable experience (Go to manjaro settings and then i choose bumblebee 390 as only other viable option)

#### Multi Monitor setup

Because of HDMI add the following to .xinitrc `xrandr --output HDMI2 --auto --right-of eDP1`

#### Touchspad gestures

#### Package Manegement

See Package Management from KDE

# X Misc

## Vivaldi Browser

# TODOS

* Have to write my own polybar config (Because neither satisfy my needs)