import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict_api(client):
    # Example input
    data = {"input": "Today has been a really good day."}
    response = client.post('/predict', json=data)

    assert response.status_code == 200
    assert 'classification' in response.json

    assert response.json == {'classification': 'Non-Bipolar', 'probability': 0.042039819061756134}