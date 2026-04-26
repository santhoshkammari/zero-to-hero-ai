# Rewrite Plan: ch10/s01 - Recurrent Models: RNN, LSTM, GRU

## Running Example
**A weather station that predicts tomorrow's weather based on a sequence of past days.**
- Start tiny: 3 days of temperature [hot, cold, mild]
- Grow: longer sequences, more features
- Thread throughout: RNN tries to remember yesterday, LSTM remembers last week's cold front, GRU does it with less machinery, bidirectional looks at forecast from both ends

## Concept Ladder (dependency order)
1. Why order matters (sequences vs bags) — motivate with weather prediction
2. The sticky note idea — hidden state as memory passed forward
3. Vanilla RNN equation — walk through with 3-number example
4. Unrolling through time — the for loop visualization
5. Training: BPTT — backprop through the unrolled graph
6. The vanishing gradient catastrophe — multiply 0.9 by itself 50 times
7. **REST STOP** — you now understand RNNs and why they fail
8. LSTM — the conveyor belt / highway analogy for cell state
9. Forget gate — what to erase
10. Input gate — what to write
11. Output gate — what to reveal
12. The key line: additive cell state update
13. Peephole connections (brief)
14. GRU — same idea, fewer moving parts
15. Update gate = forget + input combined
16. Reset gate
17. Why simpler can be better
18. Bidirectional RNNs — reading a sentence both ways
19. The sequential bottleneck — why transformers won
20. Wrap-up

## Vulnerability Moments
1. Opening: avoided RNNs, thought they were outdated
2. Vanishing gradient: "I didn't truly get it until I multiplied 0.9 fifty times"
3. LSTM equations: "These equations intimidated me for years"
4. GRU vs LSTM: "I'm still not sure when one is definitively better"
5. Peephole: "I haven't figured out a great way to explain why these help"

## Analogies (recurring)
1. **Sticky note** — hidden state is like passing a sticky note to your future self
2. **Conveyor belt / highway** — LSTM cell state runs like a conveyor belt, gates are workers adding/removing items
3. **Telephone game** — vanilla RNN is like a telephone game where the message degrades

## Rest Stop
After vanishing gradient section — reader now understands RNNs fully and why they fail. Useful mental model. Can stop here.
