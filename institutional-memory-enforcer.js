/**
 * Institutional Memory Enforcement System
 * 
 * Core enforcement engine for conventions.md and symbol-index.md integrity.
 * Prevents institutional memory drift and ensures mandatory workflow compliance.
 */

const fs = require('fs');
const path = require('path');

class InstitutionalMemoryEnforcer {
  constructor(projectRoot = process.cwd()) {
    this.projectRoot = projectRoot;
    this.conventionsPath = path.join(projectRoot, 'project-memory', 'conventions.md');
    this.symbolIndexPath = path.join(projectRoot, 'project-memory', 'symbol-index.md');
    this.enforcementLog = [];
  }

  /**
   * MANDATORY PRE-CHECK SYSTEM
   * Must pass before any development work begins
   */
  async runMandatoryPreChecks() {
    const checks = {
      filesExist: await this.validateFilesExist(),
      structureValid: await this.validateFileStructure(),
      contentCurrent: await this.validateContentFreshness(),
      noConflicts: await this.detectConventionConflicts()
    };

    const allPassed = Object.values(checks).every(check => check.passed);
    
    if (!allPassed) {
      throw new Error(`MANDATORY PRE-CHECK FAILED: ${this.getFailureReport(checks)}`);
    }

    this.log('✅ All mandatory pre-checks passed');
    return checks;
  }

  /**
   * MANDATORY CONVENTION CHECK WORKFLOW
   * Step 1: Check if decisions already exist
   */
  async checkForExistingDecision(decisionType, context = {}) {
    const conventions = await this.parseConventions();
    const matchingDecisions = this.findMatchingDecisions(conventions, decisionType, context);
    
    if (matchingDecisions.length > 0) {
      this.log(`✅ Found existing decision for ${decisionType}`);
      return {
        found: true,
        decisions: matchingDecisions,
        convention: matchingDecisions[0] // Use most recent/specific
      };
    }
    
    this.log(`❓ No existing decision found for ${decisionType}`);
    return {
      found: false,
      requiredQuestions: this.generateConventionQuestions(decisionType, context)
    };
  }

  /**
   * MANDATORY DECISION CAPTURE
   * Step 2: Capture user decision and make it available immediately
   */
  async captureAndApplyDecision(userDecision, decisionType) {
    // Validate required fields
    if (!userDecision.choice || !userDecision.rationale) {
      throw new Error('User decision must include choice and rationale');
    }

    const decision = {
      title: `${decisionType} Standard`,
      context: userDecision.context || 'Current development task',
      standard: userDecision.choice,
      rationale: userDecision.rationale,
      scope: userDecision.scope || 'This project and similar contexts',
      decisionType: decisionType,
      timestamp: new Date().toISOString()
    };

    // Immediately capture to conventions.md
    await this.captureNewDecision(decision);
    
    this.log(`✅ Decision captured and ready: ${decisionType} = ${userDecision.choice}`);
    
    return {
      captured: true,
      decision: decision,
      applyThis: userDecision.choice // What to use for development
    };
  }

  /**
   * AUTOMATIC SYMBOL INDEX UPDATE SYSTEM
   * Step 4: Update symbol index after development is complete
   */
  async updateSymbolIndexAfterDevelopment(developmentResults) {
    const timestamp = new Date().toISOString().split('T')[0];
    
    // Process new functions
    if (developmentResults.newFunctions && developmentResults.newFunctions.length > 0) {
      for (const func of developmentResults.newFunctions) {
        await this.addFunctionToSymbolIndex(func, timestamp);
      }
    }
    
    // Process new integrations/connections
    if (developmentResults.newConnections && developmentResults.newConnections.length > 0) {
      for (const connection of developmentResults.newConnections) {
        await this.addConnectionToSymbolIndex(connection, timestamp);
      }
    }
    
    // Process discovered patterns
    if (developmentResults.discoveredPatterns && developmentResults.discoveredPatterns.length > 0) {
      for (const pattern of developmentResults.discoveredPatterns) {
        await this.captureNewPattern(pattern);
      }
    }
    
    this.log(`✅ Symbol index updated with ${developmentResults.newFunctions?.length || 0} functions, ${developmentResults.newConnections?.length || 0} connections`);
    
    return {
      updated: true,
      functionsAdded: developmentResults.newFunctions?.length || 0,
      connectionsAdded: developmentResults.newConnections?.length || 0,
      patternsAdded: developmentResults.discoveredPatterns?.length || 0
    };
  }

