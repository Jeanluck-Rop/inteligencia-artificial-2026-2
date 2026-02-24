FROM python:3.12-slim

# Avoid Cache
ENV PIP_NO_CACHE_DIR=1

# Evitar warnings por no tener hostname dentro del contenedor
ENV OMPI_MCA_btl_vader_single_copy_mechanism=none
ENV OMPI_MCA_orte_leave_session_attached=1

# Install
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    python3-dev \
    openmpi-bin \
    libopenmpi-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install simpy numpy sympy pytest mpi4py pandas matplotlib scipy seaborn

WORKDIR /app

COPY . /app

CMD ["bash"]
