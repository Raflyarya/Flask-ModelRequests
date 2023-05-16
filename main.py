from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/requests-1', methods=['POST'])
def requests_1():
    isi_pesan = request.json.get('word')
    return f"{isi_pesan}"

@app.route('/requests-2', methods=['POST'])
def requests_2():
    isi_pesan = request.headers.get('word')
    return f"{isi_pesan}"

@app.route('/requests-3', methods=['GET','POST'])
def requests_3():
    isi_pesan = request.args.get('word')
    return f"{isi_pesan}"

if __name__ == '__main__':
    app.run(debug=True)
