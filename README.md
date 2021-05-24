
# Text to handwriting
> I tried make a program to transform text to handwriter.

I'm want make this program because, want **don't need writer in notebook** more, only in laptop ;)
I know it's be very basic, but still learning Python, so forgive my errors ;)
It's be better than I thinking.
Support **Windows 10** (maybe old versions) and **Linux** distributinos.
![](img/header.png)

## Setup dependencies

**Linux:**
On **terminal** using **Python3** on **debian-based** systems (can be applied in others distributions) with no user root logged, **execute this** commands.
```sh
sudo apt install python3 python3-pip
sudo pip3 install pywhatkit pysimplegui
```
**Windows:**
On **powershell** before install **python3** interpreter with graphical installer and add python to your path (maybe in the installation has been added to your path), **execute this** commands.
```sh
pip3 install pywhatkit pysimplegui
```

## Usage example

Before install dependencies, **execute this** command to run the program.
```sh
python3 handwriter.py
```
In the **window** and if it appears **put your text** that you want to transform **into the manuscript** and click on the button below. After clicking on the "Ok" button in the popup, wait for the window to close automatically. And **verify** the **program directory or desktop** directory to find your **image with converted manuscript text.**

## Release History

* 1.1.0
    * added compatibility with linux; timestamp on images archives; modified instructions texts.

## Meta

Diego Luide – [@DiegoLuide](https://twitter.com/diegoluide)
deAssis Filho - [@deAssisFilho](https://instagram.com/deassisfilhu)

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/DiegoLuide/Text-to-handwriter](https://github.com/dbader/)

## Contributing

1. Fork it (<https://github.com/DiegoLuide/Text-to-handwriter/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
