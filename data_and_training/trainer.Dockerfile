# Using an official gpu-compatible docker image as the base
# https://hub.docker.com/layers/tensorflow/tensorflow/2.20.0-gpu
# Should use tensorflow 2.20 with python 3.11
# Checked on Nov 4, 2025
FROM tensorflow/tensorflow:2.20.0-gpu

# Defining a working directory where image "lives", files will be copied here and commands will be executed here
WORKDIR /training_container

# Copying over every single file I'll need to complete the entire training process
# Note Dockerfile `COPY`-command syntax:
# `COPY <host-path> <image-path>`
# , where
# `<host-path>`:    the directory the docker build command is being run from
#                   NOTE: We assume you run this from project root!!
# `<image-path>`:   whatever's defined by the `WORKDIR` command above
COPY data_and_training/data_pipeline.sh .
COPY data_and_training/data_downloader.py .
COPY data_and_training/data_preprocessor.py .
COPY data_and_training/devtools/cocoann2tfrecord.py ./devtools/

# Installing all necessary dependencies
# Make sure you have a requirements.txt in the root by running `pip3 freeze > requirements.txt`
# project_root/requirements.txt ignored by .gitignore
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
# All PyPI dependencies should now be installed

# Adding a custom user to prevent running container as root (security concerns)
# This after installations
RUN useradd trainer
USER trainer

# Testing if all dependencies have been installed correctly
#TODO: find a proper solution for this!!
# Packaged with base image:
CMD python3 -c "import importlib.util, sys; print('Missing depedency: tensorflow') if importlib.util.find_spec('tensorflow') is None else None"
# From Python standard library: (remove if correct)
CMD python3 -c "import importlib.util, sys; print('Missing depedency: __future__') if importlib.util.find_spec('__future__') is None else None"
CMD python3 -c "import importlib.util, sys; print('Missing depedency: argparse') if importlib.util.find_spec('argparse') is None else None"
CMD python3 -c "import importlib.util, sys; print('Missing depedency: contextlib') if importlib.util.find_spec('contextlib') is None else None"
CMD python3 -c "import importlib.util, sys; print('Missing depedency: hashlib') if importlib.util.find_spec('hashlib') is None else None"
CMD python3 -c "import importlib.util, sys; print('Missing depedency: io') if importlib.util.find_spec('io') is None else None"
CMD python3 -c "import importlib.util, sys; print('Missing depedency: json') if importlib.util.find_spec('json') is None else None"
CMD python3 -c "import importlib.util, sys; print('Missing depedency: logging') if importlib.util.find_spec('logging') is None else None"
CMD python3 -c "import importlib.util, sys; print('Missing depedency: os') if importlib.util.find_spec('os') is None else None"
# From PyPI:
CMD python3 -c "import importlib.util, sys; print('Missing depedency: fiftyone') if importlib.util.find_spec('fiftyone') is None else None"
CMD python3 -c "import importlib.util, sys; print('Missing depedency: numpy') if importlib.util.find_spec('numpy') is None else None"
CMD python3 -c "import importlib.util, sys; print('Missing depedency: PIL') if importlib.util.find_spec('PIL') is None else None"
CMD python3 -c "import importlib.util, sys; print('Missing depedency: pycocotools') if importlib.util.find_spec('pycocotools') is None else None"
