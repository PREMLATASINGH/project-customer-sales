import io
import pandas as pd
import numpy as np
from flask import Flask, jsonify, send_file
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

CSV_PATH = 'customer_sales_5000.csv'

app = Flask(__name__)

def load_df():
    return pd.read_csv(CSV_PATH)

@app.route('/')
def summary():
    df = load_df()
    head = df.head().to_dict(orient='records')
    stats = {}
    if 'total_amount' in df.columns:
        s = df['total_amount']
        stats = {
            'mean': float(s.mean()),
            'median': float(s.median()),
            'min': float(s.min()),
            'max': float(s.max()),
            'std': float(s.std())
        }
    payment = {}
    if 'payment_method' in df.columns and 'total_amount' in df.columns:
        grp = df.groupby('payment_method')['total_amount']
        payment = {
            'sum': grp.sum().to_dict(),
            'mean': grp.mean().to_dict(),
            'count': grp.count().to_dict()
        }
    return jsonify({'head': head, 'stats': stats, 'payment': payment})

@app.route('/hist.png')
def hist():
    df = load_df()
    if 'total_amount' not in df.columns:
        return jsonify({'error': 'no total_amount column'}), 400
    buf = io.BytesIO()
    plt.figure()
    plt.hist(df['total_amount'].dropna(), bins=20)
    plt.xlabel('Total Amount')
    plt.ylabel('Frequency')
    plt.title('Distribution of Total Amount')
    plt.tight_layout()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
