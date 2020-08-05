source scripts/config.sh

aws s3   --profile "$PROFILE" \
    --region "$REGION" \
    sync front-end/dist s3://"$FRONTEND_S3_BUCKET"