FROM google/cloud-sdk:481.0.0-slim

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

ADD https://github.com/benbjohnson/litestream/releases/download/v0.3.13/litestream-v0.3.13-linux-amd64.tar.gz /tmp/litestream.tar.gz
RUN tar -C /usr/local/bin -xzf /tmp/litestream.tar.gz

RUN apt update && \
    apt install -y sqlite3 python3.11-venv && \
    python3 -m venv /opt/venv

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . .

CMD . /opt/venv/bin/activate && \
    ./init_db.sh && \
    litestream replicate --config litestream.yml -exec "gradio main.py"
