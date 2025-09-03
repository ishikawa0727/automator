start:
	python automator.py config.json

pdf:
	python images_to_pdf.py ./images/ -o output.pdf