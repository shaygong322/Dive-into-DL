[Data-Manipulation](Data-Manipulation.ipynb)
+ Tensor 的创建
+ Tensor 的基本操作：算术操作，索引，改变形状（view，reshape，clone，item），Concatenation，==，.sum
+ Tensor 的广播机制
+ 运算的内存开销
+ Tensor 的类型转换（主要是 NumPy）
+ Tensor on GPU

[Data-Preprocessing](Data-Preprocessing.ipynb) 参考原书，数据预处理
+ 创建 csv 文件
+ 读取 csv 文件
+ 缺失值处理
+ 转换成 Tensor

[Automatic-Differentiation](Automatic-Differentiation.ipynb) 自动求梯度，使用 PyTorch 的 autograd 包
```python
y.backward() # 如果`y`是标量，则不需要为`backward()`传入任何参数；否则，需要传入一个与`y`同形的`Tensor`。
x.grad # `x.grad`是`x`的梯度，注意grad是累加的
```
+ Tensor 的 `requires_grad` 属性, `grad` 属性, `grad_fn` 属性
+ 求梯度
    + 只允许标量对张量求导
    + 中断梯度追踪 `with torch.no_grad()`
    + 对`tensor.data`进行操作：想要修改`tensor`的数值，又不希望被`autograd`记录