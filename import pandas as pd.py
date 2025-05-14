import pandas as pd
from pyproj import Transformer

# Load the CSV file
file_path = 'shape.csv'
data = pd.read_csv(file_path)

# Initialize transformer: UTM Zone 37N → WGS84
transformer = Transformer.from_crs("EPSG:32637", "EPSG:4326", always_xy=True)

# Function to convert UTM to formatted lat/lon strings
def convert_to_latlon(row):
    lon, lat = transformer.transform(row['X'], row['Y'])
    lat_str = f" {lat:.5f}° N"
    lon_str = f" {lon:.5f}° E"
    return pd.Series({'Latitude': lat_str, 'Longitude': lon_str})

# Apply conversion
data[['Latitude', 'Longitude']] = data.apply(convert_to_latlon, axis=1)

# Save to CSV
output_file = 'shape_with_latlon.csv'
data.to_csv(output_file, index=False)

print(f"Formatted conversion complete. File saved as: {output_file}")
