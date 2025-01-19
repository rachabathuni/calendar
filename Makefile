all: clean
	mkdir -p build
	cp calendar.html build/index.html
	cp images/favicon.png build/
	cp data/holidays.csv build/

clean:
	rm -rf build


