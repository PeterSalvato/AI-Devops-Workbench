# Institutional Memory Guardrails

**Stop repeating architectural decisions. Document once, use everywhere.**

## What This Does

- Checks if your team already made an architectural decision before making a new one
- Asks you specific questions when decisions are missing, then documents the answers
- Ensures everyone uses the same documented standards consistently
- Updates documentation when you build new functionality

## How It Works

1. **Human** asks Claude to build a feature
2. **Claude** automatically checks existing architectural decisions 
3. **Claude** asks specific questions for missing decisions, then documents them
4. **Claude** implements using documented standards and updates the knowledge base
5. **Human** validates system health periodically

## Installation

### For Visual Studio + WSL Teams
```bash
# In WSL terminal within Visual Studio
cd /mnt/c/your-project-path
git clone [repository] institutional-memory-guardrails
cd institutional-memory-guardrails

# Install Node.js if needed
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install system
npm install
npm run init
```

### For Other Environments
```bash
git clone [repository]
cd institutional-memory-guardrails
npm install
npm run init
```

## Basic Usage

### What Humans Do
```bash
# One-time setup
npm install
npm run init

# Periodic maintenance  
npm run validate  # Check file integrity
npm run drift     # Find outdated documentation
```

### What Claude Does Automatically
```javascript
// Claude runs this before any development work
const guardrails = require('./institutional-memory-enforcer.js');
const decision = await guardrails.checkForExistingDecision('authentication');

if (decision.found) {
  // Use the documented standard
  use(decision.convention.standard);
} else {
  // Ask human specific questions and capture decision
  memory-enforce decision --title "..." --standard "..." --rationale "..."
}
```

## File Structure

```
project-memory/
├── conventions.md     # Team architectural decisions
└── symbol-index.md   # Code structure and patterns
```

## Commands

### Core File Operations
```bash
# Focus on conventions.md and symbol-index.md
npm run core          # Core file utilities menu
npm run search        # Search conventions.md
npm run index         # Navigate symbol-index.md
```

### System Health
```bash
npm run init          # Create initial files
npm run validate      # Complete system validation
npm run drift         # Find inconsistencies
npm run check         # Quick health check
```

### Decision Management
```bash
npm run decision      # Capture new decision
npm run pattern       # Document pattern
```

### Enhanced CLI Commands

**Search conventions.md:**
```bash
memory-enforce search "authentication"     # Find auth decisions
memory-enforce search "database" --exact   # Exact match only
memory-enforce search "api" --section "Security"  # Search in section
```

**Navigate symbol-index.md:**
```bash
memory-enforce index --functions           # List all functions
memory-enforce index --functions "auth"    # Functions matching pattern
memory-enforce index --connections "API"   # Connections for component
memory-enforce index --patterns            # Show discovered patterns
memory-enforce index --stats               # Symbol index statistics
```

**Core file utilities:**
```bash
memory-enforce core --health               # Check core file health
memory-enforce core --template technology  # Show decision template
memory-enforce core --conflicts            # Detect decision conflicts
memory-enforce core --orphans              # Find broken references
```

## Integration

### Git hooks
```bash
npm run install-hooks  # Pre-commit validation
```

### CI/CD
```yaml
- name: Validate Conventions
  run: npm run validate
```

## Decision Types

Common decisions to document:
- Authentication methods
- Database choices  
- Frontend frameworks
- API design patterns
- Testing strategies
- Deployment approaches

## Team Setup

1. **Install system** - Run `npm install && npm run init`
2. **Learn core file focus** - Study conventions.md and symbol-index.md structure
3. **Practice enhanced workflow** - Use search and core utilities
4. **Train team on Claude integration** - Review enhanced CLAUDE.md instructions
5. **Start using for all decisions** - Begin with core templates and enhanced reasoning

### Quick Start for Teams
```bash
# 1. Setup
npm install && npm run init

# 2. Learn the system
memory-enforce core --health        # Check core file status
memory-enforce core --template technology  # See decision templates

# 3. Search existing decisions
memory-enforce search "your-topic"

# 4. Capture new decisions with enhanced questions
memory-enforce decision --title "..." --standard "..." --rationale "..."

# 5. Monitor symbol index
memory-enforce index --stats
```

## Corporate Use

- **No external dependencies** - Pure Node.js, works with any git repository
- **Visual Studio + WSL compatible** - Designed for corporate development environments
- **Enhanced Claude integration** - Structured reasoning and core file focus
- **Complete audit trail** - Every decision and pattern documented
- **Core file architecture** - Two sacred files (conventions.md, symbol-index.md) + enhanced tooling

## New Features (Enhanced with Claude Code Best Practices)

### 🔍 **Enhanced Search & Discovery**
- Smart search across conventions.md with suggestions
- Pattern-based symbol-index.md navigation
- Core file health monitoring and quality scoring

### 🧠 **Structured Reasoning (Think Tool)**
- Automatic conflict detection in decisions
- Quality assessment of institutional memory
- Enhanced question generation for comprehensive documentation

### 🛠️ **Core File Utilities**
- Decision templates (Technology, Architecture, Security)
- Symbol-index templates (Functions, Connections, Patterns)
- Orphaned reference detection and cleanup
- Core file integrity validation

### 📋 **Enhanced Claude Instructions**
- Core file search patterns (`grep` commands)
- Copy-paste ready templates
- Workflow enhancement with contextual reasoning
- Symbol-index update prioritization

---

**Institutional memory guardrails enhanced with Claude Code best practices - keeping conventions.md and symbol-index.md at the center.**