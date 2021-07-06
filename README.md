# VernacularAi
## Dockerize and Creation of 2 POST API using Django restframework
Contains 2 POST Api as per the given requirements.

## Installation
- `git clone https://github.com/mornville/vernacularAi.git`
- `cd vernacularAi`
- Run Docker container as - `docker-compose up`
- Approx size of Docker Image `90.66 MB`

## Testing
- Test whether docker container is up and running by sending a POST/GET to `http://localhost:8000/`

### API 1 (POST API to validate a slot with a finite set of values.)
#### SAMPLE REQUEST
```json
{
  "invalid_trigger": "invalid_ids_stated",
  "key": "ids_stated",
  "name": "govt_id",
  "reuse": true,
  "support_multiple": true,
  "pick_first": false,
  "supported_values": [
    "pan",
    "aadhaar",
    "college",
    "corporate",
    "dl",
    "voter",
    "passport",
    "local"
  ],
  "type": [
    "id"
  ],
  "validation_parser": "finite_values_entity",
  "values": [
    {
      "entity_type": "id",
      "value": "college"
    }
  ]
}
```

#### SAMPLE RESPONSE
```json
{
    "filled": true,
    "partially_filled": false,
    "trigger": '',
    "parameters": {
        "ids_stated": ["COLLEGE"]
    }
}
```

### API 2 (POST API to validate a slot with a numeric value extracted and constraints on the value extracted.)
#### SAMPLE REQUEST
```json
{
  "invalid_trigger": "invalid_age",
  "key": "age_stated",
  "name": "age",
  "reuse": true,
  "pick_first": true,
  "type": [
    "number"
  ],
  "validation_parser": "numeric_values_entity",
  "constraint": "x>=18 and x<=30",
  "var_name": "x",
  "values": [
    {
      "entity_type": "number",
      "value": 23
    }
  ]
}
```

##### SAMPLE RESPONSE
```json
{
    "filled": true,
    "partially_filled": false,
    "trigger": '',
    "parameters": {
        "age_stated": 23
    }
}
```
