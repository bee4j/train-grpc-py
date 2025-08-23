1、Protocol Buffers, 简称 Protobuf，protoc编译器，将.proto文件编译成特定语言代码，以便在代码中方便地序列化和反序列化数据
1.1 官方下载地址 https://github.com/protocolbuffers/protobuf/releases
1.2 配置环境变量 
1.3 验证环境变量 输入命令 protoc --version
1.4 安装依赖工具 pip install grpcio grpcio-tools

2、创建gRPC接口的两种方式
2.1 输入命令
2.2 执行脚本

3、gRPC服务接口
3.1 编写.proto文件，定义服务和消息类型
3.2	编译Py代码，在项目根目录输入命令 python -m grpc_tools.protoc -I./protos --python_out=./src/generated --pyi_out=./src/generated --grpc_python_out=./src/generated ./protos/user_service.proto
3.3 编写gRPC接口内部逻辑
3.4	启动gRPC服务
3.5	测试gRPC服务

4、gRPC服务调用