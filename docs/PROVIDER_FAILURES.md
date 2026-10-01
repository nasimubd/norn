# Provider failures

Callers should catch transport errors around the decision provider and route the task to approval or retry policy. The runtime must not convert an unavailable model into unrestricted execution.
