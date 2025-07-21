### FROM here , we can get the avergae temperature , Relative Humidity and Rainfall using the
### Coordinates of a point.

import requests
from datetime import datetime, timedelta


def get_weather_info(lat, lon):
    try:
        # Get date range: past 7 days
        end_date = datetime.now() - timedelta(days=4)
        start_date = end_date - timedelta(days=6)
        start_str = start_date.strftime("%Y%m%d")
        end_str = end_date.strftime("%Y%m%d")

        # Build API request
        url = (
            "https://power.larc.nasa.gov/api/temporal/daily/point"
            "?parameters=T2M,RH2M,PRECTOTCORR"
            f"&community=AG&latitude={lat}&longitude={lon}"
            f"&start={start_str}&end={end_str}&format=JSON"
        )

        # Request data
        response = requests.get(url)
        data = response.json()
        Temperature_List = list(data['properties']['parameter']['T2M'].values())
        RH_list = list(data['properties']['parameter']["RH2M"].values())
        Rain_list = list(data['properties']['parameter']['PRECTOTCORR'].values())

        return {
            "Average Temperature": round(sum(Temperature_List) / len(Temperature_List), 2),
            "Average Relative Humidity": round(sum(RH_list) / len(RH_list), 2),
            "Average Rain": round((sum([x * 24 for x in Rain_list]) / len(Rain_list)), 2),
            # To get rain in mm/day from mm/hr
        }

    except:
        print(
            "Unable to get information for the specific point marked\nMake Sure to Enter the value such that:Latitude :- [-90,90] AND Longitude :- [-180,180]")

# Made by Sonal Singh