from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Loading the data
data = pd.read_csv("data.csv")

# Convert 'value_date' to datetime and sort the DataFrame
data['value_date'] = pd.to_datetime(data['value_date'])
data = data.sort_values(by='value_date', ascending=False)

@app.get("/power/europe")
async def get_europe_co2_emission():
    
    data_filtered = data.dropna(subset=['total_co2_emissions']) # Drop rows with empty 'total_co2_emissions'

    
    latest_data = data_filtered.iloc[0]   # Get the latest data (first row)
    
    # Convert numbers from string to float
    for col in ['domestic_aviation', 'total_ets_emissions', 'ground_transport', 'total_co2_emissions', 'power', 'industry']:
        latest_data[col] = float(latest_data[col])

    europe_co2_emission = latest_data["total_co2_emissions"]

    return {"europe_co2_emission": europe_co2_emission}


