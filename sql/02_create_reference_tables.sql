CREATE TABLE regions (
    region_id SERIAL PRIMARY KEY,
    region_name VARCHAR(100) UNIQUE NOT NULL,
    region_code VARCHAR(10) UNIQUE NOT NULL
);
CREATE TABLE districts (
    district_id SERIAL PRIMARY KEY,
    district_name VARCHAR(100) NOT NULL,
    district_code VARCHAR(10) UNIQUE NOT NULL,
    region_id INT NOT NULL REFERENCES regions(region_id)
);






