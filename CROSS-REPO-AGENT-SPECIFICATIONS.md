# Cross-Repository Agent Behavior Specifications

**Mandatory institutional memory workflow for all AI agents across both repositories**

## Overview

Both **AI DevOps Framework** and **Portableagency** agents MUST follow the identical institutional memory workflow to ensure consistent convention management and prevent knowledge drift.

---

## UNIVERSAL AGENT REQUIREMENTS

### **All Agents Must Implement:**

1. **Convention Checking** - Check existing decisions before making new ones
2. **User Decision Capture** - Ask user for missing conventions and document immediately  
3. **Symbol Index Updates** - Document functionality and connections after development
4. **Shared File Access** - Read/write same conventions.md and symbol-index.md files

---

## PORTABLEAGENCY INTEGRATION SPECIFICATIONS

### **Specialist Behavior Modifications**

**Every specialist interaction must include:**

```javascript
// MANDATORY PRE-CHECK (Before specialist execution)
const InstitutionalMemory = require('./ai-devops-framework/institutional-memory-enforcer.js');

// 1. Check for existing conventions
const conventionCheck = await InstitutionalMemory.runMandatoryWorkflow({
  decisionType: specialist.getDecisionType(), // e.g., 'frontend-framework', 'testing-strategy'
  context: {
    technology: detectedTechStack,
    domain: projectDomain,
    specialist: specialist.name
  }
});

if (conventionCheck.status === 'AWAITING_USER_DECISION') {
  // PAUSE specialist execution
  return {
    status: 'CONVENTION_REQUIRED',
    questions: conventionCheck.questions,
    nextAction: 'awaitUserDecision'
  };
}

// 2. Use existing convention for specialist work
const convention = conventionCheck.convention;
```

### **Modified Specialist Structure**

```javascript
// Enhanced Portableagency Specialist Template
{
  "specialist_metadata": {
    "name": "frontend_specialist",
    "version": "1.0.0",
    "institutional_memory_integration": true
  },
  "pre_execution_checks": [
    "technology_detection",
    "convention_validation",  // NEW: Check institutional memory
    "dependency_analysis"
  ],
  "execution_workflow": [
    "load_existing_conventions",  // NEW: Step 1
    "check_for_missing_conventions",  // NEW: Step 2  
    "execute_specialist_tasks",  // Step 3: Only if conventions exist
    "update_symbol_index"  // NEW: Step 4
  ],
  "post_execution_updates": [
    "verification_logging",
    "institutional_memory_update",  // NEW: Required
    "evidence_documentation"
  ]
}
```

### **Portableagency Manifest Modifications**

```json
{
  "version": "1.0.0",
  "type": "portable_agency",
  "institutional_memory": {
    "enabled": true,
    "ai_devops_framework_integration": true,
    "conventions_file": "./ai-devops-framework/project-memory/conventions.md",
    "symbol_index_file": "./ai-devops-framework/project-memory/symbol-index.md",
    "enforcement_engine": "./ai-devops-framework/institutional-memory-enforcer.js"
  },
  "specialists": {
    "base_pack": [
      "frontend_specialist_with_memory",
      "backend_specialist_with_memory", 
      "security_specialist_with_memory"
    ]
  },
  "verification_settings": {
    "self_verification_enabled": true,
    "institutional_memory_validation": true,  // NEW
    "convention_compliance_check": true  // NEW
  }
}
```

---

## AI DEVOPS FRAMEWORK INTEGRATION

### **Enhanced Agent Behavior**

**All enhanced agents must implement:**

```javascript
// Enhanced Agent Template (enhanced-*.json)
{
  "agent_metadata": {
    "name": "enhanced-frontend-builder",
    "methodology": "Component-driven + Accessibility",
    "institutional_memory_compliance": true
  },
  "core_methodology": {
    "framework": "Component-driven development + WCAG accessibility",
    "institutional_memory_integration": {
      "pre_check": "convention_validation",
      "decision_capture": "automatic",
      "symbol_update": "mandatory"
    }
  },
  "execution_pattern": [
    "check_existing_conventions",
    "identify_missing_conventions", 
    "pause_for_user_decisions",
    "apply_conventions_to_development",
    "update_symbol_index_with_results"
  ]
}
```

### **Orchestration Pattern Updates**

**All orchestration patterns must include institutional memory steps:**

```markdown
## Sequential Pattern (Updated)
1. **Convention Check** - Architecture agent checks existing decisions
2. **Missing Convention Discovery** - Identify gaps, ask user
3. **Convention Application** - Security agent applies documented standards  
4. **Implementation** - Backend/Frontend builders use conventions
5. **Symbol Index Update** - Document all new functionality and connections

## MapReduce Pattern (Updated)  
1. **Parallel Convention Check** - All agents check relevant conventions
2. **Convention Gap Synthesis** - Combine missing convention lists
3. **User Decision Session** - Ask for all missing conventions at once
4. **Parallel Implementation** - All agents use established conventions
5. **Coordinated Symbol Update** - Merge all new patterns and connections
```

---

## SHARED FILE INTEGRATION

### **File Access Pattern**

**Both repositories must access the same institutional memory files:**

