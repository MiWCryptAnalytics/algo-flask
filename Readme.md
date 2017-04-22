algo-flask

Simple python flask http application to provide UI for algo backend.

requires:
flask
flaskwtf
flask-bootstrap

1. Copy algo main script to repo folder
2. Run generate.py to parse algo and generate forms from strings
3. run run.py to run port 5000

Routes defined:

return ("Algo VPN Cloud Factory")

```
@app.route('/algo', methods=['GET', 'POST'])
@app.route('/roles', methods=['GET', 'POST'])
@app.route('/do', methods=['GET', 'POST'])
@app.route('/azure', methods=['GET', 'POST'])
@app.route('/aws', methods=['GET', 'POST'])
@app.route('/gce', methods=['GET', 'POST'])
@app.route('/noncloud', methods=['GET', 'POST'])
@app.route('/user', methods=['GET', 'POST'])
```


This app doesnt yet work. It is just some forms. (2017-04-21)
