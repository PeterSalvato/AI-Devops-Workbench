# Project Conventions

This file defines the development standards, patterns, and guidelines for consistent agent orchestration and production workflows.

## Architecture Overview

The system follows a three-tier architecture:

```
Intelligence Layer (Meta-Orchestrator)
    ↓
Consultation Layer (Specialist Agents)  
    ↓
Production Layer (Output Agents)
```

## Agent Development Standards

### Naming Conventions
- Agent files: `snake_case_agent.json`
- Agent names: `kebab-case-specialist`
- Capability categories: `primary`, `secondary`, `specialized`

### Agent Configuration Structure
```json
{
  "agent_identity": {
    "name": "string",
    "type": "consultant | producer | validator",
    "expertise": "string",
    "version": "semantic version",
    "persona": {
      "personality": "string",
      "communication_style": "string", 
      "approach": "string",
      "values": ["array"]
    }
  }
}
```

### Quality Standards
- All agents must include comprehensive input/output schemas
- Methodology must be multi-phase with validation criteria
- Quality assessment required in all outputs
- Confidence scoring (0-100) for all deliverables

## Orchestration Patterns

### Sequential Pattern
Used for step-by-step workflows where each phase builds on the previous.
```
Agent A → Agent B → Agent C → Final Output
```

### MapReduce Pattern  
Used for parallel processing with result aggregation.
```
Agent A ↘
Agent B → Aggregator → Final Output
Agent C ↗
```

### Consensus Pattern
Used when multiple expert opinions need agreement.
```
Agent A ↘
Agent B → Conflict Resolution → Final Output
Agent C ↗
```

### Hierarchical Pattern
Used for complex task decomposition.
```
Meta Agent
    ↓
Sub-Agent A → Sub-Agent B
    ↓           ↓
Output A    Output B → Combined Output
```

## Quality Validation Framework

### Minimum Quality Thresholds
- Methodology adherence: 85%
- Output completeness: 90% 
- Confidence score: 80%
- Consistency validation: 95%

### Validation Checkpoints
1. **Input Validation**: Context completeness and requirement clarity
2. **Process Validation**: Methodology adherence and quality gates
3. **Output Validation**: Deliverable completeness and actionability
4. **Integration Validation**: Compatibility with downstream processes

## File Organization Standards

```
/agents/
  /consultants/     # Advisory and analysis agents
  /producers/       # Content and deliverable creation agents
  /validators/      # Quality assurance and review agents
  /examples/        # Demo agents for framework illustration

/orchestration/
  /patterns/        # Orchestration pattern definitions
  /meta/           # Meta-orchestrator configurations
  /validation/     # Quality validation rules

/docs/
  /conventions.md   # This file - project standards
  /symbol-index.md  # System component mapping
  /examples/       # Usage examples and tutorials
```

## Development Workflow

### Agent Creation Process
1. **Research Phase**: Study domain expertise and methodologies
2. **Persona Development**: Define consistent personality and approach
3. **Capability Mapping**: Identify primary, secondary, specialized skills
4. **Schema Design**: Create comprehensive input/output structures
5. **Methodology Framework**: Develop multi-phase systematic process
6. **Quality Validation**: Define success criteria and measurement
7. **Testing**: Validate with realistic scenarios
8. **Documentation**: Complete usage examples and integration notes

### Quality Gates
- **Persona Consistency**: Agent behavior matches defined characteristics
- **Methodology Completeness**: All phases include validation steps
- **Schema Validation**: Input/output structures enable proper orchestration
- **Production Readiness**: Agent performs reliably under various conditions

## Integration Standards

### Context Passing
- Consistent data structures between agents
- Comprehensive context preservation
- Quality metadata propagation
- Error state handling

### Conflict Resolution
- Systematic disagreement detection
- Evidence-based resolution protocols
- Confidence-weighted decision making
- Audit trail maintenance

## Performance Standards

### Response Time Targets
- Simple consultations: < 30 seconds
- Complex orchestrations: < 5 minutes
- Quality validation: < 10 seconds
- Conflict resolution: < 2 minutes

### Quality Metrics
- First-pass success rate: > 85%
- Consistency score: > 90%
- User satisfaction: > 4.5/5
- Time to production: < 15 minutes

## Security and Privacy

### Data Handling
- No persistent storage of sensitive context
- Context sanitization between sessions
- Audit logging for quality improvement
- Privacy-preserving agent interactions

### Access Control
- Role-based agent access
- Capability-based permissions
- Quality threshold enforcement
- Production environment protection

## Customization Guidelines

### Project-Specific Adaptations
- Modify quality thresholds based on domain requirements
- Adapt orchestration patterns to team workflows
- Customize agent personas for organizational culture
- Integrate with existing development tools and processes

### Industry-Specific Considerations
- Regulatory compliance requirements
- Domain-specific quality standards
- Professional practice guidelines
- Risk management protocols

---

*This conventions file should be customized for your specific project requirements, team workflow, and quality standards. The framework provides structure while enabling adaptation to diverse use cases.*