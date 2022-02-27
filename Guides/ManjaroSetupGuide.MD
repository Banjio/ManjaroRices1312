# Manjaro Tips and Tricks 

# Installation Guide

* Use balena etcher to burn the iso on an usb
* If you do not want to use UEFI you have to disable safe boot or otherwise after installation manjaro wont boot

# 1 KDE

Tips ans trickes for Manjaro KDE

## 1.1 Package Manager

Update Manjaro and select fastest mirror
    
    > sudo pacman --fasttrack && sudo pacman -Syyu
    

Arch has a large repository for "inoficial" software called **AUR**. For install from AUR the following package is needed:

    > sudo pacman -S base-devel

If you want to install packages from AUR in the same manner as with pacman, an additional package manager is needed. **Yay** works fine for me. Install it with:

    > sudo pacman -S yay

Install packages from AUR with

    > sudo yay -a "AURPkgName"

Another option is to install **AUR** packages with the *base-devel* package directly:

    > git clone "addressToRepo" && cd ToGitRepo && makepkg -si
    
Another good Package manager is **paru** 

### 1.2.1 General Settings for Pacman

Edit the pacamn Conf 

> sudo nano /etc/pacman.conf 

Add the following lines (if not already in the conf)
```
Color
ParallelDownload=5
```


## 1.2 Various useful commands 

* Logout from KDE Session  `> loginctl terminate-user "your usrname"`
* Bug on BSPWM prevents vscode from correctly closing, but it is not apprearing anywhere in the opened processes -> Use `> code -r` to open existing vscode instances
* Deactivating Splash Screen https://archived.forum.manjaro.org/t/solved-disable-splash-screen-at-boot/89868

**Trouble with nvidia graphic card**

* On my older pc i have a nvidia card which is not supported by newer drivers.
* To downgrade use `sudo mhwd -a pci nonfree 0300` selecting the correct version for you
* It may be neccessary to remove the existing driver first `sudo mhwd -r pci`
  
## 1.3 Ricing with BSWPM (optional)

The following software is used for my bswpm setup:

* **Conky**: As system monitor 
* **Rofi**: For Window switching and programm starter
* **Sxhkd**: For shortcut settings
* **bswpwm**: As window manager
* **Plasma**: All tasks the window manager is not fulfilling (Bars, symbols, ...)
* **Picom**: Compositor for bluring effects, because kwin is also the compositor in KDE. 
  
Use the dotfiles and Scripts from this repository https://github.com/Banjio/ManjaroRices1312/tree/main/kde-plasma-bspwm

More information on how to run Plasma with Bspwm is found in this tutorial https://www.christitus.com/bspwm-on-kde/

Install the software needed with: 

    > sudo pacman -S bspwm rofi kitty conky sxhkd picom

* Move all config files from the repository to ~/.config/
* Add a file to /usr/share/xsessions/ named plasma-bspwm.desktop with the Content
```
[Desktop Entry]
Type=XSession
Exec=env KDEWM=/usr/bin/bspwm /usr/bin/startplasma-x11
TryExec=/usr/bin/startplasma-x11
DesktopNames=KDE
Name=Plasma bspwm
```

### Additional Information for the used software 

**Conky**

* Take config from dotfiles -> If it is not workings as extended run conky in Debug Mode `conky -D`
* Note that it may be neccessary to remove the conky call from bspwmrc

**Rofi**

* Basicially needs no extra config (But you can also configure it to your wishes)
  * As runer: `rofi -show run -theme sidebar -show-icons`
  * As Druner: `rofi -show drun -theme sidebar -show-icons`
  * As windows switcher:`rofi -show window -theme sidebar -show-icons`

**Change Wallpaper**

* Not working on BSWPM with plasma
* Workaround is to change the wallpaper in an Plasma Session (Or use a manage for example feh)

**Picom**

* Needed for bluring, transparency ... effects. Because kwin does both the window management and the compositing you need an own compositor. Picom works just fine. 
  * Install: `sudo pacman -S picom`
  * Start with bspwm:  Add to bswpmrc &Rightarrow; exec picom -b


## 1.X Reference install all packages at once, which i usually have on the System

* Packages i always install: 

```
sudo pacman -S doublecmd-gtk2 vivaldi pycharm-community-edition base-devel yay chromium htop
```
* All AUR Packages: 

```
yay -a visual-studio-code-bin spotify
```

# 2 Community Edition XFCE with i3

## 2.1 Ricing

This tutorial has some nice additional ressources for i3 additionally for ubuntu, but should also work on arch https://github.com/alec-kr/i3-rice or https://github.com/steelvelveteen/i3_dotfiles (which is more targeted on arch)

* Polybar: A nicer status bar than i3-status (yay install polybar from AUR)
  * For some icons font-awesome needs to be downloaded: `yay ttf-font-awesome`
* i3-gaps -> Not needed on manjaro-i3 (already installed)
* kitty: Terminal emulator `sudo pacman -S kitty` -> Use the kitty.conf from the first rice
* rofi: Replacement for dmenu (Application Launcher i.e. mod+d) `sudo pacman -S rofi` &Rightarrow; https://wiki.archlinux.org/title/Rofi (Then copy the config files from the second rice) &Rightarrow; Binding does not work right now need to find error -> Error was double binding of mod+d
  * Exec command: `rofi -show drun -theme sidebar -show-icons`
  * Exec command windows switcher:`rofi -show window -theme sidebar -show-icons`

### ZSH
* zsh/ oh-my-zsh (Manjaro comes preinstalled with zsh you just have to set it as default )
* Set as default `sudo chsh -s zsh`
* Install oh-my-zsh for arch https://github.com/ohmyzsh/ohmyzsh
* Many themes require the powerline fonts to be installed https://github.com/powerline/fonts  (which is already installed on manjaro)

### Additional Information
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


# 3 Packages

## Developing

__Editors/IDES__:
* **VSCODE**: `pacman -S code` Because i use setting sync we need to use the AUR binary https://aur.archlinux.org/packages/visual-studio-code-bin/
* **Pycharm**: `pacman -S pycharm-community-edition` or from snap https://snapcraft.io/install/pycharm-community/arch

__Languages__: 

* Rust: `curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh`

## Multimedia

* **Spotify**: AUR only for arch. Because of a wrong GPA key consider using makepkg -si --skip-checksums
* **Telegram**: 

## Browsers

I prefer chromium based browser because of the working netflix 1080

* **Vivaldi** `pacman -S vivaldi vivaldi-ffmpeg-codecs`
* **Firefox** `pacman -S firefox`
* **Chromium** `pacman -S chromium`

### File Management

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
