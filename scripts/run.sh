#!/usr/bin/env bash

source scripts/config.sh
rm -rf .aws-sam
rm -rf layer/core/
mkdir -p layer/core/python
cp -r snail layer/core/python
cp -r models layer/core/python
cp -r snippets layer/core/python
#sam build && \
sam local start-api --region "$REGION" --profile "$PROFILE"  --skip-pull-image --debug-port 5890
