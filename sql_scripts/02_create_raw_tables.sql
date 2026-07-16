-- PORTFOLIO PROJECT 5 TABLE CREATION DDL

-- 1. Create driver_table
CREATE TABLE drivers_raw (
	driver_id INT PRIMARY KEY,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	license_class VARCHAR(50),
	hire_date DATE,
	status VARCHAR(20)
);

-- Create vehicles_raw table
CREATE TABLE vehicles_raw (
	vehicle_id INT PRIMARY KEY,
	make VARCHAR(50),
	model VARCHAR(50),
	YEAR INT,
	odometer_reading INT,
	last_maintenance_date DATE
);

-- Create delivery_routes_raw table
CREATE TABLE delivery_routes_raw ( 
	route_id INT PRIMARY KEY,
	driver_id INT,
	vehicle_id INT,
	dispatch_timestamp TIMESTAMP,
	delivery_timestamp TIMESTAMP,
	distance_miles DECIMAL(10,2),
	fuel_used_gallons DECIMAL(10,2),
	FOREIGN KEY (driver_id) REFERENCES drivers_raw(driver_id),
	FOREIGN KEY (vehicle_id) REFERENCES vehicles_raw(vehicle_id)
);