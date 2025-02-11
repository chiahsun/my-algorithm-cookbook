#!/usr/bin/env bash

VERSION=10.7.3

mkdir -p languages
mkdir -p styles

curl -LO "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/$VERSION/highlight.min.js"
(cd languages && curl -LO "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/$VERSION/languages/python.min.js")
(cd styles && curl -LO "https://cdnjs.cloudflare.com/ajax/libs/highlight.js/$VERSION/styles/night-owl.min.css")
