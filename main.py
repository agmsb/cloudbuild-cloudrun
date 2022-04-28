from flask import Flask
import os
import random

app = Flask(__name__)
version = os.environ.get('VERSION')


products = ['BigQuery', 
            'Kubernetes Engine', 
            'Cloud Build', 
            'Cloud Run', 
            'Virtual Private Cloud',
            'Compute Engine', 
            'Cloud Dataflow']

@app.route('/')
def hello_product():
    product = random.choice(products)
    message = """
Which Google Cloud product are you?
Version: {version}

Your Google Cloud product is: {product}!
""".format(version=version, product=product)

    return(message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)