# Context Approval Workflow Pattern

*Systematic process for elevating individual preferences to team conventions through consensus validation*

**Pattern Type**: Governance & Decision Management  
**Use Case**: Converting successful individual patterns into team standards  
**Prerequisites**: Active hierarchical context system with team and individual preferences  

## Pattern Overview

This workflow manages the elevation of individual developer preferences to team-wide conventions through systematic validation and consensus building.

## Stakeholder Roles

### Meta-Orchestrator Responsibilities
- **Identify elevation candidates** from successful individual patterns
- **Facilitate consensus building** among team members
- **Document approval decisions** in appropriate convention files
- **Maintain approval audit trail** for governance compliance

### Human Team Lead Responsibilities  
- **Review individual pattern proposals** for team-wide applicability
- **Coordinate team consensus discussion** on proposed standards
- **Make final approval decisions** on convention elevation
- **Ensure team convention quality** and consistency

### Individual Developer Responsibilities
- **Propose successful patterns** for team adoption
- **Provide implementation evidence** of pattern effectiveness
- **Participate in consensus discussions** constructively
- **Adapt to approved team conventions** once established

## Workflow Process

### Phase 1: Identification & Proposal
```markdown
**TRIGGER**: Individual pattern shows repeated success across projects

**ORCHESTRATOR ACTIONS**:
1. **Identify Pattern**: Successful individual preference used across multiple projects
2. **Gather Evidence**: Document pattern effectiveness and project outcomes
3. **Create Proposal**: Format proposal for team review
4. **Route to Team Lead**: Present pattern with supporting evidence

**DELIVERABLE**: Structured pattern proposal with effectiveness metrics
```

### Phase 2: Team Review & Discussion  
```markdown
**TRIGGER**: Pattern proposal submitted to team lead

**TEAM LEAD ACTIONS**:
1. **Review Proposal**: Evaluate pattern for team-wide applicability
2. **Identify Stakeholders**: Determine which team members should review
3. **Facilitate Discussion**: Coordinate team input on proposed standard
4. **Document Feedback**: Capture team consensus or objections

**DELIVERABLE**: Team consensus assessment with approval recommendation
```

### Phase 3: Decision & Documentation
```markdown
**TRIGGER**: Team consensus reached (approval or rejection)

**ORCHESTRATOR ACTIONS**:
1. **Document Decision**: Record approval/rejection with rationale
2. **Update Conventions**: Add approved patterns to team conventions
3. **Notify Team**: Communicate new standards to all developers
4. **Archive Proposal**: Maintain governance audit trail

**DELIVERABLE**: Updated team conventions with new standards
```

## Approval Criteria

### Pattern Suitability Assessment
- **Broad Applicability**: Pattern applies to multiple project types
- **Team Benefit**: Measurable improvement in quality or efficiency
- **Low Conflict Risk**: Pattern doesn't conflict with existing team conventions
- **Implementation Feasibility**: Team has capability to adopt pattern

### Evidence Requirements
- **Success Metrics**: Quantifiable improvement from pattern usage
- **Project Examples**: Concrete projects where pattern proved effective
- **Risk Assessment**: Potential downsides or implementation challenges
- **Team Impact**: How pattern affects current team workflows

## Decision Documentation Format

### Approved Patterns
```markdown
## Team Convention Approved: [Date]
**Original Individual Preference**: [Developer name] - [Pattern description]
**Elevation Rationale**: [Why this became a team standard]
**Evidence**: [Success metrics and project examples]
**Team Consensus**: [Approval vote/discussion summary]
**Implementation Timeline**: [When team must adopt]
**Review Date**: [When to reassess effectiveness]

### [Convention Category]
**Team Standard**: [Approved pattern description]
**Rationale**: [Business/technical justification]
**Apply To**: [Project scope and applicability]
**Implementation**: [How team implements this standard]
```

### Rejected Patterns
```markdown
## Pattern Elevation Rejected: [Date]
**Proposed Pattern**: [Pattern description]
**Rejection Rationale**: [Why not approved for team adoption]
**Alternative Approach**: [Recommended team solution if applicable]
**Individual Usage**: [Whether individuals can continue using]
**Review Timeline**: [When pattern might be reconsidered]
```

## Integration with Context System

### Convention File Updates
- **Approved patterns** immediately added to `project-memory/conventions.md`
- **Individual preferences** updated to reference new team standards
- **Symbol index** updated with new standardized implementations

### Conflict Resolution Updates
- **New team conventions** take precedence over existing individual preferences
- **Affected developers** notified of preference overrides
- **Transition support** provided for pattern adoption

## Success Metrics

### Process Effectiveness
- **Proposal Quality**: Structured evidence and clear pattern definition
- **Team Engagement**: Active participation in consensus discussions
- **Decision Clarity**: Clear approval/rejection with documented rationale
- **Implementation Success**: Adopted patterns actually used by team

### Pattern Impact
- **Code Consistency**: Improved standardization across projects
- **Quality Improvements**: Measurable benefits from adopted patterns
- **Team Efficiency**: Reduced decision fatigue and pattern conflicts
- **Knowledge Sharing**: Better pattern propagation across team

## Anti-Patterns to Avoid

### Poor Approval Process
- **Rushed Decisions**: Insufficient review time or stakeholder input
- **Weak Evidence**: Patterns approved without measurable benefits
- **Silent Approvals**: Lack of team discussion or consensus building
- **Legacy Conflicts**: New standards that break existing conventions

### Implementation Failures
- **Inconsistent Adoption**: Team members ignoring approved conventions
- **Poor Communication**: Team not notified of new standards
- **Missing Documentation**: Approved patterns not properly documented
- **No Review Cycle**: Standards never reassessed for continued effectiveness

---

*This workflow ensures individual innovations benefit the entire team while maintaining systematic decision-making and proper governance for convention evolution.*