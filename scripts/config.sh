#!/usr/bin/env bash
# shellcheck disable=SC2034

export APP_NAME=stock-trading
export STAGE_NAME=dev
export VERSION_NAME=v1
export S3_BUCKET=$APP_NAME-$STAGE_NAME-$VERSION_NAME-bucket
export STACK_NAME=$APP_NAME-$STAGE_NAME-$VERSION_NAME-stack
export PROFILE=voathnakl
export REGION=us-east-1
export INPUT_FILE=template.yaml
export OUTPUT_FILE=packaged.yaml
