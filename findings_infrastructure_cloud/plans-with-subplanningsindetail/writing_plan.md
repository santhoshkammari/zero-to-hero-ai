# Writing Plan for Infrastructure & Cloud

## Running Example
A small startup "PetSnap" building a pet breed classifier that grows from prototype to production scale.
- Starts on laptop GPU → single cloud GPU → multi-GPU → cluster decisions
- Threads through every section naturally

## Concept Ladder
1. Why hardware matters (the "my model works on my laptop" problem)
2. GPU anatomy - what makes a GPU good for ML (VRAM, TFLOPS, bandwidth)
3. GPU landscape - T4, L4, A100, H100 and when to use each
4. VRAM math - the calculation you'll do a hundred times
5. Scaling up - vertical vs horizontal, the communication tax
6. Multi-GPU strategies - data, tensor, pipeline parallelism
7. Cloud platforms - SageMaker, Vertex AI, Azure ML
8. Spot instances - 70% savings with a catch
9. Cost optimization - right-sizing, reserved capacity
10. On-prem vs cloud - the break-even math
11. Serverless inference - when you don't want to manage GPUs at all
12. Cluster management - K8s, Ray, or managed platforms

## Rest Stop
After GPU landscape + VRAM math (sections 2-4). Reader has enough to pick a GPU.

## Vulnerability Moments
1. Opening: avoided infrastructure, thought it was "ops stuff"
2. VRAM math: first time running out of memory mid-training
3. Multi-GPU: still confused by tensor vs pipeline parallelism
4. Cost: accidentally left H100s running overnight
5. On-prem: no perfect answer, genuinely uncertain

## Recurring Analogies
1. Kitchen/restaurant: GPU is the stove, VRAM is counter space, bandwidth is how fast ingredients arrive
2. Road trip: single lane vs highway, toll roads vs free roads with traffic
