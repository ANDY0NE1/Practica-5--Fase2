from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Mi App Flask en Render</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    text-align: center;
                    background-color: #f0f0f0;
                }
                h1 {
                    color: #333;
                }
                .container {
                    background-color: white;
                    padding: 30px;
                    border-radius: 10px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 Práctica PaaS - Computación en la Nube</h1>
                <p>¡Aplicación Flask desplegada exitosamente en Render!</p>
                <p><strong>Modelo de servicio:</strong> Plataforma como Servicio (PaaS)</p>
                <p>Esta es una aplicación web simple para demostrar el despliegue en Render.</p>
            </div>
        </body>
    </html>
    """

@app.route('/info')
def info():
    return {
        'mensaje': 'API de ejemplo para práctica PaaS',
        'estudiante': 'ANDYONE1',
        'modelo': 'PaaS - Render',
        'estado': 'funcionando'
    }

if __name__ == '__main__':
    app.run(debug=True)
