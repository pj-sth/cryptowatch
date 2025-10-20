## Run with Docker

You can run CryptoWatch instantly using Docker:

```bash
# Build the image
docker build -t cryptowatch .

# Run the API server
docker run -p 8000:8000 cryptowatch