import time
import torch
print(f"Torch = {torch.__version__}")

import torchvision
print(f"Torch vision = {torchvision.__version__}")

#print(f"CUDA = {torch.cuda.is_available()}")


# Function to perform a computationally intensive task (matrix multiplication)
def matrix_multiply(size, device):
    matrix1 = torch.randn(size, size).to(device)
    matrix2 = torch.randn(size, size).to(device)
    start_time = time.time()
    result = torch.matmul(matrix1, matrix2)
    end_time = time.time()
    return end_time - start_time

# Check if CUDA is available
if torch.cuda.is_available():
    print("CUDA is available")
    device_count = torch.cuda.device_count()
    print(f"Number of CUDA devices: {device_count}")
    device = torch.device("cuda")
    for i in range(device_count):
        print(f"GPU Name: {torch.cuda.get_device_name(i)}")
else:
    print("CUDA is not available, using CPU")
    device = torch.device("cpu")

# Test with CUDA (if available)
matrix_size = 2213  # Adjust the size as needed for testing
cuda_time = matrix_multiply(matrix_size, device)
print(f"CUDA Execution time: {cuda_time:.4f} seconds")

# Test with CPU
cpu_time = matrix_multiply(matrix_size, torch.device("cpu"))
print(f"CPU Execution time: {cpu_time:.4f} seconds")

# Calculate speedup (if CUDA was used)
if device.type == "cuda":
  speedup = cpu_time / cuda_time
  print(f"Speedup: {speedup:.2f}x")



