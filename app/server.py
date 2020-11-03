import os
from flask import Flask, request, send_from_directory, render_template, jsonify
from instagram.downloader import get_user_data
from instagram.extractor import dump_coordinates

here = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    "Nereus",
    root_path=here,
    static_folder=os.path.join(here, "static"),
    template_folder=os.path.join(here, "templates"),
)

@app.route('/')
def root():
    name = request.args.get("name")
    return render_template(
        "index.html",
        name=(name or "My Friend")
    )

@app.route('/run')
def run():
    ig_user = request.args.get("iguser")
    if not ig_user:
        raise ValueError("Provided an empty user. Please provide an user using '/run?iguser=<USERNAME>'")
    
    if not os.path.exists(os.path.join(here, "data/coords.txt")):
        get_user_data(ig_user)
        dump_coordinates(ig_user)

    coords = {}
    with open(os.path.join(here, "data/coords.txt"), "r") as f:
        for i, line in enumerate(f):
            lat, lng, place = line.split('\t')[:3]
            coords["coord_{}".format(i)] = {
                "lat": lat,
                "lng": lng,
                "place": place.replace("\"", "").strip()
            }

    return jsonify(coords)


if __name__ == "__main__":
    # set the project root directory as the static folder, you can set others.
    #os.environ["FLASK_APP"] = "app"
    app.run(debug=True)