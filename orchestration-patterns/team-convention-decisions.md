# Team Convention Decision Workflow

*Systematic process for making, documenting, and implementing team-wide architectural and process decisions*

**Pattern Type**: Team Governance & Decision Management  
**Use Case**: Establishing team conventions from scratch or updating existing standards  
**Prerequisites**: Team leads identified, decision-making authority established  

## Decision Triggers

### When Team Conventions Are Needed
- **New project starting** - No existing standards for technology stack
- **Pattern conflicts** - Individual developers using different approaches  
- **Quality issues** - Inconsistent code quality across team projects
- **Process problems** - Inefficient workflows or communication gaps
- **Tool standardization** - Team using different development tools

### Who Can Initiate Decisions
- **Technical Lead** - Architecture and technology stack decisions
- **Team Members** - Process improvements and tool preferences
- **Project Manager** - Workflow and collaboration standards
- **Security Lead** - Security requirements and standards

## Decision-Making Process

### Phase 1: Problem Identification & Proposal
```markdown
**TRIGGER**: Need for team standard identified

**INITIATOR ACTIONS**:
1. **Document Problem**: What inconsistency or gap needs addressing
2. **Research Options**: Investigate available solutions and approaches  
3. **Create Proposal**: Draft specific recommendation with rationale
4. **Gather Evidence**: Collect data supporting recommended approach

**DELIVERABLE**: Team convention proposal with supporting evidence
```

### Phase 2: Team Consultation & Discussion
```markdown
**TRIGGER**: Proposal ready for team review

**TEAM LEAD ACTIONS**:
1. **Distribute Proposal**: Share with relevant team members
2. **Schedule Discussion**: Allow adequate time for review and feedback
3. **Facilitate Debate**: Ensure all perspectives are heard
4. **Document Concerns**: Record objections and alternative suggestions

**DELIVERABLE**: Team feedback summary with consensus assessment
```

### Phase 3: Decision & Implementation
```markdown
**TRIGGER**: Discussion complete, decision ready

**DECISION MAKER ACTIONS**:
1. **Make Decision**: Choose approach based on team input
2. **Document Standard**: Add to project-memory/conventions.md
3. **Communicate Decision**: Notify all team members
4. **Plan Implementation**: Define timeline and migration approach

**DELIVERABLE**: Documented team convention with implementation plan
```

## Decision Templates

### Technology Stack Decision Template
```markdown
## Technology Decision: [Component Name]
**Decision Made**: [Date]
**Decision Maker**: [Name and role]  
**Context**: [Project/situation requiring this decision]

**Options Considered**:
1. **[Option 1]**: [Pros/cons, team familiarity, cost]
2. **[Option 2]**: [Pros/cons, team familiarity, cost]  
3. **[Option 3]**: [Pros/cons, team familiarity, cost]

**Team Input Summary**:
- [Team member concerns and preferences]
- [Key discussion points and debates]
- [Consensus level achieved]

**Final Decision**: [Chosen technology]
**Rationale**: [Why this choice was made]
**Implementation Timeline**: [When team must adopt]
**Migration Plan**: [How to transition existing projects]
**Review Date**: [When to reassess this decision]

### Implementation Standard:
[Code examples, configuration, usage patterns]
```

### Process Standard Decision Template
```markdown
## Process Decision: [Process Name]
**Decision Made**: [Date]  
**Decision Maker**: [Name and role]
**Context**: [Workflow problem or improvement opportunity]

**Current State**: [How team currently handles this]
**Proposed Change**: [New process being adopted]
**Expected Benefits**: [Why this improves team effectiveness]

**Team Concerns Addressed**:
- [Concern 1]: [How decision addresses this]
- [Concern 2]: [Resolution approach]

**Implementation Plan**:
- [Step 1]: [Timeline and responsibility]
- [Step 2]: [Timeline and responsibility]
- [Training needed]: [What team needs to learn]

**Success Metrics**: [How to measure if process works]
**Review Timeline**: [When to evaluate effectiveness]
```

### Code Quality Standard Template  
```markdown
## Code Quality Decision: [Standard Name]
**Decision Made**: [Date]
**Decision Maker**: [Name and role]  
**Context**: [Quality issue or consistency need]

**Standard Definition**: [Specific requirement being established]
**Enforcement Method**: [How standard will be checked/enforced]
**Tool Requirements**: [Linters, formatters, pre-commit hooks needed]

**Examples**:
```[language]
// Good example following standard
[code example]

// Bad example violating standard  
[code example with explanation]
```

**Grandfathering Policy**: [How to handle existing code]
**Exception Process**: [When/how standards can be bypassed]
**Training Resources**: [Where team learns this standard]
```

## Decision Authority Matrix

### Decision Types & Authority Levels
| Decision Category | Final Authority | Required Input | Timeline |
|------------------|----------------|----------------|----------|
| **Architecture** | Technical Lead | Senior developers | 1-2 weeks |
| **Security** | Security Lead | Technical Lead + Team | 1 week |  
| **Process** | Team consensus | All team members | 2-3 weeks |
| **Tools** | Team Lead | Individual preferences | 1 week |
| **Code Style** | Technical Lead | Team discussion | 1 week |

### Emergency Decision Process
For urgent decisions (security issues, blocking problems):
1. **Technical Lead** makes immediate decision
2. **Document rationale** within 24 hours
3. **Team review** within 1 week
4. **Adjust if needed** based on team feedback

## Implementation Guidelines

### Convention Documentation Requirements
```markdown
## Required Information for All Decisions:
- **Decision context** - Why this was needed
- **Options considered** - What alternatives were evaluated
- **Team input** - How consensus was built
- **Implementation details** - Specific technical requirements
- **Migration plan** - How existing projects transition
- **Review schedule** - When decision will be reassessed
```

### Communication Standards
- **Decision announcements** in team meetings and chat
- **Implementation timelines** clearly communicated
- **Training resources** provided for complex standards
- **Exception requests** handled through documented process

### Convention Evolution
- **Quarterly review** of all active conventions
- **Impact assessment** - Are standards helping or hindering?
- **Update process** for outdated or ineffective standards
- **Sunset process** for conventions no longer needed

## Success Metrics

### Decision Quality Indicators
- **Team adoption rate** - Percentage actually following conventions
- **Consistency improvement** - Reduced variation across projects
- **Quality metrics** - Bug reduction, review time improvement
- **Team satisfaction** - Developer feedback on convention usefulness

### Process Effectiveness  
- **Decision speed** - Time from problem to implemented solution
- **Consensus quality** - Level of team buy-in achieved
- **Implementation success** - Standards actually adopted vs documented
- **Evolution responsiveness** - How quickly bad decisions are corrected

## Common Decision Examples

### Typical First Decisions for New Teams
1. **Backend Technology Stack** - Language, framework, database
2. **Frontend Technology Stack** - Framework, styling approach, build tools
3. **Code Style Standards** - Formatting, naming conventions, structure
4. **Git Workflow** - Branching strategy, commit message format
5. **Testing Requirements** - Coverage minimums, testing frameworks
6. **Security Baseline** - Authentication patterns, security reviews

### Process Decisions Teams Often Need
1. **Code Review Process** - Who reviews, approval requirements
2. **Deployment Workflow** - How code moves to production
3. **Documentation Standards** - What must be documented, format
4. **Communication Protocols** - Stand-ups, planning, issue reporting
5. **Quality Gates** - What must pass before code ships

---

*This workflow ensures team conventions are established systematically with proper input, clear authority, and effective implementation rather than emerging randomly or through conflict.*