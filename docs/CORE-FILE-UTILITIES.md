# Core File Utilities Documentation

**Enhanced tools for managing conventions.md and symbol-index.md**

## Overview

The enhanced institutional memory system provides powerful utilities specifically designed to maintain the quality and integrity of your two sacred files: `conventions.md` and `symbol-index.md`.

## Command Categories

### 🔍 Search Commands

#### `memory-enforce search <query>`
Smart search across conventions.md with intelligent suggestions.

```bash
# Basic search
memory-enforce search "authentication"

# Exact match only
memory-enforce search "Node.js" --exact

# Search within specific section
memory-enforce search "database" --section "Technology Stack"
```

**Features:**
- Pattern matching across title, standard, rationale, and scope
- Automatic search suggestions when no results found
- Related term suggestions (e.g., "auth" suggests "authentication", "login", "security")

#### `npm run search`
Shortcut for the search command.

### 📊 Symbol Index Navigation

#### `memory-enforce index [options]`
Query and navigate symbol-index.md contents.

```bash
# Show statistics
memory-enforce index --stats

# List all functions
memory-enforce index --functions

# Find functions matching pattern
memory-enforce index --functions "auth"

# Show connections for component
memory-enforce index --connections "API"

# List discovered patterns
memory-enforce index --patterns
```

**Output Example:**
```
📊 Symbol Index Statistics:
  Functions: 23
  Connections: 15
  Patterns: 4
  Last Updated: 2024-09-20
```

### 🛠️ Core File Health

#### `memory-enforce core --health`
Comprehensive health check for both core files.

```bash
memory-enforce core --health
```

**Output Example:**
```
📋 conventions.md:
  Decisions: 8
  Sections: 4
  Recent Activity: This month

🔗 symbol-index.md:
  Functions: 23
  Connections: 15
  Patterns: 4
  Stale References: 0
```

**Health Indicators:**
- **Decisions count**: Number of documented decisions
- **Sections**: Structural organization level
- **Recent Activity**: When last updated
- **Stale References**: Broken file paths or invalid references

### 📝 Templates

#### `memory-enforce core --template <type>`
Display decision templates for consistent documentation.

```bash
# Technology decisions
memory-enforce core --template technology

# Architecture patterns
memory-enforce core --template architecture

# Security requirements
memory-enforce core --template security
```

**Available Templates:**
- `technology` - For framework, language, and tool decisions
- `architecture` - For design patterns and system structure
- `security` - For security standards and requirements

### ⚠️ Quality Assurance

#### `memory-enforce core --conflicts`
Detect conflicting decisions in conventions.md.

```bash
memory-enforce core --conflicts
```

**Conflict Types Detected:**
- Same scope with different standards
- Similar decisions with conflicting approaches
- Overlapping requirements that contradict

#### `memory-enforce core --orphans`
Find broken references in symbol-index.md.

```bash
memory-enforce core --orphans
```

**Finds:**
- File references that no longer exist
- Invalid file paths
- Broken connections between components

## Enhanced Features

### Think Tool Integration

The enhanced system includes structured reasoning that automatically:

1. **Analyzes decision quality** - Checks for complete rationale, scope, and standards
2. **Detects conflicts** - Identifies contradictory decisions before they cause problems
3. **Assesses symbol index impact** - Prioritizes updates by architectural importance
4. **Generates contextual questions** - Creates better questions for comprehensive documentation

### Core File Quality Scoring

The system provides quality metrics for both core files:

**conventions.md Quality Score:**
- 100 points base
- -25 for missing rationale
- -25 for missing scope
- -25 for missing standard
- -25 for missing title

**symbol-index.md Quality Score:**
- 80 points base
- +10 for good documentation
- +5 for proper file paths
- +5 for connection purposes
- +5 for complexity bonus

### Search Intelligence

Enhanced search includes:
- **Pattern matching** across all decision fields
- **Related term suggestions** when searches fail
- **Context-aware results** that consider decision scope
- **Suggestion engine** for common technology terms

## Integration with Claude

### Enhanced CLAUDE.md Instructions

The system now provides Claude with:

1. **Core file search patterns** - Predefined `grep` commands for common searches
2. **Decision templates** - Copy-paste ready formats for consistent decisions
3. **Symbol-index templates** - Structured formats for function and connection documentation
4. **Workflow enhancement** - Contextual reasoning and quality validation

### Structured Reasoning Process

Claude now follows this enhanced workflow:

1. **CORE FILE ANALYSIS** - Check conventions.md for existing decisions
2. **CONFLICT DETECTION** - Analyze for conflicts that could corrupt conventions.md
3. **QUALITY ASSESSMENT** - Evaluate decision completeness and usefulness
4. **ENHANCED QUESTIONING** - Generate comprehensive questions for better documentation
5. **SYMBOL INDEX IMPACT** - Assess how changes improve symbol-index.md navigation

## Best Practices

### Daily Usage

```bash
# Morning health check
memory-enforce core --health

# Before making decisions
memory-enforce search "your-topic"

# After development work
memory-enforce index --stats
memory-enforce core --orphans
```

### Weekly Maintenance

```bash
# Comprehensive validation
npm run validate

# Check for conflicts
memory-enforce core --conflicts

# Monitor drift
npm run drift
```

### Quality Monitoring

```bash
# Track core file quality over time
memory-enforce core --health | grep -E "(Decisions|Functions|Stale)"

# Ensure search effectiveness
memory-enforce search "common-term" | wc -l
```

## Troubleshooting

### Search Returns No Results

1. Try broader terms: `memory-enforce search "auth"` instead of `memory-enforce search "authentication-middleware"`
2. Check suggestions: The system will suggest related terms
3. Use manual patterns: `grep -i "auth\|login\|security" project-memory/conventions.md`

### Health Check Shows Issues

1. **High stale references**: Run `memory-enforce core --orphans` to identify and fix
2. **Low decision count**: Focus on documenting architectural decisions
3. **Old activity**: Encourage regular decision updates

### Conflicts Detected

1. Review conflicting decisions: `memory-enforce core --conflicts`
2. Resolve by updating or merging similar decisions
3. Use scoping to differentiate when both decisions are valid

## Advanced Usage

### Custom Search Patterns

```bash
# Search by date
grep -A 5 "$(date +%Y-%m)" project-memory/conventions.md

# Search by scope
grep -A 3 -B 1 "Apply To" project-memory/conventions.md

# Find recent decisions
grep -A 2 "**Standard**:" project-memory/conventions.md
```

### Automation Integration

```bash
# CI/CD health check
memory-enforce core --health > health-report.txt

# Pre-commit validation
memory-enforce core --conflicts || exit 1

# Regular maintenance script
#!/bin/bash
memory-enforce core --health
memory-enforce core --orphans
npm run drift
```

---

**These utilities keep conventions.md and symbol-index.md as the central, high-quality source of truth for your team's institutional memory.**