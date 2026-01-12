#!/bin/bash
set -e

echo "Building Docker image..."
docker build -t cloud-app-test -f docker/Dockerfile .

echo "Starting container..."
container_id=$(docker run -d -p 8000:8000 cloud-app-test)

# Cleanup function
cleanup() {
    echo "Stopping container..."
    docker stop $container_id
    docker rm $container_id
}
trap cleanup EXIT

echo "Waiting for app to start..."
sleep 5

echo "Testing Health Endpoint..."
curl -f http://localhost:8000/health
echo -e "\nHealth check passed!"

echo "Testing Metrics Endpoint..."
curl -f http://localhost:8000/metrics | head -n 5
echo -e "\nMetrics check passed!"

echo "All tests passed!"
