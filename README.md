# English to Hangul

English sentence to naturally-sounding (augmented) Hangul notation.

  
## Installation
 
1. Download or clone this repository.
2. Type `make` in the root directory. (`sudo` required)

## How to Use

 * As a standalone program: `$ eng-to-hangul "<english-sentence-here>"`
 * As a Python package: `import eng_to_hangul`

## What is "Augmented" Hangul?

(TBD. See https://gwangmu.medium.com/extending-hangul-for-english-70e8be3fc6ef in the meantime)

## TODO

 - Write "What is augmented Hangul?"
 - Improve the handling of pronunciation variations.
 - Support the preferred ways of some pronunciations.
 - Package the repository more nicely. (Help needed!)
    - Installing non-`pip` dependencies (e.g., `python3-tk`, `python3-pil.imagetk`, and `UnDotum`)
    - Printing post-install messages after installation. (in `setup.py`)
    - Uploading this repository to a Python package manager.
