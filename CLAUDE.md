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

## TOOL INTEGRATION

### Read Files
Always check current state:
```bash
cat project-memory/conventions.md  # Check existing decisions
cat project-memory/symbol-index.md # Check current system structure
```

### Use CLI Tools Actively
```bash
# Check system health
npm run validate

# Find inconsistencies  
npm run drift

# Capture decisions
memory-enforce decision --title "..." --standard "..." --rationale "..." --scope "..."

# Document patterns
memory-enforce pattern --name "..." --description "..." --usage "..."
```

### Validate Changes
```bash
# After any institutional memory updates
npm run validate
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