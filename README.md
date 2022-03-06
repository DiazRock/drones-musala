# drones-musala
Drones fleet bussines logic for a test to Musala Softwares Corp

# Install dependencies

`make install`

# Build and run

`make buildAndRun`

# Test

Make sure you don't the all system running: this command will started it four you

`make test`


# Example request

Get a list of existing drones: GET /api/drone/

```
curl --location --request GET '<URL DJANGO SERVER>/api/drone/'
```

Create a medication: POST api/medication/:
```
    curl --location --request POST '<URL DJANGO SERVER>/api/medication/' \
    --form 'image=@"<URL IMAGE>"' \
    --form 'name="Peniciline"' \
    --form 'weight="2.5"' \
    --form 'code="555AAABB"'
```

Get availables drones for loading:

```
curl --location --request GET '<URL DJANGO SERVER>/api/drone/availables/'
```

Get existing medications: GET api/medication/


Load a med to a drone: PATCH api/drone/<int:pk>/load/

```
curl --location --request PATCH '<URL DJANGO SERVER>/api/drone/8/load/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "medications": [1]
}'
```

"medications" is an array here of medications ids
A drone is loaded with a list of drugs.

Getting current drone state

```
curl --location --request PATCH '<URL DJANGO SERVER>/api/drone/<int: pk>/state/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "state": "IDLE" # This will full the drone battery to 100
}'
```


```
curl --location --request PATCH '<URL DJANGO SERVER>/api/drone/<int: pk>/state/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "state": "IDLE" # This will full the drone battery to 100
}'
```

This will decrease the battery capacity 20%.



