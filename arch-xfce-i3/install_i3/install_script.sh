pacman-mirrors --fasttrack
pacman -Syyu
pacman -Sy $(cat install_pacman.txt)
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si
cd ..
paru -S $(cat install_aur.txt)
