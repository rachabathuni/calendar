all: clean
	mkdir -p build
	cp calendar.html build/index.html
	cp images/favicon.png build/
	mkdir -p build/data
	cp data/holidays.json build/data/

clean:
	rm -rf build


