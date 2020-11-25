
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
        <body>
            <h1>view app info at /health</h1>
        </body>
    </html>'''
@app.route('/health')
def health():
    appName = {'appName': 'TechChallenge'}
    version = {'version': 'Version 1.0'}
    dockerDigest = {'dockerDigest': '01d9d006ea042eecc60ec71b7dd4dcd137602206e4a2dd4757479e7d92adb136'}
    return '''
    <html>
        <head>
            <title> Health - Techchallenge</title>
        </head>
        <body>
            <h1> App Name: ''' + appName['appName'] + '''</h1>
            <h1> Version: ''' + version['version'] + '''</h1>
            <h1> dockerDigest: ''' + dockerDigest['dockerDigest'] + '''</h1>
        </body>
    </html>'''

if __name__ == "__main__":
    app.run(host="0.0.0.0")