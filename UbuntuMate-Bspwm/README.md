# Ubuntu Mate with BSWPM 
Tutorial: https://github.com/windelicato/dotfiles/wiki/bspwm-for-dummies


## Install Base packages

`sudo apt install bswpm sxhkd rofi`

## Create Config files 

* Use dot files from KDE Bswpm example. Note that the . directory is the directory of the Github Repository.
  * **BSPWM**: mkdir  ~/.config/bspwm && cp ./kde-plasma-bspwm/bspwm ~/.config/bspwm && chmod +x ~/.config/bspwm/bspwmrc
  * **SXHKD**: mkdir  ~/.config/sxhkd && cp ./kde-plasma-bspwm/sxhkd ~/.config/sxhkd && chmod +x ~/.config/bspwm/sxhkdrc
  * **Rofi**: mkdir  ~/.config/rofi && cp ./kde-plasma-bspwm/rofi ~/.config/rofi && chmod +x ~/.config/bspwm/config.rasi

## Edit Xsession File

* To be able to create a unique session for bswpm (This has the big advantage tha we can switch between the windo managers) we have to add the following file: 
* `touch /usr/share/xsessions/bspwm.desktop`. After installing bspwm on ubuntu it sometimes is already created. Then we only have to edit the file so that it is executed correctly 
* Add the following to the file:

```bash
[Desktop Entry]
Type=XSession
Exec=/usr/bin/bspwm
DesktopNames=MATE
Name=Plasma Ubutuntu Mate with bspwm
Comment=See https://www.christitus.com/bspwm-on-kde/
```
