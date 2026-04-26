# Research Notes - Sequential Models & PPL

## Key Topics to Cover
1. HMMs: forward/backward, Viterbi, Baum-Welch
2. Kalman filters: predict-update, Kalman gain
3. Particle filters: sequential Monte Carlo, resampling
4. PPLs: PyMC, Stan, Pyro, NumPyro
5. Model specification in PPLs
6. Posterior predictive checks
7. Model comparison: WAIC, LOO-CV
8. Bayesian neural networks
9. Uncertainty quantification: epistemic vs aleatoric

## Running Example: Weather Station Tracker
- A small town with 3 weather states (Sunny, Cloudy, Rainy)
- Observable: number of ice cream cones sold at a shop
- Builds naturally from HMM → Kalman → Particle → PPL

## Key Insights
- HMM forward algorithm: accumulate evidence from past
- HMM backward algorithm: accumulate evidence from future
- Combined: posterior probability at any time step
- Viterbi: dynamic programming for most likely path
- Kalman: continuous version, predict-update with Gaussian
- Kalman gain: trust knob between prediction and measurement
- Particle filter: when Gaussian assumption breaks, use samples
- PPLs: write the generative story, let inference engine invert it
- WAIC/LOO-CV: estimate out-of-sample predictive accuracy
- BNNs: distributions over weights → uncertainty for free
