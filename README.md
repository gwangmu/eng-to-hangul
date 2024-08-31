# English to Hangul

English sentence to naturally-sounding (augmented) Hangul notation.

## Requirement

 - For `convert`
     - Python 3
     - `eng-to-ipa` Python package
 - For `draw`
     - `matplotlib` Python package
     - `TkAgg` Pyplot backend
     - `UnDotum` font
  
## Installation

<details>
  <summary>Click here for details.</summary>
 
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

</details>

## How to Use

 * As a Standalone Program: `$ ./eng-to-han "<english-sentence-here>"`
 * As a Python package: `import <name-of-this-repo-dir>`

## What is "Augmented" Hangul?

(TBD. See https://gwangmu.medium.com/extending-hangul-for-english-70e8be3fc6ef in the meantime)

## TODO

 - Fine-tune the position of consonant annotations.
