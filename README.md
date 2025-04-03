
~~~
git clone https://github.com/dai-ichiro/debug_smolagents_gradio -b nodejs
cd debug_smolagents_gradio
~~~

~~~
docker build -t agent-sandbox .
~~~

~~~
uv venv
source .venv/bin/activate
uv pip install docker
uv run agent_runner.py
~~~
