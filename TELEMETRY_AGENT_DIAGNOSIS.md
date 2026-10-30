# TelemetryAgent diagnosis

**Summary:** ZeroDivisionError on POST /checkout when checking out an empty cart

**Likely cause:** app/cart.py:37 summary() computes `round(total / len(items), 2)` without empty-list guard, so POST /checkout with items=[] raises ZeroDivisionError via app/main.py:34 checkout()

**Why no verified fix:** patch attempts did not prove (repro must pass, no new failures)
