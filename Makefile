all: out normal social favicon

out:
	mkdir -p out

normal:
	# ----------------
	python3 logo.py 90 10 5 > out/osecz.svg
	# ----------------
	inkscape -z -e $$PWD/out/osecz.png $$PWD/out/osecz.svg
	# ----------------

social:
	# ----------------
	python3 logo.py 180 20 10 > out/osecz-xpad.svg
	# ----------------
	inkscape -z -e $$PWD/out/osecz-xpad.png $$PWD/out/osecz-xpad.svg
	# ----------------

favicon:
	# ----------------
	python3 logo.py 93 14 0 > out/favicon.svg
	# ----------------
	inkscape -z -e $$PWD/out/favicon.png $$PWD/out/favicon.svg

clean:
	rm *.svg *.png
