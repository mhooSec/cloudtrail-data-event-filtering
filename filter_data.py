import json

# Load the JSON file
with open('combined.json', 'r') as file:
    data = json.load(file)

# Print the type and a sample of data for debugging
# print(f"Data type: {type(data)}")
# print(f"Sample data: {data[:2]}")  # Print first 2 items for sample

# Function to recursively search for 'accessKeyId' in nested dictionaries
def contains_access_key_id(item):
    if isinstance(item, dict):
        if 'accessKeyId' in item:
            return True
        for value in item.values():
            if contains_access_key_id(value):
                return True
    elif isinstance(item, list):
        for sub_item in item:
            if contains_access_key_id(sub_item):
                return True
    return False

# Filter the data by checking for 'accessKeyId'
filtered_data = [item for item in data if contains_access_key_id(item)]

# Print the number of filtered items
print(f"Number of items with 'accessKeyId': {len(filtered_data)}")

# Save the filtered data to a new file if any
if filtered_data:
    with open('filtered_file.json', 'w') as file:
        json.dump(filtered_data, file, indent=4)
    print("Filtered data saved to 'filtered_file.json'.")
else:
    print("No items with 'accessKeyId' found.")
