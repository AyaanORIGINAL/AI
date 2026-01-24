import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def fair_model(marks):
    """
    A model that defers to human when uncertain
    Lower Bound 55 | Upper Bound 65
    """
    if marks >= 65:
        decision = "Auto pass"
    elif marks < 55:
        decision = "Auto fail"
    else:
        decision = "Flagged for review"

    logging.info(f"Marks: {marks} -> Decision: {decision}")
    return decision

exam_batch = [58, 61, 59, 62, 60, 59]
for n in exam_batch:
    fair_model(n)