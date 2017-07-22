# Instagram followers scraper

A tool to scrape the list of followers and people following a user and see the difference with a previously recorded list.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [TODO](#todo)

## Requirements

You need to have Python 3 and PIP installed. You can follow [these installation instructions](http://python-guide-pt-br.readthedocs.io/en/latest/starting/install/osx/).

Also, you'll need your Instagram credentials to log in. At this time the dialog with the list of followers cannot be opened as an anonymous user.


## Installation

Download this project manually or clone the repo with git:

```bash
git clone git@github.com:frabonomi/instagram-followers-scraper.git
```

Then go to the directory and install the required dependencies

```bash
cd instagram-followers-scraper
pip3 install -r requirements.txt -q
```

## Usage

After installing the dependencies run the `main.py` file with Python 3:

```bash
python3 main.py
```

## TODO

- Speed up scraping of the users. Right now scraping is quite slow and can be improved
- Handle wrong credentials or missing username
