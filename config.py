"""
Central knobs for the agent. Change behaviour here, not scattered through the code.
"""

# Which model the agent uses. A fast, capable default is fine for this project.
# If this string ever stops working, check the current model names in the Anthropic docs.
MODEL = "claude-sonnet-4-6"

# The seatbelt. The loop will stop after this many turns no matter what,
# so a confused agent can never spend money forever. Do NOT remove this.
MAX_ITERATIONS = 8

# Cap on how long any single model reply can be.
MAX_TOKENS = 1024

# Least privilege: tools listed here run WITHOUT asking a human.
# Everything else must be approved before it runs.
# Rule of thumb: reading/searching is safe; sending/deleting/spending is not.
AUTO_APPROVE = {
    "research",    # only reads/looks things up -> safe
    "save_note",   # writes only inside the notes/ folder -> safe enough
    # "send_email" is deliberately NOT here -> it will require your approval.
}

# Where things land.
NOTES_DIR = "notes"
LOG_DIR = "logs"