  /**
   * COMPLETE DEVELOPMENT WORKFLOW
   * Orchestrates the full mandatory workflow
   */
  async executeFullDevelopmentWorkflow(request) {
    const workflow = {
      step1_checkConventions: null,
      step2_captureDecision: null,
      step3_developmentResult: null,
      step4_updateSymbolIndex: null
    };
    
    try {
      // Step 1: Check existing conventions
      workflow.step1_checkConventions = await this.checkForExistingDecision(request.decisionType, request.context);
      
      let conventionToUse;
      
      if (workflow.step1_checkConventions.found) {
        // Use existing convention
        conventionToUse = workflow.step1_checkConventions.convention;
        this.log(`✅ Using existing convention: ${conventionToUse.standard}`);
      } else {
        // Step 2: Need user decision - return questions for user
        this.log(`❓ Missing convention for ${request.decisionType}`);
        return {
          status: 'AWAITING_USER_DECISION',
          questions: workflow.step1_checkConventions.requiredQuestions,
          nextStep: 'captureAndApplyDecision'
        };
      }
      
      return {
        status: 'READY_FOR_DEVELOPMENT',
        convention: conventionToUse,
        workflow: workflow
      };
      
    } catch (error) {
      this.log(`❌ Workflow failed: ${error.message}`);
      throw error;
    }
  }

  /**
   * COMPLETE DEVELOPMENT CYCLE
   * Call after development is complete
   */
  async completeDevelopmentCycle(developmentResults) {
    // Step 4: Update symbol index with what was built
    const symbolIndexUpdate = await this.updateSymbolIndexAfterDevelopment(developmentResults);
    
    this.log(`✅ Development cycle complete: ${symbolIndexUpdate.functionsAdded} functions, ${symbolIndexUpdate.connectionsAdded} connections documented`);
    
    return {
      workflowComplete: true,
      symbolIndexUpdate: symbolIndexUpdate
    };
  }

  /**
   * DECISION CAPTURE (LEGACY - kept for CLI usage)
   * Captures and documents new decisions immediately
   */
  async captureNewDecision(decision) {
    const timestamp = new Date().toISOString().split('T')[0];
    const decisionEntry = this.formatDecisionEntry(decision, timestamp);
    
    await this.appendToConventions(decisionEntry);
    this.log(`✅ Decision captured: ${decision.title}`);
    
    return { captured: true, timestamp, entry: decisionEntry };
  }

  async captureNewPattern(pattern) {
    const timestamp = new Date().toISOString().split('T')[0];
    const patternEntry = this.formatPatternEntry(pattern, timestamp);
    
    await this.appendToSymbolIndex(patternEntry);
    this.log(`✅ Pattern captured: ${pattern.name}`);
    
    return { captured: true, timestamp, entry: patternEntry };
  }

  /**
   * DRIFT PREVENTION SYSTEM
   * Detects and prevents institutional memory decay
   */
  async detectDrift() {
    const driftIssues = [];
    
    // Check for outdated file references
    const symbolIndex = await this.parseSymbolIndex();
    const invalidReferences = await this.validateCodeReferences(symbolIndex);
    if (invalidReferences.length > 0) {
      driftIssues.push({
        type: 'INVALID_CODE_REFERENCES',
        count: invalidReferences.length,
        details: invalidReferences
      });
    }

    // Check for stale conventions
    const conventions = await this.parseConventions();
    const staleConventions = this.findStaleConventions(conventions);
    if (staleConventions.length > 0) {
      driftIssues.push({
        type: 'STALE_CONVENTIONS',
        count: staleConventions.length,
        details: staleConventions
      });
    }

    // Check for convention conflicts
    const conflicts = await this.detectConventionConflicts();
    if (!conflicts.passed) {
      driftIssues.push({
        type: 'CONVENTION_CONFLICTS',
        details: conflicts.conflicts
      });
    }

    return {
      driftDetected: driftIssues.length > 0,
      issues: driftIssues,
      recommendedActions: this.generateDriftActions(driftIssues)
    };
  }

  /**
   * CORE VALIDATION METHODS
   */
  async validateFilesExist() {
    try {
      const conventionsExists = fs.existsSync(this.conventionsPath);
      const symbolIndexExists = fs.existsSync(this.symbolIndexPath);
      
      return {
        passed: conventionsExists && symbolIndexExists,
        details: {
          conventionsFile: conventionsExists,
          symbolIndexFile: symbolIndexExists
        }
      };
    } catch (error) {
      return { passed: false, error: error.message };
    }
  }

