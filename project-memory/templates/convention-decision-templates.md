# Team Convention Decision Templates

*Ready-to-use templates for documenting team architectural and process decisions*

## Quick Start Templates

### Technology Stack Decision (Copy & Customize)
```markdown
## Backend Technology Decision: [e.g., "API Framework"]
**Decision Made**: [Current Date]
**Decision Maker**: [Your Name, Technical Lead]  
**Context**: [e.g., "New customer portal project needs backend API"]

**Options Considered**:
1. **Node.js + Express**: Familiar to team, large ecosystem, JavaScript consistency
2. **Python + FastAPI**: Strong typing, auto-documentation, high performance  
3. **Java + Spring**: Enterprise-grade, team has experience, robust ecosystem

**Team Input Summary**:
- [Team member 1]: Prefers Node.js for JavaScript consistency
- [Team member 2]: Concerned about Node.js performance for high-load
- [Team member 3]: Suggests Python for better type safety

**Final Decision**: Node.js + Express + TypeScript
**Rationale**: Team JavaScript expertise, faster development, TypeScript addresses type safety
**Implementation Timeline**: Start immediately for new projects
**Migration Plan**: Existing Python services remain, new services use Node.js
**Review Date**: 6 months - assess performance and team satisfaction

### Implementation Standard:
```typescript
// API Response format
interface APIResponse<T> {
  success: boolean;
  data?: T;
  error?: { code: string; message: string; };
  timestamp: string;
}

// Error handling pattern
app.use((err, req, res, next) => {
  logger.error('API Error', { error: err.message, path: req.path });
  res.status(500).json({
    success: false,
    error: { code: 'INTERNAL_ERROR', message: 'Server error' },
    timestamp: new Date().toISOString()
  });
});
```
```

### Code Style Decision (Copy & Customize)
```markdown
## Code Style Decision: [e.g., "Function Naming Conventions"]
**Decision Made**: [Current Date]  
**Decision Maker**: [Your Name, Technical Lead]
**Context**: [e.g., "Inconsistent function naming causing confusion in code reviews"]

**Current Problem**: Team using mixture of camelCase, snake_case, and unclear naming
**Proposed Standard**: Descriptive camelCase with verb-noun pattern

**Examples**:
```javascript
// ✅ Good - Clear verb-noun pattern
function calculateTotalPrice(items) { }
function fetchUserProfile(userId) { }
function validateEmailAddress(email) { }

// ❌ Bad - Unclear or inconsistent
function calc(items) { }
function get_user(id) { }  
function checkEmail(email) { }
```

**Team Concerns Addressed**:
- Existing snake_case code: Can remain, new code uses camelCase
- Function length: Max 20 lines, extract longer logic to separate functions

**Implementation Plan**:
- ESLint rule added for camelCase enforcement
- Code review checklist updated
- Team training session scheduled for [Date]

**Grandfathering Policy**: Existing code unchanged unless being modified
**Exception Process**: Technical Lead approval for special cases
**Review Timeline**: 3 months - assess adoption and effectiveness
```

### Security Standard Decision (Copy & Customize)  
```markdown
## Security Decision: [e.g., "API Authentication Requirements"]
**Decision Made**: [Current Date]
**Decision Maker**: [Security Lead Name]  
**Context**: [e.g., "Partner API access requires standardized authentication"]

**Security Requirement**: All external APIs must use OAuth2 + JWT with rate limiting
**Threat Model**: Prevent unauthorized access, API abuse, token theft

**Implementation Standard**:
- OAuth2 client credentials flow for service-to-service
- JWT access tokens (15 min expiry) + refresh tokens (30 days)
- Rate limiting: 1000 requests/hour per API key
- Audit logging for all authentication events

**Code Template**:
```typescript
// JWT payload standard
interface JWTPayload {
  userId: string;
  clientId: string;
  permissions: string[];
  iat: number;
  exp: number;
}

// Rate limiting middleware
const rateLimiter = rateLimit({
  windowMs: 60 * 60 * 1000, // 1 hour
  max: 1000, // requests per hour
  message: 'API rate limit exceeded'
});
```

**Compliance Requirements**: SOC2, GDPR audit trail maintained
**Exception Process**: Security team approval required for deviations  
**Implementation Timeline**: All new APIs immediately, existing APIs by [Date]
**Review Schedule**: Quarterly security review
```

## Process Decision Templates

### Git Workflow Decision Template
```markdown
## Git Workflow Decision: [e.g., "Branch Strategy & PR Process"]
**Decision Made**: [Current Date]
**Decision Maker**: [Team Lead Name]  
**Context**: [e.g., "Multiple developers causing merge conflicts, inconsistent workflows"]

**Workflow Selected**: GitHub Flow with feature branches
**Branch Naming Standard**: feature/TICKET-123-short-description

**Process Requirements**:
1. All changes via Pull Requests (no direct main commits)
2. Minimum 1 reviewer approval required
3. All CI checks must pass before merge
4. Squash commits on merge to keep history clean

**Commit Message Format**:
```
feat: add user authentication endpoint

