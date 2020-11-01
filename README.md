[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

# InstagramGeolocator

Download your Instagram data and geolocate your photos.

# Setup your environment

This project uses python as backend and npm/JS as frontend.

To run the webapp locally you need to download and install python dependencies.
We suggest you to create an environment and then install dependencies in it.

You can create a python env using any of the tools available in the python ecosystem (e.g. virtualenv, pipenv ecc...).
If you use pipenv the project comes with a Pipfile defining project dependencies, otherwise you can use requirements file and install dependencies in the classic way using pip, by running `pip install -r requirements.txt`. 

If you plan to do some changes for the frontend, you will also have to install npm to manage javascript dependencies.
So you need to have npm installed on your machine and then install javascript dependencies running `npm install` at the root of the project.
This will download on your local machine all the node modules defined in the `package-lock.json` in a folder called `node_modules`.
If you do some changes to the frontend you have to recompile the bundled js. If you run the command `npm run watchJS &` (if you are on linux/mac the `&` at the end will run this process in background), this will detect the changes in `app/static/js/main.js` and compile a new file under `app/static/js/compiled/bundle.js`. 

### How to run

- Activate your python environment
- Start the web app starting the server with `python app/server.py`
- Open your favorite browser and look for `http://127.0.0.1:5000/` or `http://localhost:5000`
- Ensure your Instagram profile is public
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

Any contribution or help is appreciated.
