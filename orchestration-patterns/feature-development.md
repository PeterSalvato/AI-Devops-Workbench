# Feature Development Orchestration Pattern

## Pattern Type
**Consultation → Production Pipeline** - Strategic consultation followed by coordinated implementation

## Use Cases
- Building new features or components
- Adding major functionality to existing systems
- Implementing complex business requirements
- Cross-cutting concerns (auth, payments, integrations)

## Agent Coordination Flow

### Phase 1: Strategic Consultation
**Objective**: Understand requirements and create implementation strategy

1. **Senior Architect** (if system design needed)
   - Analyze requirements and constraints
   - Design system architecture and component structure
   - Define technology stack and implementation approach
   - Identify integration points and dependencies

2. **Domain Consultants** (as needed)
   - **Security Consultant**: For auth, payments, sensitive data
   - **UX Strategist**: For user-facing features
   - **Performance Expert**: For high-traffic or performance-critical features

### Phase 2: Production Implementation
**Objective**: Build feature according to consultation strategy

3. **Production Agents** (coordinated execution)
   - **Backend Builder**: API endpoints, business logic, data models
   - **Frontend Builder**: UI components, state management, user interactions
   - **Security Implementer**: Security controls, auth implementation
   - **CSS Specialist**: Styling, responsive design, visual polish

### Phase 3: Integration & Validation
**Objective**: Ensure quality and production readiness

4. **Code Reviewer**
   - Validate implementation against consultation recommendations
   - Check code quality, testing, and documentation
   - Ensure security and performance requirements are met

## Coordination Rules

### Consultation Phase Rules
- **Sequential execution** - architects and consultants work together
- **Consensus required** - major decisions need agreement between consultants
- **Document all decisions** - rationale and trade-offs must be clear
- **Security non-negotiable** - security consultant has veto power

### Production Phase Rules
- **Parallel execution possible** - production agents can work simultaneously
- **Clear interfaces** - API contracts must be agreed upon before frontend work
- **Continuous integration** - agents coordinate on shared interfaces
- **Quality gates** - each agent's output must meet quality standards

### Handoff Protocols
- **Consultation → Production**: Complete specifications with implementation details
- **Between Production Agents**: Clear interfaces and integration points
- **Production → Validation**: Complete implementation with tests and documentation

## Context Requirements

### Required Context
- **Feature Description**: Clear requirements and acceptance criteria
- **Technical Environment**: Current stack, deployment model, infrastructure
- **Quality Requirements**: Performance, security, compliance needs
- **Timeline and Resources**: Available time, team capacity, dependencies

### Optional Context
- **User Research**: For user-facing features
- **Business Context**: Revenue impact, strategic importance
- **Technical Constraints**: Legacy systems, compliance requirements
- **Team Preferences**: Technology choices, architectural patterns

## Quality Gates

### After Consultation Phase
- [ ] Requirements are clearly understood and documented
- [ ] Architecture decisions have clear rationale
- [ ] Security requirements are identified and specified
- [ ] Implementation strategy is feasible given constraints
- [ ] All consultants agree on major decisions

### After Production Phase
- [ ] Implementation matches consultation specifications
- [ ] All security requirements are properly implemented
- [ ] Code quality meets standards (tests, documentation, patterns)
- [ ] Integration points work correctly
- [ ] Performance requirements are met

### Final Validation
- [ ] Feature works end-to-end as specified
- [ ] Security testing passes all requirements
- [ ] Code review approves for production
- [ ] Documentation is complete and accurate
- [ ] Monitoring and observability are in place

## Common Variations

### Simple Feature (Backend Only)
- Senior Architect (if needed) → Backend Builder → Code Reviewer

### User-Facing Feature
- Senior Architect + UX Strategist → Backend Builder + Frontend Builder + CSS Specialist → Code Reviewer

### Security-Critical Feature
- Senior Architect + Security Consultant → Backend Builder + Security Implementer → Security testing → Code Reviewer

### Performance-Critical Feature
- Senior Architect + Performance Expert → Backend Builder (with optimization focus) → Performance testing → Code Reviewer

## Success Criteria
- Feature meets all requirements and acceptance criteria
- Implementation follows consultation recommendations
- Code quality and security standards are met
- Documentation and tests are complete
- Feature is production-ready with proper monitoring