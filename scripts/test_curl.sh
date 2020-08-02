
# List
curl --location http://0.0.0.0:3000/hello | json_pp

curl "$(sh scripts/describe-stack-api-url.sh)hello"

curl "$(sh scripts/describe-stack-api-url.sh)todos" -H 'Authorization: allow'