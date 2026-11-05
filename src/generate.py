"""Generate text from the fitted n-gram baseline."""
from .model import NGramModel


def generate(model: NGramModel, prompt: str, steps=30) -> str:
    tokens=prompt.split()
    for _ in range(steps):
        token=model.next_token(tokens)
        if token is None: break
        tokens.append(token)
    return " ".join(tokens)

