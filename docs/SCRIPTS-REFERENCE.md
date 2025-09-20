# Scripts Reference

**Complete guide to all npm scripts and CLI commands**

## Core npm Scripts

### System Health Scripts

#### `npm run validate`
**Full system validation with enhanced checks**
```bash
npm run validate
```
- Runs complete institutional memory validation
- Checks core file integrity (conventions.md + symbol-index.md)
- Detects drift and inconsistencies
- Enhanced with think tool reasoning
- Exit code 1 if validation fails

#### `npm run check`
**Quick health check of institutional memory files**
```bash
npm run check
```
- Fast validation of file existence and basic structure
- No drift detection (use for CI/CD where speed matters)
- Basic structural integrity only

#### `npm run drift`
**Detect institutional memory drift and inconsistencies**
```bash
npm run drift
```
- Enhanced with structured reasoning
- Identifies stale references and conflicting decisions
- Provides prioritized resolution plan with effort estimates
- Uses think tool for intelligent analysis

### Core File Operations

#### `npm run search`
**Search conventions.md intelligently**
```bash
npm run search "authentication"
npm run search "database" --exact
```
- Smart pattern matching across all decision fields
- Automatic suggestions when no results found
- Related term recommendations

#### `npm run index`
**Navigate and query symbol-index.md**
```bash
npm run index --stats
npm run index --functions
npm run index --connections "API"
```
- Function and connection navigation
- Pattern discovery and documentation
- Symbol index health statistics

#### `npm run core`
**Core file utilities and health checks**
```bash
npm run core --health
npm run core --template technology
npm run core --conflicts
```
- Comprehensive core file utilities
- Decision templates and quality assessment
- Conflict detection and resolution

### Decision Management

#### `npm run decision`
**Capture new architectural decisions**
```bash
npm run decision
```
- Interactive decision capture with enhanced questioning
- Uses think tool for quality validation
- Applies appropriate templates based on decision type

#### `npm run pattern`
**Document discovered patterns**
```bash
npm run pattern
```
- Captures reusable patterns for symbol-index.md
- Enhanced with architectural impact assessment

### System Setup

#### `npm run init`
**Initialize institutional memory system**
```bash
npm run init
npm run init --force  # Reinitialize if needed
```
- Creates project-memory/ directory structure
- Generates clean template files for both core files
- Sets up basic validation structure

#### `npm run install-hooks`
**Install git pre-commit validation hooks**
```bash
npm run install-hooks
```
- Adds pre-commit validation to prevent corrupted institutional memory
- Runs `npm run validate` before each commit

### Development Scripts

#### `npm run enforce`
**Verbose validation for development**
```bash
npm run enforce
```
- Same as `npm run validate` but with detailed output
- Shows complete validation results and reasoning
- Useful for debugging validation issues

### Internal Scripts

#### `npm run memory:validate`
**Direct memory validation (used internally)**
```bash
npm run memory:validate
```
- Bypasses CLI wrapper for direct validation
- Used by other scripts and CI/CD integration

#### `npm run memory:drift`
**Direct drift detection (used internally)**
```bash
npm run memory:drift
```
- Direct drift detection without CLI formatting
- Returns exit code 1 if drift detected

## Enhanced CLI Commands

### Search Commands

#### `memory-enforce search <query> [options]`
**Advanced search with multiple options**

**Options:**
- `--exact` - Exact match instead of pattern matching
- `--section <section>` - Search within specific section

**Examples:**
```bash
memory-enforce search "authentication"
memory-enforce search "Node.js" --exact
memory-enforce search "database" --section "Technology Stack"
```

**Search Intelligence:**
- Patterns: title, standard, rationale, scope matching
- Suggestions: Related terms when no results found
- Context-aware: Considers decision scope and relationships

### Index Commands

#### `memory-enforce index [options]`
**Symbol-index.md navigation and querying**

**Options:**
- `--functions [pattern]` - List functions, optionally matching pattern
- `--connections [component]` - Show connections for component
- `--patterns` - List discovered patterns
- `--stats` - Show symbol index statistics

