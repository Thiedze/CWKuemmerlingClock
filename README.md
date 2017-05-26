# CWKuemmerlingClock
Kuemmerling clock with ws2812 LEDs

# Install neopixel
sudo apt-get update
sudo apt-get install build-essential python-dev git scons swig

git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons

cd python
sudo python setup.py install
