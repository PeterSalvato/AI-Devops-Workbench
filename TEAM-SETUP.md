# Team Setup Guide (Enhanced)

**Get your team using enhanced institutional memory guardrails in one week.**

## Day 1: Installation and Enhanced Setup

### Install system (Visual Studio + WSL)
```bash
# In WSL terminal within Visual Studio
cd /mnt/c/your-project-path
git clone [repository] institutional-memory-guardrails
cd institutional-memory-guardrails
npm install
npm run init
```

### Test enhanced installation
```bash
npm run validate        # Complete system validation
npm run core --health   # Check core file health
npm run search "test"   # Test search functionality
npm run index --stats   # Check symbol index statistics
```

### Team meeting (45 minutes)
- **Explain enhanced concept**: Two sacred files (conventions.md + symbol-index.md) + powerful tooling
- **Show enhanced workflow**: search → think → capture → document → validate
- **Demo new features**: Core file utilities, templates, structured reasoning
- **Claude integration**: Enhanced instructions for better decision support
- Get team agreement to try enhanced system for one week

## Day 2: Document Existing Standards

### Identify your current decisions
What has your team already decided? Common examples:
- Backend framework (Node.js, Python, Go, etc.)
- Database (PostgreSQL, MySQL, MongoDB, etc.)
- Frontend framework (React, Vue, Angular, etc.)
- Authentication method (JWT, sessions, OAuth, etc.)
- Testing approach (unit, integration, E2E tools)
- Code style (linting, formatting rules)

### Capture decisions with enhanced CLI
```bash
# Use enhanced templates
memory-enforce core --template technology  # See template first

# Capture with structured approach
memory-enforce decision \
  --title "Backend Framework" \
  --standard "Node.js + Express + TypeScript" \
  --rationale "Team knows it, good ecosystem, strong typing" \
  --scope "All backend services"

memory-enforce decision \
  --title "Database Choice" \
  --standard "PostgreSQL" \
  --rationale "ACID compliance, team experience, enterprise features" \
  --scope "Primary data storage"
```

### Enhanced validation
```bash
npm run validate            # Complete system validation
npm run core --health       # Check core file quality
npm run core --conflicts    # Detect any decision conflicts
memory-enforce search "backend"  # Test search functionality
```

## Day 3: Practice the Enhanced Workflow

### Each developer practices enhanced search
```bash
# Enhanced search patterns (from CLAUDE.md)
memory-enforce search "authentication"        # Smart search
memory-enforce search "auth" --exact          # Exact match
grep -i "authentication\|auth\|login" project-memory/conventions.md  # Manual pattern

# Navigate symbol index
memory-enforce index --functions              # See all functions
memory-enforce index --connections            # See all connections
memory-enforce index --stats                  # Get overview
```

### Practice enhanced scenarios
- **"We need to add authentication"** →
  1. `memory-enforce search "auth"`
  2. If not found, use `memory-enforce core --template security`
  3. Capture with enhanced questions
- **"Should we use REST or GraphQL?"** →
  1. `memory-enforce search "api"`
  2. Check existing API standards
  3. Use think tool reasoning for conflicts
- **"What testing framework?"** →
  1. `memory-enforce search "test"`
  2. Review existing testing decisions

### Set up enhanced automation
```bash
npm run install-hooks      # Git pre-commit validation
npm run core --health      # Add to CI/CD pipeline
```

## Day 4: Apply Enhanced Guardrails to Real Work

### Enhanced decision workflow
1. **Smart search first**: `memory-enforce search "your-topic"`
2. **Use structured reasoning**: Think tool automatically analyzes conflicts
3. **Apply templates**: Use appropriate template for decision type
4. **Quality validation**: System checks decision completeness
5. **Document with context**: Enhanced questions capture comprehensive info

### Enhanced symbol index updates
```bash
# After building features, Claude automatically:
# 1. Analyzes new functions and connections
# 2. Detects emerging patterns
# 3. Assesses symbol-index.md quality improvements
# 4. Prioritizes updates by architectural impact

# Manual symbol index health check
memory-enforce index --stats        # Check current state
memory-enforce core --orphans       # Find broken references
```

