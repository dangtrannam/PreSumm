import torch
import collections
import torch.optim
import argparse
from contextlib import contextmanager

@contextmanager
def safe_model_loading():
    """Context manager to temporarily allow all required globals for model loading."""
    # Since add_safe_globals is not available in PyTorch 1.13.1,
    # we'll just yield the context and let PyTorch handle deserialization
    try:
        yield
    finally:
        pass 