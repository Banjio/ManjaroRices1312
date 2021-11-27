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

#### base-devel


For installing any package from AUR do `sudo pacman -S base-devel`

### 1.2 Install needed packages

* Packages i always install: `sudo pacman -S doublecmd-gtk2 vivaldi pycharm-community-edition base-devel yay`
* Bspwm packages in one go `sudo pacman -S bspwm rofi kitty conky sxhkd picom`
* All AUR Packages: `yay -a visual-studio-code-bin`

### 1.3 Ricing (optional)

* Select best mirror & Update System: `sudo pacman-mirrors --fasttrack && sudo pacman -Syyu`
* It may be neccessary to change the nvidia driver afterwards (For some reason this breaks --> see misco  on how to do that)

#### 1.1 bspwm

Using the guide provided from lukas we start with this: https://www.christitus.com/bspwm-on-kde/ and the dotfiles are provided here https://github.com/Banjio/ManjaroRices1312/tree/main/kde-plasma-bspwm
* Install bswpm: `sudo pacman -S bspwm`
* Install sxhkd and rofi for hotkeys and druner  `sudo pacman -S sxhkd rofi`
* Install picom (Optional but needed for kitty and transparency): `sudo pacman -S picom`
* After adding the config files we need to add an xsession so that we can login into kde-plasma-bspwm:
  * Add a file to /usr/share/xsessions/ named plasma-bspwm.desktop with the Content
```
[Desktop Entry]
Type=XSession
Exec=env KDEWM=/usr/bin/bspwm /usr/bin/startplasma-x11
TryExec=/usr/bin/startplasma-x11
DesktopNames=KDE
Name=Plasma bspwm
```
* Make Konsole transparent: https://askubuntu.com/questions/189487/how-do-i-configure-background-transparency-for-kdes-terminal

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


##### Deactivating Splash Screen


#### Getting a compositor

* Needed for bluring, transparency ... effects. Because kwin does both the window management and the compositing you need an own compositor. Picom works just fine. 
  * Install: `sudo pacman -S picom`
  * Start with bspwm:  Add to bswpmrc &Rightarrow; exec picom -b


#### XXX

Make your os look nice. We will install the following packages

* latte-dock: A mac like dock for KDE


```
sudo pacman -S latte-dock konsole
```

#### Developing

#### Editors/IDES
* VSCODE:  `pacman -S code` Because i use setting sync we need to use the AUR binary https://aur.archlinux.org/packages/visual-studio-code-bin/
* Pycharm: `pacman -S pycharm-community-edition` or from snap https://snapcraft.io/install/pycharm-community/arch
* typora: m


### 1.3 Standard Settings

* Change do dark desing, change shortcuts (TODO: Find shortcut for swithcing between workspaces)

#### X MISC

**Trouble with nvidia graphic card**

* On my older pc i have a nvidia card which is not supported by newer drivers.
* To downgrade use `sudo mhwd -a pci nonfree 0300` selecting the correct version for you
* It may be neccessary to remove the existing driver first `sudo mhwd -r pci`


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
