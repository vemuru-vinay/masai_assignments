# api-security — Weather Alert Script

A secure, production-ready weather fetching script built for a healthcare clinic
environment using the [OpenWeatherMap API](https://openweathermap.org/api).

---

## Setup

### 1. Install dependencies
```bash
pip install requests python-dotenv
```

### 2. Configure your API key
```bash
cp .env.example .env
# Open .env and replace the placeholder with your real API key
```

### 3. Run
```bash
python weather.py
```

---

## Security & Privacy Q&A

### What are the real-world consequences of exposing an API key on GitHub?

When an API key is pushed to a public GitHub repository, automated bots scan for
it within seconds and can begin abusing it immediately. The consequences include
unexpected billing charges (some APIs charge per call), service suspension by the
provider, data breaches if the key grants access to sensitive resources, and
reputational or legal liability for the organisation. In a healthcare context,
compromised keys can expose patient-adjacent data and result in HIPAA violations
carrying fines of up to $1.9 million per violation category per year.

### Why does your company's privacy policy prohibit logging city names?

Location data — even a city name — is considered personal data under the GDPR
and can be classified as Protected Health Information (PHI) under HIPAA when it
is associated with a patient interaction in a healthcare setting. Logging it
creates a persistent record of a user's whereabouts that could be subpoenaed,
leaked, or misused. The data minimisation principle (GDPR Article 5) requires
that only data strictly necessary for the service be collected and retained;
since the city name is needed only for a single API call and not for any
downstream purpose, it must not be stored or logged.

---

## Security Measures Implemented

| Task | What was done |
|------|--------------|
| **Task 1 — API Key** | Removed hardcoded key; loaded securely from `.env` via `python-dotenv`. `.env` is excluded from Git via `.gitignore`. |
| **Task 2 — Rate Limiting** | HTTP status codes (429, 401, 404, and others) are checked explicitly; user sees a clean, friendly message instead of a crash. |
| **Task 3 — Privacy** | Removed the `print(f"Fetching weather for: {city}...")` log line. A detailed comment in `weather.py` explains the GDPR/HIPAA rationale. |

---

## File Structure

```
api-security/
├── weather.py          # Main script
├── .env.example        # Template — copy to .env and add your key
├── .env                # Your real key — NOT committed (see .gitignore)
├── .gitignore          # Ensures .env is never tracked by Git
└── README.md           # This file
```
