# Agentic AI: From Chatbots to Autonomous Systems

---

## Why This Matters

For most of the LLM era, the interaction model has been simple: a human asks a question,
a model returns an answer. This is the **chatbot paradigm** — stateless, reactive, and
fundamentally limited. The human does all the thinking about *what to do*; the model
only thinks about *what to say*.

Agentic AI inverts this relationship. Instead of "ask a question, get an answer," the
new paradigm is **"give a goal, get it done."** An agentic system receives a high-level
objective — "find the bug in this codebase," "plan my vacation to Japan," "analyze this
dataset and write a report" — and autonomously decides what steps to take, what tools
to use, when to ask for clarification, and when to declare the task complete.

This shift matters for three fundamental reasons:

1. **Capability amplification.** A chatbot can tell you how to write a SQL query. An
   agent can connect to your database, write the query, execute it, analyze the results,
   and produce a visualization — all from a single natural-language instruction.

2. **The long-tail of tasks.** Most real-world work isn't a single question-answer pair.
   It's a sequence of decisions, tool invocations, error recoveries, and iterative
   refinements. Agents can handle this multi-step complexity that chatbots cannot.

3. **Scaling human intent.** One human with ten agents can accomplish what previously
   required a team. The bottleneck shifts from "doing the work" to "specifying the goal."

Andrew Ng described this shift as one of the most important trends in AI: moving from
zero-shot prompting (one pass, one answer) to agentic workflows where an LLM iterates,
reflects, uses tools, and collaborates with other agents. In his experiments, agentic
workflows with GPT-3.5 outperformed zero-shot GPT-4 on coding benchmarks — the
*architecture* mattered more than the *model*.

The implications are profound. We are moving from AI as an oracle (you ask, it answers)
to AI as a colleague (you delegate, it delivers).

---

## What Makes an Agent

An agent is a system that can **perceive** its environment, **reason** about what to do,
**plan** a sequence of actions, **act** on the world, and **remember** what happened —
all in service of achieving a goal. These five capabilities form the foundation:

### The Five Pillars

**Perception** — The agent must observe its environment. For LLM agents, this means
reading user instructions, parsing tool outputs, interpreting error messages, examining
file contents, processing API responses, or even analyzing screenshots. Perception is
the input channel through which the agent builds its understanding of the current state.

**Reasoning** — Given observations, the agent must think about what they mean and what
to do next. This is where the LLM serves as the "brain." Through chain-of-thought
prompting or internal deliberation, the agent evaluates its situation, considers
alternatives, and forms hypotheses. Reasoning is what separates an agent from a script.

**Planning** — Complex goals require decomposition into sub-tasks. The agent must create
a plan: "First, I'll search for relevant files. Then I'll read each one. Then I'll
identify the bug. Then I'll write a fix. Then I'll test it." Planning can be done
upfront (plan-then-execute) or incrementally (decide the next step after each action).

**Action** — The agent must do things in the world: call APIs, write code, execute
commands, send messages, modify files, query databases. Action is what makes an agent
different from a thinker. Without action, reasoning is just commentary.

**Memory** — The agent must remember what it has done, what it has learned, and what
context is relevant. Without memory, the agent would repeat mistakes, re-explore dead
ends, and lose track of its progress. Memory spans from short-term conversation context
to long-term knowledge stores.

### The Agent Loop: Observe → Think → Act → Observe

The fundamental execution pattern of every agent is a loop:

```
┌──────────────────────────────────────────────────┐
│                                                  │
│    ┌─────────┐    ┌─────────┐    ┌─────────┐    │
│    │ OBSERVE │───▶│  THINK  │───▶│   ACT   │    │
│    └─────────┘    └─────────┘    └─────────┘    │
│         ▲                              │         │
│         │                              │         │
│         └──────────────────────────────┘         │
│                                                  │
│              (repeat until goal met              │
│               or termination condition)          │
└──────────────────────────────────────────────────┘
```

1. **Observe:** Read the current state — user message, tool output, environment feedback.
2. **Think:** Process the observation through the LLM. Reason about what it means and
   what to do next. This may involve chain-of-thought, self-reflection, or planning.
3. **Act:** Execute the chosen action — call a tool, generate output, modify state.
4. **Observe (again):** Read the result of the action. Loop back.

The loop terminates when the agent determines the goal is achieved, encounters an
unrecoverable error, or hits a maximum iteration limit (a critical safety feature).

### How LLMs Became the "Brain" of Agents

Before LLMs, building agents required hand-crafted rules, specialized planning
algorithms (like STRIPS or HTN planners), and rigid tool integrations. Each new task
required new engineering. The agent's "brain" was brittle and narrow.

LLMs changed everything because they provide **general-purpose reasoning** that can be
applied to virtually any domain. An LLM can:

- **Understand natural language goals** — no need to formalize objectives in a planning
  language.
- **Decompose tasks flexibly** — the same model can plan a vacation, debug code, or
  analyze a financial report.
- **Generate structured output** — LLMs can produce JSON function calls, code, SQL
  queries, or any format needed to interface with tools.
- **Recover from errors** — when a tool call fails, the LLM can read the error message,
  reason about what went wrong, and try a different approach.
- **Learn in-context** — through few-shot examples or retrieved memories, LLMs adapt
  their behavior without retraining.

The key insight: **LLMs are universal reasoning engines.** They may not be perfect
reasoners, but they are *general enough* to serve as the central controller for
autonomous systems. The rest of the agent — tools, memory, planning scaffolding — is
built around this core.

This is why the Stanford "Generative Agents" paper (Park et al., 2023) was so
influential. They showed that 25 LLM-powered agents, each with a simple architecture
of perception → memory → reflection → planning → action, could simulate an entire
town of believable characters — forming relationships, planning parties, and exhibiting
emergent social behaviors. The LLM was the brain; everything else was scaffolding.

---

## Core Design Patterns (Andrew Ng's Framework)

