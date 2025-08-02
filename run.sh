#!/bin/bash
set -e

docker-compose up -d --build

echo "Waiting for PostgreSQL to start..."
until docker-compose exec db pg_isready -U inv_user; do
  sleep 2
done

echo "Applying initial schema..."
docker-compose exec -T db psql -U inv_user -d inventory_db < schema.sql

echo "Environment setup complete. FastAPI running on localhost:8000."
