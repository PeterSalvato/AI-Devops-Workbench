# AI DevOps Framework Refactor Plan
*Documentation-Driven Agent Orchestration*

## Vision
Transform complex Python framework into lean documentation-driven system where Claude Code becomes the meta-orchestrator by reading agent documentation.

## Current Problems
- Over-engineered Python abstractions
- Mock outputs instead of real AI
- Complex orchestration patterns that may not matter
- Agent loading from JSON configs
- Arbitrary quality metrics

## New Approach: Documentation-Native Orchestration

### Core Concept
1. **Git clone template repo** with structured docs
2. **Claude Code init** - reads docs, understands structure  
3. **User requests** - "Claude, build auth with backend + security perspectives"
4. **Claude becomes meta-agent** - coordinates consultation → production flow
5. **Self-documenting evolution** - learns and updates conventions over time

### Repository Structure
```
ai-devops-framework/
├── README.md                           # Claude's meta-orchestrator instructions
├── consultation-agents/                # Strategic advisors (think, don't code)
│   ├── senior-architect.md
│   ├── security-consultant.md
│   ├── ux-strategist.md
│   ├── performance-expert.md
│   └── code-reviewer.md
├── production-agents/                  # Implementation specialists (build code)
│   ├── backend-builder.md
│   ├── frontend-builder.md
│   ├── security-implementer.md
│   ├── ui-component-builder.md
│   └── css-specialist.md
├── orchestration-patterns/             # How to coordinate agents
│   ├── feature-development.md          # consultation → production pipeline
│   ├── code-review.md                  # consensus validation
│   ├── security-audit.md               # hierarchical security analysis
│   └── architecture-design.md          # system design coordination
├── conventions.md                      # Living orchestration rules (auto-updated)
├── symbol-index.md                     # Component relationships (auto-updated)
└── project-memory/                     # Session learnings and decisions
    ├── decisions-log.md
    ├── patterns-learned.md
    └── conflict-resolutions.md
```

## Implementation Plan

### Phase 1: Foundation
- [ ] Create lean repo structure
- [ ] Write README.md (Claude's meta-orchestrator guide)
- [ ] Design agent documentation templates
- [ ] Create initial consultation agents
- [ ] Create initial production agents
- [ ] Write basic orchestration patterns

### Phase 2: Self-Updating System  
- [ ] Design conventions.md auto-update system
- [ ] Design symbol-index.md relationship tracking
- [ ] Create project-memory documentation system
- [ ] Test documentation-driven coordination

### Phase 3: Validation & Refinement
- [ ] Test real development workflows
- [ ] Refine agent personas and methodologies
- [ ] Optimize orchestration patterns
- [ ] Document extension patterns

## Key Innovation Points

### 1. Claude as Meta-Orchestrator
- No Python framework needed
- Reads documentation to understand roles
- Naturally coordinates multiple perspectives
- Handles conflict resolution through reasoning

### 2. Consultation → Production Pipeline
- **Consultation agents**: Strategic thinking, no code output
- **Production agents**: Implementation, actual deliverables
- Clear handoff protocols between layers

### 3. Living Documentation
- Conventions evolve based on decisions made
- Symbol index tracks component relationships
- Project memory captures institutional knowledge
- Each session makes the system smarter

### 4. Developer Experience
```bash
# Simple developer workflow
git clone ai-devops-template my-project
cd my-project
claude init  # Reads docs, becomes meta-orchestrator

# Natural interaction
"Claude, build user authentication using backend expert and security consultant"
"Claude, review this PR with security and performance perspectives"
"Claude, architect a payment system with all relevant experts"
```

## Success Metrics
- [ ] Zero Python framework code needed
- [ ] Claude successfully coordinates agent personas
- [ ] Documentation auto-updates with learnings
- [ ] Real development tasks complete successfully
- [ ] System improves over multiple sessions

## Migration Strategy
1. Keep current framework as reference
2. Build new documentation system alongside
3. Test with real development tasks
4. Validate agent coordination works
5. Replace framework with docs-only approach

---

## Session Progress Tracking

### Current Session Goals
- [x] Review and validate refactor approach
- [x] Create this planning document
- [x] Design initial repo structure
- [x] Create agent documentation templates (senior-architect, security-consultant, backend-builder)
- [x] Create orchestration pattern (feature-development)
- [ ] Write README.md for Claude meta-orchestrator
- [ ] Create self-updating conventions system

### Next Session Goals  
- [ ] Complete remaining consultation agents (ux-strategist, performance-expert, code-reviewer)
- [ ] Complete remaining production agents (frontend-builder, security-implementer, css-specialist)
- [ ] Create remaining orchestration patterns (code-review, security-audit, architecture-design)
- [ ] Write conventions.md and symbol-index.md auto-update system
- [ ] Test Claude coordination with real development task

### Roadmap Items
- [ ] Concurrent agent execution capability
- [ ] Advanced conflict resolution patterns
- [ ] Integration with external AI providers
- [ ] Performance optimization for large projects

---

*This document should be updated after each work session to maintain progress continuity.*