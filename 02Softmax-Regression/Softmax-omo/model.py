from torch import nn
import torch

class SoftmaxGST(nn.Module):
    def __init__(self, num_inputs, num_outputs):
        super(SoftmaxGST, self).__init__()
        self.linear = nn.Linear(num_inputs, num_outputs)
    def forward(self, x): # x shape: (batch, 1, 28, 28)
        y = self.linear(x.view(x.shape[0], -1))
        return y
