all: out logo bright favicon

out: FORCE
	rm -rf out
	mkdir out

logo:
	# ----------------
	python3 logo.py 180 20 10 '#ec0304' '#028902' '#166bff' > out/osecz.svg
	# ----------------
	inkscape -z -e $$PWD/out/osecz.png $$PWD/out/osecz.svg
	# ----------------

bright:
	# ----------------
	python3 logo.py 180 20 10 '#ff6657' '#02b102' '#129dff' > out/osecz-bright.svg
	# ----------------
	inkscape -z -e $$PWD/out/osecz-bright.png $$PWD/out/osecz-bright.svg
	# ----------------

favicon:
	# ----------------
	python3 logo.py 93 14 0  '#ec0304' '#028902' '#166bff' > out/favicon.svg
	# ----------------
	inkscape -z -e $$PWD/out/favicon.png $$PWD/out/favicon.svg

clean:
	rm *.svg *.png

FORCE:
