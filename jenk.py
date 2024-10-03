import requests
import pandas as pd

# Step 1: Download the CSV file
url = "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv"
response = requests.get(url)

# Save the CSV file locally
with open("/tmp/taxi_zone_lookup.csv", "wb") as file:
    file.write(response.content)

# Step 2: Load the dataset using pandas
df = pd.read_csv("/tmp/taxi_zone_lookup.csv")

# Step 3: a. Find the Total Number of Records
total_records = len(df)

# Step 4: b. Find Unique Borough in Sorted Order
unique_boroughs = sorted(df["Borough"].unique())

# Step 5: c. Find Number of Records for Brooklyn Borough
brooklyn_records = len(df[df["Borough"] == "Brooklyn"])

# Step 6: d. Save the results in a file at /root/taxi_zone_output.txt
with open("/root/taxi_zone_output.txt", "w") as output_file:
    output_file.write(f"Total Number of Records: {total_records}\n")
    output_file.write(f"Unique Boroughs (Sorted): {', '.join(unique_boroughs)}\n")
    output_file.write(f"Number of Records for Brooklyn Borough: {brooklyn_records}\n")

print("Facts saved to /root/taxi_zone_output.txt")
