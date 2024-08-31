# English to Hangul

English sentence to naturally-sounding (enhanced) Hangul notation.

## Requirement

 - For `convert`
     - Python 3
     - `eng-to-ipa` Python package
 - For `draw`
     - `matplotlib` Python package
     - `TkAgg` Pyplot backend
     - `UnDotum` font
  
## Installation

1. **Install dependencies.** Assuming Ubuntu 22.04,
```
$ # For 'convert'
$ sudo apt install python3 pip
$ sudo pip install eng-to-ipa
$ # For 'draw'
$ sudo pip install matplotlib
$ sudo apt install python3-tk python3-pil.imagetk
$ sudo apt install fonts-unfonts-core
```

2. **Download this repository.** You may clone this repository or download it as an archive (zip).

## How to Use

### As a Standalone Program

Type this command on the downloaded directory to convert English sentences. Use `-h` for available flags.
```
$ ./eng-to-han "<english-sentence-here>"
```

### As a Python Package

Import the downloaded directory after placing it somewhere appropriate in your Python project.
```
import <name-of-this-repo-dir>
```
Two API methods are available: `convert` and `draw`. See `interface.py` for the signatures.

## What is "Enhanced" Hangul?

(TBD. See https://gwangmu.medium.com/extending-hangul-for-english-70e8be3fc6ef in the meantime)

## TODO

 - Fine-tune the position of consonant annotations.
