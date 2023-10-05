from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for auctions (in-memory storage, replace with a database)
auctions = []

@app.route('/')
def index():
    return render_template('index.html', auctions=auctions)

@app.route('/create_auction', methods=['GET', 'POST'])
def create_auction():
    if request.method == 'POST':
        item_name = request.form['item_name']
        start_price = float(request.form['start_price'])
        start_time = request.form['start_time']
        end_time = request.form['end_time']

        auction = {
            'item_name': item_name,
            'start_price': start_price,
            'start_time': start_time,
            'end_time': end_time,
            'bids': []
        }
        auctions.append(auction)

        return redirect(url_for('index'))

    return render_template('create_auction.html')
    

if __name__ == '__main__':
    app.run(debug=True)
