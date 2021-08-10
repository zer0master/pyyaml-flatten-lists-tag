# just can't escape it, can we?
#
PACKAGE_DIR := dist

.PHONY: \
	help \
	test \
	clean \
	build

build: test
	@python3 -m build

clean:
	@rm -Rf ${PACKAGE_DIR}/*

# probably cleaner way to do this...
test:
	@python3 -m unittest -v \
		tests.test_attrs \
		tests.test_load

# show available targets
help:
	@awk '/^[-a-z]+:/' Makefile | cut -f1 -d\  | sort
