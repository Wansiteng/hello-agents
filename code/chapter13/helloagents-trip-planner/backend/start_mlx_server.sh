#!/bin/bash
# 启动本地 MLX 模型服务器
# 提供 OpenAI 兼容 API，端口 8080
#
# 使用方法：
#   chmod +x start_mlx_server.sh
#   ./start_mlx_server.sh

MODEL="mlx-community/Qwen2.5-7B-Instruct-4bit"
HOST="127.0.0.1"
PORT=8080

echo "========================================"
echo " 启动本地 MLX 模型服务器"
echo " 模型: $MODEL"
echo " 地址: http://$HOST:$PORT/v1"
echo "========================================"

python -m mlx_lm server \
    --model "$MODEL" \
    --host "$HOST" \
    --port "$PORT" \
    --max-tokens 4096
