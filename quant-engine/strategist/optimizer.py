import torch
def calculate_covariance_matrix(returns_matrix:torch.Tensor):
    """
    Calculate how assets move together.
    Essential for diversifying risk.
    """
    # Returns_matrix shape: [Assets, Time]
    centered_matrix = returns_matrix - returns_matrix.mean(dim=1, keepdim= True)
    cov = torch.mm(centered_matrix, centered_matrix.t())/(returns_matrix.shape[1]-1)
    return cov
