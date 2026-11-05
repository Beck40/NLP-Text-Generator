"""Export token-frequency and training-loss visuals."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def generate(output_dir="assets/charts"):
    out=Path(output_dir); out.mkdir(parents=True,exist_ok=True)
    fig,ax=plt.subplots(figsize=(8,5)); ax.bar(["the","of","and","to","in"],[100,82,75,64,58],color="#17becf"); ax.set(title="Most frequent training tokens",ylabel="Count"); fig.tight_layout(); fig.savefig(out/"01_token_distribution.png",dpi=160); plt.close(fig)
    fig,ax=plt.subplots(figsize=(8,5)); epochs=np.arange(1,21); ax.plot(epochs,np.exp(-epochs/7)+.05,marker="o",color="#e377c2"); ax.set(title="Training loss",xlabel="Epoch",ylabel="Loss"); fig.tight_layout(); fig.savefig(out/"02_training_loss.png",dpi=160); plt.close(fig)

if __name__=="__main__": generate()
