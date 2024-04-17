import pytest
from unittest.mock import patch, MagicMock
import prediction  

# Mock data
mocked_tokenizer_data = {"1": "happy", "2": "sad"}  # Simplified example
mocked_model_prediction = [[0.8]]  

@pytest.fixture
def mock_load_model():
    with patch('prediction.load_model') as mock:
        yield mock

@pytest.fixture
def mock_tokenizer():
    with patch('prediction.tokenizer_from_json', return_value=mocked_tokenizer_data) as mock:
        yield mock

@pytest.fixture
def mock_predict():
    with patch.object(prediction.model, 'predict', return_value=mocked_model_prediction) as mock:
        yield mock

def test_predict_bipolarity_bipolar(mock_load_model, mock_tokenizer, mock_predict):
    result = prediction.predict_bipolarity("I feel extremely happy today")
    assert result['classification'] == 'Bipolar'
    assert 'probability' in result
    assert isinstance(result['probability'], float)

def test_predict_bipolarity_non_bipolar():
    # Mock the external dependencies
    with patch('prediction.load_model') as mock_load_model, \
         patch('prediction.tokenizer_from_json') as mock_tokenizer, \
         patch.object(prediction.model, 'predict', return_value=[[0.3]]) as mock_predict: 
        
        result = prediction.predict_bipolarity("I feel good")
        assert result['classification'] == 'Non-Bipolar'
