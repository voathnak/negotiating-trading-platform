#!/usr/bin/env bash

rm -rf layer/core/
mkdir -p layer/core/python
cp -rf snail layer/core/python
cp -rf models layer/core/python
cp -rf snippets layer/core/python