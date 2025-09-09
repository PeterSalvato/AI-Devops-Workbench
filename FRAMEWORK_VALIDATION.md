# Framework Self-Validation

*Automated validation that the AI DevOps Framework is working correctly and providing expected context management and systematic development capabilities.*

## Validation Tests

### Context Management Validation

#### Test 1: Conventions Application
**Test**: Claude should apply architectural decisions from project-memory/conventions.md consistently
**Validation Command**: 
```
"Claude, create a new API endpoint for user profile updates following our established standards"
```
**Expected Behavior**:
- Uses Node.js + Express + TypeScript (from backend standards)
- Implements standardized API response format
- Applies authentication requirements (JWT validation)
- Uses established error handling patterns
- Follows naming conventions (camelCase, etc.)

#### Test 2: Symbol Index Usage
**Test**: Claude should understand codebase structure from project-memory/symbol-index.md
**Validation Command**:
```
"Claude, modify the user authentication to add password complexity validation without breaking existing integrations"
```
**Expected Behavior**:
- References existing `authenticateUser()` function location
- Identifies dependent services (User Service, Admin Service)
- Understands integration points that could be affected
- Proposes changes that maintain existing API contracts

### Agent Coordination Validation

#### Test 3: Systematic Consultation
**Test**: Security-sensitive requests should trigger consultation before implementation
**Validation Command**:
```
"Claude, implement payment processing for our e-commerce system"
```
**Expected Behavior**:
- Identifies this as security-critical system requiring consultation
- Engages Senior Architect for system design
- Engages Security Consultant for threat analysis and compliance
- Presents options with trade-offs before implementation
- Documents decisions in project-memory/conventions.md

#### Test 4: Quality Validation
**Test**: Complex implementations should use consensus validation pattern
**Validation Command**:
```  
"Claude, review this authentication implementation for production readiness"
```
**Expected Behavior**:
- Applies multi-expert validation (Security + Architecture + Code Quality)
- Validates against established conventions
- Checks integration points against symbol-index
- Provides comprehensive production readiness assessment

### Framework Completeness Validation

#### Test 5: Project Organization
**Test**: New projects should follow established structure
**Validation Command**:
```
"Claude, start a new microservice for inventory management"
```
**Expected Behavior**:
- Updates PROJECT_ITINERARY.md with new project
- Creates structured project directory in .output/
- Applies consultation → production workflow
- Generates complete project deliverables with documentation

#### Test 6: Learning Integration
**Test**: Framework should capture and apply new patterns
**Validation Command**:
```
"Claude, we decided to use Redis for all caching. Update our standards and apply to current projects"
```
**Expected Behavior**:
- Updates project-memory/conventions.md with new caching standard
- Identifies existing projects that could benefit from this decision
- Updates symbol-index.md with new dependency patterns
- Proposes systematic application across codebase

## Validation Results Log

### Latest Validation: [Date]
**Tester**: [Name]
**Framework Version**: [Current commit hash]

#### Test Results:
- [ ] **Context Management**: Conventions properly applied
- [ ] **Symbol Index**: Codebase understanding demonstrated  
- [ ] **Systematic Consultation**: Security/architecture consultation triggered
- [ ] **Quality Validation**: Multi-expert validation performed
- [ ] **Project Organization**: Proper structure and documentation
- [ ] **Learning Integration**: New patterns captured and applied

#### Issues Identified:
- [List any failures or gaps discovered]

#### Improvements Made:
- [List any framework improvements implemented]

## Framework Confidence Score

**Overall Framework Readiness**: [Score]/6 tests passing

### Scoring:
- **6/6**: Production ready - Framework working as designed
- **5/6**: Minor issues - Safe for team adoption with monitoring
- **4/6**: Moderate issues - Framework needs refinement
- **<4/6**: Major issues - Framework not ready for team adoption

## Manual Validation Checklist

### Pre-Deployment Validation
- [ ] **Documentation Complete**: All agent files properly structured
- [ ] **Examples Working**: User authentication example project complete
- [ ] **Context Files Populated**: conventions.md and symbol-index.md have realistic content
- [ ] **Integration Points Clear**: Agent coordination patterns documented
- [ ] **Business Value Demonstrated**: ROI and efficiency gains quantified

### Post-Deployment Monitoring
- [ ] **Team Adoption**: Developers successfully using framework
- [ ] **Context Accuracy**: project-memory files staying current and accurate
- [ ] **Quality Consistency**: Implementations following established conventions
- [ ] **Learning Loop**: Framework getting smarter through use
- [ ] **Business Impact**: Measurable improvements in development efficiency

## Troubleshooting Common Issues

### Issue: Claude Not Applying Conventions
**Symptoms**: New code doesn't follow established standards
**Diagnosis**: Check if project-memory/conventions.md is properly formatted and accessible
**Resolution**: Verify Claude reads conventions at session start, update format if needed

### Issue: Symbol Index Out of Date  
**Symptoms**: Claude suggests changes that would break existing integrations
**Diagnosis**: symbol-index.md not reflecting current codebase structure
**Resolution**: Update symbol-index.md with current function exports and dependencies

### Issue: Agent Coordination Not Triggered
**Symptoms**: Complex/security-sensitive work proceeds without consultation  
**Diagnosis**: Agent triggering logic not recognizing complexity indicators
**Resolution**: Review orchestration patterns, update triggering criteria

### Issue: Learning Not Persisting
**Symptoms**: Same decisions requested repeatedly across sessions
**Diagnosis**: project-memory files not being updated during work sessions  
**Resolution**: Verify update triggers in CLAUDE.md, check file write permissions

---

*This validation framework ensures the AI DevOps Framework is functioning correctly and provides the expected systematic development and context management capabilities before team adoption.*