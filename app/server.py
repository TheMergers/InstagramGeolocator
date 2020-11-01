import os
from flask import Flask, request, send_from_directory, render_template
#from instagram import instagram_downloader, coordinates_extractor

here = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    "InstagramGeolocator",
    static_folder=os.path.join(here, "static"),
    template_folder=os.path.join(here, "templates"),
)

@app.route('/')
def root():
    name = request.args.get("name")
    return render_template(
        "index.html",
        name=name
    )

#@app.route('/run')
#def run():
#    pass

if __name__ == "__main__":
    # set the project root directory as the static folder, you can set others.
    #os.environ["FLASK_APP"] = "app"
    app.run(debug=True)