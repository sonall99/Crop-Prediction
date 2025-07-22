### FROM here , we can get the Nitrogen Amount and Ph level of the soil using the
### Coordinates of a point.
import requests

def fetch_soil(lat, lon):
    try:
        # Valid coordinate range check
        if not (-90 <= lat <= 90 and -180 <= lon <= 180):
            return {
                "error": "Please enter coordinates within:\nLatitude: [-90, 90], Longitude: [-180, 180]"
            }

        # Round to 1 decimal for better nearby searches
        url = (
            f"https://rest.isric.org/soilgrids/v2.0/properties/query?"
            f"lon={round(lon, 1)}&lat={round(lat, 1)}"
            f"&property=nitrogen&property=phh2o&depth=0-5cm&value=Q0.5"
        )

        resp = requests.get(url)
        resp_json = resp.json()

        layers = resp_json.get('properties', {}).get('layers', [])
        if len(layers) < 2:
            raise ValueError("Incomplete soil data returned.")

        Nitrogen = list(layers[0]['depths'][0]['values'].values())[0]
        Ph = list(layers[1]['depths'][0]['values'].values())[0]

        # If any value is missing, try nearby points
        if Nitrogen is None or Ph is None:
            for i in [+0.1, -0.1, +0.2, -0.2, +0.3, -0.3, +0.4, -0.4, +0.5, -0.5, +0.6, -0.6]:
                nearby_url = (
                    f"https://rest.isric.org/soilgrids/v2.0/properties/query?"
                    f"lon={round(lon + i, 1)}&lat={round(lat + i, 1)}"
                    f"&property=nitrogen&property=phh2o&depth=0-5cm&value=Q0.5"
                )
                nearby_resp = requests.get(nearby_url)
                nearby_json = nearby_resp.json()

                try:
                    N_temp = list(nearby_json['properties']['layers'][0]['depths'][0]['values'].values())[0]
                    Ph_temp = list(nearby_json['properties']['layers'][1]['depths'][0]['values'].values())[0]
                    if N_temp is not None and Ph_temp is not None:
                        return {
                            "Nitrogen": N_temp / 10,
                            "Ph": Ph_temp / 10
                        }
                except:
                    continue  # Try next nearby point

            return {
                "error": "Could not find valid soil data nearby. Try a different location."
            }

        # Return valid values
        return {
            "Nitrogen": Nitrogen / 10,
            "Ph": Ph / 10
        }

    except Exception as e:
        return {
            "error": f"Error while fetching soil data: {str(e)}"
        }

#Made by Sonal