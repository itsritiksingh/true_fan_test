CREATE USER ritik PASSWORD '1234';
CREATE DATABASE dynamicJobs;
GRANT ALL PRIVILEGES ON DATABASE dynamicJobs TO ritik;

\connect dynamicJobs;

CREATE SEQUENCE product_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 99999
	START 1

CREATE TABLE public.products (
	id int4 NOT NULL DEFAULT nextval('product_id_seq'),
	"name" varchar NULL,
	category varchar NULL,
	price float8 NULL,
	CONSTRAINT products_pkey PRIMARY KEY (id)
);