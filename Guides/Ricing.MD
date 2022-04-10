## 1 Ricing with BSWPM (optional)

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


## 2 Ricing i3

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

## I3-gaps besides KDE

1. __First__ we need to install i3-gaps `sudo paru -S i3-gaps`
2. Next we need to add i3 as session to kde so that we can select it on login screen
   1. Create a file called i3-with-plasma.desktop
   2. Add the following
      ```
      [Desktop Entry]
      Name=i3
      Comment=improved dynamic tiling window manager
      Exec=i3
      TryExec=i3
      Type=Application
      X-LightDM-DesktopName=i3
      DesktopNames=i3
      Keywords=tiling;wm;windowmanager;window;manager;
      ```
3. Before the first start of i3 you have to atleast create a default config file. We use the one provided in this repo.

### Install additional software

* We use rofi as starter

# General Tips

* Using multiple ttys (You can imagine a tty as multiple virtual consoles that each start their own headless linux session when activated) can help to debug problem when logging in over the default logging manager (sddm in manjaro kde) &Rightarrow; Starting a tty is usually down by using the shortcut `strg+alt+F2(3/4/...)` where each fkey starts the corresponding session, e.g. F2 starts session 2, F3 session 3 and so on. 
* When you have terminal access `loginctl list-sessions` shows all sessions currently running on the machine (In general loginctl is a very useful tool to terminate sessions or all sessions owned by users, call `loginctl --help` or man loginctl to see the problems)
* Additionally what can help when you want to add a window manager to an existing installation (e.g. manjaro kde)is to create a "clean environment" with a new user that can be then be configured testwise before you use your main user and break something
  1. (Sudo access needed): Add new user `$ sudo useradd -m username` with a home directory
  2. Create passwd for this user: `$ sudo passwd username`
  3. More information can be found here: https://linuxize.com/post/how-to-create-users-in-linux-using-the-useradd-command/ 