  async validateFileStructure() {
    try {
      const conventionsContent = fs.readFileSync(this.conventionsPath, 'utf8');
      const symbolIndexContent = fs.readFileSync(this.symbolIndexPath, 'utf8');
      
      const conventionsValid = this.validateConventionsStructure(conventionsContent);
      const symbolIndexValid = this.validateSymbolIndexStructure(symbolIndexContent);
      
      return {
        passed: conventionsValid.valid && symbolIndexValid.valid,
        details: {
          conventions: conventionsValid,
          symbolIndex: symbolIndexValid
        }
      };
    } catch (error) {
      return { passed: false, error: error.message };
    }
  }

  async validateContentFreshness() {
    try {
      const conventionsStats = fs.statSync(this.conventionsPath);
      const symbolIndexStats = fs.statSync(this.symbolIndexPath);
      
      const daysSinceConventionsUpdate = this.daysSince(conventionsStats.mtime);
      const daysSinceSymbolIndexUpdate = this.daysSince(symbolIndexStats.mtime);
      
      // Flag as stale if not updated in 30 days
      const maxStaleDays = 30;
      
      return {
        passed: daysSinceConventionsUpdate < maxStaleDays && daysSinceSymbolIndexUpdate < maxStaleDays,
        details: {
          conventionsAge: daysSinceConventionsUpdate,
          symbolIndexAge: daysSinceSymbolIndexUpdate,
          maxAllowedAge: maxStaleDays
        }
      };
    } catch (error) {
      return { passed: false, error: error.message };
    }
  }

  async detectConventionConflicts() {
    try {
      const conventions = await this.parseConventions();
      const conflicts = [];
      
      // Check for conflicting technology decisions
      const techDecisions = conventions.filter(c => c.category === 'technology');
      const conflictingTech = this.findConflictingDecisions ? this.findConflictingDecisions(techDecisions) : [];
      if (conflictingTech.length > 0) {
        conflicts.push(...conflictingTech);
      }
      
      return {
        passed: conflicts.length === 0,
        conflicts: conflicts
      };
    } catch (error) {
      return { passed: false, error: error.message };
    }
  }

  /**
   * UTILITY METHODS
   */
  validateConventionsStructure(content) {
    const requiredSections = [
      '# Team Conventions',
      '## Technology Stack',
      '## Security Standards',
      '## Code Quality Standards'
    ];
    
    const missingSections = requiredSections.filter(section => 
      !content.includes(section)
    );
    
    return {
      valid: missingSections.length === 0,
      missingSections: missingSections
    };
  }

  validateSymbolIndexStructure(content) {
    const requiredSections = [
      '# Codebase Symbol Index',
      '## Core System Architecture',
      '## Function Index'
    ];
    
    const missingSections = requiredSections.filter(section => 
      !content.includes(section)
    );
    
    return {
      valid: missingSections.length === 0,
      missingSections: missingSections
    };
  }

  async parseConventions() {
    const content = fs.readFileSync(this.conventionsPath, 'utf8');
    // Simple parser - could be enhanced with proper markdown parsing
    const decisions = [];
    const lines = content.split('\n');
    let currentDecision = null;
    
    for (const line of lines) {
      if (line.startsWith('**Decision Made**:')) {
        if (currentDecision) decisions.push(currentDecision);
        currentDecision = { line, content: [line] };
      } else if (currentDecision) {
        currentDecision.content.push(line);
      }
    }
    
    if (currentDecision) decisions.push(currentDecision);
    return decisions;
  }

