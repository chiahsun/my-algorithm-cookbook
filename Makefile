.PHONY: build view 

all: build view

highlight/highlight.min.js:
	cd highlight && ./download.sh

build: dark.css highlight/highlight.min.js
	asciidoctor -a stylesheet=dark.css -a highlightjsdir=highlight -v -t index.adoc

view:
	open index.html


dark.css:
	curl -LO https://github.com/darshandsoni/asciidoctor-skins/raw/gh-pages/css/dark.css
