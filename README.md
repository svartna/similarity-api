# Similarity API

Small and lightweight backend service that computes
similarity scores between items provided by a user based
on their personal numeric and categorical features

It is meant to be general and reusable, for multiple types
of uses and cases in which you might need data cross referenced
inside a matrix of key values

It is derived from my recommendation logic used in my [Spotify
Recommendation Engine](github.com/svartna/spotify-recommendation-engine)

Instead of only comparing spotify songs data,it now accepts any dataset
that is formatted as pairs of items with named features

## How it works

- uses FastAPI and is served by uvicorn
- Able to take in lists of items populated by ids and dictionaries
of features
- if there is a missing feature in a given item, it will be saved as
a 0 (using pandas feature) so items with varying features are still able
to be compared
- computes using the cosine similarity function across the items and returns a
fully calculated similarity matrix

## Setup

- Clone the repo and create a virtual environment

```zshrc
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- Run the server:

```zshrc
uvicorn main:app --reload
```

- Navigate to `http://127.0.0.1:8000/docs` to use the
interactive API documentation

## Example request

```json
POST /similarity
{
  "items": [
    {"id": "song1", "features": {"duration": 0.3, "pop": 1, "rock": 0}},
    {"id": "song2", "features": {"duration": 0.4, "pop": 1, "rock": 0}},
    {"id": "song3", "features": {"duration": 0.9, "pop": 0, "rock": 1}}
  ]
}
```

## Limitations

- returns a full matrix instead of just a ranked list of top-N results (coming soon!)
- no limiting for rate or authentication service
- the values must be encoded before being compared, the api does not encode your
data before using it

## License

MIT