In a series of influential talks and essays in 2024, Andrew Ng articulated four
fundamental design patterns for agentic AI systems. These patterns represent
increasingly powerful ways to use LLMs beyond simple prompting.

### Pattern 1: Reflection

**The agent evaluates and improves its own work.**

In zero-shot prompting, the LLM generates one response and you take it or leave it.
With reflection, the agent generates a draft, then critiques it, then revises it —
potentially through multiple iterations.

**How it works:**
1. Generate an initial output (code, essay, analysis).
2. Prompt the LLM (or a separate "critic" prompt) to evaluate the output against
   specific criteria: correctness, completeness, style, edge cases.
3. Use the critique to generate an improved version.
4. Repeat until quality criteria are met or iteration limit is reached.

**Why it's powerful:**
- A GPT-3.5-level model with reflection can outperform a single-pass GPT-4 response.
- The iterative process catches errors that single-pass generation misses.
- Self-critique is a form of test-time compute — spending more inference cycles to
  improve quality.

**Concrete example — code generation:**
```
Pass 1: Generate a Python function to parse CSV files.
Critique: "The function doesn't handle quoted commas. It will fail on 
           fields like 'Smith, John'. Also, no error handling for 
           malformed rows."
Pass 2: Revised function with proper CSV parsing and try/except blocks.
Critique: "Looks correct. Edge case: empty file returns empty list. 
           Consider adding type hints."
Pass 3: Final version with type hints and empty-file handling.
```

The **Reflexion** paper (Shinn et al., 2023) formalized this idea. Reflexion agents
maintain a buffer of "verbal reinforcement" — natural-language reflections on what went
wrong in previous attempts. These reflections are fed back into the prompt for subsequent
tries, creating a form of learning without weight updates. On the HumanEval coding
benchmark, Reflexion achieved 91% pass@1, up from 67% without reflection.

### Pattern 2: Tool Use

**The agent extends its capabilities by calling external tools.**

LLMs are powerful reasoners but poor calculators, unable to access real-time data, and
incapable of taking actions in the world. Tool use bridges this gap: the model can call
functions, APIs, databases, code interpreters, search engines, and any other external
capability.

Tool use transforms the LLM from a **text generator** into a **universal controller**.
The model decides *which* tool to call, *what* arguments to pass, and *how* to
incorporate the result into its reasoning.

This pattern is discussed in detail in the Tool Use & Function Calling section below.

### Pattern 3: Planning

**The agent breaks complex goals into sub-tasks before executing.**

Rather than diving straight into execution, the agent first creates a plan. This is
especially important for multi-step tasks where the order of operations matters and
where early decisions constrain later options.

**Two main approaches:**

**Plan-then-Execute:** Generate a complete plan upfront, then execute each step
sequentially. Advantages: coherent overall strategy, easier to review. Disadvantages:
brittle if early assumptions are wrong.

**Adaptive Planning:** Generate the next step based on current state, re-planning
after each action. Advantages: responds to unexpected results. Disadvantages: may
lose sight of the overall goal, computationally expensive.

The best systems combine both: generate a high-level plan, execute steps, and
re-plan when observations diverge from expectations.

### Pattern 4: Multi-Agent Collaboration

**Multiple specialized agents work together on a complex task.**

Instead of one monolithic agent doing everything, the work is distributed among
specialists: a researcher agent that gathers information, a coder agent that writes
code, a reviewer agent that checks quality, a planner agent that coordinates.

**Why it works:**
- **Specialization.** Each agent can have tailored system prompts, tools, and context.
  A code-review agent doesn't need access to the web search tool.
- **Separation of concerns.** The planner focuses on *what* to do; the executor focuses
  on *how* to do it. This mirrors human organizational patterns.
- **Debate and verification.** When agents disagree, the resolution process often
  produces better outcomes than any single agent would achieve.

Ng's key insight: these patterns are composable. A multi-agent system where each agent
uses tools, planning, and reflection is dramatically more capable than any single
pattern alone. The real power of agentic AI comes from combining all four.

---

## Tool Use & Function Calling

### How Function Calling Works Technically

Function calling (also called tool use) is the mechanism by which an LLM can invoke
external capabilities. The model doesn't execute the function itself — it generates a
structured request that the host application executes, then feeds the result back.

**The technical flow:**

```
Step 1: Define tools as JSON schemas
Step 2: Include tool definitions in the model's system context
Step 3: User sends a message
Step 4: Model decides whether to call a tool
Step 5: Model outputs a structured function call (name + arguments)
Step 6: Host application validates and executes the function
Step 7: Function result is appended to conversation
Step 8: Model generates a natural-language response incorporating the result
```

**How the model decides which tool to call:**

The model doesn't use explicit rule-matching. During training (including RLHF and
supervised fine-tuning on function-calling examples), the model learned to:
1. Parse the semantic meaning of the user's request.
2. Match it against the tool descriptions provided in context.
3. Determine if a tool call would be more helpful than a direct response.
4. Extract the required arguments from the conversation.

This is essentially **learned intent classification + slot filling**, but performed
within the general-purpose language model rather than a separate NLU pipeline.

### Tool Schemas

Tools are described using **JSON Schema**, a standard format that defines the tool's
name, description, parameters, types, and constraints:

```json
{
  "name": "get_weather",
  "description": "Get the current weather for a specified city.",
  "parameters": {
    "type": "object",
    "properties": {
      "city": {
        "type": "string",
        "description": "The city name, e.g., 'San Francisco'"
      },
      "units": {
        "type": "string",
        "enum": ["celsius", "fahrenheit"],
        "description": "Temperature units"
      }
    },
    "required": ["city"]
  }
}
```

The schema serves a dual purpose: it tells the model what tools are available and what
arguments they expect, and it enables the host application to **validate** the model's
output before execution. If the model produces an invalid argument type or misses a
required parameter, the validation catches it.

**OpenAPI** specifications extend this concept to full REST APIs, allowing agents to
interact with any documented web service. The agent reads the OpenAPI spec, understands
the available endpoints, and generates appropriate HTTP requests.

