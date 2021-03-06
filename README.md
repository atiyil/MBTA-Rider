# MBTA-Rider
## Overview
A python restful command-line application to provide ride schedules using MBTA API at https://api-v3.mbta.com

## Prerequisites
- python v3.6 or later
- python package `requests` v2.25.1 or later
- python package `pytest` v6.2.2 or later

## Running
Unzip the package and run `python3 mbta_rider.py`

## Testing
'pytest' has been used for automated testing and several examples are provided. Feel free to add more cases.

## Assumptions
- Heavy rails are Orange, Red and Blue lines. Light rails are Green lines and Mattapan trolley.

## Design Decisions
- `json.loads` is preferred to `ast.literal_eval` in order to parse GET response. This is because MBTA uses a JSON API

## Future Development
- The application can be converted to a pip package for easy installation and support. `setup.py` must be defined
- While extending this project, library and utility functions can be defined in `util` folder and automated tests can be added to `tests` folder
- The command line application can be converted to a web application using `flask` or `django` for better user interaction
- More automated tests must be added
- More error and exception handling should be added
- More refactoring will be done