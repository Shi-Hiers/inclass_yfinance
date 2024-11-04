from flask import Blueprint, render_template, request
import yfinance as yf

stocks_bp = Blueprint('stocks', __name__)

@stocks_bp.route('/stocks', methods=['GET', 'POST'])
def get_stock_price():
    stock_data = None
    ticker = None

    if request.method == 'POST':
        ticker = request.form.get('ticker')
        if ticker:
            stock = yf.Ticker(ticker)
            stock_data = stock.history(period="1d")
            if not stock_data.empty:
                stock_data.reset_index(inplace=True)
                stock_data = stock_data.to_dict('records')

    return render_template('stocks.html', stock_data=stock_data, ticker=ticker)
