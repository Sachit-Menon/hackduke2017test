import keras
import os
from flask import Flask, render_template, request

app = Flask(__name__)
UPLOAD_FOLDER = "/Users/ZhipingLu/Downloads/hackduke2017test-master/production"
model_path = UPLOAD_FOLDER + '/models'

APP_ROOT = os.path.dirname(os.path.abspath(__file__) )
@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'production/')
    print(target)

    if not os.path.isdir(target):
        os.mkrdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
    final_model = model.load(model_path + 'final.h5')

    production_path = 'production/'
    batch = get_batches(production_path, batch_size=1, shuffle=False)
    predictions = final_model.predict(batch, batch_size=1)
    print(predictions)
        
    return render_template("complete.html")
if __name__=="__main__":
    app.run(host="0.0.0.0")