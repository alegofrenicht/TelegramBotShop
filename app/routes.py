from app import app


@app.route('/')
@app.route('/health')
def health():
    return "ok"
