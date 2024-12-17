FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

# Copy wheel and tutorial notebook
COPY wheelhouse/dual_autodiff_x-0.1.0-cp310-cp310-linux_x86_64.whl .
COPY examples/dual_autodiff_tutorial.ipynb .

# Install required packages
RUN pip install jupyter numpy matplotlib
RUN pip install dual_autodiff_x-0.1.0-cp310-cp310-linux_x86_64.whl

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]