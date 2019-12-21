import csv
import json
from collections import Counter


def read_csv() -> object:

    data = csv.DictReader(open('dataset/bink_dataset.csv'))

    return data


def sorted_list(csv_dict: dict, parameter: str) -> list:

    new_array = []

    for datapoint in csv_dict:
        new_array.append(float(datapoint[parameter]))

    new_array.sort()

    return new_array


def master_list_filtered(csv_dict: dict, parameter_to_filter_by: str, filter_by: str) -> list:

    master_array = []

    for row in csv_dict:
        if row[parameter_to_filter_by] == filter_by:
            master_array.append(row)

    return master_array


def calculate_total_rent(list_of_properties: list) -> float:

    total_rent = 0

    for property_info in list_of_properties:
        total_rent += float(property_info['Current Rent'])

    return total_rent


def count_total_masts_by_tenant(csv_dict: dict) -> dict:

    tenant_list = []

    for tenant in csv_dict:
        tenant_list.append(tenant['Tenant Name'])

    return json.dumps(Counter(tenant_list), sort_keys=True, indent=2)
