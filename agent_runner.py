from sandbox import DockerSandbox

# DockerSandboxのインスタンスを作成
sandbox = DockerSandbox()

agent_code = """
import sys

from smolagents import CodeAgent, OpenAIServerModel, GradioUI

model = OpenAIServerModel(
    model_id="gemma-3-12b-it-4bit",
    api_base="http://192.168.11.18:8080",
    api_key="EMPTY"
)

agent = CodeAgent(
    model=model,
    tools=[],
    additional_authorized_imports=["PIL", "PIL.Image", "os", "os.path", "pathlib", "pathlib.Path"]
)

# エージェントの実行
GradioUI(agent).launch(server_name='0.0.0.0', server_port=7860, share=False)
"""
try:
    sandbox.gradio_run(agent_code)
    print("\nアプリ実行中... Ctrl+C で終了します")
    try:
        while True:
            None
    except KeyboardInterrupt:
        print("\nExecution interrupted by user")

finally:
    # 終了処理
    sandbox.cleanup()