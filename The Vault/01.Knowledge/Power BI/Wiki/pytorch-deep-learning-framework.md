---
created: 2026-07-28
updated: 2026-08-02
source: Artificial Intelligence with Power BI (Diepeveen)
note_type: reference
tags: [pytorch, deep-learning, framework, reference]
---

# PyTorch — Deep Learning Framework Reference

Microsoft's open-source deep learning framework — widely used for custom neural network architectures.

## Quick Reference

```bash
pip install torch torchvision
```

## Core Concepts

| Concept | Description |
|---------|-------------|
| **Tensor** | Multi-dimensional array (like numpy array, GPU-accelerated) |
| **Autograd** | Automatic differentiation — computes gradients for backpropagation |
| **nn.Module** | Base class for all neural network layers |
| **DataLoader** | Batches, shuffles, and parallelises data loading |
| **GPU acceleration** | `.to('cuda')` moves tensors to GPU |

## Basic Example

```python
import torch
import torch.nn as nn

# Simple feedforward network
model = nn.Sequential(
    nn.Linear(10, 64),
    nn.ReLU(),
    nn.Linear(64, 1)
)

# Forward pass
x = torch.randn(32, 10)  # batch of 32, 10 features
output = model(x)         # shape: (32, 1)
```

## When to Use PyTorch

- Custom neural network architectures beyond standard layers
- Computer vision (CNNs) and NLP (transformers, LSTMs)
- Research and experimentation (dynamic computation graph)
- Integration with Azure ML via Python Script component

## Azure ML Integration

Azure ML Designer → Python Script component or Azure ML compute with PyTorch environment.

## Related

- [[deep-learning-artificial-neural-networks]]
- [[explain-black-box-models]]
