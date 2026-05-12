# Install PEA git hooks into the current repo's .git/hooks/.
# Run from the target repo root.
$ErrorActionPreference = 'Stop'

$repoRoot = (git rev-parse --show-toplevel 2>$null)
if (-not $repoRoot) {
    Write-Error "Not inside a git repo."
    exit 1
}

$hooksSrc = Join-Path $PSScriptRoot 'hooks'
$hooksDst = Join-Path $repoRoot '.git\hooks'

Copy-Item (Join-Path $hooksSrc 'pre-commit') (Join-Path $hooksDst 'pre-commit') -Force

Write-Host "Installed pre-commit hook to $hooksDst\pre-commit"
