FROM python:3.12-bullseye

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential curl gnupg net-tools
    
# Node.jsの公式リポジトリを追加
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm@latest && \
    npm i -g @playwright/mcp@latest && \
    npx playwright install chrome

# Pythonパッケージのインストール
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir 'smolagents[openai,mcp,gradio]' && \
    # クリーンアップ
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 作業ディレクトリの設定
WORKDIR /app

# デフォルトコマンド
CMD ["python", "-c", "print('Container ready')"]