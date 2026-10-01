# Decision provider adapter

Norn expects a TypeSafe-compatible `/v1/systemone` endpoint. This permits local implementations such as Decider, Von, or Laya to be swapped without changing routing policy.

The provider may return more than one answer in a request. Norn currently asks one route question and uses the full probability distribution for logging and future calibration.
