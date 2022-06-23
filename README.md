# XKCD Inspired Code

Some comic strips deserve more than a simple smirk.

![random-output](imgs/xkcd1930_calendar-facts_statement.jpg)


## Source of Inspiration
The code implemented herein was motivated by xkcd's [comic 1930](https://xkcd.com/1930/).
Munroe shows how one could generate random and absurd calendar "facts" using a
flowchart. This repository implements a Python-implementation of a script generating
calendar facts based on the strip's flowchart.

![origin](https://imgs.xkcd.com/comics/calendar_facts.png)


## Implementation
The code is written in Python3 and tested with Python 3.8.7. The main (and only)
script to be run is `xkcd1930.py`. Running
```bash
./xkcd1930.py
```
Will output 10 calendar facts to the std-out and generate a JPG of the last generated fact.
The image will be stored in `imgs/` and is included at the beginning of this README. There is one
third-party dependency namely `matplotlib` which is used to draw the image.

Unit-tests and linting can be run with
```bash
./x/run_tests.sh
./x/run_linting.sh
```
respectively.

`Pydoc`-generated documentation is found in `doc/` and can be generated calling
```bash
./x/generate_doc.sh
```

**Configuration** options are set in the files found in the subdirectory `config/`. In particular
`config/config.json` can be modified to change the script's behavior. You may modify this at your
own risk.
