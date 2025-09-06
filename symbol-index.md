# Component Relationship Index

*This document maps relationships between agents, patterns, and system components for intelligent coordination.*

## Agent Relationship Map

### Consultation Agents (Strategic Layer)

#### Senior Architect
- **Provides input to**: All production agents (design specifications)
- **Requires input from**: None (can work independently)  
- **Coordinates with**: Security consultant (for security requirements), UX strategist (for user requirements)
- **Authority level**: High for technical architecture decisions
- **Trigger patterns**: System design, technology selection, complex features

#### Security Consultant  
- **Provides input to**: Security implementer (detailed requirements), Backend builder (secure coding), All agents (security constraints)
- **Requires input from**: Senior architect (system context)
- **Coordinates with**: All agents (security is cross-cutting)
- **Authority level**: Absolute for security requirements (veto power)
- **Trigger patterns**: Authentication, payments, sensitive data, compliance

#### UX Strategist
- **Provides input to**: Frontend builder (user requirements), UI component builder (interaction patterns)
- **Requires input from**: None (can work independently)
- **Coordinates with**: Senior architect (for technical constraints)
- **Authority level**: High for user experience decisions
- **Trigger patterns**: User-facing features, interfaces, workflows

#### Performance Expert
- **Provides input to**: Backend builder (optimization requirements), Frontend builder (performance constraints)
- **Requires input from**: Senior architect (system design)
- **Coordinates with**: All builders (performance is cross-cutting)
- **Authority level**: High for performance-critical decisions
- **Trigger patterns**: High-traffic features, optimization needs, scalability

#### Code Reviewer
- **Provides input to**: All agents (quality feedback)
- **Requires input from**: All other agents (for context)
- **Coordinates with**: All agents (review is final validation)
- **Authority level**: Gate-keeper for production deployment
- **Trigger patterns**: All production code, quality validation

### Production Agents (Implementation Layer)

#### Backend Builder
- **Receives input from**: Senior architect (design), Security consultant (requirements), Performance expert (constraints)
- **Provides output to**: Frontend builder (API contracts), Security implementer (integration points)
- **Coordinates with**: Frontend builder (API design), Security implementer (auth integration)
- **Dependencies**: Architecture decisions, security requirements
- **Specialization**: APIs, databases, business logic, server-side implementation

#### Frontend Builder  
- **Receives input from**: Senior architect (architecture), UX strategist (requirements), Backend builder (API contracts)
- **Provides output to**: UI component builder (component specs), CSS specialist (integration needs)
- **Coordinates with**: Backend builder (API contracts), UI component builder (component integration)
- **Dependencies**: UX strategy, API availability, component library
- **Specialization**: React/Vue/Angular, state management, user interactions

#### Security Implementer
- **Receives input from**: Security consultant (detailed requirements), Backend builder (system context)
- **Provides output to**: All agents (security integration points)
- **Coordinates with**: Backend builder (authentication systems), Frontend builder (security UI)
- **Dependencies**: Security analysis complete, system architecture defined
- **Specialization**: Authentication, authorization, encryption, security middleware

#### UI Component Builder
- **Receives input from**: UX strategist (design patterns), Frontend builder (integration needs)
- **Provides output to**: CSS specialist (styling requirements), Frontend builder (components)
- **Coordinates with**: CSS specialist (visual design), Frontend builder (integration)
- **Dependencies**: Design system, UX patterns defined
- **Specialization**: Reusable components, design system, accessibility

#### CSS Specialist
- **Receives input from**: UI component builder (components), UX strategist (design requirements)
- **Provides output to**: Frontend builder (styled components)
- **Coordinates with**: UI component builder (component styling), Frontend builder (integration)
- **Dependencies**: Component library, design specifications
- **Specialization**: Styling, responsive design, visual polish, CSS architecture

## Orchestration Pattern Triggers

### Pattern: consultation_then_production
**Triggered by**: "Build [feature]", "Implement [system]", "Create [component]"
**Agent flow**: 
1. Senior architect (if system design needed)
2. Domain consultants (security, UX, performance as needed)
3. Production agents (backend, frontend, security implementer as needed)
4. Code reviewer (validation)

### Pattern: consensus_validation  
**Triggered by**: "Review [code]", "Validate [implementation]", "Approve [PR]"
**Agent flow**:
1. Relevant consultants (parallel review)
2. Consensus building
3. Code reviewer (final approval)

### Pattern: hierarchical_security
**Triggered by**: "Security audit", "Penetration test", "Compliance check"
**Agent flow**:
1. Security consultant (threat analysis)
2. Security implementer (implementation review)
3. Penetration testing
4. Code reviewer (security approval)

### Pattern: collaborative_design
**Triggered by**: "Design system", "Architecture decision", "Technology selection"  
**Agent flow**:
1. Senior architect (design options)
2. Relevant consultants (domain input)
3. Consensus and ratification
4. Documentation update

## Quality Threshold Matrix

| Component Type | Min Quality | Required Agents | Special Rules |
|---------------|-------------|-----------------|---------------|
| Authentication | 95% | Architect + Security + Backend + Security Impl | Penetration testing required |
| Payment Processing | 95% + PCI | Architect + Security + Backend + Security Impl | Compliance validation required |
| Public APIs | 90% | Architect + Backend + Security | Rate limiting + documentation required |
| User Interfaces | 90% | Architect + UX + Frontend + UI Builder | Accessibility validation required |
| Performance Critical | 90% + benchmarks | Architect + Performance + Relevant builders | Load testing required |
| Security Critical | 95% | Security + Relevant implementers | Security testing required |

## Conflict Resolution Matrix

| Conflict Type | Resolution Authority | Escalation Path | Decision Factors |
|---------------|---------------------|-----------------|------------------|
| Architecture vs Security | Security consultant | User decision | Security requirements non-negotiable |
| UX vs Performance | Senior architect | User preference | Balance user needs vs technical constraints |
| Implementation approach | Senior architect | Consensus building | Technical merit and maintainability |
| Resource allocation | User decision | Project priorities | Business requirements and timeline |
| Quality standards | Code reviewer | Quality framework | Established quality gates |

## Dependency Relationships

### Critical Path Dependencies
1. **Architecture → Implementation**: All production agents depend on architectural decisions
2. **Security Analysis → Security Implementation**: Security implementer depends on security consultant
3. **UX Strategy → Frontend**: Frontend builder depends on UX strategist for user-facing features
4. **API Design → Frontend**: Frontend builder depends on backend builder for API contracts

### Optional Dependencies  
1. **Performance Analysis → Optimization**: Performance expert input enhances but doesn't block implementation
2. **Code Review → All**: Code reviewer can work with any completed implementation
3. **Component Library → Styling**: UI components can be styled after creation

## Communication Protocols

### Formal Handoffs (Required)
- **Consultation → Production**: Complete specifications with acceptance criteria
- **Architecture → Implementation**: Technical specifications with implementation details
- **Security Requirements → Implementation**: Detailed security specifications with validation criteria
- **API Contracts**: Agreed interface specifications before frontend development

### Informal Coordination (Recommended)
- **Cross-cutting concerns**: Security, performance, quality considerations shared across agents
- **Integration planning**: Early coordination on integration points and dependencies
- **Quality feedback**: Continuous feedback loops between agents during development

---

*This document is automatically updated based on agent coordination patterns and relationship learnings. Last updated: [Date will be auto-updated by Claude during sessions]*