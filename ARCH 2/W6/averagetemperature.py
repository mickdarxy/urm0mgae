temperatures = (
    ('1995', '3', ['47.3', '40.0', '38.3', '36.3', '37.4', '40.3', '41.1', '40.5', '41.6', '43.2', '46.2', '45.8', '44.9', '39.4', '40.5',
     '42.0', '46.5', '46.2', '43.3', '41.7', '40.7', '39.6', '44.2', '47.8', '45.9', '47.3', '39.8', '35.2', '38.5', '40.5', '47.0']),
    ('2010', '3', ['39.2', '36.7', '35.5', '35.2', '35.8', '33.8', '30.7', '33.2', '32.3', '33.3', '37.3', '39.9', '40.8', '42.9', '42.7',
     '42.6', '44.8', '50.3', '52.2', '55.2', '47.2', '45.0', '48.6', '55.0', '57.4', '50.9', '48.6', '46.2', '49.6', '50.1', '43.6']),
    ('2020', '3', ['43.2', '41.1', '40.0', '43.6', '42.6', '44.0', '44.0', '47.9', '46.6', '50.5', '51.5', '47.7', '44.7', '44.0', '48.9',
     '45.3', '46.6', '49.7', '47.2', '44.8', '41.8', '40.9', '41.0', '42.7', '43.4', '44.0', '46.4', '45.5', '40.7', '39.5', '40.6'])
)

#creating a function for the first task to be calculated
def temperatures_95_10():
    # assigning the right info of each year in the right variable
    temp_info_95 = temperatures[0]
    temp_info_10 = temperatures[1]
    # now storing all the temperatures belonging to each year accordingly
    alltemps_95 = temp_info_95[2]
    alltemps_10 = temp_info_10[2]
    # simple addition of all the temperatures together
    alltemps_combined = alltemps_10 + alltemps_95
    # making a set for the different temperatures
    unique_temps = set()
    # if the temperature is different it is added into the unique temperature variable
    for temp in alltemps_combined:
        if temp not in unique_temps:
            unique_temps.add(temp)
    return len(unique_temps)


def temperatures_95_20():
    # assigning the right info of each year in the right variable
    temp_info_95 = temperatures[0]
    temp_info_20 = temperatures[2]
    # now storing all the temperatures belonging to each year accordingly
    alltemps_95 = temp_info_95[2]
    alltemps_20 = temp_info_20[2]
    # simple addition of all the temperatures together
    alltemps_combined = alltemps_20 + alltemps_95
    # making a set for the different temperatures
    unique_temps = set()
    # if the temperature is different it is added into the unique temperature variable
    for temp in alltemps_combined:
        if temp not in unique_temps:
            unique_temps.add(temp)
    return len(unique_temps)


def highest_temp_march():
    #collecting and assigning all the corresponding temperatures
    temp_info_95 = temperatures[0]
    temp_info_10 = temperatures[1]
    temp_info_20 = temperatures[2]
    

def warmest_march():
