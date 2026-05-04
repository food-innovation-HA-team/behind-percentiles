def generate_summary(reported, lower, upper):
    """
    Generate a short, plain‑English explanation of the plausible range.
    """

    # Core message
    summary = (
        f"The reported reduction is {reported}%. "
        f"Given typical uncertainty in environmental data and modelling, "
        f"a plausible range could be between {lower}% and {upper}%. "
        "This illustrates that percentage reductions are point estimates, "
        "and the true magnitude may be higher or lower."
    )

    return summary


def get_learn_more_points():
    """
    Provide conceptual notes for the 'Learn more' section.
    """

    return [
        "Percentage reductions are point estimates based on specific data sources and modelling choices.",
        "Data quality, representativeness, and system boundaries can all widen the plausible range.",
        "Allocation decisions and methodological choices can shift results substantially.",
        "Uncertainty affects the magnitude of a reduction more than its direction.",
        "A component‑level reduction (e.g., packaging) may represent a small share of the total footprint.",
        "Wide uncertainty bands encourage humility when interpreting environmental claims."
    ]