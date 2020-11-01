from flask import Flask, request, send_from_directory, render_template
from instagram import instagram_downloader, coordinates_extractor

app = Flask(
    "InstagramGeolocator",
    static_url_path="",
    template_folder="templates",
)

#@app.route('/js/<path:path>')
#def send_js(path):
#    return send_from_directory('js', path)

@app.route('/')
def root():
    name = request.args.get("name")
    return render_template('index.html', name=name)
    #return app.send_static_file('./templates/index.html')

@app.route('/run')
def run():
    pass

if __name__ == "__main__":
    # set the project root directory as the static folder, you can set others.
    app.run()