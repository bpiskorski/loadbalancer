from flask import Flask
import os 

app = Flask(__name__)
server_id = os.environ.get('SERVER_NAME')
@app.route("/")
def str():    
    return "Testing load balancer \nusing server: " + server_id

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)