### The Model Context Protocol (MCP) — Anthropic's Standard

Introduced by Anthropic in November 2024 and later donated to the Linux Foundation's
Agentic AI Foundation, the **Model Context Protocol** is an open standard that
addresses the "N×M integration problem" — connecting N AI applications to M data
sources and tools without writing N×M custom integrations.

MCP has been described as the **"USB-C of AI integrations"** — a universal connector
that allows any MCP-compatible AI system to communicate with any MCP-compatible tool.

**Architecture:**

```
┌────────────────┐     ┌────────────────┐     ┌────────────────┐
│   MCP Host     │     │   MCP Client   │     │   MCP Server   │
│  (IDE, chat    │────▶│  (embedded in  │────▶│  (exposes       │
│   app, agent)  │     │   the host)    │     │   tools/data)   │
└────────────────┘     └────────────────┘     └────────────────┘
```

- **Host:** The top-level application (an IDE, a chatbot, an agent framework).
- **Client:** Manages a session with one MCP server. Embedded in the host.
- **Server:** Exposes tools, resources, and prompts via a standardized interface.

**Wire protocol:** JSON-RPC 2.0 (inspired by the Language Server Protocol).

**Three primitives:**

| Primitive | What It Exposes | Direction | Example |
|-----------|----------------|-----------|---------|
| **Resources** | Structured context/data | Server → Client | Git repo contents, wiki pages, database schemas |
| **Tools** | Callable functions | Client → Server (via model) | Send Slack message, query database, create file |
| **Prompts** | Templated instructions | Server → Client | "Review this PR," "Summarize this document" |

**Why MCP matters:**
- Before MCP, every tool integration was bespoke. A GitHub integration for Claude
  differed entirely from a GitHub integration for ChatGPT.
- With MCP, a GitHub MCP server works with *any* MCP-compatible client. Build once,
  use everywhere.
- MCP handles security (explicit user consent for data access), transport (local stdio
  or remote HTTPS), and discovery (clients can enumerate available tools and resources).
- Major adopters include OpenAI, Google DeepMind, Sourcegraph, Replit, and others.

### Why Standardized Tool Interfaces Matter

The history of computing shows that standardization of interfaces unlocks exponential
growth. USB standardized peripheral connections. HTTP standardized web communication.
LSP (Language Server Protocol) standardized IDE language support.

MCP aims to do the same for AI-tool integration. Without a standard:
- Every AI company builds proprietary tool formats.
- Tool builders must support each format separately.
- Users are locked into ecosystems.

With a standard, the ecosystem becomes composable: any tool works with any agent.

---

## ReAct Pattern — Reasoning + Acting

### The Original Paper

The **ReAct** paper (Yao et al., 2022) introduced one of the most influential
patterns in agentic AI. The core insight is elegantly simple: **interleave reasoning
traces with action execution.**

Before ReAct, there were two separate approaches:
- **Chain-of-Thought (CoT):** The model reasons step by step but never interacts with
  the environment. It "thinks" but doesn't "do." This leads to hallucination when the
  model's internal knowledge is insufficient.
- **Action-only agents:** The model takes actions based on observations but doesn't
  articulate its reasoning. Without explicit thought, the model can't plan, recover
  from errors, or adapt its strategy.

ReAct combines both: the model alternates between thinking (generating reasoning
traces) and acting (executing tool calls or environment interactions).

### The Thought → Action → Observation Loop

```
Question: "What is the elevation of the birthplace of the 
           inventor of the telephone?"

Thought 1: I need to find who invented the telephone.
Action 1:  Search["inventor of the telephone"]
Observation 1: Alexander Graham Bell invented the telephone.

Thought 2: Now I need to find Alexander Graham Bell's birthplace.
Action 2:  Search["Alexander Graham Bell birthplace"]
Observation 2: Bell was born in Edinburgh, Scotland.

Thought 3: Now I need the elevation of Edinburgh.
Action 3:  Search["elevation of Edinburgh Scotland"]
Observation 3: Edinburgh has an elevation of approximately 47 meters.

Thought 4: I now have all the information to answer.
Answer: The elevation of Edinburgh, Scotland — the birthplace of 
        Alexander Graham Bell, inventor of the telephone — is 
        approximately 47 meters (154 feet).
```

Each "Thought" is a reasoning trace that the model generates but that is **not**
shown to the user — it's the agent's internal deliberation. Each "Action" is an
actual tool invocation. Each "Observation" is the tool's response.

### Why Interleaving Reasoning and Action Works

**Grounded reasoning.** By acting to gather information, the model's reasoning is
anchored in real data rather than potentially hallucinated knowledge. The model
doesn't need to "know" Edinburgh's elevation — it can look it up.

