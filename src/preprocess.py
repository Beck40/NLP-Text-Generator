"""Tokenise a training corpus for next-word modelling."""
from collections import Counter
import re


def tokenize(text: str) -> list[str]:
    return re.findall(r"[A-Za-z']+", text.lower())


def build_vocabulary(tokens, min_count=1):
    counts=Counter(tokens); words=[w for w,c in counts.items() if c >= min_count]
    return {word:i+1 for i,word in enumerate(sorted(words))}

