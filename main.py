from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def google_map():
    return render_template('map.html')

@app.route('/demand')
def demand():
    return render_template('demand.html')

@app.route('/ads')
def ads():
    return render_template('ads.html')

@app.route('/apps')
def apps():
    return render_template('apps.html')

@app.route('/extra')
def extra():
    return render_template('extra.html')

if __name__ == '__main__':
    app.debug = True
    app.run()