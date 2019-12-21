import csv


def read_csv():

    data = csv.DictReader(open('dataset/bink_dataset.csv'))

    return data


def sorted_list(csv_dict: dict, parameter: str):

    new_array = []

    for datapoint in csv_dict:
        new_array.append(float(datapoint[parameter]))

    new_array.sort()

    return new_array


def master_list_filtered(csv_dict: dict, parameter_to_filter_by: str, filter_by: str):

    master_array = []

    for row in csv_dict:
        if row[parameter_to_filter_by] == filter_by:
            master_array.append(row)

    return master_array


def calculate_total_rent(array: list):

    total_rent = 0

    for property_info in array:
        total_rent += float(property_info['Current Rent'])

    return total_rent
