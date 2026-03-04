"""LLM服务模块 - 使用本地 Ollama 模型（Metal 加速）

本模块通过 Ollama 提供的 OpenAI 兼容 API 访问本地模型，无需任何云端 API。
运行前请确保 Ollama App 已启动，且已执行：ollama pull qwen2.5:32b

本地服务器信息:
  模型: qwen2.5:32b  (~20GB, Q4_K_M 量化，Metal GPU 加速)
  接口: http://127.0.0.1:11434/v1  (OpenAI 兼容格式)
"""

from hello_agents import HelloAgentsLLM
from ..config import get_settings

# 全局LLM实例
_llm_instance = None


def get_llm() -> HelloAgentsLLM:
    """
    获取LLM实例(单例模式)

    通过环境变量 OPENAI_BASE_URL / OPENAI_MODEL 连接本地 MLX 服务器。
    需先运行 start_mlx_server.sh。

    Returns:
        HelloAgentsLLM实例
    """
    global _llm_instance

    if _llm_instance is None:
        settings = get_settings()

        # 直接传入参数并指定 provider='custom'，确保使用本地 Ollama 服务
        # HelloAgentsLLM 读取 LLM_* 前缀变量，不读取 OPENAI_* 变量
        _llm_instance = HelloAgentsLLM(
            model=settings.openai_model,
            api_key=settings.openai_api_key,
            base_url=settings.openai_base_url,
            provider="custom",
            max_tokens=4096,
            timeout=3600,  # 设为1小时，避免默认60秒超时
        )

        print(f"✅ LLM服务初始化成功（本地 Ollama 模型，Metal 加速）")
        print(f"   服务地址: {settings.openai_base_url}")
        print(f"   模型: {settings.openai_model}")

    return _llm_instance


def reset_llm():
    """重置LLM实例(用于测试或重新配置)"""
    global _llm_instance
    _llm_instance = None

