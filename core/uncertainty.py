def compute_range(reported_percent, uncertainty_level, mode):
    """
    Compute the plausible range around a reported percentage reduction
    using wide illustrative uncertainty bands.

    Parameters
    ----------
    reported_percent : int or float
        The reported percentage reduction (0–100).
    uncertainty_level : str
        One of: "Low", "Medium", "High".
    mode : str
        "Relative" or "Absolute".

    Returns
    -------
    (lower, upper) : tuple of floats
        The plausible lower and upper bounds.
    """

    # Map uncertainty levels to ± percentage-point bands
    bands = {
        "Low": 25,
        "Medium": 50,
        "High": 75
    }

    band = bands.get(uncertainty_level, 50)  # default to Medium if anything odd happens

    # Compute raw bounds
    lower = reported_percent - band
    upper = reported_percent + band

    # Clip to 0–100
    lower = max(0, lower)
    upper = min(100, upper)

    # For v0.1, "Absolute" behaves the same as "Relative"
    # (true absolute logic arrives in v0.2)
    if mode == "Absolute":
        return lower, upper

    return lower, upper