# Hotel Booking API

## Usage

1. Install dependencies:

    pip install -r requirements.txt

2. Run the API:

    python main.py

3. Access endpoints:
- Interactive docs: http://localhost:8000/docs
- Health check: http://localhost:8000/

Example POST request to /ask:

    curl -X POST http://localhost:8000/ask -H "Content-Type: application/json" -d '{"question": "What is the average room rate?"}'
