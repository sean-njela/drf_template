FROM mcr.microsoft.com/devcontainers/python:1-3.13-bullseye

ENV PYTHONUNBUFFERED 1

USER vscode
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH "/home/vscode/.poetry/bin:$PATH"
RUN /home/vscode/.local/bin/poetry config virtualenvs.in-project true

# [Optional] If your requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
