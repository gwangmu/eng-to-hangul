all:
	sudo pip install .
	sudo rm -r build *.egg-info

uninstall:
	sudo pip uninstall -y eng_to_hangul
