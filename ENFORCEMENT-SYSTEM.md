# Institutional Memory Enforcement System

**Prevents institutional memory drift and ensures convention-driven development**

## Overview

This enforcement system makes `conventions.md` and `symbol-index.md` the **mandatory foundation** for all development work. It prevents the institutional memory failures that plague most development teams by:

- **Automatic validation** of institutional memory integrity
- **Mandatory pre-checks** before any development begins
- **Drift detection** to catch when documentation becomes outdated
- **Automatic updates** when new decisions are made
- **Built-in enforcement** that makes bypassing impossible

## Quick Start

### Installation
```bash
npm install
```

### Initialize for New Project
```bash
npm run init
# Creates project-memory/conventions.md and project-memory/symbol-index.md templates
```

### Validate Institutional Memory
```bash
npm run validate
# Runs complete validation of institutional memory integrity
```

### Quick Health Check
```bash
npm run check
# Fast check of file existence and structure
```

## Core Commands

### Validation Commands
```bash
# Complete validation with drift detection
npm run validate

# Quick health check only
npm run check

# Detect institutional memory drift
npm run drift

# Verbose validation output
npm run enforce
```

### Decision Capture Commands
```bash
# Capture new architectural decision
npm run decision -- --title "Authentication Standard" --context "User login system" --standard "JWT + OAuth2" --rationale "Security and scalability" --scope "All auth systems"

# Capture new coordination pattern
npm run pattern -- --name "Sequential Validation" --context "Multi-agent coordination" --description "Architecture then security review" --usage "For system design decisions"
```

### Development Workflow
```bash
# Before starting any development
npm run validate

# During development - capture decisions immediately
memory-enforce decision --title "..." --context "..." --standard "..." --rationale "..."

# Validate continuously
npm run drift
```

## CLI Tool Reference

The `memory-enforce` CLI provides comprehensive institutional memory management:

### Commands

#### `memory-enforce validate`
Runs complete institutional memory validation:
- File existence and structure validation
- Content freshness checks (flags files older than 30 days)
- Convention conflict detection
- Automatic drift detection

**Options:**
- `-v, --verbose`: Show detailed validation results

#### `memory-enforce check`
Quick health check of institutional memory files:
- Validates required files exist
- Checks file structure integrity
- Fast validation for CI/CD pipelines

#### `memory-enforce drift`
Detects institutional memory drift:
- Invalid code references in symbol-index.md
- Stale conventions in conventions.md
- Convention conflicts
- Provides recommended corrective actions

#### `memory-enforce decision`
Captures new architectural decisions:
```bash
memory-enforce decision \
  --title "Database Architecture" \
  --context "E-commerce platform" \
  --standard "PostgreSQL + Redis" \
  --rationale "ACID compliance + caching performance" \
  --scope "All backend services"
```

**Required Options:**
- `-t, --title`: Decision title
- `-c, --context`: Project context
- `-s, --standard`: Technical standard chosen
- `-r, --rationale`: Why this decision was made

**Optional:**
- `--scope`: Application scope (defaults to "This project")

#### `memory-enforce pattern`
Captures coordination patterns:
```bash
memory-enforce pattern \
  --name "Security-First Design" \
  --context "Multi-agent coordination" \
  --description "Security review before implementation" \
  --usage "For all user-facing features" \
  --integrations "Security consultant, Senior architect"
```

**Required Options:**
- `-n, --name`: Pattern name
- `-c, --context`: Discovery context
- `-d, --description`: Pattern description
- `-u, --usage`: How to use the pattern

**Optional:**
- `-i, --integrations`: Integration points (comma-separated)

#### `memory-enforce init`
Initializes institutional memory for new projects:
- Creates `project-memory/` directory
- Generates template `conventions.md`
- Generates template `symbol-index.md`

**Options:**
- `--force`: Overwrite existing files

## Integration with Development Workflow

