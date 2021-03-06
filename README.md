## Disclaimer
If you want to get know my technical skills better, take a look at this repository: https://github.com/grzesiekdev/indeed_scraper

# Snake game

Simple snake game written in Python 3.8 for Linux Terminal. My main goal was to keep it away from big libraries like curses, pygame, or even tkinter. I've tried to make it working in terminal, and i think that i've achieved that. 
![Sample snake game in Ubuntu terminal](https://i.imgur.com/UCZUd7r.png)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See 'Run live version' for notes on how to deploy the project on a live system. 


### Prerequisites

What things you need to install the software and how to install them

```
pip install -r requirements.txt
```

## Running the tests

```
cd tests
sudo python test_main.py
```

## Run live version

After you've cloned the repo, you can simply run: 
```
sudo python main.py
```
Unfortunetly, on Linux you need to run app with root privileges, because keyboard lib needs it. 


You can change size of board and snake speed by changing following line in _main.py_ 
```
    board_obj = Board(15, 7, 0.3)  # Set: width, height, speed
```

## Authors

* **Grzegorz Bednarski** - *Whole project*