```
Project Structure:
workspace/
├── ai-devops-framework/
│   ├── project-memory/
│   │   ├── conventions.md          # SHARED - Both repos read/write
│   │   └── symbol-index.md         # SHARED - Both repos read/write  
│   └── institutional-memory-enforcer.js  # SHARED - Both repos use
└── portableagency/
    ├── .claude-agency/
    │   ├── manifest.json             # References AI DevOps files
    │   └── specialists/              # Modified to use institutional memory
    └── [portableagency files]
```

### **Cross-Repo File Synchronization**

```javascript
// Portableagency file access configuration
const INSTITUTIONAL_MEMORY_CONFIG = {
  conventionsPath: '../ai-devops-framework/project-memory/conventions.md',
  symbolIndexPath: '../ai-devops-framework/project-memory/symbol-index.md',
  enforcerPath: '../ai-devops-framework/institutional-memory-enforcer.js'
};

// AI DevOps Framework file access (native)
const INSTITUTIONAL_MEMORY_CONFIG = {
  conventionsPath: './project-memory/conventions.md',
  symbolIndexPath: './project-memory/symbol-index.md', 
  enforcerPath: './institutional-memory-enforcer.js'
};
```

---

## IMPLEMENTATION STEPS

### **For Portableagency Repository**

1. **Add Institutional Memory Dependency**
   ```json
   // package.json
   "dependencies": {
     "ai-devops-framework": "file:../ai-devops-framework"
   }
   ```

2. **Modify Specialist Templates**
   - Add convention checking to pre-execution
   - Add symbol index updates to post-execution
   - Include user decision capture workflow

3. **Update Manifest Schema**
   - Add institutional memory configuration
   - Reference AI DevOps Framework files
   - Enable convention compliance checking

4. **Modify Verification Workflow**
   - Include convention compliance in verification
   - Validate institutional memory updates
   - Check for missing decisions before execution

### **For AI DevOps Framework Repository**

1. **Create Portableagency Integration Layer**
   ```javascript
   // portableagency-integration.js
   module.exports = {
     validateSpecialistCompliance: async (specialist) => {
       // Validate specialist follows institutional memory workflow
     },
     
     syncInstitutionalMemory: async () => {
       // Ensure both repos have same institutional memory state
     }
   };
   ```

2. **Update Enhanced Agents**
   - Add portableagency specialist coordination
   - Include technical verification + convention compliance
   - Ensure consistent institutional memory updates

---

## DECISION TYPE MAPPING

### **Portableagency Specialist → Decision Types**

```javascript
const SPECIALIST_DECISION_MAPPING = {
  'frontend_specialist': ['frontend-framework', 'ui-components', 'state-management'],
  'backend_specialist': ['backend-framework', 'database', 'api-design'],
  'security_specialist': ['authentication', 'authorization', 'security-standards'],
  'testing_specialist': ['testing-strategy', 'test-frameworks', 'coverage-requirements'],
  'deployment_specialist': ['deployment-strategy', 'infrastructure', 'monitoring']
};
```

### **AI DevOps Enhanced Agents → Decision Types**

```javascript
const ENHANCED_AGENT_DECISION_MAPPING = {
  'enhanced-senior-architect': ['architecture-patterns', 'system-design', 'technology-stack'],
  'enhanced-security-consultant': ['security-frameworks', 'threat-modeling', 'compliance'],
  'enhanced-ux-strategist': ['user-experience', 'accessibility', 'design-systems'],
  'enhanced-backend-builder': ['backend-implementation', 'database-schema', 'api-implementation'],
  'enhanced-frontend-builder': ['frontend-implementation', 'component-architecture', 'styling']
};
```

---

## VALIDATION AND TESTING

### **Cross-Repo Compliance Testing**

```bash
# Test institutional memory integration
npm run test:institutional-memory

# Test cross-repo file access
npm run test:cross-repo-access

# Test convention synchronization  
npm run test:convention-sync

# Test specialist compliance
npm run test:specialist-workflow
```

### **Success Criteria**

- ✅ Both repos read/write same institutional memory files
- ✅ All specialists follow mandatory workflow  
- ✅ All enhanced agents follow mandatory workflow
- ✅ No duplicated convention decisions across repos
- ✅ Symbol index reflects functionality from both repos
- ✅ Convention compliance verified in both systems

---

## ROLLOUT STRATEGY

### **Phase 1: Core Integration**
1. Implement institutional memory enforcer in AI DevOps Framework
2. Create cross-repo file access patterns
3. Test basic convention checking and capture

### **Phase 2: Portableagency Integration**  
1. Modify portableagency specialists to use institutional memory
2. Update manifest and verification workflows
3. Test specialist workflow compliance

### **Phase 3: Full Workflow Integration**
1. Integrate both systems in live development scenarios
2. Validate cross-repo institutional memory maintenance  
3. Document discovered patterns and optimizations

### **Phase 4: Production Deployment**
1. Deploy integrated system to development teams
2. Monitor institutional memory consistency
3. Iterate based on real-world usage patterns

---

**This specification ensures that both AI DevOps Framework and Portableagency work together seamlessly to maintain consistent institutional memory, preventing the architectural drift and knowledge loss that plague most development teams.**