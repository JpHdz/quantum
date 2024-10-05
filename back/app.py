from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

app = Flask(__name__)
CORS(app)
@app.route('/run', methods=['POST'])
def run_code():
    code = request.json.get('code')
    try:
        # Running the code in a subprocess (use Docker for better isolation)
        venv_python = 'C:/Users/jpnat/OneDrive/Documentos/IDEBothSides/back/venv/Scripts/python.exe'
        result = subprocess.run([venv_python,'py', '-c', code], capture_output=True, text=True, timeout=5)
        output = result.stdout if result.stdout else result.stderr
        return jsonify({'output': output})
    except subprocess.TimeoutExpired:
        return jsonify({'output': 'Error: Code execution timed out.'})
    except Exception as e:
        return jsonify({'output': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
