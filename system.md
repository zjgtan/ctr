# 系统设计文档
## 监控模块

监控变量  
1. loss: 训练集、测试集
2. 测试集auc  

监控类： TraceService  
接口：traceTrainLoss traceTestLoss traceTestAuc  

tensorboard使用  
1. 初始化  
```python
from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter('/path/to/logdir')
```
2. 添加标量
```python
writer.add_scalar('training loss', 纵坐标, 横坐标)
```

3. 通过页面查看
```python
tensorboard --logdir=/path/to/logdir
```