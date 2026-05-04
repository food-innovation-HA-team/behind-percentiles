The ± Behind the %

A teaching tool for understanding uncertainty in percentage‑based environmental claims.
Purpose

Environmental claims often state that a product or process results in “X% fewer CO₂‑eq emissions.”
These numbers are directionally useful — but the magnitude is often uncertain, sometimes highly so.

The ± Behind the % is a simple, illustrative tool designed to help users understand:

    that a reported percentage reduction is a point estimate,
    that the true magnitude may lie within a much wider range,
    and that this uncertainty is shaped by data quality, representativeness, modelling choices, and system boundaries.

This tool is not an LCA calculator.
It is a pedagogical lens for exploring uncertainty.
What the tool does (v0.1)

    Accepts a reported percentage reduction (e.g., “30% fewer CO₂‑eq”).
    Allows users to choose between Low, Medium, and High uncertainty.
    Converts the reported % into a plausible range using wide, illustrative bands:

        Low → ±25 percentage points
        Medium → ±50 percentage points
        High → ±75 percentage points

    Clips all values between 0% and 100%.
    Provides a toggle between relative and absolute views.
    Offers 2–3 preset examples for quick exploration.
    Displays a clean visual showing the reported % and the plausible range.
    Generates a short explanation in plain English.
    Includes an expandable “Learn more” section with conceptual notes.
    Provides a reset button to return to defaults.
    Includes a small note clarifying that the tool is illustrative, not prescriptive.

Why this matters

Percentage reductions can be misleading without context.
For example:

    A “30% reduction” in packaging emissions may correspond to <5% of the total system footprint.

This tool helps users understand:

    the difference between component‑level and system‑level changes,
    why uncertainty affects magnitude more than direction,
    and why environmental claims should be interpreted with humility.

How to run the tool

From the project root:

    Activate the virtual environment:

Code

source .venv/bin/activate

    Run the Streamlit app:

Code

streamlit run app/main.py

    A browser window will open automatically.

Project structure
Code

THE-PLUS-MINUS-BEHIND-THE-PERCENT/
│
├── app/
│   └── main.py
│
├── core/
│   ├── uncertainty.py
│   └── explanations.py
│
├── assets/
│
├── README.md
│
└── requirements.txt

    app/ contains the Streamlit interface.
    core/ contains the logic and explanation engine.
    assets/ is reserved for future visuals.

Roadmap
v0.1 — Conceptual demonstrator (current)

    Single uncertainty slider
    Wide illustrative bands
    Clean visualisation
    Plain‑English explanations
    Presets and reset button
    Relative/absolute toggle

v0.2 — Expanded uncertainty model

    Multiple uncertainty dimensions
    More nuanced explanations
    Optional baseline editing

v0.3 — Real‑world examples

    Curated Agribalyse subset (CSV, not Excel)
    Contribution analysis
    System‑wide vs component‑wide framing

v0.4 — Teaching mode

    Exportable visuals
    Classroom prompts
    Scenario comparisons

License

To be added later.
Acknowledgements

Developed as part of a broader effort to improve environmental uncertainty communication and critical thinking around sustainability claims.