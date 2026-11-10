## 8thlyr

**Open-source infrastructure for running fleets of AI agents.**

Small, sharp tools for the layer under the agent: runtimes, auth and gateways, browser and computer-use plumbing, CLIs built for agents to drive, eval harnesses, observability, orchestration and MCP servers. Each one does one job, ships with tests, CI and a demo, and runs on a box you own.

### Projects

<!-- PROJECTS:START -->
| Project | What it does | Lang |
|---|---|---|
| [**leakgate**](https://github.com/8thlyr/leakgate) | Pre-commit gate for the secrets AI coding agents write into config: blocks .claude/settings.local.json-style leaks gitleaks misses. | Go |
| [**seats**](https://github.com/8thlyr/seats) | Run your AI agents as seats in an org, kept in plain files: a charter, one approvals queue, a friction log and a nightly manager sweep. No server. | Python |
| [**nod**](https://github.com/8thlyr/nod) | A human approval queue for AI agents, kept in a markdown file. Agents ask, you nod, the blocked command continues. CLI + MCP server. | Go |
| [**studio-template**](https://github.com/8thlyr/studio-template) | Starter for 8thlyr agent-infra projects: Python, TypeScript or Go with CI, releases, Dependabot and a vhs demo, green on first push _(template)_ | Python |
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
