# Framework Compliance Validation

*Mandatory validation commands to verify the AI DevOps Framework is being followed correctly.*

## COMPLIANCE CHECK COMMANDS

### Test Command 1: Context Reading Verification
**Command**: 
```
Claude, what architectural conventions should I follow for backend development?
```

**REQUIRED Response Format**:
```
## 📋 APPLIED CONVENTIONS  
Reading from project-memory/conventions.md:
- Backend Development Standards: Node.js + Express + TypeScript + PostgreSQL (decided 2024-08-15)
- API Response Format: Standardized APIResponse<T> interface
- [Additional conventions found in file]

## 🗂️ CODEBASE CONTEXT
Reading from project-memory/symbol-index.md:
- [Relevant codebase structure if applicable]

[Answer to question]

## 🔍 VALIDATION REQUEST
Are these conventions still appropriate for your current project needs?
```

**❌ FAILURE INDICATORS**:
- Response doesn't reference project-memory/conventions.md
- Missing mandatory format sections
- Generic advice instead of specific established conventions

---

### Test Command 2: Feedback Processing Verification  
**Command**:
```
Claude, I've decided we should use Python instead of Node.js for ML projects. Update our standards.
```

**REQUIRED Response Behavior**:
1. **MUST use MultiEdit tool** to update project-memory/conventions.md
2. **MUST add new decision** in correct format with date, context, rationale
3. **MUST confirm** exactly what was changed in the file
4. **MUST include** validation request about scope (just ML projects vs all projects)

**❌ FAILURE INDICATORS**:  
- Says "I'll update that" without actually using MultiEdit tool
- Doesn't show file changes
- Doesn't ask for scope clarification

---

### Test Command 3: Development Request Handling
**Command**:
```
Claude, create a user profile API endpoint
```

**REQUIRED Response Format**:
```
## 📋 APPLIED CONVENTIONS
[Must cite specific conventions from project-memory/conventions.md]

## 🔄 ORCHESTRATION PATTERNS
[Must reference relevant orchestration patterns]  

## 🗂️ CODEBASE CONTEXT
[Must reference symbol-index.md for integration points]

## Implementation Approach
[Actual technical response]

## 🔍 VALIDATION REQUEST
[Ask user to validate applied conventions]

## 📝 CONVENTION UPDATES
[Document any new patterns discovered]
```

**❌ FAILURE INDICATORS**:
- Missing any required format sections
- Doesn't actually read project-memory files before responding
- Generic implementation without referencing established conventions

---

## COMPLIANCE SCORING

### Grade A: Framework Working Correctly
- [✅] Reads project-memory files before every development response  
- [✅] Uses mandatory transparency format consistently
- [✅] Updates files immediately when user provides feedback
- [✅] References established conventions instead of making generic suggestions
- [✅] Validates context accuracy with user regularly

### Grade B: Partial Compliance  
- [⚠️] Usually reads context files but sometimes skips
- [⚠️] Uses transparency format but not consistently  
- [⚠️] Updates files when reminded but not automatically
- [⚠️] Mix of established conventions and generic advice

### Grade F: Framework Not Functional
- [❌] Doesn't read project-memory files before responding
- [❌] Provides generic advice instead of applying established conventions
- [❌] Doesn't use mandatory transparency format
- [❌] Doesn't update files when user provides feedback
- [❌] Framework is just documentation, not functional behavior

## DEBUGGING NON-COMPLIANCE

### When Claude Doesn't Read Context Files
**Problem**: Claude gives generic advice instead of applying established conventions
**Debug Steps**:
1. Check if CLAUDE.md MANDATORY STARTUP SEQUENCE is clear enough
2. Verify project-memory files exist and are accessible
3. Test with explicit command: "Claude, read project-memory/conventions.md first, then answer"

### When Claude Doesn't Use Transparency Format
**Problem**: Responses don't include required format sections
**Debug Steps**:
1. Check if CLAUDE.md format requirements are mandatory enough
2. Verify format template is clear and unambiguous
3. Test with explicit command: "Claude, use the mandatory transparency format"

### When Claude Doesn't Update Files
**Problem**: User feedback doesn't result in actual file changes
**Debug Steps**:
1. Check if FEEDBACK PROCESSING REQUIREMENTS are strong enough
2. Verify MultiEdit tool is available and working
3. Test with explicit command: "Claude, update conventions.md immediately with this decision"

## FRAMEWORK READINESS CHECKLIST

**Before presenting to stakeholders or deploying to team:**
- [ ] **Context Reading**: Claude consistently reads project-memory files before development responses
- [ ] **Transparency Format**: All development responses use mandatory format  
- [ ] **Feedback Loop**: User feedback immediately updates project-memory files
- [ ] **Convention Application**: Established conventions applied instead of generic advice
- [ ] **Validation Working**: User can validate and correct framework behavior

**If any item fails, the framework is NOT functional and should not be deployed.**

---

*This compliance check ensures the AI DevOps Framework actually works as intended, not just as documented.*