### Core file quality monitoring
```bash
memory-enforce core --health        # Check both core files
memory-enforce core --conflicts     # Detect decision conflicts
npm run drift                      # Find documentation drift
```

## Day 5: Review and Optimize Enhanced System

### Evaluate enhanced features
- **Core file quality**: Run `memory-enforce core --health` - are both files comprehensive?
- **Search effectiveness**: Is `memory-enforce search` finding relevant decisions?
- **Think tool value**: Are conflict detections and quality assessments helpful?
- **Template usage**: Are decision templates improving documentation consistency?

### Enhanced optimization strategies
```bash
# Create team-specific shortcuts
alias mem-search='memory-enforce search'
alias mem-health='memory-enforce core --health'
alias mem-template='memory-enforce core --template'

# Integrate with IDE (Visual Studio + WSL)
# Add core file status to status bar
# Create snippets for common decision templates
```

### Core file excellence metrics
- **conventions.md**: Decision quality score >80%, no conflicts
- **symbol-index.md**: <5 stale references, comprehensive pattern documentation
- **Team adoption**: >90% of architectural decisions documented
- **Search usage**: Developers use search before asking questions

## Enhanced Ongoing Maintenance

### Weekly (Enhanced)
```bash
npm run drift                    # Check for documentation drift
memory-enforce core --health     # Monitor core file quality
memory-enforce core --orphans    # Find broken references
memory-enforce index --stats     # Symbol index health check
```

### Monthly (Enhanced)
```bash
npm run validate                 # Complete system validation
memory-enforce core --conflicts  # Check for decision conflicts
memory-enforce search "recent"   # Review recent decisions
```

### Quarterly (New)
- **Core file quality review**: Assess decision completeness and symbol index accuracy
- **Think tool effectiveness**: Review conflict detections and reasoning quality
- **Template refinement**: Update decision templates based on team usage
- **Search pattern optimization**: Improve search patterns for common queries

## Team Roles

### Technical Lead
- Final decision authority for architectural choices
- Maintains institutional memory system health
- Resolves conflicts between documented standards

### Developers  
- Check conventions before architectural decisions
- Propose new decisions when gaps found
- Update symbol index after building features

### Team
- Consensus on general coding standards
- Input on major architectural directions
- Feedback on guardrails process improvements

## Common Issues

### "Too much overhead"
- Focus only on architectural decisions, not minor preferences
- Pre-populate common decisions to reduce questioning
- Streamline CLI commands for frequent use cases

### "Decisions are outdated"
- Regular review schedule (monthly)
- Update rationale when context changes
- Remove or modify decisions that no longer apply

### "Team doesn't follow documented standards"
- Add validation to CI/CD pipeline
- Include convention compliance in code review
- Address specific friction points in workflow

## Success Indicators

- Repeated architectural discussions decrease
- New team members understand standards faster
- Implementation consistency improves across projects
- Team knowledge preserved when people change roles

## Enhanced Success Indicators

### Core File Quality Metrics
- **conventions.md quality score**: >85% (use `memory-enforce core --health`)
- **symbol-index.md completeness**: <3 stale references
- **Decision search success**: >95% of searches find relevant decisions
- **Conflict prevention**: Zero conflicting decisions detected

### Team Performance Indicators
- **Reduced decision time**: 50% faster architectural choices
- **Improved consistency**: Uniform implementation across features
- **Enhanced onboarding**: New team members productive in <2 days
- **Knowledge retention**: Decisions survive team member transitions

### Enhanced Tool Adoption
- **Search-first behavior**: Developers search before asking
- **Template usage**: >80% of decisions use templates
- **Core file monitoring**: Regular health checks performed
- **Claude integration**: Enhanced reasoning actively used

---

**Enhanced institutional memory guardrails with Claude Code best practices - keeping conventions.md and symbol-index.md at the center.**