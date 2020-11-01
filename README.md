[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# InstagramGeolocator

Download your Instagram data and geolocate your photos

## Modules

```
pip install instaloader
pip install -U Flask
pip install geopy
```

## Usage

### How to run

- Ensure your Instagram profile is public
- Download this project as zip or place everything in the same folder
- Open a terminal/cmd inside the folder and run a `npm install`
- Now run `python app/server.py`
- Open your favourite browser and look for `http://127.0.0.1:5000/`
- Submit your Instagram username
- Wait depending on the number of posts you have. You can track the process looking at the terminal.

### How to exit

<strong>Windows</strong>
- CTRL + C
- Run `netstat -ano | findstr :5000`
- Look for the PID
- Run `taskkill /PID your_PID /F`

<strong>Unix</strong>
- CTRL + C
- Or use `pkill`

## Contributing

Any contribution or help is appreciated
