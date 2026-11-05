from src.generate import generate
from src.model import NGramModel
from src.preprocess import build_vocabulary, tokenize


def test_tokenizer_and_vocabulary_handle_punctuation():
    tokens = tokenize("Hello, hello! Risk-aware generation.")
    assert tokens == ["hello", "hello", "risk", "aware", "generation"]
    assert build_vocabulary(tokens)["hello"] > 0


def test_generation_stops_when_context_is_unknown():
    model = NGramModel().fit(["risk", "models", "need", "controls"])
    assert generate(model, "unknown", steps=5) == "unknown"
