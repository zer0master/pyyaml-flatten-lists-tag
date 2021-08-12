# just can't escape it, can we?
#
TWINE_CMD := python3 -m twine
PACKAGE_DIR := dist
PACKAGE_NAME := flatten_lists_tag_zer0master
# probably handle this differently later
VERSION := 0.1

.PHONY: \
	help \
	test \
	clean \
	build

# figure out once and for all how to create dependencies for things like this
build: test
	@python3 -m build

clean:
	@rm -Rf ${PACKAGE_DIR}/*

# probably cleaner way to do this...
test:
	@python3 -m unittest -v \
		tests.test_attrs \
		tests.test_load
	@touch .tested

checkvars:
	$(if $(TWINE_REPOSITORY_URL),,$(error TWINE_REPOSITORY_URL not set))
	$(if $(TWINE_USERNAME),,$(error TWINE_USERNAME not set))
	$(if $(TWINE_PASSWORD),,$(error TWINE_PASSWORD not set))

register: checkvars
	@${TWINE_CMD} register \
		--verbose \
		${PACKAGE_DIR}/${PACKAGE_NAME}-${VERSION}.tar.gz

check:
	@${TWINE_CMD} check ${PACKAGE_DIR}/*

upload: checkvars 
	@${TWINE_CMD} upload \
		--repository-url ${TWINE_REPOSITORY_URL} \
		--username ${TWINE_USERNAME} \
		--password ${TWINE_PASSWORD} \
		--verbose \
		${PACKAGE_DIR}/*

# show available targets
help:
	@awk '/^[-a-z]+:/' Makefile | cut -f1 -d\  | sort
