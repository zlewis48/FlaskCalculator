from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('calculator.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data['expression']
    try:
        # Securely evaluate the expression
        result = str(eval(expression))
    except Exception as e:
        result = "Error"
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)