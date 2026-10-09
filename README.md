
# Simulating 2 dimensional Ising Model 

Ising models are ubiquitious in models and simulaitons in statistical mechancis and form a gateway into the subject. My project revolves around using monte carlo simulations to model ferromagnets at their critical temperature.

We begin with the a primitive algorithm: the Metropolis Algorithm.
Detailed balance results in the following metropolis hastings correction.

### Metropolis–Hastings Acceptance Probability

It says that when a spin is proposed to flip from one spin to another, if the energy of the new state is lower than the previous state it just accepts the spin flip, otherwise it will accept with the probability of P=e^((-Kb*delE)/T)

This translates into our code where we first create a matrix to represent spins of random values that then go through different sweeps where spins either accpet or reject the change. All of this is of course governed by the hamiltonian for this model which is related to the neighbouring spins.

### Takeaways

Spins at lower temperatures have a magnetisation of around 1 because they all tend to want to have the same spin configuration as their neighbouring spins so rarely do they accept changes in state, however as temperature increases, temperature fluctuations allow the spins to now be able to actually interact with the probability we mentioned earlier since now the temperture does not negate the probability of having differnet spin configuration compared to the neighbouring spins.

So we see that at a critical temperture, the magnetisation also changes and we can see that using the monte carlo simulation where we use numerical methods to estimate this critical temperature. 

We also observe the relation between susceptibility and the peak of 1/x at around the Tc (critical temperature).

The project also offers an animation in python to help understand the changes and temperature fluctuations in different temperatures as required. 

