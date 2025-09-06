# Feature Development Orchestration Pattern

## Pattern Type
**Hierarchical Management** - Human decision maker → Claude as dept head manager → Consultation agents as team leads → Production agents as specialists

## Use Cases
- Building new features or components
- Adding major functionality to existing systems
- Implementing complex business requirements
- Cross-cutting concerns (auth, payments, integrations)

## Management Hierarchy

### Level 1: Human Decision Maker
**Role**: Strategic direction, business requirements, final approval
- Defines project requirements and priorities
- Makes business and preference decisions
- Approves major architectural choices
- Sets quality thresholds and timeline constraints

### Level 2: Claude Meta-Orchestrator  
**Role**: Department head managing consultation team leads
- Interprets human requirements into technical specifications
- Assigns consultation agents based on project complexity
- Coordinates between consultation team leads
- Manages conflicts and escalations
- Ensures quality gates are met

### Level 3: Consultation Agents (Team Leads)
**Role**: Technical department heads who dispatch and manage production specialists

#### Senior Architect (Systems Team Lead)
- **Analyzes** system requirements and constraints
- **Designs** architecture and component structure  
- **Dispatches** backend builders, database specialists
- **Coordinates** between all production agents
- **Validates** implementation against architectural decisions

#### Security Consultant (Security Team Lead)  
- **Analyzes** threat models and security requirements
- **Designs** security architecture and controls
- **Dispatches** security implementers, penetration testers
- **Coordinates** security integration across all components
- **Validates** security implementations and testing

#### UX Strategist (UX Team Lead)
- **Analyzes** user requirements and experience flows
- **Designs** user interface strategy and patterns
- **Dispatches** frontend builders, CSS specialists
- **Coordinates** user experience across all touchpoints
- **Validates** user interface implementation and usability

### Level 4: Production Agents (Specialists)
**Role**: Implementation specialists managed by consultation team leads

#### Under Senior Architect Management
- **Backend Builder**: APIs, business logic, data models
- **Database Specialist**: Schema design, optimization, migrations  
- **Integration Specialist**: External APIs, microservices communication

#### Under Security Consultant Management  
- **Security Implementer**: Auth systems, encryption, security controls
- **Penetration Tester**: Security validation, vulnerability assessment

#### Under UX Strategist Management
- **Frontend Builder**: UI components, state management, user interactions
- **CSS Specialist**: Styling, responsive design, visual polish
- **Accessibility Specialist**: WCAG compliance, inclusive design

### Project Output Structure
All work outputs to organized project folders:
```
.output/project-name/
├── requirements/           # Human requirements and decisions
├── architecture/          # Senior architect specifications and decisions  
├── security/             # Security consultant analysis and requirements
├── ux-strategy/          # UX strategist wireframes and user flows
├── code/                 # Production agent implementations
│   ├── backend/          # Backend builder outputs
│   ├── frontend/         # Frontend builder outputs  
│   ├── security/         # Security implementer outputs
│   └── styles/           # CSS specialist outputs
├── documentation/        # Generated docs from all agents
├── testing/             # Test plans and results
└── session-log.md       # Management coordination record
```

## Management Coordination Rules

### Human → Claude Meta-Orchestrator
- **Human provides**: Requirements, priorities, business context, quality expectations
- **Claude interprets**: Technical implications, agent requirements, coordination strategy
- **Human approves**: Major architectural decisions, resource allocation, timeline changes
- **Claude reports**: Progress, conflicts, quality status, completion

### Claude → Consultation Team Leads  
- **Claude assigns**: Consultation agents based on project complexity and requirements
- **Consultation leads analyze**: Requirements within their domain expertise
- **Consultation leads propose**: Technical approach, resource needs, implementation strategy  
- **Claude coordinates**: Between team leads, resolves conflicts, ensures consensus

### Consultation Team Leads → Production Specialists
- **Team leads dispatch**: Specific production agents based on technical analysis
- **Team leads provide**: Detailed specifications, quality requirements, integration points
- **Production agents implement**: According to team lead specifications and coordination
- **Team leads validate**: Implementation against specifications and quality standards

### Cross-Team Coordination
- **Senior architect coordinates** all technical integration points
- **Security consultant validates** all security implementations across teams  
- **UX strategist ensures** consistent user experience across all components
- **Claude manages** conflicts between team leads and escalates to human as needed

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