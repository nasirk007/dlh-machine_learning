def from_numpy(array):
    """
    Convert a NumPy array to a PyTorch tensor.

    Args:
        array (numpy.ndarray): The input NumPy array.

    Returns:
        torch.Tensor: The converted PyTorch tensor.
    """
    import torch
    return torch.from_numpy(array)
