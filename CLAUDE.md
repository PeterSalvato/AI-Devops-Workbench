# Claude Instructions: Institutional Memory Guardrails

**You must actively use the institutional memory system and tools to maintain current documentation.**

## MANDATORY WORKFLOW

**Before ANY architectural decision or development work:**

### 1. Check Existing Conventions
```javascript
// Always run this first
const enforcer = require('./institutional-memory-enforcer.js');
const decision = await enforcer.checkForExistingDecision('authentication');

if (decision.found) {
  // Use the documented standard
  console.log(`Using existing standard: ${decision.convention.standard}`);
  // Apply this standard to your work
} else {
  // Go to step 2
}
```

### 2. Ask User for Missing Decisions
```javascript
if (!decision.found) {
  // STOP development and ask user
  console.log(`Missing convention for: ${decisionType}`);
  console.log('Questions for user:');
  decision.requiredQuestions.questions.forEach(q => console.log(`- ${q}`));
  
  // Wait for user response, then capture immediately
  const captured = await enforcer.captureAndApplyDecision(userResponse, decisionType);
}
```

### 3. Update Symbol Index After Work
```javascript
// After completing any development
await enforcer.completeDevelopmentCycle({
  newFunctions: [
    {
      name: 'functionName',
      file: 'path/to/file.js',
      purpose: 'what it does',
      dependencies: ['what it depends on']
    }
  ],
  newConnections: [
    {
      from: 'ComponentA',
      to: 'ComponentB', 
      type: 'API call',
      purpose: 'data flow description'
    }
  ]
});
```

## ACTIVE TOOL USAGE

### Before Starting Development
```bash
# Always validate system first
npm run validate

# Check for documentation drift
npm run drift
```

### During Development
```bash
# When you need to capture a decision
memory-enforce decision \
  --title "Decision Name" \
  --standard "What was chosen" \
  --rationale "Why this choice" \
  --scope "Where this applies"
```

### After Development
```bash
# Update institutional memory
memory-enforce pattern \
  --name "Pattern Name" \
  --description "What pattern was used" \
  --usage "When to apply this pattern"
```

## SPECIFIC INSTRUCTIONS

### When User Asks for Development Work
1. **Read conventions.md** - Check for relevant existing decisions
2. **If convention exists** - Use it and reference it in your response
3. **If convention missing** - Stop and ask user for the decision
4. **Capture decision immediately** - Use the CLI tools to document it
5. **Proceed with development** using the documented standard
6. **Update symbol index** when work is complete

### When User Makes Architectural Decisions
```bash
# Immediately capture any architectural choice
memory-enforce decision \
  --title "User's Decision Title" \
  --standard "What user decided" \
  --rationale "User's reasoning" \
  --scope "Where this applies"
```

### When You Build Functionality
```javascript
// Always update symbol index
const developmentResults = {
  newFunctions: [/* document all functions you create */],
  newConnections: [/* document all integrations */],
  discoveredPatterns: [/* document successful approaches */]
};

await enforcer.completeDevelopmentCycle(developmentResults);
```

## CORE FILE MASTERY

### conventions.md Search Patterns
Essential grep patterns for finding existing decisions:
```bash
# Search by technology type
grep -i "authentication\|auth\|login" project-memory/conventions.md
grep -i "database\|db\|postgres\|mysql" project-memory/conventions.md
grep -i "frontend\|react\|vue\|angular" project-memory/conventions.md
grep -i "api\|endpoint\|rest\|graphql" project-memory/conventions.md

# Search by decision scope
grep -A 3 -B 1 "Apply To" project-memory/conventions.md
grep -A 2 "**Standard**:" project-memory/conventions.md

# Find recent decisions
grep -A 5 "$(date +%Y-%m)" project-memory/conventions.md
```

### symbol-index.md Quick Reference
Essential commands for symbol index navigation:
```bash
# Find functions by name pattern
grep -A 2 "### [A-Z]" project-memory/symbol-index.md

# Find connections between components
grep -A 1 "**From:**" project-memory/symbol-index.md

# Find patterns by type
grep -A 3 "**Pattern:**" project-memory/symbol-index.md

# Check for stale references
grep -o "src/[^)]*" project-memory/symbol-index.md | sort -u
```

### Core File Health Commands
Quick diagnostic checks for the two sacred files:
```bash
# Validate conventions.md structure
grep -c "**Decision Made**" project-memory/conventions.md
grep -c "**Standard**:" project-memory/conventions.md

# Validate symbol-index.md completeness
grep -c "### " project-memory/symbol-index.md
grep -c "**From:**" project-memory/symbol-index.md

# Check for file integrity
npm run validate
npm run drift
```

### Decision Templates
Copy-paste ready formats for conventions.md:

**Technology Choice Template:**
```markdown
### [Technology Category] Decision
**Decision Made**: [Date] - [Technology Name]
**Standard**: [Specific technology/approach chosen]
**Rationale**: [Why this choice over alternatives]
**Apply To**: [Scope of application]
**Dependencies**: [Required tools/libraries]
**Migration**: [How to adopt in existing code]
```

