import torch
class Verifier:
    """
    The quality control (QC) lab for the Nucleus.
    """
    @staticmethod
    def martingale_test(paths: torch.Tensor, s0: float, tolerance: float = 0.05):
        """
        In a rish-neutral world , E[St] = s0.
        If the average of your 100k paths is far from S0, the solver is biased.

        """
        terminal_mean = torch.mean(paths[-1])
        error = torch.abs(terminal_mean - s0)/s0
        is_passed = error< tolerance
        return {"error_pct": error.item()* 100, "passed": is_passed}

    @staticmethod
    def convergence_test(solver, sde, s0, sampler, t, step_configs:list):
        """
        Tests how fast the error drops as we add more time steps.
        Essential for the High performance modelling
        """
        results = []
        for steps in step_configs:
            #Run simulation and measure error vs theoretical
            paths = solver.simulate(sde, s0, sampler, t, steps, n_paths= 50000)
            results.append((steps, torch.mean(paths[-1]).item()))
        return results
