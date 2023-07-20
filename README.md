# Python Minesweeper

This is an implementation in Python of the famous Minesweeper game using the Pygame module.

## How to play

If you don't know the game, you can visit [this link](https://en.wikipedia.org/wiki/Minesweeper_(video_game)).

- To reveal a square, left-click on it.
- To place a flag on a square that is not revealed, right-click on it.
- To clear all unrevealed squares and unflaged squares next to a square that is already revealed and which has the rigth number of flags next to it, left-click on it.

## Installation, test, launch and customize

Warning, note that all the following steps concern Linux distributions. If you have another operating system, you can follow these steps but there will likely be differences.

### Play quickly

If you have a Linux distribution, you can directly launch the compiled file `minesweeper` executing the command `./minesweeper`. This works only for Linux distro (and maybe MacOS) but if you use Windows and want to laucnh the game with a .exe, you will have to compile it yourself following the steps below.

### Test with Python 3

You want to create a virtual environment in order to keep your python installation clean. To do so, install module `virtualenv` globally (see [this link](https://virtualenv.pypa.io/en/latest/) for more informations and help) : 

- For Ubuntu : `sudo apt install python-virtualenv`
- For Arch : `sudo pacman -S python-virtualenv`

At the root of the project, create a new virtual environment in folder `env` using `virtualenv env` and source it using `source env/bin/activate` then install all dependencies using `pip install -r requirements.txt`.

You can now test the game by executing script `main.py` using `python main.py`.

### Compile the game in one file

To compile all the project in one file (as the file `minesweeper`), you can use `pyinstaller` module. To learn more about this module and sea documentaion, follow [this link](https://pyinstaller.org/en/stable/). Install it using `pip` in your virtual environment and use the following command to compile the project in one file : 

```bash
pyinstaller --name minesweeper \
    --windowed -y --clean --onefile \
    --paths env/lib/python3.11/site-packages \
    --add-data "assets:assets" \
    --add-data "src:src" \ 
    main.py
```

You can find the new compiled file in folder `dist` and execute it using `./dist/minesweeper`.

### Customize the game

You can customize the game by modifying file `settings.json`. To see your change, you need to relaunch the game if you lanched it with `python main.py` or to recompiled it if you launched it with `./dist/minesweeper`.