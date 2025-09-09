# Team Decision Documentation Format

*Standardized format for documenting all team conventions and architectural decisions*

## Documentation Structure

### File Organization
```
project-memory/
├── conventions.md                    # Active team conventions (what Claude reads)
├── decisions/                        # Decision archive (how conventions were made)
│   ├── 2024-01-tech-stack-backend.md
│   ├── 2024-02-git-workflow-change.md  
│   └── 2024-03-security-auth-standard.md
└── templates/                        # Decision-making templates
    ├── convention-decision-templates.md
    └── team-decision-voting-system.md
```

## Standard Decision Documentation Format

### Complete Decision Record Template
```markdown
# Decision: [Brief Descriptive Title]

## Decision Summary
**Date**: [YYYY-MM-DD]  
**Decision ID**: [YYYY-MM-category-brief-name] (for cross-referencing)
**Decision Maker**: [Name and role]
**Status**: [Proposed | Approved | Implemented | Superseded]

## Context & Problem
**Problem Statement**: [What issue required a decision]
**Business Impact**: [Why this matters for project/team success]  
**Technical Context**: [Relevant technical constraints or requirements]
**Timeline Pressure**: [Any deadline or urgency factors]

## Options Considered

### Option 1: [Name]
**Description**: [What this approach involves]
**Pros**: 
- [Advantage 1]
- [Advantage 2]
**Cons**:
- [Disadvantage 1] 
- [Disadvantage 2]
**Implementation Effort**: [High/Medium/Low + time estimate]
**Risk Level**: [High/Medium/Low + key risks]

### Option 2: [Name]  
[Same format as Option 1]

### Option 3: [Name]
[Same format as Option 1]

## Team Input Process
**Discussion Method**: [GitHub Discussion | Slack thread | Team meeting]
**Participants**: [Who provided input]
**Key Concerns Raised**:
- [Concern 1]: [How addressed]
- [Concern 2]: [Resolution approach]
**Consensus Level**: [Full agreement | Majority support | Split decision]

## Decision Details
**Chosen Option**: [Selected approach]
**Primary Rationale**: [Top 2-3 reasons for this choice]
**Trade-offs Accepted**: [What we're giving up for this choice]
**Assumptions Made**: [Key assumptions this decision relies on]

## Implementation Plan
**Timeline**: 
- [Phase 1]: [What by when]
- [Phase 2]: [What by when] 
- [Fully Implemented]: [Target date]

**Responsible Parties**:
- **Technical Implementation**: [Who codes it]
- **Documentation Updates**: [Who updates docs]
- **Team Communication**: [Who tells everyone]
- **Training/Onboarding**: [Who ensures team adoption]

**Success Criteria**:
- [Measurable outcome 1]
- [Measurable outcome 2]
- [How we'll know this worked]

## Migration & Rollback
**Existing Code Impact**: [How this affects current projects]
**Migration Strategy**: [How to transition existing work]
**Rollback Plan**: [How to reverse if this doesn't work]
**Rollback Triggers**: [What conditions would trigger rollback]

## Monitoring & Review
**Review Date**: [When to assess effectiveness] 
**Success Metrics**: [How to measure if working]
**Review Process**: [Who reviews and how]
**Update Triggers**: [What would cause us to change this decision]

## Related Decisions
**Supersedes**: [Any previous decisions this replaces]
**Related To**: [Other decisions that connect to this one]
**Dependencies**: [Decisions that must be made before/after this]
**Conflicts With**: [Any conventions this changes or contradicts]

## Convention Updates Required
**Files to Update**:
- [ ] project-memory/conventions.md - [What sections to modify]
- [ ] README.md - [Documentation changes needed]
- [ ] [Other files] - [What changes needed]

**Convention Text**:
```markdown
[Exact text to add to conventions.md]
```

---
**Decision Archive**: Stored in project-memory/decisions/[decision-id].md
**Convention Reference**: [Link to where this appears in active conventions]
```

## Quick Decision Format (For Minor Decisions)

