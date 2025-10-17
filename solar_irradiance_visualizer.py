
import requests
import matplotlib.pyplot as plt
from datetime import datetime

#Enter your lat&long
LAT = 6.4474
LON = 3.3903
DATE = datetime.today().strftime("%Y-%m-%d")

# Open-Meteo endpoint for hourly shortwave radiation
url = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={LAT}&longitude={LON}"
    f"&hourly=shortwave_radiation"
    f"&start_date={DATE}&end_date={DATE}"
    f"&timezone=Africa/Lagos"
)

response = requests.get(url)
data = response.json()

# Extract data
hours = list(range(24))
irradiance = data.get("hourly", {}).get("shortwave_radiation", [0]*24)

# Plot
plt.figure(figsize=(10,5))
plt.plot(hours, irradiance, marker='o', color='orange')
plt.title(f"Hourly Solar Irradiance on {DATE} at ({LAT}, {LON})")
plt.xlabel("Hour of Day")
plt.ylabel("Solar Radiation (W/m²)")
plt.xticks(hours)
plt.grid(True)
plt.tight_layout()
plt.show()

