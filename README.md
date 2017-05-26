# CWKuemmerlingClock
Kuemmerling clock with ws2812 LEDs

## Install neopixel
sudo apt-get update
sudo apt-get install build-essential python-dev git scons swig

git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons

cd python
sudo python setup.py install

## Disable Audio Device
cd /etc/modprobe.d
sudo nano alsa-blacklist.conf

add blacklist snd_bcm2835 to the file.
save it

sudo reboot
