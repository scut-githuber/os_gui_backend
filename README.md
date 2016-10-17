# os-gui-backend
操作系统-GUI平台实现组-后端

- Python3 · Django 1.10
- 用MySQL做数据库
- 开发环境：Linux(Ubuntu) + PyCharm
- [doc](doc/README.md)目录里是一些重要的文档
- app is legoc，意为 乐高积木般组合的C代码
- legoc目录中
  - cadapter：放与util组交互的代码
  - control：放控制层代码，这里之后根据需求还会做横向分层
  - db：放数据库操作代码
  - util：放业务逻辑无关的工具代码
- views.py一定一定不要写控制层代码，只能写：
  - 参数检验（最好也放到控制层）
  - 对control中代码的调用
  - 响应

- 前后端交互数据使用JSON

- 接口见wiki
