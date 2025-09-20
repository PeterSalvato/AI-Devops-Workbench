# Institutional Memory Guardrails

**Stop repeating architectural decisions. Document once, use everywhere.**

## What This Does

- Checks if your team already made an architectural decision before making a new one
- Asks you specific questions when decisions are missing, then documents the answers
- Ensures everyone uses the same documented standards consistently
- Updates documentation when you build new functionality

## How It Works

1. **Check existing decisions** - Before any architectural choice, check if it's already documented
2. **Capture missing decisions** - If no decision exists, ask team lead and document immediately  
3. **Use documented standards** - Apply established conventions to development work
4. **Update knowledge base** - Document new functionality and patterns after building

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

### Check for existing decision
```javascript
const guardrails = require('./institutional-memory-enforcer.js');
const decision = await guardrails.checkForExistingDecision('authentication');

if (decision.found) {
  // Use the documented standard
  use(decision.convention.standard);
} else {
  // Need to ask team and document decision
}
```

### Capture new decision
```bash
memory-enforce decision \
  --title "Database Choice" \
  --standard "PostgreSQL" \
  --rationale "ACID compliance needed" \
  --scope "All backend services"
```

### Validate system health
```bash
npm run validate  # Check file integrity
npm run drift     # Find outdated documentation
```

## File Structure

```
project-memory/
├── conventions.md     # Team architectural decisions
└── symbol-index.md   # Code structure and patterns
```

## Commands

```bash
npm run init          # Create initial files
npm run validate      # Check system health
npm run drift         # Find inconsistencies
npm run check         # Quick validation

memory-enforce decision   # Capture decision
memory-enforce pattern    # Document pattern
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

1. Install system
2. Document existing team standards
3. Train team on workflow (1 hour)
4. Start using for all architectural decisions

## Corporate Use

- No external dependencies
- Uses standard git repositories
- Integrates with existing development tools
- Complete audit trail of decisions

---

**Simple institutional memory for development teams.**