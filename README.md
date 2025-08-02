# Task Overview
The Utkrusht Inventory API enables teams to add and list product records in a digital inventory. FastAPI endpoints for adding a new product and retrieving all products are already in place, but the PostgreSQL schema and database integration logic have not been created. Accurately designing and integrating the database layer is critical for reliable, scalable product management and supports future analytics and reporting needs.

# Guidance
- Review `app/main.py` to see the API endpoints you need to support.
- Focus on implementing `app/database.py`, `app/models.py`, and the initial schema in `schema.sql` for product data.
- Use the `run.sh` script to deploy your database, build services, and apply schema changes via Docker Compose.

# Objectives
- Create a PostgreSQL schema for storing products, including relevant fields (name, SKU, price, quantity, timestamp, etc.), with appropriate types and constraints.
- Implement the SQLAlchemy ORM model for the products table, ensuring fields match the schema.
- Write full async database integration logic to (a) add a new product and (b) fetch all products, as required by the API endpoints. Integrate this logic in `app/database.py` and `app/models.py`.
- Ensure product `sku` values are unique and searchable. Enforce not-null constraints and correct indexing for common queries.
- Your database layer must use asynchronous operations, integrate cleanly with FastAPI, and avoid blocking calls.

# How to Verify
- Launch the app and POST a new product using `/products`—confirm it is saved in PostgreSQL and returned by the GET endpoint.
- Make a GET request to `/products`—validate that all added products (including newly added ones) are returned.
- Attempt to add a product with a duplicate SKU—verify the API or DB correctly rejects/disallows it.
- Inspect the schema using psql/pgAdmin/DBeaver to ensure columns, constraints, and indexing are correctly applied.
- Confirm all DB logic works asynchronously (does not block FastAPI event loop).