### Lightweight Template for Style/Tool Decisions
```markdown
# Quick Decision: [Title]

**Date**: [YYYY-MM-DD] | **Decider**: [Name] | **Type**: [Style|Tool|Process]

## Problem
[One sentence: what needed deciding]

## Decision  
[One sentence: what was chosen]

## Rationale
[2-3 sentences: why this choice]

## Implementation
- **Effective**: [When this starts]
- **Applies To**: [New code only | All code | Specific projects]
- **Tools Updated**: [Linters, configs, etc.]

## Team Impact
**Affected Developers**: [Who needs to know]
**Training Needed**: [None | Link to docs | Meeting required]
**Review Date**: [When to check if working]

---
**Convention Update**: Added to conventions.md line [X] on [date]
```

## Decision Amendment Format

### When Updating Existing Decisions
```markdown
# Decision Amendment: [Original Decision Title]

**Amendment Date**: [YYYY-MM-DD]
**Original Decision**: [Link to original decision record]
**Amendment Author**: [Name and role]

## What Changed
**Original Decision**: [Brief summary of original choice]
**New Decision**: [What's changing]
**Scope of Change**: [Minor adjustment | Major revision | Complete reversal]

## Why Amendment Needed
**Trigger**: [What caused need for change]
**Evidence**: [Data/experience that informed change]  
**Problem With Original**: [What wasn't working]

## Impact Assessment
**Code Changes Required**: [How much work to implement]
**Team Disruption**: [How much this affects current work]
**Risk Level**: [Low | Medium | High - risk of making change]

## Updated Implementation
[Use same format as original decision for new implementation plan]

## Notification Plan
- [ ] Team announcement: [Date and method]
- [ ] Documentation updates: [Who and when]  
- [ ] Tool/config changes: [What needs updating]
- [ ] Training if needed: [Schedule and format]

---
**Files Updated**: 
- [x] Original decision record (marked as superseded)
- [ ] project-memory/conventions.md  
- [ ] [Other affected files]
```

## Documentation Quality Checklist

### Before Publishing Decision
- [ ] **Clear problem statement** - Anyone can understand what needed deciding
- [ ] **Complete option analysis** - Major alternatives considered with pros/cons
- [ ] **Team input documented** - Shows how consensus was built or why not needed
- [ ] **Implementation details** - Clear next steps and responsibilities  
- [ ] **Review schedule** - When and how effectiveness will be assessed
- [ ] **Cross-references** - Links to related decisions and affected conventions

### After Implementation
- [ ] **Status updated** - Decision record marked as "Implemented"  
- [ ] **Conventions updated** - Active conventions reflect new decision
- [ ] **Team notified** - All affected developers know about change
- [ ] **Tools configured** - Linters, build tools, etc. updated if needed
- [ ] **Success metrics baseline** - Initial measurements taken for future review

## Integration with Framework

### How This Connects to conventions.md
```markdown
**Decision Record** (project-memory/decisions/2024-01-backend-tech.md):
- Full context, options considered, rationale
- Team discussion summary  
- Implementation timeline
- Review schedule

**Active Convention** (project-memory/conventions.md):
- Current standard that Claude follows
- Implementation examples
- When to apply
- References decision record for context

**Relationship**: Decision records explain WHY conventions exist, 
conventions tell Claude WHAT to do now.
```

### How This Supports Hierarchical Context
```markdown
**Team Decision Process** → **Team Convention** → **Overrides Individual Preferences**

1. Team uses decision workflow to choose standard
2. Decision documented using this format
3. Convention added to project-memory/conventions.md  
4. Claude applies team convention even if individual prefers different approach
5. Decision reviewed periodically for effectiveness
```

## Common Documentation Anti-Patterns

### Poor Decision Records
❌ **"We decided to use React"** - No context, options, or rationale  
✅ **Complete record** with problem, options, team input, and reasoning

❌ **Decisions never reviewed** - Standards become stale and ineffective
✅ **Scheduled reviews** with metrics and update triggers

❌ **Missing implementation details** - Team doesn't know how to apply decision
✅ **Clear implementation** with examples, timelines, and responsibilities

❌ **No connection to active conventions** - Decision records divorced from daily practice  
✅ **Linked documentation** where decision records explain active conventions

### Convention Documentation Issues  
❌ **Vague standards** - "Write good code" provides no actionable guidance
✅ **Specific examples** with code samples and clear requirements

❌ **Outdated conventions** - Standards that no longer reflect team reality
✅ **Living documentation** updated when decisions change

❌ **Missing context** - Rules without understanding why they exist
✅ **Decision references** so team knows rationale behind standards

---

*This format ensures all team decisions are documented consistently with sufficient detail for future reference and systematic review.*