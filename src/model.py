"""Small, framework-independent next-token baseline."""
from collections import defaultdict, Counter


class NGramModel:
    def __init__(self, order=2):
        self.order=order; self.counts=defaultdict(Counter)

    def fit(self, tokens):
        for i in range(len(tokens)-self.order+1):
            self.counts[tuple(tokens[i:i+self.order-1])][tokens[i+self.order-1]] += 1
        return self

    def next_token(self, context):
        options=self.counts.get(tuple(context[-(self.order-1):]), Counter())
        return options.most_common(1)[0][0] if options else None

