## The following code will import the necessary libraries, create the paths to the correct places, load a model, and use it to evaluate a single image put in production. What you guys need to do is put it into a Flask server that simply takes in the image the user uploads, places it in 'production/', and runs this code. https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world has most things you'd want to know about flask. So... yeah. Test it by commenting out everything below and instead including a print("It worked!") statement that runs when this code should run. I'll provide the model that will make it work in the morning. 

import utils; reload(utils)
from utils import *

path = "data/nails/"
model_path = path + 'models/'

final_model.load(model_path + 'final.h5')

production_path = 'production/'
batch = get_batches(production_path, batch_size = 1, shuffle = False)
predictions = final_model.predict(batch, batch_size = 1)
print(predictions)