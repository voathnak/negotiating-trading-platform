#!/usr/bin/env bash

source scripts/config.sh
aws cloudformation describe-stacks --stack-name "$STACK_NAME" --region "$REGION" 