### Pre-commit Hooks
```bash
npm run install-hooks
# Installs git pre-commit hook that validates institutional memory
```

### CI/CD Integration
```yaml
# GitHub Actions example
- name: Validate Institutional Memory
  run: npm run validate
```

### Claude Integration
The framework provides an enhanced CLAUDE.md (`CLAUDE-ENFORCED.md`) that integrates enforcement:

```javascript
// Mandatory pre-checks before any AI development work
const enforcer = require('./institutional-memory-enforcer.js');
await enforcer.runMandatoryPreChecks();
```

## Enforcement Architecture

### Validation Layers

1. **File Existence & Structure**
   - Validates required files exist
   - Checks mandatory sections are present
   - Ensures proper markdown structure

2. **Content Freshness**
   - Flags files not updated in 30+ days
   - Detects stale conventions
   - Monitors institutional memory currency

3. **Convention Consistency**
   - Detects conflicting architectural decisions
   - Validates decision scope and applicability
   - Ensures single source of truth

4. **Reality Validation**
   - Cross-checks documented code references
   - Validates function locations and file paths
   - Prevents documentation drift from codebase

### Automatic Updates

When new decisions are made:
```javascript
const enforcer = new InstitutionalMemoryEnforcer();

// Immediately capture architectural decision
await enforcer.captureNewDecision({
  title: "Authentication Standard",
  context: "User management system",
  standard: "JWT + TOTP 2FA",
  rationale: "Security requirements + user experience",
  scope: "All authentication systems"
});

// Immediately capture coordination pattern
await enforcer.captureNewPattern({
  name: "Consensus Validation",
  context: "Security-critical decisions",
  description: "Multi-expert agreement required",
  usage: "For authentication, payment, data access decisions",
  integrations: ["Security consultant", "Senior architect", "Domain expert"]
});
```

## Failure Prevention

### Common Failure Modes Prevented

1. **Outdated Documentation**
   - Automatic freshness checking
   - Drift detection for code references
   - Stale convention identification

2. **Convention Conflicts**
   - Automatic conflict detection
   - Forced resolution before development
   - Clear precedence rules

3. **Bypassed Institutional Memory**
   - Mandatory pre-checks block development
   - No way to proceed without validation
   - Integration with all development tools

4. **Lost Architectural Decisions**
   - Immediate capture requirement
   - Structured decision documentation
   - Automatic pattern recognition

### Recovery Procedures

**If validation fails:**
1. Run `npm run drift` to identify specific issues
2. Follow recommended corrective actions
3. Re-run `npm run validate` to confirm fixes
4. Only proceed with development after validation passes

**If files are corrupted:**
1. Run `memory-enforce init --force` to restore structure
2. Manually restore content from git history
3. Validate restoration with `npm run check`
4. Update with current architectural state

## Success Metrics

The enforcement system is successful when:

- ✅ **Zero drift incidents** - Documentation always matches reality
- ✅ **100% decision capture** - All architectural choices documented
- ✅ **Convention compliance** - No conflicting or outdated standards
- ✅ **Automatic maintenance** - Institutional memory self-maintains
- ✅ **Development confidence** - Teams trust documented conventions

## Advanced Usage

### Custom Validation Rules
Extend the enforcer with project-specific validation:

```javascript
class CustomEnforcer extends InstitutionalMemoryEnforcer {
  async validateCustomRules() {
    // Add project-specific validation logic
  }
}
```

### Integration with Portableagency
When used with Portableagency, this system provides the institutional memory layer while Portableagency handles technical verification:

```javascript
// Portableagency handles technical validation
// AI DevOps Framework handles convention compliance
const memoryValid = await enforcer.runMandatoryPreChecks();
const techValid = await portableagency.runVerification();
```

---

**The enforcement system ensures that institutional memory becomes a living, self-maintaining foundation for all development work, preventing the knowledge decay and architectural drift that derail most software projects.**