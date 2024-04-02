import torch

# Example list of elements
elements = ['1', '2', '3', '4', '5']

# Convert each element into a PyTorch tensor
tensor_elements = [torch.tensor(int(elem)) for elem in elements]

if tensor_elements[0] == 1:
    print('yes')

# Print the resulting tensor objects
print(tensor_elements)