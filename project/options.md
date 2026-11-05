# Project options

Each option has a **core** that's required and **extensions** you can add for depth. A solid core with clean tests beats a half-working extension.

## 1. Loan amortization calculator

- **Core:** given a principal, an annual rate, and a term, print the monthly payment and the full amortization schedule. Use `Decimal` for money.
- **Extensions:** extra-payment scenarios; compare two loans; export the schedule to CSV; plot the balance over time.
- **Lectures used:** L16 (CSV), L20 (dataclasses), L22 (`Decimal`).

## 2. Monte Carlo option pricer

- **Core:** price a European call option by simulating stock paths, and compare the result with the Black–Scholes formula.
- **Extensions:** put options; show how the error shrinks as the number of simulations grows; check a fast version against a slow one on random inputs.
- **Lectures used:** L10 (simulation), L19 (measurement), L23 (slow vs. fast checks).

## 3. Portfolio backtester

- **Core:** read daily prices from a CSV, apply a fixed allocation, and report the total return, the worst drop from a peak (maximum drawdown), and the volatility.
- **Extensions:** periodic rebalancing; compare two strategies; plot the equity curve.
- **Lectures used:** L16 (CSV), L20 (dataclasses), L22 (floats and money).

## 4. Number theory explorer

- **Core:** a command-line tool that factors integers, finds GCDs and LCMs, and lists primes with a sieve.
- **Extensions:** modular inverses; test the Goldbach conjecture up to N; measure sieve vs. trial-division performance.
- **Lectures used:** L09–L10 (loops), L17 (recursion), L19 (Big-O).

## 5. Gradebook

- **Core:** read a roster and scores from CSV, apply weighted categories and drop the lowest score, then output letter grades and per-assignment statistics.
- **Extensions:** "what score do I need on the final?"; detect outliers; a histogram of grades.
- **Lectures used:** L13 (dicts), L16 (CSV), L20–L21 (modeling).
