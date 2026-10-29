from flask import Flask, request, jsonify
from app import calculate_total, calculate_discounted_total

app = Flask(__name__)

@app.get("/")
def home():
    return {
        "message": "Shopping Bill Calculator API",
        "options": [
            "GET /bill?price=10&quantity=2",
            "GET /discount?price=10&quantity=2&discount=10"
        ]
    }

@app.get("/bill")
def bill():
    price = float(request.args.get("price", 0))
    quantity = int(request.args.get("quantity", 0))
    total = calculate_total(price, quantity)
    return jsonify({"subtotal": total})

@app.get("/discount")
def discounted_bill():
    price = float(request.args.get("price", 0))
    quantity = int(request.args.get("quantity", 0))
    discount = float(request.args.get("discount", 10))
    subtotal, discount_amount, final_total = calculate_discounted_total(price, quantity, discount)
    return jsonify({
        "subtotal": subtotal,
        "discount_amount": discount_amount,
        "final_total": final_total
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)