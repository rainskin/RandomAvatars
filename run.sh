ENV_FILENAME=".env"
ENV_EXAMPLE_FILENAME=".env.example"

if [ ! -f $ENV_FILENAME ]; then
  echo "You must create file '$ENV_FILENAME' using '$ENV_EXAMPLE_FILENAME'"
  return
fi

docker compose up --build -d