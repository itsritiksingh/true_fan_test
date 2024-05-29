CREATE USER ritik PASSWORD '1234';
CREATE DATABASE dynamicJobs;
GRANT ALL PRIVILEGES ON DATABASE dynamicJobs TO ritik;

\connect dynamicJobs;

CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price FLOAT NOT NULL
);
