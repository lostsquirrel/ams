SHELL=/bin/bash

VERSION=$(shell echo `git describe --abbrev=0 --tags`)
VERSION_TAG=$(VERSION)
REGISTRY=registry.cn-hangzhou.aliyuncs.com
IMAGE=$(REGISTRY)/lisong/ams
VERSIONED_IMAGE=$(IMAGE):$(VERSION_TAG)

export VERSION
export VERSIONED_IMAGE


push:
	docker push $(VERSIONED_IMAGE)

pull:
	docker pull $(VERSIONED_IMAGE)

build: code
	docker build --no-cache -t $(VERSIONED_IMAGE) .

restart:
	docker-compose restart

clean:
	docker-compose down
	docker-compose rm --force

code:
	git pull

update:
	git pull
up:
	docker-compose up -d

.PHONY: build clean  push up