**Architecture Pattern Template:**
```markdown
### [Pattern Name] Architecture
**Decision Made**: [Date] - [Pattern approach]
**Standard**: [How to implement this pattern]
**Rationale**: [Benefits and reasoning]
**Apply To**: [Where this pattern should be used]
**Examples**: [Code examples or references]
**Alternatives Rejected**: [What we considered but didn't choose]
```

**Security Standard Template:**
```markdown
### [Security Domain] Requirements
**Decision Made**: [Date] - [Security approach]
**Standard**: [Specific security requirements]
**Implementation**: [How to implement securely]
**Apply To**: [What components this covers]
**Compliance**: [Regulatory/company requirements met]
**Validation**: [How to verify compliance]
```

### Symbol-Index Update Templates
Copy-paste ready formats for symbol-index.md:

**Function Documentation Template:**
```markdown
### [FunctionName]
**File**: [path/to/file.js]:[lineNumber]
**Purpose**: [What this function does]
**Parameters**: [Input parameters and types]
**Returns**: [What it returns]
**Dependencies**: [What it depends on]
**Used By**: [What calls this function]
**Added**: [Date] - [Context/Feature]
```

**Component Connection Template:**
```markdown
### [ComponentA] → [ComponentB] Integration
**From**: [Source component/file]
**To**: [Destination component/file]
**Type**: [API call, data flow, event, etc.]
**Purpose**: [Why this connection exists]
**Data**: [What data flows through]
**Added**: [Date] - [Context/Feature]
```

**Pattern Documentation Template:**
```markdown
### [Pattern Name] Pattern
**Discovered**: [Date] - [Context where found]
**Pattern**: [Description of the pattern]
**Usage**: [When to apply this pattern]
**Examples**: [Where it's used in codebase]
**Benefits**: [Why this pattern is valuable]
**Integration Points**: [How it connects to other patterns]
```

### Core File Workflow Enhancement
Enhanced decision capture process:

**Step 1: Smart Search Before Asking**
```bash
# Use multiple search patterns before declaring "not found"
grep -i "auth" project-memory/conventions.md
grep -i "login\|signin\|credential" project-memory/conventions.md
grep -i "security\|token\|session" project-memory/conventions.md

# Check related decisions that might apply
grep -B 2 -A 5 "user\|access\|permission" project-memory/conventions.md
```

**Step 2: Contextual Decision Capture**
```javascript
// Enhanced decision context gathering
const context = {
  related_decisions: await findRelatedDecisions(decisionType),
  existing_patterns: await findRelevantPatterns(decisionType),
  scope_analysis: await analyzeScopeOverlap(decisionType, userContext)
};

// Use think tool for better question generation
const reasoning = this.thinkTool.reasonAboutDecision(decisionType, [], context);
```

**Step 3: Symbol Index Auto-Update Priority**
```javascript
// Prioritize symbol index updates by impact
const updatePriority = {
  high: ['new architectural components', 'cross-service integrations'],
  medium: ['utility functions', 'data transformations'],
  low: ['helper functions', 'local utilities']
};
```

## EXAMPLE INTERACTION

**User**: "Add authentication to the app"

**You**: 
```bash
# First, check existing conventions
grep -i "authentication" project-memory/conventions.md
```

**If found**: "Using existing authentication standard: JWT + OAuth2 (documented in conventions.md). Proceeding with implementation..."

**If not found**: "No authentication standard documented. Need to capture this decision first.

Questions:
- What authentication method? (JWT, sessions, OAuth2, etc.)
- What security level needed? (basic, 2FA, enterprise)
- What token storage approach?

Please provide your choices and I'll document them immediately."

**After user responds**:
```bash
memory-enforce decision \
  --title "Authentication Method" \
  --standard "JWT + OAuth2" \
  --rationale "Security requirements and scalability" \
  --scope "All user authentication"
```

**After implementation**:
```javascript
await enforcer.completeDevelopmentCycle({
  newFunctions: [
    {
      name: 'authenticateUser',
      file: 'src/auth.js', 
      purpose: 'Validates user credentials with JWT',
      dependencies: ['jsonwebtoken', 'bcrypt']
    }
  ],
  newConnections: [
    {
      from: 'LoginForm',
      to: 'AuthService',
      type: 'Authentication request',
      purpose: 'User credential validation'
    }
  ]
});
```

## FAILURE MODES

### If Tools Don't Work
```bash
# Diagnose issues
npm run validate
npm run check

# Manual fallback
echo "Manual update needed" >> project-memory/conventions.md
```

### If Files Are Missing
```bash
# Reinitialize if needed
npm run init --force
```

### If Drift Detected
```bash
npm run drift
# Address specific issues reported
# Update documentation to match reality
```

## ENFORCEMENT RULES

### Never Do
- Make architectural decisions without checking conventions first
- Proceed with development if conventions are missing
- Complete work without updating symbol index
- Assume what the user wants - always ask for missing decisions

### Always Do  
- Run tools to check and update institutional memory
- Use CLI commands to capture decisions immediately
- Update documentation after any development work
- Reference documented conventions in your responses

---

**You are responsible for actively maintaining the institutional memory system through tool usage and keeping documentation current.**