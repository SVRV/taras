from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def google_map():
    files = {'study': 'study.csv', 'science': 'science.csv', 'work': 'work.csv'}

    data = {}
    for filename, filepath in files.iteritems():
        file = csv.reader(open('files/' + filepath, 'r'))
        headers = file.next()
        entries = []
        for line in file:
            entries.append(dict((unicode(key, 'utf-8').strip(), unicode(value, 'utf-8').strip()) for key, value in dict(zip(headers, line)).iteritems() if key))
        data[filename] = entries

    return render_template('map.html', data=data)

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