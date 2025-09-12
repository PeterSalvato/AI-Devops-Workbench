# Decision Transparency & Feedback Integration

*Framework for Claude to reference and explain which conventions, patterns, and decisions inform its recommendations, creating accountability and learning opportunities.*

## Transparency Requirements

### When Making Recommendations, Claude Should Reference:

#### 1. Conventions Applied
**Format**:
```
📋 **Applying Conventions**:
- Technology Stack: Node.js + Express + TypeScript (from conventions.md: Backend Development Standards, decided 2024-08-15)
- API Format: Standardized APIResponse<T> interface (from conventions.md: Backend Standards)
- Authentication: JWT + OAuth2 pattern (from conventions.md: Authentication Requirements, decided 2024-09-06)
```

#### 2. Patterns Referenced  
**Format**:
```
🔄 **Following Patterns**:
- Orchestration: Security-First Development (from orchestration-patterns/security-first-development.md)
- Coordination: Senior Architect → Security Consultant → Backend Builder (from project-memory/coordination-discoveries.md)
- Quality: Consensus validation required for authentication systems (from conventions.md: Authentication Systems)
```

#### 3. Codebase Context Used
**Format**:
```
🗂️ **Referencing Codebase**:
- Integration Point: authenticateUser() function in src/services/auth/ (from symbol-index.md: Authentication Service)
- Dependencies: Will need to update User Service calls to validateSession() (from symbol-index.md: User Management Service)
- Breaking Changes: None - maintaining existing API contracts
```

## Implementation in Agent Responses

### Consultation Agent Transparency
When consultation agents make recommendations:

```markdown
## Senior Architect Recommendation

### Technology Stack Analysis
📋 **Applying Conventions**: 
- Following established Node.js + TypeScript standard (conventions.md: Backend Development Standards)
- Using PostgreSQL + Redis pattern (conventions.md: Database Standards, decided 2024-08-15)

🔄 **Following Patterns**:
- Database-per-service pattern from previous e-commerce architecture decisions
- Performance-first caching strategy from established patterns

### Recommendation
Based on established conventions and patterns, I recommend...

### New Decision Required
This project introduces [new requirement] not covered by existing conventions. Options:
1. [Option A] - extends existing patterns
2. [Option B] - establishes new pattern
[Analysis and trade-offs]
```

### Production Agent Transparency  
When production agents implement features:

```markdown
## Backend Builder Implementation

### Implementation Approach  
📋 **Applying Conventions**:
- API Response Format: Using standardized APIResponse<T> (conventions.md: Backend Standards)
- Error Handling: Implementing APIError class pattern (conventions.md: Error Handling Standards)
- Testing: Jest + 80% coverage requirement (conventions.md: Testing Requirements)

🗂️ **Referencing Codebase**:
- Integration: Calling authenticateUser() from src/services/auth/ (symbol-index.md: Authentication Service)
- Dependencies: Will integrate with existing emailService for notifications

### Implementation Details
[Actual implementation following referenced standards]

### Convention Updates Needed
This implementation reveals need to document [new pattern] in conventions.md for future reuse.
```

## Feedback Collection Mechanisms

### 1. Decision Validation Feedback
After applying conventions, ask for validation:

```markdown
### 🔍 **Decision Validation**
I applied the following conventions in this recommendation:
- JWT authentication pattern (established 2024-09-06)
- Node.js + TypeScript stack (established 2024-08-15)

**Feedback Questions**:
- Are these conventions still appropriate for this use case?
- Should any conventions be updated based on new requirements?
- Are there new decisions that should be documented?
```

### 2. Pattern Effectiveness Feedback
After using orchestration patterns:

```markdown
### 📊 **Pattern Effectiveness Check**
I used the Security-First Development pattern for this authentication feature:
- Security Consultant → Senior Architect → Backend Builder coordination
- Early threat modeling before implementation
- Multi-expert validation before production

**Feedback Questions**:
- Was this coordination effective for this project?
- Should this pattern be applied to similar future projects?
- Are there improvements to document in coordination-discoveries.md?
```