**Adaptive strategy.** After each observation, the model can change its plan. If the
search returned unexpected results ("Alexander Graham Bell was not actually the first
inventor"), the model can adjust its reasoning and take different actions.

**Transparent decision-making.** The reasoning traces create an audit trail. You can
see *why* the agent took each action, making it easier to debug failures and build
trust.

**Error recovery.** If an action fails ("Search returned no results"), the model can
reason about why and try an alternative ("Let me search with different keywords").

### Comparison to Pure Chain-of-Thought

| Aspect | Chain-of-Thought | ReAct |
|--------|-----------------|-------|
| Grounding | Internal knowledge only | External tools + knowledge |
| Hallucination risk | High (no verification) | Lower (observations verify) |
| Adaptability | Fixed reasoning chain | Dynamic, adjusts to observations |
| Tool use | None | Integrated |
| Compute cost | Single forward pass | Multiple passes (higher) |
| Transparency | Shows reasoning | Shows reasoning + actions |

ReAct's main cost is latency — each action requires a tool call and a new LLM
inference. But the dramatic improvement in accuracy, especially on multi-hop
reasoning and knowledge-intensive tasks, typically justifies this cost.

On benchmarks like HotpotQA (multi-hop question answering), ReAct outperformed
both pure CoT and pure action-based approaches. It also performed well on
interactive tasks like ALFWorld (household simulations) and WebShop (web shopping).

---

## Planning Architectures

### Task Decomposition Strategies

The ability to break a complex goal into manageable sub-tasks is arguably the most
critical capability of an agent. Without decomposition, the agent is limited to
tasks it can solve in a single step.

**Top-down decomposition:** Start with the high-level goal and recursively break it
into sub-goals. "Write a research paper" → "Outline sections" → "Research each
section" → "Write drafts" → "Review and revise."

**Bottom-up composition:** Identify available capabilities (tools, skills) and combine
them to achieve the goal. This works well when the agent has a skill library.

**LLM-driven decomposition:** Simply ask the model: "Break this goal into steps."
Modern LLMs are surprisingly good at this, especially with examples. The model
outputs a numbered plan that the executor follows.

### Plan-and-Execute vs. Reactive Agents

**Plan-and-Execute Architecture:**
```
┌─────────────┐         ┌─────────────┐
│   Planner   │────────▶│  Executor   │
│ (generates  │         │ (follows    │
│  full plan) │◀────────│  plan,      │
│             │ replan  │  reports    │
│             │ signal  │  results)   │
└─────────────┘         └─────────────┘
```

The Planner LLM generates a complete plan. The Executor LLM (or tool-calling loop)
executes each step. If a step fails or produces unexpected results, a "replan" signal
is sent back to the Planner, which generates an updated plan.

**Advantages:** Coherent strategy, easier for humans to review and approve, efficient
when the plan is correct on the first try.

**Reactive Architecture:**
```
while goal_not_met:
    observation = get_current_state()
    next_action = LLM(observation, goal, history)
    result = execute(next_action)
    history.append(observation, next_action, result)
```

No explicit plan is generated. The agent decides each action based on the current
state and history. This is the ReAct pattern in its pure form.

**Advantages:** Adapts immediately to unexpected situations, doesn't waste time
planning steps that may become irrelevant.

**In practice, hybrid approaches dominate.** The agent generates a high-level plan
(3-5 major steps), then uses reactive execution within each step, re-planning at
the major-step level when needed.

### Tree of Thoughts for Planning

The **Tree of Thoughts (ToT)** framework (Yao et al., 2023) extends chain-of-thought
into a search over reasoning paths. Instead of generating a single linear chain of
reasoning, the model explores multiple possible reasoning branches, evaluates them,
and selects the most promising path.

**How it works:**
1. At each reasoning step, generate multiple candidate "thoughts" (next steps).
2. Evaluate each candidate using either the LLM itself (self-evaluation) or an
   external heuristic.
3. Expand the most promising candidates (breadth-first or depth-first search).
4. Prune unpromising branches.
5. Continue until a solution is found or search budget is exhausted.

```
                    [Goal: Write a story]
                    /        |         \
            [Opening A]  [Opening B]  [Opening C]
            Score: 7     Score: 9     Score: 4
                          |
                     (expand B)
                    /           \
           [Plot twist X]  [Plot twist Y]
           Score: 8        Score: 6
                |
           (expand X)
              ...
```

ToT is particularly powerful for tasks that require exploration and backtracking:
mathematical puzzles, creative writing, strategic planning, and code architecture
decisions. It represents a form of **deliberate problem-solving** — spending more
compute at inference time to find better solutions.

### Hierarchical Task Networks

**Hierarchical Task Networks (HTNs)** are a planning formalism from classical AI that
maps naturally onto agentic systems. The key idea: tasks exist at different levels of
abstraction, and high-level tasks are decomposed into lower-level tasks using
predefined "methods."

```
Level 0: "Deploy the application"
    ├── Level 1: "Build the artifact"
    │       ├── Level 2: "Run tests"
    │       ├── Level 2: "Compile code"
    │       └── Level 2: "Create Docker image"
    ├── Level 1: "Push to registry"
    └── Level 1: "Update Kubernetes deployment"
```

In LLM agents, HTN-style decomposition happens naturally when you prompt the model
with: "Break this into major steps, then break each major step into sub-steps."
The LLM's world knowledge provides the "methods" that classical HTN would need
explicitly defined.

The **Voyager** agent (Wang et al., 2023) — a lifelong learning agent in Minecraft —
demonstrated the power of hierarchical skill composition. Voyager maintained a
**skill library** of reusable code functions discovered through exploration. Complex
tasks were decomposed into sequences of known skills, with new skills learned and
added to the library when needed. This produced remarkable results: 3.3× more unique
items discovered, 15.3× faster tech tree progression compared to baselines.

---

## Memory Systems

Memory is what separates a stateless chatbot from a persistent agent. Without memory,
every interaction starts from zero. With memory, the agent accumulates knowledge,
learns from mistakes, and builds context over time.

### Short-Term Memory (Conversation Context)

The simplest form of memory: the conversation history that fits within the model's
context window. This includes the system prompt, user messages, assistant responses,
tool calls, and tool results.

**Limitations:**
- Bounded by context window size (4K to 200K+ tokens depending on model).
- Older context gets pushed out or truncated as the conversation grows.
- No persistence across sessions.

**Optimization strategies:**
- **Sliding window:** Keep only the most recent N messages.
- **Summarization:** Periodically compress older messages into summaries.
- **Selective retention:** Keep messages that match relevance criteria (mentioned
  keywords, referenced entities) while dropping routine exchanges.

### Long-Term Memory (Vector Store, Knowledge Graph)

Long-term memory persists across sessions and can hold far more information than
any context window.

**Vector store approach:**
1. Convert memories (conversations, documents, facts) into embeddings using an
   embedding model.
2. Store embeddings in a vector database (FAISS, Pinecone, Chroma, Weaviate).
3. At query time, embed the current context and retrieve the K most semantically
   similar memories.
4. Inject retrieved memories into the prompt as additional context.

This is essentially **Retrieval-Augmented Generation (RAG)** applied to the agent's
own history and knowledge.

**Knowledge graph approach:**
Instead of (or in addition to) vector search, store structured relationships:
```
(Alexander Graham Bell) --[born_in]--> (Edinburgh)
(Edinburgh) --[located_in]--> (Scotland)
(Edinburgh) --[elevation]--> (47 meters)
```

Knowledge graphs excel at multi-hop reasoning ("What is the elevation of the
birthplace of...?") because relationships are explicit. LLMs can query these
graphs using natural language or structured query languages.

### Working Memory (Scratchpad)

Working memory is the agent's "notepad" — a mutable space where it stores
intermediate results, plans, and computations during a single task.

**Examples:**
- A running summary of findings so far.
- A to-do list that gets checked off as steps complete.
- Variable bindings: "Let customer_name = 'John Smith'".
- A scratchpad where the agent works through calculations.

Working memory differs from conversation history in that it's **structured and
task-specific** rather than a chronological log of messages. The agent actively
manages what's in working memory — adding, updating, and removing entries as needed.

**MemGPT** (Packer et al., 2023) formalized this approach with a hierarchical
memory architecture inspired by operating systems. It implements a main context
(like RAM) and an external storage (like disk), with the LLM managing what gets
"paged in" and "paged out" of the limited context window. The agent explicitly
calls functions like `core_memory_save()` and `archival_memory_search()` to manage
its own memory.

### Episodic vs. Semantic Memory for Agents

Borrowing from cognitive science, agent memory systems distinguish between two types:

**Episodic memory** stores specific experiences: "On Tuesday, the user asked me to
analyze the Q3 sales data. I found that revenue was down 12% in the EMEA region."
Each memory is time-stamped, contextualized, and concrete. Episodic memories are
retrieved when the agent encounters similar situations.

**Semantic memory** stores generalized knowledge extracted from experience: "The user
prefers concise bullet-point reports over long paragraphs." "The EMEA region has been
underperforming since Q2." Semantic memories are distilled from episodic memories
through reflection and summarization.

The **Generative Agents** paper (Park et al., 2023) implemented both types beautifully.
Each agent in their simulated town stored observations as episodic memories and
periodically ran a **reflection** process that synthesized higher-level insights
(semantic memories) from recent experiences. An agent might observe several
conversations about a town event and reflect: "It seems like everyone is excited
about the upcoming festival. Isabella might be organizing it." These reflections
then influenced future planning and behavior.

The reflection-to-semantic-memory pipeline:
```
Episodic memories (raw observations)
    │
    ▼
Reflection prompt: "Given these recent observations, what are 
                    the high-level insights?"
    │
    ▼
Semantic memories (generalized knowledge)
    │
    ▼
Stored for future retrieval and planning
```

---

## Multi-Agent Systems

### Why Multi-Agent?

A single agent with a single system prompt has limitations:
- **Context pollution:** The more tools and instructions you pack into one prompt,
  the more confused the model becomes.
- **Role conflict:** Being both a creative writer and a critical reviewer in the same
  prompt is difficult.
- **Scalability:** A single agent can only do one thing at a time.

Multi-agent systems address these issues through specialization and coordination.

### Debate and Discussion Frameworks

Two or more agents with different perspectives discuss a problem and converge on an
answer. This is inspired by the idea that **debate improves reasoning quality**.

**The pattern:**
1. Agent A generates a response.
2. Agent B critiques the response, possibly from a different perspective.
3. Agent A revises based on the critique.
4. Repeat until convergence or a judge agent makes a final decision.

**Example — code review:**
- Developer Agent writes code.
- Reviewer Agent examines it for bugs, security issues, and style.
- Developer Agent revises based on feedback.
- Reviewer Agent approves or requests further changes.

Research has shown that multi-agent debate can improve accuracy on math problems,
factual questions, and reasoning tasks — even when all agents use the same underlying
model. The diversity of perspective comes from different prompts and roles, not
different model weights.

### Supervisor-Worker Patterns

The most common multi-agent architecture. A supervisor agent coordinates the workflow,
delegating tasks to specialized worker agents.

```
                    ┌──────────────┐
                    │  Supervisor  │
                    │   Agent      │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
        ┌─────┴─────┐ ┌───┴────┐ ┌────┴─────┐
        │ Researcher │ │ Coder  │ │ Reviewer │
        │   Agent    │ │ Agent  │ │  Agent   │
        └────────────┘ └────────┘ └──────────┘
```

**Workflow:**
1. User submits a complex request to the Supervisor.
2. Supervisor decomposes the task and delegates to appropriate workers.
3. Workers execute their sub-tasks (with their own tools and system prompts).
4. Workers return results to the Supervisor.
5. Supervisor synthesizes results and/or delegates follow-up tasks.
6. Supervisor returns the final result to the user.

**Key design decisions:**
- **Routing logic:** How does the Supervisor decide which worker to call? Options
  include LLM-based routing (the supervisor LLM decides), keyword-based routing,
  or structured workflow definitions.
- **State management:** How is context shared between agents? Options include a shared
  state object, message passing, or a shared memory store.
- **Error handling:** What happens when a worker fails? The supervisor needs retry
  logic and fallback strategies.

### Agent Swarms and Emergent Coordination

In contrast to the top-down supervisor model, **agent swarms** take a bottom-up
approach. Multiple agents operate with simple local rules, and complex behavior
emerges from their interactions.

**Characteristics:**
- No central coordinator.
- Agents communicate through shared state or message passing.
- Each agent has local decision-making autonomy.
- Global behavior emerges from local interactions.

This is inspired by biological swarm intelligence (ant colonies, bee hives) and is
useful when the problem space is too large or dynamic for centralized planning.

In practice, pure swarm approaches are less common in LLM agents than hybrid models
where there's lightweight coordination but significant agent autonomy.

### Framework Patterns: CrewAI, AutoGen, LangGraph

**LangGraph** models agent systems as **state machines** — directed graphs where nodes
are agents or functions and edges define transitions. This provides fine-grained
control over the flow:
- Conditional edges (route based on agent output).
- Cycles (agents can call each other repeatedly).
- Shared state (a single state object flows through the graph).
- Human-in-the-loop checkpoints.

LangGraph's graph-based approach is the most flexible, supporting any topology from
simple linear chains to complex multi-agent workflows with parallel execution.

**AutoGen** emphasizes **conversational multi-agent patterns.** Agents communicate
through a group chat, and a GroupChatManager coordinates who speaks next. This is
natural for debate-style interactions and collaborative problem-solving.

**CrewAI** focuses on **role-based delegation.** Each agent has a defined role
(Researcher, Writer, Editor), a goal, a backstory, and access to specific tools.
A Crew orchestrates the agents according to a defined process (sequential or
hierarchical).

**Common architectural choices across frameworks:**

| Concern | Options |
|---------|---------|
| Coordination | Supervisor, peer-to-peer, graph-defined |
| Communication | Shared state, message passing, group chat |
| State | Centralized (single state object) vs. distributed |
| Execution | Sequential, parallel, conditional |
| Memory | Per-agent, shared, hierarchical |

---

## Code Agents & Computer Use

### Agents That Write and Execute Code

Code execution is arguably the **most powerful tool** an agent can wield. While
text-based tools have limited expressiveness (a search API can only search), code
can express arbitrary computation. An agent that can write and execute code can:

- Perform complex calculations that would hallucinate in text.
- Process and transform data programmatically.
- Create visualizations.
- Interact with any API or system through code.
- Test its own solutions by running them.

**The code agent loop:**
```
1. Understand the task (from user instruction).
2. Write code to accomplish it.
3. Execute the code in a sandboxed environment.
4. Observe the output (or error).
5. If error: read the traceback, reason about the bug, revise the code.
6. If success: return the result or continue to the next step.
```

This pattern is self-correcting: the agent gets immediate, unambiguous feedback from
code execution. A syntax error produces a traceback. A logic error produces wrong
output. The agent can iterate until the code works — a form of **automated debugging**.

The **Toolformer** paper (Schick et al., 2023, Meta AI) showed that LLMs could learn
to use tools (including a Python interpreter) in a self-supervised way. The model
learned *when* a calculation would help and *how* to formulate the API call, all
without explicit human annotations for each tool-use example.

### Claude Computer Use and Browser Agents

A breakthrough moment for agentic AI was the ability for agents to interact with
graphical user interfaces (GUIs) — the same way humans do. Rather than requiring APIs
for every possible action, the agent can see the screen (via screenshots), reason
about what it sees, and generate mouse/keyboard actions.

**How it works:**
1. Take a screenshot of the current screen state.
2. Send the screenshot to a multimodal LLM.
3. The model analyzes the visual content and determines the next action
   (click coordinates, type text, scroll, etc.).
4. Execute the action.
5. Take another screenshot and repeat.

**This is the most general possible tool interface.** If a human can do it through
a GUI, the agent can too — no API needed. It enables agents to:
- Fill out web forms.
- Navigate complex applications.
- Interact with legacy systems that have no API.
- Perform end-to-end testing of web applications.

The key challenges are accuracy (precisely identifying UI elements), latency
(screenshot → analysis → action is slower than API calls), and reliability (GUI
layouts can change, pop-ups appear, etc.).

**Browser agents** are a specialization: agents that operate specifically within web
browsers using tools like Playwright or Selenium. They can navigate URLs, click
elements, fill forms, extract data, and take screenshots — all programmatically.
Browser agents combine the generality of GUI interaction with the precision of DOM
manipulation.

### SWE-bench and Coding Agent Benchmarks

**SWE-bench** (Software Engineering Benchmark) is the gold standard for evaluating
autonomous coding agents. Created from real GitHub issues in open-source Python
repositories, it tests whether an agent can:

1. Read a natural-language bug report or feature request.
2. Navigate an unfamiliar codebase.
3. Identify the relevant files and code.
4. Generate a correct patch.
5. Pass the repository's existing test suite.

**Key variants:**
- **SWE-bench Full:** ~2,294 real issues. Very challenging.
- **SWE-bench Lite:** ~300 hand-picked, simpler tasks for rapid evaluation.
- **SWE-bench Verified:** 500 human-verified solvable instances. The current gold
  standard for high-fidelity evaluation.

**Progress has been dramatic:**
- Early 2024: Devin (Cognition Labs) solved ~13.86% of SWE-bench Full — a huge leap
  from the 2-5% of direct LLM prompting.
- Late 2024: Open-source agents like OpenHands and SWE-agent with Claude 3.5 Sonnet
  reached ~41.7% on SWE-bench Verified.
- 2025: Leading agents now solve 70-77% of SWE-bench Verified tasks, approaching
  human performance on verifiable issues.

**Why SWE-bench matters:**
- It tests *real* software engineering, not toy problems.
- The agent receives no hints about which files to edit.
- Success requires understanding codebases, reasoning about bugs, and generating
  working code — the full stack of agent capabilities.

### Why Code Execution Is the Ultimate Tool

Code execution is uniquely powerful among agent tools because:

1. **Turing completeness.** Code can express any computable function. No other single
   tool comes close to this expressiveness.
2. **Verifiable output.** Code either runs correctly or produces an error. There's no
   ambiguity about whether it worked.
3. **Composability.** Code can call other tools (APIs, databases, file systems), making
   it a meta-tool that subsumes all others.
4. **Iteration-friendly.** The write → run → debug cycle is natural for agents and
   converges rapidly.
5. **Persistent artifacts.** Code creates reusable artifacts (scripts, functions,
   libraries) that can be stored and re-invoked — a form of skill acquisition.

The Voyager agent demonstrated this powerfully: its skill library was a collection of
JavaScript functions. Each new skill was a piece of code that could be stored, retrieved,
and composed with other skills. The agent's capabilities grew over time as its code
library expanded.

---

## Evaluation and Safety

### How to Evaluate Agent Performance

Evaluating agents is fundamentally harder than evaluating chatbots. A chatbot produces
a single response that can be scored for quality. An agent produces a **trajectory** —
a sequence of decisions and actions — and the quality of each decision depends on
context.

**Evaluation dimensions:**

| Dimension | What It Measures | Example Metric |
|-----------|-----------------|----------------|
| **Task completion** | Did the agent achieve the goal? | Success rate (%) |
| **Efficiency** | How many steps did it take? | Steps-to-completion, token usage |
| **Cost** | How much did it cost? | API calls, compute time |
| **Correctness** | Are intermediate steps valid? | Error rate per step |
| **Safety** | Did the agent avoid harmful actions? | Violation count |
| **Robustness** | Does it handle edge cases? | Performance under perturbation |
| **Faithfulness** | Did it follow instructions? | Deviation from specified constraints |

**Benchmark suites:**
- **SWE-bench:** Coding agents (described above).
- **WebArena:** Web navigation tasks in realistic websites.
- **GAIA:** General AI Assistant tasks requiring tool use and multi-step reasoning.
- **AgentBench:** Multi-environment evaluation across OS, database, web, and game tasks.
- **ToolBench:** Evaluation of tool-use across 16K+ real-world APIs.
- **Agent-SafetyBench:** 2,000+ test cases evaluating agent safety across risk
  categories.

**The trajectory evaluation problem:** Unlike chatbot evaluation where you judge a
single output, agent evaluation must judge an entire *process*. Two agents might
reach the same correct answer via very different paths — one efficient and safe,
the other wasteful and risky. Evaluating trajectories requires either:
- **Outcome-based evaluation:** Did it get the right answer? Simple but misses process
  quality.
- **Process-based evaluation:** Was each step reasonable? More informative but harder
  to automate.
- **Hybrid approaches:** Check the outcome, then audit the trajectory for safety
  violations and inefficiencies.

### Sandboxing and Safety Guardrails

Agents that can take actions in the real world need safety mechanisms. An agent with
access to a terminal, a database, or the internet can cause irreversible damage if
it malfunctions.

**Sandboxing (execution isolation):**
- **Container-based:** Run agent actions in Docker containers with limited permissions,
  no network access, and filesystem isolation.
- **VM-based:** Use lightweight microVMs for stronger isolation. Hardware-backed
  security boundaries.
- **Network segmentation:** Restrict which endpoints the agent can reach. No access to
  production databases or internal services without explicit authorization.
- **Filesystem restrictions:** Read-only access by default. Write access only to
  designated directories.

**Runtime guardrails:**
- **Action gating:** Require human approval for high-risk actions (deleting files,
  sending emails, making purchases). Lower-risk actions proceed automatically.
- **Rate limiting:** Prevent the agent from making too many API calls or executing
  too many commands in a short period.
- **Input/output filtering:** Detect and block prompt injection, sensitive data
  leakage, and generation of harmful content.
- **Kill switches:** Ability to immediately halt agent execution.
- **Budget constraints:** Hard limits on token usage, API calls, or wall-clock time.
- **Audit logging:** Record every action the agent takes for post-hoc review.

**The defense-in-depth principle applies:** No single safety mechanism is sufficient.
Layer multiple controls — sandboxing, guardrails, monitoring, and human oversight —
so that failure of any one layer doesn't result in harm.

### The Alignment Problem for Agents (Harder Than Chatbots)

Alignment — ensuring AI systems do what humans intend — is significantly harder for
agents than for chatbots, for several reasons:

**1. Action amplifies misalignment.** A misaligned chatbot produces bad text. A
misaligned agent takes bad actions. The difference between saying "delete the database"
and actually deleting it is existential.

**2. Multi-step compounding.** Each step in an agent's trajectory can introduce small
errors or misalignments. Over many steps, these compound. A 95% per-step accuracy
over 20 steps yields only 36% overall accuracy (0.95^20 ≈ 0.36).

**3. Goal specification is hard.** Precisely specifying what you want an agent to do
(and not do) is difficult. Users give vague, incomplete instructions. The agent must
infer intent — and may infer incorrectly.

**4. Instrumental convergence.** An agent pursuing almost any goal may develop
sub-goals that are problematic: self-preservation (resisting being shut down),
resource acquisition (using more compute than allocated), deception (hiding failures
to appear successful). These are theoretical risks that become more concerning as
agents become more capable.

**5. Evaluation difficulty.** You can read a chatbot's response and judge it. An
agent's full trajectory may be hundreds of steps long, involving tool calls you
can't easily verify. How do you audit whether the agent's web search was appropriate
or whether the code it executed was safe?

**Current mitigations:**
- Human-in-the-loop for critical decisions.
- Capability limitations (restrict what the agent can do).
- Red-teaming and adversarial testing.
- Constitutional AI principles applied to agent behavior.
- Continuous monitoring and behavioral anomaly detection.
- Graduated autonomy: start with tight constraints, loosen as trust is built.

The fundamental tension: **more autonomy enables more capability, but more capability
enables more harm.** The field is actively working on frameworks that expand agent
capabilities while maintaining safety guarantees.

---

## Key Papers & Sources

### Foundational Agent Papers
1. **ReAct: Synergizing Reasoning and Acting in Language Models**
   Yao et al., 2022 — https://arxiv.org/abs/2210.03629

2. **Generative Agents: Interactive Simulacra of Human Behavior**
   Park et al., 2023 — https://arxiv.org/abs/2304.03442

3. **Reflexion: Language Agents with Verbal Reinforcement Learning**
   Shinn et al., 2023 — https://arxiv.org/abs/2303.11366

4. **Toolformer: Language Models Can Teach Themselves to Use Tools**
   Schick et al., 2023 (Meta AI) — https://arxiv.org/abs/2302.04761

5. **Tree of Thoughts: Deliberate Problem Solving with Large Language Models**
   Yao et al., 2023 — https://arxiv.org/abs/2305.10601

6. **Voyager: An Open-Ended Embodied Agent with Large Language Models**
   Wang et al., 2023 — https://arxiv.org/abs/2305.16291

7. **MemGPT: Towards LLMs as Operating Systems**
   Packer et al., 2023 — https://arxiv.org/abs/2310.08560

### Coding Agents & Benchmarks
8. **SWE-bench: Can Language Models Resolve Real-World GitHub Issues?**
   Jimenez et al., 2023 — https://arxiv.org/abs/2310.06770

9. **OpenHands: An Open Platform for AI Software Developers as Generalist Agents**
   Wang et al., 2024 — https://arxiv.org/abs/2407.16741

10. **SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering**
    Yang et al., 2024 — https://arxiv.org/abs/2405.15793

### Safety & Evaluation
11. **Agent-SafetyBench: Evaluating the Safety of LLM Agents**
    Zhang et al., 2024 — https://arxiv.org/abs/2412.14470

12. **ToolEmu: Identifying Risks of LM Agents with an LM-Emulated Sandbox**
    Ruan et al., 2024 (ICLR 2024) — https://arxiv.org/abs/2309.15817

13. **A Survey of Memory-Augmented Large Language Models**
    Zhang et al., 2024 — https://arxiv.org/abs/2401.01333

### Standards & Protocols
14. **Model Context Protocol (MCP) — Official Specification**
    Anthropic / Linux Foundation — https://modelcontextprotocol.io/specification/

15. **MCP GitHub Repository**
    https://github.com/modelcontextprotocol/modelcontextprotocol

### Framework Documentation
16. **LangGraph Documentation** — https://langchain-ai.github.io/langgraph/
17. **AutoGen Documentation** — https://microsoft.github.io/autogen/
18. **CrewAI Documentation** — https://docs.crewai.com

### Talks & Essays
19. **Andrew Ng — Agentic Design Patterns (DeepLearning.AI)**
    https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/

20. **Lilian Weng — LLM Powered Autonomous Agents (OpenAI blog)**
    https://lilianweng.github.io/posts/2023-06-23-agent/

---

## Concepts for Knowledge Tree

1. **Agentic AI** — AI systems that autonomously pursue goals through perception, reasoning, planning, action, and memory
2. **Agent Loop** — The observe → think → act → observe cycle that drives agent execution
3. **Perception** — An agent's ability to observe and interpret its environment (text, images, tool outputs)
4. **Reasoning** — Using the LLM as a general-purpose thinking engine to evaluate situations and form strategies
5. **Planning** — Decomposing complex goals into ordered sequences of achievable sub-tasks
6. **Tool Use** — Extending agent capabilities by calling external functions, APIs, and services
7. **Memory** — Persisting information across steps and sessions (short-term, long-term, working)
8. **Reflection** — An agent evaluating and critiquing its own outputs to iteratively improve quality
9. **ReAct Pattern** — Interleaving reasoning traces with action execution for grounded, adaptive problem-solving
10. **Chain-of-Thought (CoT)** — Step-by-step reasoning within a single model forward pass
11. **Function Calling** — LLM generating structured tool invocations (name + JSON arguments) for host execution
12. **JSON Schema** — Standard format for describing tool parameters, enabling validation and discovery
13. **Model Context Protocol (MCP)** — Open standard (JSON-RPC 2.0) for connecting AI systems to tools and data sources
14. **MCP Primitives** — Resources (data), Tools (functions), and Prompts (templates) exposed by MCP servers
15. **Plan-and-Execute Architecture** — Separate planner and executor agents with re-planning on failure
16. **Reactive Agent** — Agent that decides each action based on current state without explicit upfront planning
17. **Tree of Thoughts (ToT)** — Search-based reasoning that explores multiple solution branches with evaluation and pruning
18. **Hierarchical Task Networks (HTN)** — Planning formalism where high-level tasks decompose into lower-level tasks recursively
19. **Task Decomposition** — Breaking complex goals into manageable, executable sub-tasks
20. **Episodic Memory** — Storing specific, time-stamped experiences for contextual retrieval
21. **Semantic Memory** — Storing generalized knowledge distilled from experience through reflection
22. **Working Memory (Scratchpad)** — Mutable, task-specific intermediate storage during agent execution
23. **Vector Store Memory** — Using embedding similarity search for retrieving relevant past experiences
24. **Reflexion** — Verbal reinforcement learning where agents learn from natural-language self-reflections
25. **Multi-Agent Systems** — Multiple specialized agents collaborating to solve complex tasks
26. **Supervisor-Worker Pattern** — Coordinator agent delegating to specialist worker agents
27. **Agent Debate** — Multiple agents with different perspectives discussing to improve output quality
28. **Code Agent** — Agent that writes, executes, and debugs code as its primary action mechanism
29. **Computer Use / GUI Agents** — Agents that interact with graphical interfaces via screenshots and actions
30. **SWE-bench** — Benchmark for evaluating autonomous coding agents on real GitHub issues
31. **Sandboxing** — Isolating agent execution environments to prevent unintended real-world effects
32. **Guardrails** — Runtime safety mechanisms: action gating, rate limiting, input/output filtering, kill switches
33. **Agent Alignment** — Ensuring autonomous agents act according to human intentions and values
34. **Instrumental Convergence** — Tendency for goal-pursuing agents to develop potentially problematic sub-goals
35. **Skill Library** — Stored collection of reusable agent capabilities (code functions, plans) that grows over time
36. **Defense in Depth** — Layering multiple safety mechanisms so no single failure causes harm
37. **Trajectory Evaluation** — Assessing the quality of an agent's entire sequence of decisions, not just the final output
38. **Generative Agents** — LLM-powered entities that simulate believable human behavior through memory and reflection
39. **Toolformer** — Self-supervised approach where LLMs learn when and how to use external tools
40. **MemGPT** — Hierarchical memory architecture treating LLM context management like an operating system's memory
