from flask import Flask, render_template, request, flash, redirect, send_from_directory, jsonify
import csv 
import json

app = Flask(__name__)

@app.route("/main")
def main():
    return render_template("main_layout.html")

def custom_static(filename):
    return send_from_directory('static', filename)

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/riwayat")
def riwayat():
    return render_template("riwayat.html")

@app.route("/cv")
def cv():
    return render_template("cv.html")

@app.route("/portofolio")
def portofolio():
    return render_template("portofolio.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")



#CSV to JSON
def csv_to_json(file):
    with open(file, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        field_names = next(csv_reader)

        data = []
        for row in csv_reader:
            data.append(dict(zip(field_names, row)))

    return jsonify(data)

@app.route("/csvtojson", methods=["GET"])
def csvtojson():
    jsondata = None

    csv_file_path = r"C:\Users\Zoen\Documents\SCHOOL\1 U N A I R\3 SEMESTER 3\A L P R O 2\W10\datapribadi.csv"

    try:
        jsondata = csv_to_json(csv_file_path).get_data(as_text=True)  

    except Exception as e:
        flash(f'Error: {str(e)}')

    return render_template("csvtojson.html", jsondata=jsondata)

#Fibonaci
def fibonaci(limit):
    sequence = [0, 1]
    for i in range(2, limit):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

@app.route("/fibo", methods=['GET', 'POST'])
def fibo():
    result = None

    if request.method == 'POST':
        limit = int(request.form['limit'])
        result = fibonaci(limit)

    return render_template("fibo.html", result=result)


#Form
@app.route("/form", methods=['POST'])
def form():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    return render_template("form.html", first_name=first_name, last_name=last_name, email=email)

@app.route("/formulir")
def formulir():
    return render_template("formulir.html")


