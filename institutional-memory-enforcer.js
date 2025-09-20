/**
 * Institutional Memory Enforcement System
 * 
 * Core enforcement engine for conventions.md and symbol-index.md integrity.
 * Prevents institutional memory drift and ensures mandatory workflow compliance.
 */

const fs = require('fs');
const path = require('path');
const ThinkTool = require('./think-tool.js');

class InstitutionalMemoryEnforcer {
  constructor(projectRoot = process.cwd()) {
    this.projectRoot = projectRoot;
    this.conventionsPath = path.join(projectRoot, 'project-memory', 'conventions.md');
    this.symbolIndexPath = path.join(projectRoot, 'project-memory', 'symbol-index.md');
    this.enforcementLog = [];
    this.thinkTool = new ThinkTool();
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
   * Step 1: Check if decisions already exist (with structured reasoning)
   */
  async checkForExistingDecision(decisionType, context = {}) {
    const conventions = await this.parseConventions();
    const matchingDecisions = this.findMatchingDecisions(conventions, decisionType, context);

    // Use think tool for structured reasoning
    const reasoning = this.thinkTool.reasonAboutDecision(decisionType, matchingDecisions, context);

    if (reasoning.action === 'resolve_conflicts') {
      this.log(`⚠️ CONFLICTS DETECTED for ${decisionType} - requires resolution`);
      return {
        found: true,
        has_conflicts: true,
        conflicts: reasoning.conflicts,
        resolution_required: true
      };
    }

    if (reasoning.action === 'use_existing') {
      this.log(`✅ Found existing decision for ${decisionType}`);
      return {
        found: true,
        decisions: matchingDecisions,
        convention: matchingDecisions[0], // Use most recent/specific
        reasoning_summary: this.thinkTool.getReasoningSummary()
      };
    }

    if (reasoning.action === 'capture_decision') {
      this.log(`❓ No existing decision found for ${decisionType}`);
      return {
        found: false,
        requiredQuestions: {
          questions: reasoning.questions,
          reasoning_context: this.thinkTool.getReasoningSummary()
        }
      };
    }
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

    // Use think tool for structured reasoning about the update
    const reasoning = this.thinkTool.reasonAboutSymbolUpdate(
      developmentResults.newFunctions || [],
      developmentResults.newConnections || [],
      developmentResults.context || {}
    );

    this.log(`🤔 Symbol update reasoning: ${reasoning.patterns_to_document.length} patterns detected`);

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

    // Capture patterns discovered by think tool reasoning
    if (reasoning.patterns_to_document && reasoning.patterns_to_document.length > 0) {
      for (const pattern of reasoning.patterns_to_document) {
        await this.captureNewPattern(pattern);
      }
    }

    // Process explicitly provided patterns
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
      patternsAdded: (reasoning.patterns_to_document?.length || 0) + (developmentResults.discoveredPatterns?.length || 0),
      reasoning_summary: this.thinkTool.getReasoningSummary(),
      impact_assessment: reasoning.impact_assessment
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
        severity: 'critical',
        count: invalidReferences.length,
        details: invalidReferences,
        impact: invalidReferences.length * 2
      });
    }

    // Check for stale conventions
    const conventions = await this.parseConventions();
    const staleConventions = this.findStaleConventions(conventions);
    if (staleConventions.length > 0) {
      driftIssues.push({
        type: 'STALE_CONVENTIONS',
        severity: 'warning',
        count: staleConventions.length,
        details: staleConventions,
        impact: staleConventions.length
      });
    }

    // Check for convention conflicts
    const conflicts = await this.detectConventionConflicts();
    if (!conflicts.passed) {
      driftIssues.push({
        type: 'CONVENTION_CONFLICTS',
        severity: 'critical',
        details: conflicts.conflicts,
        impact: conflicts.conflicts.length * 3
      });
    }

    // Use think tool for structured reasoning about drift
    const driftReport = {
      driftDetected: driftIssues.length > 0,
      issues: driftIssues
    };

    const reasoning = this.thinkTool.reasonAboutDrift(driftReport);

    this.log(`🤔 Drift analysis: ${reasoning.requires_immediate_action ? 'CRITICAL' : 'OK'} - ${reasoning.resolution_plan.length} steps needed`);

    return {
      driftDetected: driftIssues.length > 0,
      issues: driftIssues,
      reasoning_analysis: reasoning,
      recommendedActions: reasoning.resolution_plan,
      estimated_effort_minutes: reasoning.estimated_effort,
      reasoning_summary: this.thinkTool.getReasoningSummary()
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
**Discovered**: ${timestamp}${pattern.context ? ` (${pattern.context})` : ''}
**Pattern**: ${pattern.description}
**Usage**: ${pattern.usage}
**Integration Points**: ${pattern.integrations ? pattern.integrations.join(', ') : 'N/A'}
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

  /**
   * CORE FILE UTILITY METHODS
   * Methods to support enhanced CLI commands focusing on core files
   */

  async searchConventions(query, options = {}) {
    const conventions = await this.parseConventions();
    const results = [];

    for (const decision of conventions) {
      let matches = false;

      if (options.exact) {
        matches = decision.title?.toLowerCase() === query.toLowerCase() ||
                 decision.standard?.toLowerCase() === query.toLowerCase();
      } else {
        const searchPattern = new RegExp(query, 'i');
        matches = searchPattern.test(decision.title) ||
                 searchPattern.test(decision.standard) ||
                 searchPattern.test(decision.rationale) ||
                 searchPattern.test(decision.scope);
      }

      if (matches) {
        results.push(decision);
      }
    }

    return results;
  }

  async generateSearchSuggestions(query) {
    const commonTerms = {
      'auth': ['authentication', 'login', 'security', 'token', 'session'],
      'db': ['database', 'postgres', 'mysql', 'storage', 'data'],
      'api': ['endpoint', 'rest', 'graphql', 'service', 'http'],
      'front': ['frontend', 'react', 'vue', 'angular', 'ui'],
      'test': ['testing', 'jest', 'cypress', 'unit', 'integration']
    };

    const suggestions = [];
    const lowerQuery = query.toLowerCase();

    // Find related terms
    for (const [key, terms] of Object.entries(commonTerms)) {
      if (lowerQuery.includes(key) || terms.some(term => term.includes(lowerQuery))) {
        suggestions.push(...terms);
      }
    }

    // Add generic suggestions if no specific matches
    if (suggestions.length === 0) {
      suggestions.push('authentication', 'database', 'frontend', 'api', 'testing');
    }

    return [...new Set(suggestions)].slice(0, 5);
  }

  async getSymbolIndexStats() {
    const content = fs.readFileSync(this.symbolIndexPath, 'utf8');

    // Count different types of entries by pattern matching
    const functions = (content.match(/^### [A-Z]/gm) || []).length;
    const connections = (content.match(/\*\*From:\*\*/gm) || []).length;
    const patterns = (content.match(/\*\*Pattern:\*\*/gm) || []).length;

    const stats = fs.statSync(this.symbolIndexPath);

    return {
      functions,
      connections,
      patterns,
      lastUpdated: stats.mtime.toISOString().split('T')[0]
    };
  }

  async queryFunctions(pattern = '') {
    const content = fs.readFileSync(this.symbolIndexPath, 'utf8');
    const functions = [];

    // Parse function entries from symbol index
    const functionMatches = content.match(/^### ([^\n]+)\n\*\*File:\*\* ([^\n]+)\n\*\*Purpose:\*\* ([^\n]+)/gm);

    if (functionMatches) {
      for (const match of functionMatches) {
        const lines = match.split('\n');
        const name = lines[0].replace('### ', '');
        const file = lines[1].replace('**File:** ', '');
        const purpose = lines[2].replace('**Purpose:** ', '');
        functions.push({ name, file, purpose });
      }
    }

    if (!pattern) return functions;

    const searchPattern = new RegExp(pattern, 'i');
    return functions.filter(func =>
      searchPattern.test(func.name) ||
      searchPattern.test(func.file) ||
      searchPattern.test(func.purpose)
    );
  }

  async queryConnections(component = '') {
    const content = fs.readFileSync(this.symbolIndexPath, 'utf8');
    const connections = [];

    // Parse connection entries from symbol index
    const connectionMatches = content.match(/\*\*From:\*\* ([^\n]+)\n\*\*To:\*\* ([^\n]+)\n\*\*Type:\*\* ([^\n]+)\n\*\*Purpose:\*\* ([^\n]+)/gm);

    if (connectionMatches) {
      for (const match of connectionMatches) {
        const lines = match.split('\n');
        const from = lines[0].replace('**From:** ', '');
        const to = lines[1].replace('**To:** ', '');
        const type = lines[2].replace('**Type:** ', '');
        const purpose = lines[3].replace('**Purpose:** ', '');
        connections.push({ from, to, type, purpose });
      }
    }

    if (!component) return connections;

    const searchPattern = new RegExp(component, 'i');
    return connections.filter(conn =>
      searchPattern.test(conn.from) ||
      searchPattern.test(conn.to) ||
      searchPattern.test(conn.purpose)
    );
  }

  async queryPatterns() {
    const content = fs.readFileSync(this.symbolIndexPath, 'utf8');
    const patterns = [];

    // Parse pattern entries from symbol index
    const patternMatches = content.match(/### ([^\n]+) Pattern\n\*\*Discovered:\*\* ([^\n]+)\n\*\*Pattern:\*\* ([^\n]+)\n\*\*Usage:\*\* ([^\n]+)/gm);

    if (patternMatches) {
      for (const match of patternMatches) {
        const lines = match.split('\n');
        const name = lines[0].replace('### ', '').replace(' Pattern', '');
        const discovered = lines[1].replace('**Discovered:** ', '');
        const description = lines[2].replace('**Pattern:** ', '');
        const usage = lines[3].replace('**Usage:** ', '');
        patterns.push({ name, discovered, description, usage });
      }
    }

    return patterns;
  }

  async checkConventionsHealth() {
    const conventions = await this.parseConventions();
    const content = fs.readFileSync(this.conventionsPath, 'utf8');

    const decisions = conventions.length;
    const sections = (content.match(/^## /gm) || []).length;
    const recentActivity = this.checkRecentActivity(content);

    return { decisions, sections, recentActivity };
  }

  async checkSymbolIndexHealth() {
    const content = fs.readFileSync(this.symbolIndexPath, 'utf8');

    // Count different types of entries by pattern matching
    const functions = (content.match(/^### [A-Z]/gm) || []).length;
    const connections = (content.match(/\*\*From:\*\*/gm) || []).length;
    const patterns = (content.match(/\*\*Pattern:\*\*/gm) || []).length;

    // Check for stale references (simplified)
    const staleReferences = await this.countStaleReferences(content);

    return { functions, connections, patterns, staleReferences };
  }

  checkRecentActivity(content) {
    const currentMonth = new Date().toISOString().slice(0, 7); // YYYY-MM
    const lastMonth = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString().slice(0, 7);

    const currentMonthMatches = (content.match(new RegExp(currentMonth, 'g')) || []).length;
    const lastMonthMatches = (content.match(new RegExp(lastMonth, 'g')) || []).length;

    if (currentMonthMatches > 0) return 'This month';
    if (lastMonthMatches > 0) return 'Last month';
    return 'Older than 1 month';
  }

  async countStaleReferences(content) {
    // Simplified stale reference detection
    const fileReferences = content.match(/src\/[^)\s]*/g) || [];
    let staleCount = 0;

    for (const ref of fileReferences) {
      try {
        if (!fs.existsSync(ref)) {
          staleCount++;
        }
      } catch (error) {
        // Ignore errors for now
      }
    }

    return staleCount;
  }

  async getDecisionTemplate(type) {
    const templates = {
      'technology': `### [Technology Category] Decision
**Decision Made**: [Date] - [Technology Name]
**Standard**: [Specific technology/approach chosen]
**Rationale**: [Why this choice over alternatives]
**Apply To**: [Scope of application]
**Dependencies**: [Required tools/libraries]
**Migration**: [How to adopt in existing code]`,

      'architecture': `### [Pattern Name] Architecture
**Decision Made**: [Date] - [Pattern approach]
**Standard**: [How to implement this pattern]
**Rationale**: [Benefits and reasoning]
**Apply To**: [Where this pattern should be used]
**Examples**: [Code examples or references]
**Alternatives Rejected**: [What we considered but didn't choose]`,

      'security': `### [Security Domain] Requirements
**Decision Made**: [Date] - [Security approach]
**Standard**: [Specific security requirements]
**Implementation**: [How to implement securely]
**Apply To**: [What components this covers]
**Compliance**: [Regulatory/company requirements met]
**Validation**: [How to verify compliance]`
    };

    return templates[type] || templates['technology'];
  }

  async detectDecisionConflicts() {
    const conventions = await this.parseConventions();
    const conflicts = [];

    for (let i = 0; i < conventions.length; i++) {
      for (let j = i + 1; j < conventions.length; j++) {
        const conflict = this.checkConflictBetween(conventions[i], conventions[j]);
        if (conflict) {
          conflicts.push({
            decision1: conventions[i],
            decision2: conventions[j],
            reason: conflict
          });
        }
      }
    }

    return conflicts;
  }

  checkConflictBetween(decision1, decision2) {
    // Check for scope overlap with different standards
    if (decision1.scope && decision2.scope &&
        decision1.scope === decision2.scope &&
        decision1.standard !== decision2.standard) {
      return `Same scope (${decision1.scope}) with different standards`;
    }

    // Check for similar titles with different approaches
    if (decision1.title && decision2.title) {
      const title1Words = decision1.title.toLowerCase().split(' ');
      const title2Words = decision2.title.toLowerCase().split(' ');
      const commonWords = title1Words.filter(word => title2Words.includes(word));

      if (commonWords.length >= 2 && decision1.standard !== decision2.standard) {
        return `Similar decisions with different standards`;
      }
    }

    return null;
  }

  async findOrphanedReferences() {
    const content = fs.readFileSync(this.symbolIndexPath, 'utf8');
    const orphans = [];

    // Find file references that don't exist
    const fileReferences = content.match(/src\/[^)\s]*/g) || [];

    for (const ref of fileReferences) {
      try {
        if (!fs.existsSync(ref)) {
          orphans.push({
            reference: ref,
            type: 'file',
            location: 'symbol-index.md'
          });
        }
      } catch (error) {
        orphans.push({
          reference: ref,
          type: 'invalid_path',
          location: 'symbol-index.md'
        });
      }
    }

    return orphans;
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