- Implement JWT token generation
- Add password validation 
- Include rate limiting

Resolves: TICKET-123
```

**Implementation Plan**:
- GitHub branch protection rules configured
- Team training on new workflow: [Date]
- Old feature branches migrated by: [Date]

**Review Timeline**: 2 months - assess merge conflicts and velocity
```

### Code Review Process Template
```markdown
## Process Decision: Code Review Requirements
**Decision Made**: [Current Date]
**Decision Maker**: [Technical Lead Name]  
**Context**: Quality issues in production, inconsistent review depth

**Review Requirements**:
- **All production code**: Requires 1 senior developer approval
- **Critical systems**: Requires 2 approvals (1 security, 1 architecture)  
- **Documentation changes**: Requires 1 approval from any team member

**Review Focus Areas**:
1. **Security**: Authentication, authorization, input validation
2. **Architecture**: Design patterns, performance implications
3. **Business Logic**: Correctness, edge cases, error handling
4. **Code Quality**: Readability, maintainability, testing

**Review Timeline Standards**:
- **Small PRs (<100 lines)**: 24 hour review
- **Medium PRs (100-500 lines)**: 48 hour review  
- **Large PRs (>500 lines)**: Break down or 72 hour review

**Review Checklist**:
- [ ] Code follows team conventions
- [ ] Tests cover new functionality  
- [ ] Security implications considered
- [ ] Documentation updated if needed
- [ ] Performance impact assessed

**Implementation**: GitHub PR templates updated with checklist
**Review Date**: Monthly - assess review effectiveness and bottlenecks
```

## Decision Documentation Helpers

### Quick Decision Capture Format
```markdown
## Quick Decision: [Brief Title]
**Date**: [Today's Date] | **Decider**: [Your Name] | **Context**: [One sentence]

**Decision**: [What was decided in one sentence]
**Rationale**: [Why this choice in 2-3 sentences]  
**Impact**: [Who/what this affects]
**Timeline**: [When this takes effect]

**Follow-up Needed**: 
- [ ] Update team documentation
- [ ] Configure tooling/automation
- [ ] Schedule team communication
- [ ] Plan implementation timeline
```

### Decision Review Template
```markdown
## Decision Review: [Original Decision Title]
**Original Date**: [When decided] | **Review Date**: [Today] | **Reviewer**: [Your Name]

**Current Effectiveness**:
- **Working Well**: [What's successful about this decision]
- **Pain Points**: [Where the decision is causing problems]
- **Usage Reality**: [How team actually follows vs. intended]

**Metrics Since Implementation**:
- [Quantitative measures of impact]
- [Team satisfaction scores]
- [Process efficiency changes]

**Recommendation**:
- [ ] **Continue as-is** - Decision working well
- [ ] **Minor adjustments** - [What specific changes]
- [ ] **Major revision** - [Why and what changes] 
- [ ] **Sunset decision** - [Why no longer needed]

**Next Review Date**: [When to reassess again]
```

## Common Decision Scenarios

### New Team Starting
```markdown
Priority 1 Decisions (Week 1):
- [ ] Backend technology stack
- [ ] Frontend technology stack  
- [ ] Database choice
- [ ] Git workflow
- [ ] Basic code style (formatting, naming)

Priority 2 Decisions (Month 1):
- [ ] Testing requirements
- [ ] Security baseline
- [ ] Code review process
- [ ] Documentation standards
- [ ] Deployment workflow

Priority 3 Decisions (Quarter 1):
- [ ] Performance requirements
- [ ] Monitoring/logging standards
- [ ] Error handling patterns
- [ ] API design standards
- [ ] Third-party service policies
```

### Growing Team (Adding Developers)
```markdown
Onboarding Decision Checklist:
- [ ] Update team conventions with new perspectives
- [ ] Review decision authority (who decides what)
- [ ] Assess if current standards scale to larger team
- [ ] Update communication protocols
- [ ] Review tool access and permissions
```

### Legacy System Integration  
```markdown
Integration Decision Template:
- [ ] Which conventions apply to legacy systems
- [ ] Migration timeline for bringing legacy into compliance
- [ ] Exception process for legacy system constraints
- [ ] Gradual adoption vs. big-bang conversion
- [ ] Risk assessment for convention changes
```

---

*Use these templates to make team decisions systematically rather than letting conventions emerge randomly. Customize the templates for your specific team context and decision-making style.*