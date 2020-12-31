# 用于创建插件压缩包和编译镜像

VERSION?=$(shell grep '^version: ' plugin.spec.yaml | sed 's/version: //')
NAME?=$(shell grep '^name: ' plugin.spec.yaml | sed 's/name: //')
VENDOR?=$(shell grep '^vendor: ' plugin.spec.yaml | sed 's/vendor: //')
CWD?=$(shell basename $(PWD))
_NAME?=$(shell echo $(NAME) | awk '{ print toupper(substr($$0,1,1)) tolower(substr($$0,2)) }')
PKG=$(VENDOR)-$(NAME)-$(VERSION).tar.gz

.DEFAULT_GOAL := default

default: sync_version image tarball

sync_version:
	sed -i -E "s/^[\s]*Version[\s]*(.*)/Version = \"$(VERSION)\"/g" bin/*
	sed -i -E "s/[\s]*version(.*)/version=\"$(VERSION)\",/g" setup.py

tarball: sync_version
	$(info [$(YELLOW)*$(NORMAL)] Creating plugin tarball)
	rm -rf build
	rm -rf $(PKG)
	tar -cvzf $(PKG) --exclude=$(PKG) --exclude=tests --exclude=run.sh *

image: sync_version
	$(info [$(YELLOW)*$(NORMAL)] Building plugin image)
	docker build --pull -t $(VENDOR)/$(NAME):$(VERSION) .
	docker tag $(VENDOR)/$(NAME):$(VERSION) $(VENDOR)/$(NAME):latest
