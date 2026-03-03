"""启动脚本"""

import sys
import uvicorn
from app.config import get_settings

# 强制无缓冲输出，确保日志实时可见
sys.stdout.reconfigure(line_buffering=True)
sys.stderr.reconfigure(line_buffering=True)

if __name__ == "__main__":
    settings = get_settings()
    
    uvicorn.run(
        "app.api.main:app",
        host=settings.host,
        port=settings.port,
        reload=False,  # 关闭reload避免子进程吞掉日志
        log_level=settings.log_level.lower()
    )

