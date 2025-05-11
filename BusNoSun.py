from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import math
from datetime import datetime
from astral.sun import sun
from astral import LocationInfo




# מקבל מיקום נוכחי ויעד
def get_coordinates(place_name):
    geolocator = Nominatim(user_agent="sunbus")
    location = geolocator.geocode(place_name)
    print(location)
    if location:
        return (location.latitude, location.longitude)
    else:
        raise Exception(f"מיקום לא נמצא: {place_name}")


# מחשב כיוון בין שתי נקודות
def calculate_bearing(start, end):
    lat1, lon1 = map(math.radians, start)
    lat2, lon2 = map(math.radians, end)
    delta_lon = lon2 - lon1
    x = math.sin(delta_lon) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(delta_lon)
    bearing = math.atan2(x, y)
    bearing_deg = (math.degrees(bearing) + 360) % 360
    return bearing_deg


# המרת כיוון למילה
def bearing_to_direction(deg):
    directions = ["צפון", "צפון-מזרח", "מזרח", "דרום-מזרח", "דרום", "דרום-מערב", "מערב", "צפון-מערב"]
    ix = int((deg + 22.5) / 45) % 8
    return directions[ix]


# חישוב מיקום השמש
#def get_sun_azimuth(lat, lon):
#    city = LocationInfo(latitude=lat, longitude=lon)
#    s = sun(city.observer, date=datetime.now())
#    azimuth = city.solar_azimuth(datetime.now())
#    return azimuth


# המלצה על צד באוטובוסbearing
def decide_seat(bearing, sun_azimuth ):
    diff = (sun_azimuth - 360) % 360
    print(diff)
    if 45 < diff < 135:
        return "שב בצד השאלי"
    elif 225 < diff < 315:
        return "שב בצד הימני"
    else:
        return "אין שמש ישירה – שב איפה שנוח"

def fun():
# MAIN
    from geopy.geocoders import Nominatim

    geolocator = Nominatim(user_agent="sunbus")

    location = geolocator.geocode("תל אביב")
    print(location.latitude, location.longitude)
if __name__ == "__main__":
    current_location = input("הזן את מיקומך הנוכחי (למשל 'תל אביב'): ")
    destination = input("הזן את יעד הנסיעה (למשל 'ירושלים'): ")

    curr_coords = get_coordinates(current_location or "tel aviv")
    dest_coords = get_coordinates(destination)

    curr_lat, curr_lon = curr_coords
    dest_lat, dest_lon = dest_coords

    # עכשיו אפשר להשתמש במשתנים:
    print(f"נקודת ההתחלה: רוחב {curr_lat}, אורך {curr_lon}")
    print(f"נקודת היעד: רוחב {dest_lat}, אורך {dest_lon}")

    bearing = calculate_bearing(curr_coords, dest_coords)
    print(f"--------------- {bearing} --------------")
#    sun_azimuth = get_sun_azimuth(*curr_coords)

    print(f"כיוון הנסיעה: {bearing_to_direction(bearing)} ({round(bearing)}°)")
    #print(f"כיוון השמש: {round(sun_azimuth)}°")
    sun_azimuth =  datetime.now().strftime("%H")
    print(sun_azimuth)
    sun_azimuth = 5
    if(sun_azimuth>7 and sun_azimuth<13):
        print("yes")
        sun_azimuth = 0;
    elif(sun_azimuth>15 and sun_azimuth<19):
        print("no")
        sun_azimuth = 180
    else:
        print("black")
        sun_azimuth = 45
    print(decide_seat(bearing, sun_azimuth))
    print(decide_seat(bearing, 0))
