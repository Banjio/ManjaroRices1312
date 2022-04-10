# 0 Installation

I for myself usually alwayse use the Manjaro KDE https://manjaro.org/downloads/official/kde/ version. Because for me i like the feature richness of kde but the ease of use of manjaro plus the rolling release model.

## Installation Steps

### Partitioning

* Apart from Partitioning the installation using the manjaro installer is straight forward. As partitioning scheme is use a btrfs filesystem. When using btrfs an efi partition is neede mounted at /boot/efi with mark boot.
* Secure boot must be disabled
* A extensive guide on btrfs with arch is found here https://wiki.archlinux.org/title/btrfs

# 1 Configuration and Packages

## 1.1 Package Manager

Update Manjaro and select fastest mirror

	> sudo pacman-mirrors --fasttrack

Afterwards a full system update is recommended:

	> sudo pacman -Syyu

Arch has a large repository for "inoficial" software called **AUR**. To install packages from AUR the different approaches are feasbible:

1. Cloning the repository from AUR and compiling the package using makepkg. Fur this purpose inside cloned AUR repo do

		> makepkg -si

Note that no root user is neede for this and makepkg can be installed with the package **base-devel**.

2. A more convenient way is to use a package manager that has AUR incorporated. I recommend paru or yay. yay can be found in the official repos (`using sudo pacman -S yay`). Paru needs to be installed from AUR

		> git clone https://aur.archlinux.org/paru.git && cd paru && makepkg -si

As of now this does yield an error because rust needs to be configured using

	> rustup update stable && rustup default stable

Sometimes packages updates are lagging a little bit behind the official pacman repositories (The reason ist that manjaro takes itself some time to test the updates which result in a more stable experience compaired to vanilla arch). Thus if you are dependent on a new package and cannot wait you can change the upstream mirror 

	$ sudo pacman-mirrors --api --set-branch testing 
	
After that reset the mirror list and update 

	$ sudo pacman-mirrors --fasttrack && pacman -Syyu


### 1.1.1 General Settings for Pacman

Edit the pacaman Conf

	> sudo nano /etc/pacman.conf

Add the following lines (if not already in the conf)
```
Color
ParallelDownload=5
```

Additionally BottomUp can be uncommented when using paru in /etc/paru.conf

This greatly increases the download speed and make the console output more readable

## 1.2 Typical packages on my system

### 1.2.1 File Explorer

I prefer doublecommander

	> sudo pacman -S doublecmd

#### Configure

* **Show hidden files**: `Configuration > Fileview > Show hidden and system files`

### 1.2.2 Terminal Emulator and shell

**Shell**

I prefer zsh over bash, because zsh has a great tool called oh-my-zsh https://github.com/ohmyzsh/ohmyzsh. This enhances zsh by a lot of tools. In newer manjaro kde versions zsh is the standard tool. The github link provides a good installation guide for both zsh and oh-my-zsh.

**Terminal Emulator**

I prefer one of **kitty, terminator** or the standard terminal installed in manjaro kde **konsole** all can be installed from the official repositories

## 1.2.3 Developing

__Editors/IDES__:
* **VSCODE**: `pacman -S code` Because i use setting sync we need to use the AUR binary https://aur.archlinux.org/packages/visual-studio-code-bin/
* **Pycharm**: `pacman -S pycharm-community-edition` or from snap https://snapcraft.io/install/pycharm-community/arch
* **Micro**: An lightweight terminal editor https://micro-editor.github.io/ `pacman -S micro`
* **R-Studio**: The best ide for Rlang `paru -S rstudio-desktop` 

__Languages__:

* Rust: `curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh`

### 1.2.4 Multimedia

* **Spotify**: AUR only for arch. Because of a wrong GPA key consider using makepkg -si --skip-checksums
* **Telegram**:

### 1.2.5 Browsers

I prefer chromium based browser because of the working netflix 1080

* **Vivaldi** `pacman -S vivaldi vivaldi-ffmpeg-codecs`
* **Firefox** `pacman -S firefox`
* **Chromium** `pacman -S chromium`

### File Management

# 2. Known Problems

## Bluemann

__Problem__: Not working by default -> Ressource not available Error message
__Solution__:

## Nvidia Drivers

## Visual Studio Code

Depending on the version your using, the setting sync is no longer working (Apparently this is also the case in the newest version for code-bin). Then use the extension

	> ext install Shan.code-settings-sync

### Solution for Binary packages

Install 

	> -S gnome-keyring libsecret libgnome-keyring   

Additionally xdg-utils may be neccessary which is not installed on all manjaro installations

**Trouble with nvidia graphic card**

* On my older pc i have a nvidia card which is not supported by newer drivers.
* To downgrade use `sudo mhwd -a pci nonfree 0300` selecting the correct version for you
* It may be neccessary to remove the existing driver first `sudo mhwd -r pci`

If this does not help try: I have an older graphic card and thus had to downgrad the driver for a more stable experience (Go to manjaro settings and then i choose bumblebee 390 as only other viable option)

## Multi Monitor setup

Because of HDMI add the following to .xinitrc `xrandr --output HDMI2 --auto --right-of eDP1`

## Touchspad gestures

# 99. Common patterns

## Install all preferred packages at once

	> sudo paru -S --needed visual-studio-code-bin spotify vivaldi vivaldi-ffmpeg-codecs firefox pycharm-community-edition chromium htop terminator micro

## Ssh generation

For me i like the trade off between compatibility and usability the most for the ecdsa algorithm:

	> ssh-keygen -t ecdsa -b 521

This guide tells you all you should know https://www.ssh.com/academy/ssh/keygen#choosing-an-algorithm-and-key-size

## Useful commands

* Logout from KDE Session  `> loginctl terminate-user "your usrname"`
* Bug on BSPWM prevents vscode from correctly closing, but it is not apprearing anywhere in the opened processes -> Use `> code -r` to open existing vscode instances
* Deactivating Splash Screen https://archived.forum.manjaro.org/t/solved-disable-splash-screen-at-boot/89868
