from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__, static_url_path='')

#@app.route('/js/<path:path>')
#def send_js(path):
#    return send_from_directory('js', path)

@app.route('/')
def root():
    name = "Ciccio"
    return render_template('/Users/mdeluca/_projects/__personal/InstagramGeolocator/app/templates/index.html', name=name)
    #return app.send_static_file('./templates/index.html')

if __name__ == "__main__":
    # set the project root directory as the static folder, you can set others.
    app.run()