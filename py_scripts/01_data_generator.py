#!/usr/bin/env python
# coding: utf-8

# # Portfolio Project #5
# ## Logistics & Fleet Managment

# In[4]:


import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()
Faker.seed(42)
random.seed(42)
np.random.seed(42)


# In[5]:


# --- 1. GENERATE DRIVERS (100 records) ---
# Schema: driver_id (Primary Key), first_name, last_name, license_class, hire_date, status (Active/Inactive)
print('Generating Drivers...')
drivers_data = []
license_classes = ['Class A', 'Class B', 'Class C']
statuses = ['Active', 'Active', 'Active', 'Inactive'] # Weight towards Active

for driver_id in range(1, 101):
    drivers_data.append({
        'driver_id': driver_id,
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'license_class': random.choice(license_classes),
        'hire_date': fake.date_between(start_date='-5y', end_date='today'),
        'status': random.choice(statuses)
    })
df_drivers = pd.DataFrame(drivers_data)


# In[6]:


# --- 2. GENERATE VEHICLES (50 records) ---
# Schema: vehicle_id (Primary Key), make, model, year, odometer_reading, last_maintenance_date
print('Generating Vehicles...')
vehicles_data = []
makes_models = {'Ford': ['Transit', 'F-250'], 'Mercedes': ['Sprinter'], 'Ram': ['ProMaster', '2500']}

for vehicle_id in range(1, 51):
    make = random.choice(list(makes_models.keys()))
    model = random.choice(makes_models[make])

    # Inject "Dirt": Leave ~10% of last_maintenance_date fields blank (Null)
    if random.random() < 0.010:
        maintenance_date = np.nan
    else:
        maintenance_date = fake.date_between(start_date='-1y', end_date='today')

    vehicles_data.append({
        'vehicle_id': vehicle_id,
        'make': make,
        'model': model,
        'year': random.randint(2015, 2023),
        'odometer_reading': random.randint(10000, 150000),
        'last_maintenance_date': maintenance_date
    })
df_vehicles = pd.DataFrame(vehicles_data)


# In[12]:


# --- 3. Generate delivery_routes ---
# Schema: route_id (Primary Key), driver_id (Foriegn Key), vehicle_id (Foreign Key), dispatch_timestamp,
# delivery_timestamp, distance_miles, fuel_used_gallons.

# --- 3. GENERATE DELIVERY ROUTES (10,000 records) ---
print("Generating Delivery Routes...")
routes_data = []

for route_id in range(1, 10001):
    # Base route info
    driver = random.randint(1, 100)
    vehicle = random.randint(1, 50)
    distance = round(random.uniform(5.0, 300.0), 2)

    # Calculate realistic fuel used (assuming avg 10-15 mpg)
    realistic_mpg = random.uniform(10.0, 15.0)
    fuel_used = round(distance / realistic_mpg, 2)

    # Generate Timestamps
    dispatch_time = fake.date_time_between(start_date='-1y', end_date='now')
    # Add between 30 mins and 8 hours for delivery
    duration = timedelta(minutes=random.randint(30, 480)) 
    delivery_time = dispatch_time + duration

    # --- INJECTING THE "DIRT" ---

    # Dirt 1: 5% of Fuel_Used_Gallons are negative or massive outliers
    anomaly_roll = random.random()
    if anomaly_roll < 0.025: # 2.5% chance of negative fuel
        fuel_used = -abs(fuel_used)
    elif anomaly_roll < 0.05: # 2.5% chance of massive outlier (e.g., 5000 gallons)
        fuel_used = round(random.uniform(1000, 5000), 2)

    # Dirt 2: 3% of Delivery_Timestamps occur BEFORE Dispatch_Timestamp
    if random.random() < 0.03:
        delivery_time = dispatch_time - timedelta(minutes=random.randint(10, 120))

    routes_data.append({
        'route_id': route_id,
        'driver_id': driver,
        'vehicle_id': vehicle,
        'dispatch_timestamp': dispatch_time,
        'delivery_timestamp': delivery_time,
        'distance_miles': distance,
        'fuel_used_gallons': fuel_used
    })

df_routes = pd.DataFrame(routes_data)




# In[8]:


# --- 4. EXPORT TO CSV ---
print("Exporting to CSV...")
df_drivers.to_csv('drivers_raw.csv', index=False)
df_vehicles.to_csv('vehicles_raw.csv', index=False)
df_routes.to_csv('delivery_routes_raw.csv', index=False)

print("Data generation complete! You now have three raw CSV files ready for PostgreSQL.")


# In[17]:


# Explority Analysis of Drivers table for snapshot of data

print("Structural Dimension (rows, columns")
print("------------------------------------")
print(df_drivers.shape)
print("------------------------------------")
print("Inspection of first 10 rows")
print("------------------------------------")
print(df_drivers.head())
print("------------------------------------")
print("Data types, non-null counts")
print("------------------------------------")
print(df_drivers.info())


# In[18]:


# Explority Analysis of VEHICLES table for snapshot of data

print("Structural Dimension (rows, columns")
print("------------------------------------")
print(df_vehicles.shape)
print("------------------------------------")
print("Inspection of first 10 rows")
print("------------------------------------")
print(df_vehicles.head())
print("------------------------------------")
print("Data types, non-null counts")
print("------------------------------------")
print(df_vehicles.info())


# In[20]:


# Explority Analysis of DELIVERY ROUTES table for snapshot of data

print("Structural Dimension (rows, columns")
print("------------------------------------")
print(df_routes.shape)
print("------------------------------------")
print("Inspection of first 10 rows")
print("------------------------------------")
print(df_routes.head())
print("------------------------------------")
print("Data types, non-null counts")
print("------------------------------------")
print(df_routes.info())
print("------------------------------------")
print(df_routes.isna().sum())

