# Handoff — public replication preparation

**Status:** pre-release. This repository is *not* a verified replication of a scientific article. No publication-specific software or numerical results have been released.

**Repository relationship:** the complete research workspace is maintained separately and privately. There is no automatic synchronization or copied Git history. Do not provide its URL in anonymous-review documents.

**What is safe here now:** release instructions, scaffolding, safety checks, and synthetic/example placeholders. Do not confuse a scaffold test with numerical validation.

**Next authorized release task:** select files from the private research workspace using an explicit allowlist; audit intellectual-property and data rights, redact paths and identifiers, preserve licenses and provenance, and only then submit a public PR containing code, tests, dependencies and permitted outputs.

**Mandatory checks before asserting reproducibility:** successful clean-environment run, fixed seeds/tolerances, source-to-result provenance, non-proprietary test fixtures, and actual comparison to paper tables and figures. Retain a release manifest and record a reproducible commit/tag.

**Privacy:** no commercial Barchart/Databento observations, no private research history, no credentials. Public source and derivatives must be verified against vendor terms before release.

**GitHub Actions:** lightweight public-scaffold CI only. Heavy simulations and publication builds remain manual-only.
