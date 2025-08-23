#!/usr/bin/env python3
import os
import subprocess
import sys

def generate_proto_code():
    proto_dir = "protos"
    output_dir = "src/generated"

    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)

    # 创建 __init__.py 文件
    init_file = os.path.join(output_dir, "__init__.py")
    if not os.path.exists(init_file):
        with open(init_file, "w") as f:
            f.write("# Generated package\n")

    # 生成代码
    cmd = [
        sys.executable, "-m", "grpc_tools.protoc",
        f"-I{proto_dir}",
        f"--python_out={output_dir}",
        f"--pyi_out={output_dir}",
        f"--grpc_python_out={output_dir}",
        os.path.join(proto_dir, "user_service.proto")
    ]

    print("Running:", " ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print("✓ Proto files generated successfully!")
        # 检查生成的文件
        generated_files = [
            "user_service_pb2.py",
            "user_service_pb2.pyi",
            "user_service_pb2_grpc.py"
        ]
        for file in generated_files:
            file_path = os.path.join(output_dir, file)
            if os.path.exists(file_path):
                print(f"✓ {file} generated")
            else:
                print(f"✗ {file} not found")
    else:
        print("✗ Code generation failed:")
        print(result.stderr)
        return False

    return True


if __name__ == "__main__":
    success = generate_proto_code()
    sys.exit(0 if success else 1)