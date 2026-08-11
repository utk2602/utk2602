<div align="center">

<img src="./ascii.svg" width="460" alt="utkarsh — self-typing ASCII portrait"/>

<img src="./stats.svg" width="620" alt="Contributions in the last year"/>

[x / twitter](https://x.com/utkarshhhhhhh26) &nbsp;·&nbsp;
[resume](https://github.com/utk2602/utkarsh-resume) &nbsp;·&nbsp;
[email](mailto:workutkarshkashyap@gmail.com)

</div>

<img src="./hd-about.svg" width="620" alt="about"/>

> coffee and code, from india.<br>
> TypeScript for most things, Go when the backend is the point.

Right now that's [rabbit-stack](https://github.com/utk2602/rabbit-stack) — self-hosted AI code review for GitHub — and<br>
[NomadNote](https://github.com/utk2602/Normad-Note), a local-first workspace that syncs through its own Go backend.

<img src="./hd-stack.svg" width="620" alt="stack"/>

<samp>typescript &nbsp; javascript &nbsp; go &nbsp; python &nbsp; react &nbsp; next.js &nbsp; node &nbsp; socket.io &nbsp; postgres &nbsp; prisma &nbsp; docker &nbsp; git</samp>

<img src="./hd-projects.svg" width="620" alt="projects"/>

**[rabbit-stack](https://github.com/utk2602/rabbit-stack)** &nbsp;·&nbsp; <samp>typescript, next.js</samp><br>
Self-hosted AI code review for GitHub. OAuth sign-in, fail-closed webhook<br>
verification, repo indexing with sensitive-file filters, structured reviews<br>
posted back to the pull request.

**[NomadNote](https://github.com/utk2602/Normad-Note)** &nbsp;·&nbsp; <samp>typescript, go</samp><br>
Local-first collaborative workspace. Edits land in IndexedDB first, queue<br>
through an operation outbox, then sync over WebSockets with Lamport-clock<br>
ordering and block-level conflict history.

**[HookForge](https://github.com/utk2602/Hooklikecrazy)** &nbsp;·&nbsp; <samp>go, react</samp><br>
Webhook delivery system: ingest URL in, Postgres event store, worker-pool<br>
delivery with retries and a dead-letter state, all visible on a dashboard.

**[Kysync](https://github.com/utk2602/Kysynq)** &nbsp;·&nbsp; <samp>typescript, socket.io</samp><br>
Real-time competitive typing duels — Next.js front, Socket.io game server,<br>
Postgres via Prisma. Has a terminal cousin in Go: [KeySync-CLI](https://github.com/utk2602/KeySync-CLI).

<img src="./hd-stats.svg" width="620" alt="stats"/>

<div align="center">

<img src="./streak.svg" width="620" alt="Current and longest streak"/>

<img src="./langs.svg" width="620" alt="Top languages by bytes and by repo"/>

<img src="./year.svg" width="620" alt="The last year of contributions, day by day"/>

</div>

<img src="./hd-about-this-page.svg" width="620" alt="about this page"/>

Every graphic here is generated, not embedded from anyone else's server.<br>
`ascii.svg` is my avatar pushed through a character ramp by<br>
[`scripts/avatar_portrait.py`](scripts/avatar_portrait.py); the stat graphics and<br>
these section headings are drawn by [a scheduled action](.github/workflows/stats.yml)<br>
straight from the GitHub GraphQL API, once a day, committing only what changed.

They animate with SMIL inside the SVG, because GitHub strips scripts from<br>
READMEs — and since nothing loads from a third party, nothing here can<br>
rate-limit or go dark. The headings are SVGs for the same reason: GitHub also<br>
strips CSS, so an image is the only way to put this page's own typeface on them.

The typeface is [JetBrains Mono](scripts/fonts), subset to just the characters<br>
each graphic draws and inlined as base64. Design and pipeline follow<br>
[a github profile that generates itself](https://agreeable-credit-859.notion.site/A-GitHub-profile-that-generates-itself-3abedfe9a65a81e4afc9daed90cb4e7e), by [andriidrok1](https://github.com/andriidrok1/andriidrok1).

Language totals cover public repositories only.
