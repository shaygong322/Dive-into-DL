Q1：reshape和view的区别？  
View为浅拷贝，只能作用于连续型张量；Contiguous函数将张量做深拷贝并转为连续型；Reshape在张量连续时和view相同，不连续时等价于先contiguous再view。  

Q2：数组计算吃力怎么办？  
学习numpy的知识。  

Q3：如何快速区分维度？  
利用a.shape或a.dim()。  

Q4：Tensor和Array有什么区别？  
Tensor是数学上定义的张量，Array是计算机概念数组，但在深度学习中有时将Tensor视为多维数组。  

Q5：新分配了y的内存，那么之前y对应的内存会自动释放吗？  
Python会在不需要时自动释放内存。