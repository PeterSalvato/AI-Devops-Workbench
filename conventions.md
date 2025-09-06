# Meta-Agent Orchestration Conventions

*This document defines the rules and patterns for coordinating AI agents in development workflows.*

## Core Orchestration Principles

### 1. Consultation Before Production
- **Always consult before building** - Strategic analysis precedes implementation
- **Document all decisions** - Rationale and trade-offs must be clear
- **Pass complete context** - Production agents receive full consultation outputs

### 2. Agent Coordination Rules
- **Security consultant required** for authentication, payments, sensitive data handling
- **Senior architect required** for system design and technology stack decisions
- **UX strategist required** for user-facing features and interfaces
- **Performance expert required** for high-traffic or performance-critical components

### 3. Quality Gates
- **90% minimum** for production deployments
- **95% minimum** for security-critical systems (auth, payments, PII)
- **All agents must agree** on major architectural decisions
- **Security requirements are non-negotiable** - security consultant has veto power

## Agent Handoff Protocols

### Consultation → Production Pipeline
1. **Consultation Phase Complete** when:
   - Requirements are clearly understood and documented
   - Architecture decisions have clear rationale
   - Security requirements are identified and specified
   - All consultants agree on approach

2. **Production Handoff Includes**:
   - Complete technical specifications
   - Implementation strategy with clear phases
   - Security requirements and validation criteria
   - Quality standards and acceptance criteria

3. **Production Phase Complete** when:
   - Implementation matches consultation specifications
   - All security requirements are properly implemented
   - Code quality meets standards (tests, documentation, patterns)
   - Integration points work correctly

### Inter-Agent Communication
- **Backend ↔ Frontend**: API contracts must be agreed before implementation
- **Security → All Agents**: Security requirements flow to all relevant agents
- **Architect → Builders**: Architecture decisions guide all implementation
- **Reviewers**: Validate against consultation recommendations

## Conflict Resolution Strategies

### When Agents Disagree
1. **Present Options** - Show all perspectives with trade-offs
2. **Highlight Implications** - What each choice means for the project
3. **Seek User Input** - For business/preference decisions
4. **Apply Hierarchy** - For technical decisions, defer to domain expert

### Resolution Hierarchy
- **Security**: Security consultant > All others (for security concerns)
- **Architecture**: Senior architect > Builders (for design decisions)
- **UX**: UX strategist > All others (for user experience decisions)
- **Performance**: Performance expert > All others (for optimization decisions)

### Escalation Rules
- **Technical conflicts**: Escalate to senior architect
- **Security concerns**: Security consultant has final say
- **Business decisions**: Present options to user for choice
- **Resource constraints**: Document trade-offs, user decides

## Pattern-Specific Rules

### Feature Development
- **Pattern**: consultation_then_production
- **Required**: Senior architect OR existing architecture + domain consultants
- **Flow**: Consultation → Production → Validation
- **Quality Gate**: 90% minimum, all requirements met

### Code Review
- **Pattern**: consensus_validation
- **Required**: Relevant domain experts (security, performance, architecture)
- **Flow**: Parallel review → Consensus → Recommendations
- **Quality Gate**: 95% minimum for production approval

### Security Audit
- **Pattern**: hierarchical_security
- **Required**: Security consultant + relevant implementation experts
- **Flow**: Threat analysis → Implementation review → Penetration testing
- **Quality Gate**: 100% security requirements, no critical vulnerabilities

### Architecture Design
- **Pattern**: collaborative_design
- **Required**: Senior architect + relevant domain consultants
- **Flow**: Requirements → Design options → Consensus → Specification
- **Quality Gate**: Architecture supports all requirements, clear rationale

## Self-Updating Rules

### When to Update This Document
- **New patterns emerge** from successful project coordination
- **Conflict resolution learnings** from difficult decisions
- **Quality threshold adjustments** based on project outcomes
- **Process improvements** discovered during development

### Update Format
```markdown
## New Rule Added: [Date]
- **Context**: [What situation led to this rule]
- **Rule**: [The new convention or process]
- **Rationale**: [Why this improves coordination]
- **Impact**: [What changes in behavior]
```

### Review Triggers
- After major project completions
- When patterns consistently fail or succeed
- When new agent types are added
- When quality issues are discovered

## Project-Specific Overrides

### Authentication Systems
- **Quality threshold**: 95% minimum
- **Required agents**: Senior architect + Security consultant + Backend builder + Security implementer
- **Special rules**: Penetration testing required, compliance validation

### Payment Processing  
- **Quality threshold**: 100% security, 95% overall
- **Required agents**: Senior architect + Security consultant + Backend builder + Security implementer
- **Special rules**: PCI DSS compliance, financial regulations, audit trail

### Public APIs
- **Quality threshold**: 90% minimum
- **Required agents**: Senior architect + Backend builder + Security consultant
- **Special rules**: Rate limiting required, comprehensive documentation, versioning strategy

### Performance-Critical Features
- **Quality threshold**: 90% minimum + performance benchmarks
- **Required agents**: Senior architect + Performance expert + relevant builders
- **Special rules**: Load testing required, monitoring implementation, optimization validation

---

*This document is automatically updated based on project learnings and coordination experiences. Last updated: [Date will be auto-updated by Claude during sessions]*