# Team Setup Guide

**Get your team using institutional memory guardrails in one week.**

## Day 1: Installation and Basic Setup

### Install system
```bash
git clone [repository]
cd institutional-memory-guardrails
npm install
npm run init
```

### Test installation
```bash
npm run validate  # Should pass
npm run check     # Should show template files exist
```

### Team meeting (30 minutes)
- Explain concept: document decisions once, use everywhere
- Show basic workflow: check → ask → capture → use
- Get team agreement to try for one week

## Day 2: Document Existing Standards

### Identify your current decisions
What has your team already decided? Common examples:
- Backend framework (Node.js, Python, Go, etc.)
- Database (PostgreSQL, MySQL, MongoDB, etc.)
- Frontend framework (React, Vue, Angular, etc.)
- Authentication method (JWT, sessions, OAuth, etc.)
- Testing approach (unit, integration, E2E tools)
- Code style (linting, formatting rules)

### Capture decisions with CLI
```bash
memory-enforce decision \
  --title "Backend Framework" \
  --standard "Node.js + Express + TypeScript" \
  --rationale "Team knows it, good ecosystem" \
  --scope "All backend services"

memory-enforce decision \
  --title "Database" \
  --standard "PostgreSQL" \
  --rationale "ACID compliance, team experience" \
  --scope "Primary data storage"
```

### Validate
```bash
npm run validate
cat project-memory/conventions.md  # Check your decisions are there
```

## Day 3: Practice the Workflow

### Each developer practices
1. Check for existing decision: `grep -i "authentication" project-memory/conventions.md`
2. If missing, capture new decision using CLI
3. Update symbol index with current codebase structure

### Practice scenarios
- "We need to add authentication" → Check conventions first
- "Should we use REST or GraphQL?" → Check conventions first  
- "What testing framework?" → Check conventions first

### Set up automation
```bash
npm run install-hooks  # Git pre-commit validation
```

## Day 4: Apply to Real Work

### Use guardrails for actual decisions
- Before making any architectural choice, check conventions first
- If no decision exists, ask team lead and document immediately
- Use documented standards consistently

### Update documentation
- After building anything, document new functions and patterns
- Keep symbol index current with actual codebase

## Day 5: Review and Optimize

### Evaluate what worked
- How much time saved on repeated discussions?
- Are documented decisions being followed?
- What friction points need addressing?

### Optimize process
- Simplify common decision types
- Create shortcuts for frequent patterns
- Integrate better with existing tools

## Ongoing Maintenance

### Weekly
- Run `npm run drift` to check for outdated documentation
- Update symbol index with new code structure
- Review and refine documented decisions

### Monthly
- Full validation: `npm run validate`
- Team retrospective on guardrails usage
- Update decision rationale if context changes

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

---

**Simple institutional memory for your development team.**