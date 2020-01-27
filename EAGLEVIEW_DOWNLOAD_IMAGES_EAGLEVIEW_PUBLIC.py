import requests

##BASIC STRAIGHT FORWARD SCRIPT THAT SHOWS HOW TO DOWNLOAD A LAT LONG SINGLE FILES FROM THE API SERVER
##ALSO DEMOSTRATES HOW TO USE PARAMETERS IN THE URL, SUCH AS WIDTH, HEIGHT, IMAGE FORMAT

## ASSUMING YOU RAN FIRST SCRIPT--HMAC SCRIPT
## DO NOT ACTUALLY STORE PLAIN TEXT IN SCRIPT IN REAL LIFE, USE ENV VARIABLES OR SOME OTHER METHOD

EAGLEVIEW_API_KEY = "YOUR_API_KEY_HERE_HOWEVER_YOU_STORE_IT" 

##PASS LAT AND LONG HERE

lat = "LAT"
long = "LONG"

lat_long_query_string = f"{lat},{long}"

query_url = f"https://pol.pictometry.com/Gateway/v1/search/{lat_long_query_string}/{EAGLEVIEW_API_KEY}"

r = requests.get(query_url)

if r.status_code == 200:

    json_response = r.json()

    north_image = json_response['response']['images']['north'][0]['imageResource']
    east_image = json_response['response']['images']['east'][0]['imageResource']
    south_image = json_response['response']['images']['south'][0]['imageResource']
    west_image = json_response['response']['images']['west'][0]['imageResource']

    north_image_filename = "EAGLEVIEW_FILE_NORTH.jpg"
    east_image_filename = "EAGLEVIEW_FILE_EAST.jpg"
    south_image_filename = "EAGLEVIEW_FILE_SOUTH.jpg"
    west_image_filename = "EAGLEVIEW_FILE_WEST.jpg"

    ##DOWNLOADS EACH FILE AS BINARY, WRITES TO FILE NAME

    r = requests.get(f"{north_image}/{EAGLEVIEW_API_KEY}/width:300;height:300;imageFormat:jpg")
    open(r"YOUR_PATH_HERE" + north_image_filename, 'wb').write(r.content)

    r = requests.get(f"{east_image}/{EAGLEVIEW_API_KEY}/width:300;height:300;imageFormat:jpg")
    open(r"YOUR_PATH_HERE" + east_image_filename, 'wb').write(r.content)

    r = requests.get(f"{south_image}/{EAGLEVIEW_API_KEY}/width:300;height:300;imageFormat:jpg")
    open(r"YOUR_PATH_HERE" + south_image_filename, 'wb').write(r.content)

    r = requests.get(f"{west_image}/{EAGLEVIEW_API_KEY}/width:300;height:300;imageFormat:jpg")
    open(r"YOUR_PATH_HERE" + west_image_filename, 'wb').write(r.content)





