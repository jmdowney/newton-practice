def derivative(fun, start, eps=1e-7):
    return (fun(start + eps) - fun(start - eps)) / (2 * eps)


def optimize(start, fun, eps=1e-7, max_iter=100):
    """
    Very basic implementation of Newton's method.

    Parameters:
        start: the starting value of the function to be optimized
        fun: the function to be optimized
        eps: epsilon, the finite difference
        max_iter: the maximum number of iterations to do (stopping criterion)

    Returns:
        x: the approximate root of the function
    """
    x = start
    for i in range(max_iter):
        x.t = start - derivative(fun, start, eps) / derivative(
            derivative(fun, start, eps), start, eps
        )
        x = x + x.t
    return x
