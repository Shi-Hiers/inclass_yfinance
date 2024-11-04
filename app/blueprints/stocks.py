from flask import Blueprint, render_template, request
import yfinance as yf

stocks_bp = Blueprint('stocks', __name__)

@stocks_bp.route('/stocks', methods=['GET', 'POST'])
def get_stock_price():
    stock_data = None
    if request.method == 'POST':
        ticker = request.form.get('ticker')
        if ticker:
            stock = yf.Ticker(ticker)
            stock_data = stock.history(period="1d")
    return render_template('stocks.html', stock_data=stock_data)