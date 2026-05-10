# GrowHub.ai — Flask Edition

A pure HTML + CSS website with a **Python (Flask)** backend. No JavaScript build step, no React — just templates and a tiny API.

## Structure

```
growhub-flask/
├── app.py                 # Flask backend (routes + form APIs)
├── requirements.txt       # Python deps
├── templates/             # HTML pages (Jinja-rendered)
│   ├── index.html
│   ├── services.html
│   ├── results.html
│   ├── process.html
│   ├── proof.html
│   ├── booking.html
│   └── contact.html
├── static/
│   └── css/style.css      # Shared design system
└── data/                  # Auto-created: contacts.json, bookings.json
```

## Run locally

```bash
cd growhub-flask
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open **http://127.0.0.1:5000**

## Routes

| Path           | Purpose                          |
|----------------|----------------------------------|
| `/`            | Home                             |
| `/services`    | Services                         |
| `/results`     | Results                          |
| `/process`     | Process                          |
| `/proof`       | Proof                            |
| `/booking`     | Book a call                      |
| `/contact`     | Contact                          |
| `/api/contact` | POST — saves to `data/contacts.json` |
| `/api/booking` | POST — saves to `data/bookings.json` |
| `/api/health`  | Health check                     |

## Forms

Both `contact.html` and `booking.html` post to the API endpoints. Submissions are appended to JSON files in `data/`. Swap that for a real DB (Postgres, SQLite, Mongo) when you're ready — the handlers are 5 lines each.