  async parseSymbolIndex() {
    const content = fs.readFileSync(this.symbolIndexPath, 'utf8');
    // Extract file references and function locations
    const references = [];
    const lines = content.split('\n');
    
    for (const line of lines) {
      const fileMatch = line.match(/`([^`]+\.[a-zA-Z]+)`/g);
      if (fileMatch) {
        references.push(...fileMatch.map(m => m.replace(/`/g, '')));
      }
    }
    
    return { references };
  }

  hasConvention(conventions, required) {
    return conventions.some(conv => 
      conv.content.join(' ').toLowerCase().includes(required.toLowerCase())
    );
  }

  /**
   * FIND MATCHING DECISIONS
   * Searches for existing decisions that match the current need
   */
  findMatchingDecisions(conventions, decisionType, context) {
    const matches = [];
    
    for (const convention of conventions) {
      const content = convention.content.join(' ').toLowerCase();
      const typeMatches = content.includes(decisionType.toLowerCase());
      
      // Check for context matches if provided
      let contextMatches = true;
      if (context.technology) {
        contextMatches = content.includes(context.technology.toLowerCase());
      }
      if (context.domain) {
        contextMatches = contextMatches && content.includes(context.domain.toLowerCase());
      }
      
      if (typeMatches && contextMatches) {
        matches.push({
          content: convention.content,
          standard: this.extractStandard(convention.content),
          rationale: this.extractRationale(convention.content),
          scope: this.extractScope(convention.content)
        });
      }
    }
    
    return matches;
  }

  /**
   * GENERATE CONVENTION QUESTIONS
   * Creates specific questions to ask user for missing conventions
   */
  generateConventionQuestions(decisionType, context) {
    const questionTemplates = {
      'authentication': [
        'What authentication method should be used? (JWT, Sessions, OAuth2, etc.)',
        'What level of security is required? (Basic, 2FA, Enterprise)',
        'How should tokens be stored and managed?'
      ],
      'database': [
        'What database technology should be used? (PostgreSQL, MySQL, MongoDB, etc.)',
        'What data consistency requirements? (ACID, Eventually consistent)',
        'What performance requirements? (OLTP, OLAP, Real-time)'
      ],
      'frontend-framework': [
        'What frontend framework should be used? (React, Vue, Angular, etc.)',
        'What styling approach? (CSS Modules, Styled Components, Tailwind)',
        'What state management? (Redux, Context, Zustand)'
      ],
      'api-design': [
        'What API style should be used? (REST, GraphQL, gRPC)',
        'What versioning strategy? (URL versioning, Header versioning)',
        'What error handling approach? (Standard HTTP codes, Custom error format)'
      ]
    };
    
    const questions = questionTemplates[decisionType] || [
      `What approach should be used for ${decisionType}?`,
      `What are the key requirements for ${decisionType}?`,
      `What constraints or preferences apply to ${decisionType}?`
    ];
    
    return {
      decisionType: decisionType,
      context: context,
      questions: questions,
      format: 'Please provide: 1) Your choice, 2) Rationale for the choice, 3) Scope of application'
    };
  }

  /**
   * SYMBOL INDEX UPDATE HELPERS
   */
  async addFunctionToSymbolIndex(functionInfo, timestamp) {
    const entry = `
### ${functionInfo.name}
- **Location**: \`${functionInfo.file}:${functionInfo.line || 'N/A'}\`
- **Purpose**: ${functionInfo.purpose}
- **Parameters**: ${functionInfo.parameters || 'See function signature'}
- **Returns**: ${functionInfo.returns || 'See function documentation'}
- **Dependencies**: ${functionInfo.dependencies?.join(', ') || 'None documented'}
- **Added**: ${timestamp}
- **Context**: ${functionInfo.context || 'Development session'}
`;
    
    await this.appendToSymbolIndex(entry);
  }

  async addConnectionToSymbolIndex(connectionInfo, timestamp) {
    const entry = `
### ${connectionInfo.from} → ${connectionInfo.to}
- **Connection Type**: ${connectionInfo.type}
- **Purpose**: ${connectionInfo.purpose}
- **Data Flow**: ${connectionInfo.dataFlow || 'See implementation'}
- **Dependencies**: ${connectionInfo.dependencies?.join(', ') || 'Direct connection'}
- **Added**: ${timestamp}
- **Context**: ${connectionInfo.context || 'Development session'}
`;
    
    await this.appendToSymbolIndex(entry);
  }

  /**
   * CONVENTION CONTENT EXTRACTORS
   */
  extractStandard(content) {
    const standardLine = content.find(line => line.includes('**Standard**:') || line.includes('**Technology**:'));
    return standardLine ? standardLine.split(':')[1]?.trim() || 'See content' : 'Not specified';
  }

  extractRationale(content) {
    const rationaleLine = content.find(line => line.includes('**Rationale**:'));
    return rationaleLine ? rationaleLine.split(':')[1]?.trim() || 'See content' : 'Not specified';
  }

  extractScope(content) {
    const scopeLine = content.find(line => line.includes('**Apply To**:') || line.includes('**Scope**:'));
    return scopeLine ? scopeLine.split(':')[1]?.trim() || 'See content' : 'Not specified';
  }

  /**
   * FIND CONFLICTING DECISIONS
   * Check for contradictory architectural choices
   */
  findConflictingDecisions(decisions) {
    const conflicts = [];
    
    // Group decisions by type
    const decisionsByType = {};
    decisions.forEach(decision => {
      const type = decision.decisionType || 'general';
      if (!decisionsByType[type]) {
        decisionsByType[type] = [];
      }
      decisionsByType[type].push(decision);
    });
    
    // Check for conflicts within each type
    Object.entries(decisionsByType).forEach(([type, typeDecisions]) => {
      if (typeDecisions.length > 1) {
        // Multiple decisions of same type - potential conflict
        const standards = typeDecisions.map(d => d.standard || 'unknown');
        const uniqueStandards = new Set(standards);
        
        if (uniqueStandards.size > 1) {
          conflicts.push({
            type: type,
            conflictingStandards: Array.from(uniqueStandards),
            decisions: typeDecisions
          });
        }
      }
    });
    
    return conflicts;
  }

  /**
   * VALIDATE CODE REFERENCES
   * Check if documented file references actually exist
   */
  async validateCodeReferences(symbolIndex) {
    const invalidReferences = [];
    
    if (symbolIndex.references && symbolIndex.references.length > 0) {
      for (const reference of symbolIndex.references) {
        const fullPath = path.join(this.projectRoot, reference);
        if (!fs.existsSync(fullPath)) {
          invalidReferences.push(reference);
        }
      }
    }
    
    return invalidReferences;
  }

  /**
   * FIND STALE CONVENTIONS
   * Identify conventions that may be outdated
   */
  findStaleConventions(conventions) {
    const staleConventions = [];
    const currentDate = new Date();
    const staleThresholdDays = 180; // 6 months
    
    conventions.forEach(convention => {
      // Try to extract date from decision
      const dateMatch = convention.content.join(' ').match(/Decision Made.*?(\d{4}-\d{2}-\d{2})/);
      if (dateMatch) {
        const decisionDate = new Date(dateMatch[1]);
        const daysDiff = (currentDate - decisionDate) / (1000 * 60 * 60 * 24);
        
        if (daysDiff > staleThresholdDays) {
          staleConventions.push({
            decision: convention,
            daysSinceDecision: Math.floor(daysDiff),
            reason: 'Decision older than 6 months'
          });
        }
      }
    });
    
    return staleConventions;
  }

  /**
   * GENERATE DRIFT ACTIONS
   * Create recommended actions for drift issues
   */
  generateDriftActions(driftIssues) {
    const actions = [];
    
    driftIssues.forEach(issue => {
      switch (issue.type) {
        case 'INVALID_CODE_REFERENCES':
          actions.push(`Update symbol-index.md: Remove ${issue.count} invalid file references`);
          break;
        case 'STALE_CONVENTIONS':
          actions.push(`Review conventions.md: ${issue.count} decisions older than 6 months`);
          break;
        case 'CONVENTION_CONFLICTS':
          actions.push(`Resolve conventions.md: ${issue.details.length} conflicting decisions found`);
          break;
        default:
          actions.push(`Address drift issue: ${issue.type}`);
      }
    });
    
    return actions;
  }

  daysSince(date) {
    return Math.floor((Date.now() - date.getTime()) / (1000 * 60 * 60 * 24));
  }

  formatDecisionEntry(decision, timestamp) {
    return `
### ${decision.title}
**Decision Made**: ${timestamp} (${decision.context})  
**Standard**: ${decision.standard}  
**Rationale**: ${decision.rationale}  
**Apply To**: ${decision.scope}  

${decision.details || ''}
`;
  }

  formatPatternEntry(pattern, timestamp) {
    return `
### ${pattern.name}
**Discovered**: ${timestamp} (${pattern.context})  
**Pattern**: ${pattern.description}  
**Usage**: ${pattern.usage}  
**Integration Points**: ${pattern.integrations.join(', ')}  
`;
  }

  async appendToConventions(entry) {
    fs.appendFileSync(this.conventionsPath, entry);
  }

  async appendToSymbolIndex(entry) {
    fs.appendFileSync(this.symbolIndexPath, entry);
  }

  log(message) {
    const timestamp = new Date().toISOString();
    this.enforcementLog.push({ timestamp, message });
    console.log(`[${timestamp}] ${message}`);
  }

  getFailureReport(checks) {
    const failures = Object.entries(checks)
      .filter(([_, check]) => !check.passed)
      .map(([name, check]) => `${name}: ${check.error || JSON.stringify(check.details)}`)
      .join('; ');
    return failures;
  }
}

/**
 * HELPER FUNCTION FOR AI AGENTS
 * Simplified interface for the mandatory workflow
 */
InstitutionalMemoryEnforcer.runMandatoryWorkflow = async function(request) {
  const enforcer = new InstitutionalMemoryEnforcer();
  return await enforcer.executeFullDevelopmentWorkflow(request);
};

InstitutionalMemoryEnforcer.captureUserDecision = async function(userDecision, decisionType) {
  const enforcer = new InstitutionalMemoryEnforcer();
  return await enforcer.captureAndApplyDecision(userDecision, decisionType);
};

InstitutionalMemoryEnforcer.completeDevCycle = async function(developmentResults) {
  const enforcer = new InstitutionalMemoryEnforcer();
  return await enforcer.completeDevelopmentCycle(developmentResults);
};

module.exports = InstitutionalMemoryEnforcer;