### 3. Context Accuracy Feedback
When referencing symbol-index.md:

```markdown
### 🎯 **Codebase Context Verification**
I referenced these integration points from symbol-index.md:
- authenticateUser() function dependencies
- User Service integration requirements
- Expected API contract maintenance

**Feedback Questions**:
- Are these integration points still accurate?
- Have any dependencies changed since last update?
- Should symbol-index.md be updated with new information?
```

## Convention Update Triggers

### Automatic Updates Based on Feedback

#### When User Confirms New Pattern
```markdown
User: "Yes, this JWT + TOTP approach worked well and should be our standard"

Claude Response:
📝 **Updating Conventions**: Adding TOTP 2FA requirement to Authentication Standards in conventions.md
🔄 **Updating Patterns**: Documenting Security-First + UX collaboration pattern in coordination-discoveries.md

Updated conventions will be applied to future authentication projects automatically.
```

#### When User Corrects Context
```markdown
User: "Actually, the authenticateUser() function was moved to src/auth-service/core.ts"

Claude Response:
🔧 **Updating Symbol Index**: Correcting authenticateUser() location in symbol-index.md
📍 **Verifying Dependencies**: Checking other references to this function for consistency

Symbol index updated - future recommendations will reference correct location.
```

#### When User Rejects Recommendation
```markdown
User: "No, don't use our standard Node.js stack for this project - use Python instead"

Claude Response:
📋 **Convention Override**: Using Python instead of established Node.js standard for this project
❓ **Convention Update Question**: Should this be:
  1. One-time exception (keep Node.js as standard)
  2. New convention (Python becomes new standard)
  3. Context-specific rule (Python for ML projects, Node.js for APIs)

Please clarify so I can update conventions.md appropriately.
```

## Learning Loop Integration

### Session-End Convention Review
At the end of development sessions:

```markdown
## 📚 **Session Learning Review**

### Conventions Applied This Session
- Authentication: JWT + OAuth2 pattern (worked effectively)
- Database: PostgreSQL + Redis pattern (performance was good)
- Testing: 80% coverage requirement (caught 3 bugs)

### New Patterns Discovered  
- Security + UX early collaboration reduced design changes by 60%
- API contract iteration between Frontend/Backend worked better than sequential handoff

### Convention Updates Made
- Added TOTP 2FA requirement to Authentication Standards
- Documented Security-UX collaboration pattern in coordination-discoveries.md

### Questions for Future Sessions
- Should the 80% test coverage be increased to 85% based on bug prevention success?
- Is the Security-UX collaboration pattern applicable to all user-facing features?
```

## Feedback Integration in CLAUDE.md

Update CLAUDE.md to require transparency:

```markdown
## Decision Transparency Requirements

When making any recommendation or implementation, Claude must:

1. **Reference Applied Conventions**: Cite specific conventions.md decisions being applied
2. **Explain Pattern Usage**: Reference orchestration patterns and coordination approaches used
3. **Show Codebase Context**: Reference symbol-index.md for integration points and dependencies
4. **Request Feedback**: Ask for validation of applied conventions and patterns
5. **Update Documentation**: Immediately update project-memory files when user provides feedback

### Transparency Format
Use consistent format for decision references:
- 📋 **Applying Conventions**: [specific decisions from conventions.md]
- 🔄 **Following Patterns**: [orchestration patterns being used]
- 🗂️ **Referencing Codebase**: [symbol-index.md context being applied]
- 🔍 **Feedback Request**: [questions for user validation]
```

This creates a complete feedback loop where:
1. **Claude explains** which decisions inform its recommendations
2. **User validates** whether those decisions are still appropriate  
3. **System updates** conventions and patterns based on feedback
4. **Future sessions** benefit from refined context and patterns

Should I implement these transparency requirements throughout the framework?