**Examples:**
```bash
memory-enforce index --stats
memory-enforce index --functions "auth"
memory-enforce index --connections "API"
memory-enforce index --patterns
```

### Core File Utilities

#### `memory-enforce core [options]`
**Comprehensive core file management**

**Options:**
- `--health` - Check core file health and quality
- `--template <type>` - Show decision template (technology/architecture/security)
- `--conflicts` - Detect decision conflicts
- `--orphans` - Find orphaned symbol references

**Examples:**
```bash
memory-enforce core --health
memory-enforce core --template technology
memory-enforce core --conflicts
memory-enforce core --orphans
```

### Decision Capture

#### `memory-enforce decision [options]`
**Structured decision capture with enhanced questioning**

**Options:**
- `--title <title>` - Decision title
- `--context <context>` - Project context
- `--standard <standard>` - Technical standard
- `--rationale <rationale>` - Decision rationale
- `--scope <scope>` - Application scope

**Enhanced Features:**
- Think tool integration for quality validation
- Contextual question generation
- Template application based on decision type
- Conflict detection before capture

### Pattern Documentation

#### `memory-enforce pattern [options]`
**Document patterns for symbol-index.md**

**Options:**
- `--name <name>` - Pattern name
- `--description <description>` - Pattern description
- `--usage <usage>` - When to apply this pattern
- `--context <context>` - Discovery context

**Enhanced Features:**
- Architectural impact assessment
- Symbol-index structure improvement analysis
- Integration point detection

## Script Combinations

### Daily Development Workflow
```bash
# Morning health check
npm run core --health

# Search before decisions
npm run search "your-topic"

# Capture decisions with enhanced questioning
npm run decision

# Check symbol index health
npm run index --stats
```

### Weekly Maintenance
```bash
# Comprehensive validation
npm run validate

# Check for conflicts and orphans
npm run core --conflicts
npm run core --orphans

# Monitor drift
npm run drift
```

### CI/CD Integration
```bash
# Fast validation for CI
npm run check

# Full validation for deployment
npm run validate

# Drift monitoring for quality gates
npm run drift
```

### Team Onboarding
```bash
# Setup system
npm run init

# Learn the structure
npm run core --health
npm run index --stats

# Practice search
npm run search "test"

# Install development hooks
npm run install-hooks
```

## Error Handling

### Common Exit Codes
- **0**: Success
- **1**: Validation failure, drift detected, or conflicts found

### Troubleshooting Scripts

#### Validation Failures
```bash
# Get detailed information
npm run enforce  # Verbose output

# Check specific issues
npm run core --health
npm run core --conflicts
```

#### Search Issues
```bash
# Try broader terms
npm run search "auth" instead of "authentication-service"

# Check suggestions in output
npm run search "nonexistent-term"  # Will show suggestions
```

#### Symbol Index Problems
```bash
# Check for broken references
npm run core --orphans

# Review statistics
npm run index --stats

# Validate structure
npm run validate
```

## Performance Notes

- **Fast commands**: `check`, `core --health`, `search`
- **Medium commands**: `validate`, `index --stats`
- **Slower commands**: `drift` (analyzes entire codebase), `core --orphans`

## Integration Examples

### Git Hooks
```bash
#!/bin/sh
# Pre-commit hook
npm run validate || exit 1
```

### CI/CD Pipeline
```yaml
steps:
  - name: Quick Health Check
    run: npm run check

  - name: Full Validation
    run: npm run validate

  - name: Drift Detection
    run: npm run drift
```

### Development Scripts
```bash
#!/bin/bash
# Daily development startup
echo "🔍 Checking institutional memory health..."
npm run core --health

echo "📊 Symbol index statistics:"
npm run index --stats

echo "⚠️  Checking for conflicts:"
npm run core --conflicts
```

---

**All scripts focus on maintaining high-quality conventions.md and symbol-index.md as the core institutional memory.**