all:
	sudo pip install .
	sudo rm -r build *.egg-info

dep-ubuntu:
	sudo apt install python3-tk python3-pil.imagetk fonts-unfonts-core
	rm -f ~/.cache/matplotlib/font*.json

uninstall:
	sudo pip uninstall -y eng_to_hangul
