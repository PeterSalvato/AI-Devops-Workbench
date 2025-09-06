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

### 3. Quality Standards
- **Production readiness** validated through systematic review
- **Security-critical systems** require comprehensive security consultant validation
- **Major architectural decisions** require consensus across relevant agents
- **Security requirements are non-negotiable** - security consultant has veto authority

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
- **Completion**: All requirements implemented and validated

### Code Review
- **Pattern**: consensus_validation
- **Required**: Relevant domain experts (security, performance, architecture)
- **Flow**: Parallel review → Consensus → Recommendations
- **Completion**: Production-ready code with documented recommendations

### Security Audit
- **Pattern**: hierarchical_security
- **Required**: Security consultant + relevant implementation experts
- **Flow**: Threat analysis → Implementation review → Security testing
- **Completion**: Security requirements satisfied, vulnerabilities addressed

### Architecture Design
- **Pattern**: collaborative_design
- **Required**: Senior architect + relevant domain consultants
- **Flow**: Requirements → Design options → Consensus → Specification
- **Completion**: Architecture specification with clear rationale and trade-offs

## Human Decision Codification

### When Conventions Are Established
- **Human makes architectural decisions** during agent proposal phases
- **Technology stack preferences** chosen from architect recommendations  
- **Security standards selected** from security consultant options
- **Process preferences established** when coordinating multi-agent work

### Convention Update Triggers
- **Immediate**: When human decides on architectural approaches, technology choices, security standards
- **Project completion**: Process improvements and coordination patterns that worked well
- **Conflict resolution**: When resolution approaches prove effective for similar future conflicts

### Decision Documentation Format
```markdown  
## Decision Codified: [Date]
- **Context**: [What project/situation required this decision]
- **Human Decision**: [Specific architectural/technical choice made]
- **Agent Proposals**: [What options were presented by which agents]
- **Rationale**: [Why human selected this approach]
- **Scope**: [This project only / Similar projects / All future projects]
```

### Process Pattern Format
```markdown
## Process Pattern: [Date]  
- **Context**: [What coordination challenge was solved]
- **Pattern**: [How agents worked together successfully]
- **Agents Involved**: [Which agents participated and how]
- **Effectiveness**: [Why this coordination approach worked]
```

### Review Triggers
- After major project completions
- When patterns consistently fail or succeed
- When new agent types are added
- When quality issues are discovered

## Project-Specific Overrides

### Authentication Systems
- **Required agents**: Senior architect + Security consultant + Backend builder + Security implementer
- **Special requirements**: Security testing, compliance validation, audit trail

### Payment Processing  
- **Required agents**: Senior architect + Security consultant + Backend builder + Security implementer
- **Special requirements**: PCI DSS compliance, financial regulations, comprehensive audit trail

### Public APIs
- **Required agents**: Senior architect + Backend builder + Security consultant
- **Special requirements**: Rate limiting, comprehensive documentation, versioning strategy

### Performance-Critical Features
- **Required agents**: Senior architect + Performance expert + relevant builders
- **Special requirements**: Load testing, monitoring implementation, performance benchmarking

---

*This document is automatically updated based on project learnings and coordination experiences. Last updated: [Date will be auto-updated by Claude during sessions]*