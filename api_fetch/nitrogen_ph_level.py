### FROM here , we can get the Nitrogen Amount and Ph level of the soil using the
### Coordinates of a point.
import requests

def fetch_soil(lat, lon):
    url = (f"https://rest.isric.org/soilgrids/v2.0/properties/query?lon={int(round(lon,0))}&lat={int(round(lat,0))}&property=nitrogen&property=phh2o&depth=0-5cm&value=Q0.5")
    resp = requests.get(url).json()

    try:

        if 180 > lon > -180 and 90 > lat > -90:
            try:
                Nitrogen = list(resp['properties']['layers'][0]['depths'][0]['values'].values())[0]
                Ph = list(resp['properties']['layers'][1]['depths'][0]['values'].values())[0]

                if (Ph == None) or (Nitrogen == None):
                    # Trying to get info of any nearby point
                    for i in [+0.1,-0.1,+0.2,-0.2,+0.3,-0.3,+0.4,-0.4,+0.5,-0.5,+0.6,-0.6]:
                        url2 = (f"https://rest.isric.org/soilgrids/v2.0/properties/query?lon={int(round(lon+i,0))}&lat={int(round(lat+i,0))}&property=nitrogen&property=phh2o&depth=0-5cm&value=Q0.5")
                        resp2 = requests.get(url2).json()
                        Nitrogen = list(resp2['properties']['layers'][0]['depths'][0]['values'].values())[0]
                        Ph = list(resp2['properties']['layers'][1]['depths'][0]['values'].values())[0]
                        if (Ph != None) and (Nitrogen != None):
                            return {
                                "Nitrogen" : Nitrogen/10,
                                "Ph" : Ph/10 # Ph was earlier multiplied by 10 (d_factor) while requesting the URL , thus making it back to normal value
                            }

                return {
                        "Nitrogen" : Nitrogen/10,
                        "Ph" : Ph/10 # Ph was earlier multiplied by 10 while requesting the URL , thus making it back to normal value
                    }
            except:
                raise ('Value(s) Not Found\n\nPossible Troubleshoot :-\n'
                        '1) Check the coordinates entered\n'
                        '2) The order with which coordinates are entered is correct i.e. latitude, then longitude\n'
                        '3) Land marked is not good for crop production, try another nearby point.')

    except:
        raise "Please Enter the value such that:\nLatitude :- [-90,90] AND Longitude :- [-180,180]"

#Made by Sonal Singh