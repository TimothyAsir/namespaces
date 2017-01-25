NAME=namespaces
VERSION=4.2.0
RELEASE=1
COMMIT := $(shell git rev-parse HEAD)
SHORTCOMMIT := $(shell echo $(COMMIT) | cut -c1-7)
GIT_RELEASE := $(shell git describe --tags --match 'v*' \
                 | sed 's/^v//' \
                 | sed 's/^[^-]*-//' \
                 | sed 's/-.*//')

all: srpm

clean:
	rm -rf dist/
	rm -f $(NAME)-$(VERSION).tar.gz
	rm -rf $(NAME)-$(VERSION)-$(RELEASE).el7.src.rpm

dist:
	python setup.py sdist \
	  && mv dist/$(NAME)-$(VERSION).tar.gz .

srpm: dist
	fedpkg --dist epel7 srpm

rpm: dist
	mock -r epel-7-x86_64 rebuild $(NAME)-$(VERSION)-$(RELEASE).el7.src.rpm --resultdir=. --define "dist .el7"

.PHONY: dist rpm srpm
