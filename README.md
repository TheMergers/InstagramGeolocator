# InstagramGeolocator

Download your Instagram data and geolocate your photos

## Modules

```
pip install geopy
pip install instaloader
pip install json
```

## Usage

- Ensure your profile is public
- Set your public porfile name in `instagram_downloader.py`
- Set your public porfile name in `coordinates_extracor.py`
- Set a [Mapbox](https://account.mapbox.com/access-tokens/) token in `geolocator.html`
- Download this project as zip or place everything in the same folder
- Run `instagram_downloader.py` to extract your Instagram data
- Re-running `instagram_downloader.py` will download your new published posts
- Run `coordinates_extractor.py`, `coords.txt` will be created
- Open `geolocator.html` in a browser
- Up-left on the webpage, upload `coords.txt`

## Contributing

It's the first time I'm using HTML/CSS/JavaScript in a project, any help or
correction is appreciated
