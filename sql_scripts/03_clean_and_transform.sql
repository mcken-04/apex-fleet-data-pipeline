-- Create a clean view for vehicles
CREATE OR REPLACE VIEW vehicles_clean AS 
SELECT
	vehicle_id,
	make,
	model,
	YEAR,
	odometer_reading,
	-- Fix missing dates in last_maintenance_date to a defualt date
	COALESCE(last_maintenance_date, '1900-01-01'::DATE) AS last_maintenance_date,
	-- Make a flag for dashboard determined by maintenance dates
	CASE
		WHEN last_maintenance_date IS NULL THEN 'Missing Log'
		WHEN last_maintenance_date < CURRENT_DATE - INTERVAL '6 months' THEN 'Overdue'
		ELSE 'Up to Date'
	END AS maintenance_status
FROM vehicles_raw;

-- Create a clean view for dlivery routes
CREATE OR REPLACE VIEW delivery_routes_clean AS
WITH route_calculations AS (
	SELECT
		route_id,
		driver_id,
		vehicle_id,
		dispatch_timestamp,
		delivery_timestamp,
		distance_miles,
		fuel_used_gallons,
		-- Calculate the delivery durations from the dispatch_timestanp and delivery_timestamp
		EXTRACT(EPOCH FROM (delivery_timestamp - dispatch_timestamp)) / 60 AS delivery_duration_minutes
	FROM delivery_routes_raw
)

SELECT
	route_id,
	driver_id,
	vehicle_id,
	dispatch_timestamp,
	delivery_timestamp,
	distance_miles,
	fuel_used_gallons,
	delivery_duration_minutes,
	-- Flag invalid timestamps
	CASE 
		WHEN delivery_duration_minutes < 0 THEN 'Error: Delivered before dispatch'
		ELSE 'Valid'
	END AS timestamp_status,
	-- Flag incorrect fuel consumption either below 0 or improper usage amounts
	CASE 
		WHEN fuel_used_gallons < 0 THEN 'Error: Negative Fuel'
		WHEN (distance_miles / NULLIF(fuel_used_gallons, 0)) < 2 OR (distance_miles / NULLIF(fuel_used_gallons, 0)) > 50 THEN 'Error: Impossible MPG'
		ELSE 'Valid'
	END AS fuel_status
FROM route_calculations;

-- While we could just filter out the data less than 0 with a WHERE clause, we created status flags to show these errors in our dashboard.

-- Create a clean view for driver table
CREATE OR REPLACE VIEW drivers_clean AS
SELECT
	driver_id,
	first_name,
	last_name,
	license_class,
	hire_date,
	status
FROM drivers_raw;

--------------------------------------------------------------------------------------------------------------------
-- Created queries to view the VIEWS created before transfering to Power BI 

SELECT *
FROM drivers_raw
LIMIT 10;

SELECT *
FROM delivery_routes_clean
WHERE fuel_status <> 'Valid'
LIMIT 10;

SELECT *
FROM vehicles_clean
LIMIT 10;