# -------------------------------------
# MAKEFILE
# -------------------------------------

# settings

DOCKER_IMAGE ?= fenix-sdk-demo

DOCKER ?= docker


# default

.PHONY: all
all: build run


# build

.PHONY: build
build:
	${DOCKER} build --force-rm . --tag ${DOCKER_IMAGE}


# run

VOLUME = -v ${PWD}/:/usr/demo
ENVIRONMENT = -e FENIX_API_KEY

.PHONY: run
run:
	${DOCKER} run --rm ${VOLUME} ${ENVIRONMENT} -ti ${DOCKER_IMAGE} python -m demo


# clean

.PHONY: clean
clean:
	rm -rf __pycache__
	${DOCKER} rmi ${DOCKER_IMAGE}
