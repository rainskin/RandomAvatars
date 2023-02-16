ENV_FILE=".env"
ENV_EXAMPLE_FILE=".env.example"

if [ ! -f $ENV_FILE ]; then
  echo "You must create file '$ENV_FILE' using '$ENV_EXAMPLE_FILE'"
  return
fi

docker compose up --build -d
