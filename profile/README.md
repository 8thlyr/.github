## 8thlyr

**Open-source infrastructure for running fleets of AI agents.**

Small, sharp tools for the layer under the agent: runtimes, auth and gateways, browser and computer-use plumbing, CLIs built for agents to drive, eval harnesses, observability, orchestration and MCP servers. Each one does one job, ships with tests, CI and a demo, and runs on a box you own.

### Projects

<!-- PROJECTS:START -->
| Project | What it does | Lang |
|---|---|---|
| [**tuitree**](https://github.com/8thlyr/tuitree) | Terminal dashboard for git worktrees and GitHub PRs, built for running parallel coding agents | Rust |
| [**fan-curve**](https://github.com/8thlyr/fan-curve) | Native macOS temperature-based fan curve controller | Swift |
| [**runtest**](https://github.com/8thlyr/runtest) | Run coding-agent test commands at background priority on macOS (local/auto modes; remote routing planned) | Python |
<!-- PROJECTS:END -->

<sub>This list regenerates from the org's public repos on every push and once a day.</sub>

### Also by the maintainer

- [tuitree](https://github.com/jonathancostin/tuitree): a terminal dashboard for git worktrees and GitHub PRs. With one worktree per coding agent, it shows which are ahead, behind or conflicted.
- [runtest](https://github.com/jonathancostin/runtest): put it in front of an agent's test command (`runtest npm test`) and macOS runs it at background priority.
- [fan-curve](https://github.com/jonathancostin/fan-curve): a macOS menu-bar app that sets fan speed from CPU temperature.

### How we build

- **One job per tool.** Small enough to read in an afternoon, composable with the rest.
- **Agent-first interfaces.** Stable output, `--json`, real exit codes, no interactive traps.
- **Self-hostable.** No hosted dependency you can't swap out.
- **MIT licensed.** Use it, fork it, ship it.

### Get in touch

Open an issue on the repo it's about. Bugs, ideas and PRs are all welcome there.

Maintained by [Jonathan Costin](https://github.com/jonathancostin).
