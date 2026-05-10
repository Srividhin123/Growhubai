"""
GrowHub.ai — Flask backend
Run: python app.py
Then open: http://127.0.0.1:5000
"""
import json
import os
from datetime import datetime
import flask

app = flask.Flask(__name__)
app.secret_key = "growhub-dev-secret-change-me"

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)
CONTACTS_FILE = os.path.join(DATA_DIR, "contacts.json")
BOOKINGS_FILE = os.path.join(DATA_DIR, "bookings.json")


def _load(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def _save(path, items):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)


# ---------- page routes ----------
@app.route("/")
def home():
    return flask.render_template("index.html")


@app.route("/services")
def services():
    return flask.render_template("services.html")


@app.route("/results")
def results():
    return flask.render_template("results.html")


@app.route("/process")
def process():
    return flask.render_template("process.html")


@app.route("/proof")
def proof():
    return flask.render_template("proof.html")


@app.route("/booking")
def booking():
    return flask.render_template("booking.html")


@app.route("/contact")
def contact():
    return flask.render_template("contact.html")


# ---------- form endpoints ----------
@app.route("/api/contact", methods=["POST"])
def api_contact():
    data = flask.request.form.to_dict() or flask.request.get_json(silent=True) or {}
    required = ["name", "email", "message"]
    if not all(data.get(k) for k in required):
        return flask.jsonify({"ok": False, "error": "Missing required fields"}), 400
    entry = {
        "name": data.get("name"),
        "email": data.get("email"),
        "company": data.get("company", ""),
        "message": data.get("message"),
        "received_at": datetime.utcnow().isoformat() + "Z",
    }
    items = _load(CONTACTS_FILE)
    items.append(entry)
    _save(CONTACTS_FILE, items)
    if flask.request.is_json:
        return flask.jsonify({"ok": True, "message": "Message received."})
    return flask.render_template("contact.html", success=True)


@app.route("/api/booking", methods=["POST"])
def api_booking():
    data = flask.request.form.to_dict() or flask.request.get_json(silent=True) or {}
    required = ["name", "email", "date", "time"]
    if not all(data.get(k) for k in required):
        return flask.jsonify({"ok": False, "error": "Missing required fields"}), 400
    entry = {
        "name": data.get("name"),
        "email": data.get("email"),
        "company": data.get("company", ""),
        "date": data.get("date"),
        "time": data.get("time"),
        "notes": data.get("notes", ""),
        "received_at": datetime.utcnow().isoformat() + "Z",
    }
    items = _load(BOOKINGS_FILE)
    items.append(entry)
    _save(BOOKINGS_FILE, items)
    if flask.request.is_json:
        return flask.jsonify({"ok": True, "message": "Booking confirmed."})
    return flask.render_template("booking.html", success=True)


@app.route("/api/health")
def health():
    return flask.jsonify({"status": "ok", "service": "growhub.ai", "time": datetime.utcnow().isoformat() + "Z"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
