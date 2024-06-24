import torch
from torch import nn
from tools import *


def evaluate_accuracy(test_loader, model, device):
    acc_sum, n = 0.0, 0
    model.eval()  # 将模型设置为评估模式，一次调用即可
    with torch.no_grad():  # 禁用梯度计算
        for X, y in test_loader:
            X, y = X.to(device), y.to(device)  # 将数据移动到设备
            y_hat = model(X)
            acc_sum += (y_hat.argmax(dim=1) == y).sum().item()
            n += y.shape[0]
    return acc_sum / n


def train(model, train_loader, test_loader, num_epochs):
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
    loss = nn.CrossEntropyLoss()
    device = get_device()

    train_l_sum, train_acc_sum, n = 0.0, 0.0, 0
    for epoch in range(num_epochs):
        train_l_sum, train_acc_sum, n = 0.0, 0.0, 0
        for X, y in train_loader:
            X, y = X.to(device), y.to(device)  # Move data to the device
            y_hat = model(X)
            l = loss(y_hat, y).sum()

            optimizer.zero_grad()
            l.backward()
            optimizer.step()

            train_l_sum += l.item()
            train_acc_sum += (y_hat.argmax(dim=1) == y).sum().item()
            n += y.shape[0]

        test_acc = evaluate_accuracy(test_loader, model, device)
        print('epoch %d, loss %.4f, train acc %.3f, test acc %.3f' % (epoch + 1, train_l_sum / n, train_acc_sum / n, test_acc))