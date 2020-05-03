# Snake game

Simple snake game written in Python 3.8 for Linux Terminal

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system. 


### Prerequisites

What things you need to install the software and how to install them

```
pip install -r requirements.txt
```
Required libs: 
-keyboard


## Running the tests

More tests will be made, but you can run current ones by: 
```
cd tests
sudo python test_main.py
```

### Break down into end to end tests

These tests help to keep track on what program is doing, for example: 

```
    def test_inital_create_board(self):
        board_1 = [["□", "□", "□"], ["□", "□", "□"], ["□", "□", "□"]]
        self.assertEqual(board_1, self.board_1.board)

        board_2 = []
        self.assertEqual(board_2, self.board_2.board)
```
Allow us to check if board is printing in the right way


## Run live version

After you've cloned the repo, you can simply run: 
```
sudo python main.py
```
Unfortunetly, on Linux you need to run program with root privileges, because keyboard lib needs it. 



## Authors

* **Grzegorz Bednarski** - *Initial work*

