from utils import read_csv, sorted_list, master_list_filtered, calculate_total_rent, count_total_masts_by_tenant, tenant_data_between_dates


def first_user_input():
    user_input = input(
        'Hi, would you like to run the whole script, or just a section?\n\
        [1] Whole Script\n\
        [2] Specific Section\n\
        '
    )

    if user_input == '1':
        print(sorted_list(read_csv(), 'Current Rent')[:5])
        print(master_list_filtered(read_csv(), 'Lease Years', '25'))
        print('Total Rent: ' + str(calculate_total_rent(master_list_filtered(read_csv(), 'Lease Years', '25'))))
        print(count_total_masts_by_tenant(read_csv()))
        print(tenant_data_between_dates(read_csv(), '01-Jun-1999', '31-Aug-2007'))

    elif user_input == '2':
        second_user_input()

    else:
        print('Sorry, your selection is not valid, please try again.\n')
        first_user_input()


def second_user_input():
    user_input = input(
        'What section would you like to run?\n\
        [1]List of first 5 items sorted by Current Rent\n\
        [2]List of all mast data where the Lease Years is 25 + the Total Rent for the Properties in the list\n\
        [3]A Dictionary of all the Tenants and the count of masts for each\n\
        [4]List of all mast data where the Lease Start Date is between 1st of June 1999 and 31st of August 2007\n\
        '
    )

    if user_input == '1':
        print(sorted_list(read_csv(), 'Current Rent')[:5])
    
    elif user_input == '2':
        print(master_list_filtered(read_csv(), 'Lease Years', '25'))
        print('Total Rent: ' + str(calculate_total_rent(master_list_filtered(read_csv(), 'Lease Years', '25'))))
    
    elif user_input == '3':
        print(count_total_masts_by_tenant(read_csv()))
    
    elif user_input == '4':
        print(tenant_data_between_dates(read_csv(), '01-Jun-1999', '31-Aug-2007'))
    
    else:
        print('Sorry, your selection is not valid, please try again.\n')
        second_user_input()


if __name__ == "__main__":
    first_user_input()
