/**
 * Think Tool for Institutional Memory Reasoning
 *
 * Provides structured reasoning capabilities for complex institutional memory decisions.
 * Based on Anthropic's think tool pattern for policy-heavy environments.
 */

class ThinkTool {
  constructor() {
    this.thoughtLog = [];
    this.currentContext = null;
  }

  /**
   * Core think function - records structured reasoning
   */
  think(thought, context = {}) {
    const timestamp = new Date().toISOString();
    const entry = {
      timestamp,
      thought,
      context,
      stage: context.stage || 'general'
    };

    this.thoughtLog.push(entry);

    // In actual implementation, this would be logged appropriately
    console.log(`🤔 [${context.stage || 'THINK'}] ${thought}`);

    return entry;
  }

  /**
   * Structured reasoning for institutional memory decisions
   * Enhanced with core file focus
   */
  reasonAboutDecision(decisionType, existingDecisions, context) {
    this.currentContext = { decisionType, context };

    // Stage 1: Analyze existing decisions with core file perspective
    this.think(
      `CORE FILE ANALYSIS: Analyzing conventions.md for ${decisionType}. Found ${existingDecisions.length} related decisions.`,
      { stage: 'ANALYSIS', decisionType, coreFile: 'conventions.md' }
    );

    if (existingDecisions.length > 0) {
      // Enhanced conflict analysis focusing on conventions.md integrity
      this.think(
        `CONVENTIONS CHECK: Found decisions [${existingDecisions.map(d => d.title || 'Untitled').join(', ')}]. Analyzing for conflicts that could corrupt conventions.md.`,
        { stage: 'CONFLICT_CHECK', decisions: existingDecisions, focus: 'conventions_integrity' }
      );

      const conflicts = this.analyzeConflicts(existingDecisions);
      if (conflicts.length > 0) {
        this.think(
          `CONVENTIONS CORRUPTION RISK: ${conflicts.length} conflicting decisions detected. Immediate resolution required to prevent conventions.md integrity loss.`,
          { stage: 'CONFLICT_RESOLUTION', conflicts, severity: 'CRITICAL' }
        );
        return { action: 'resolve_conflicts', conflicts, core_file_impact: 'high' };
      }

      // Check for decision quality and completeness
      const qualityIssues = this.assessDecisionQuality(existingDecisions);
      if (qualityIssues.length > 0) {
        this.think(
          `DECISION QUALITY CHECK: Found ${qualityIssues.length} quality issues in existing decisions that may impact conventions.md usefulness.`,
          { stage: 'QUALITY_ASSESSMENT', issues: qualityIssues }
        );
      }

      this.think(
        `CONVENTIONS VALIDATED: Existing decisions are consistent and properly documented in conventions.md.`,
        { stage: 'VALIDATION', quality: 'high' }
      );
      return { action: 'use_existing', decisions: existingDecisions, quality_score: this.calculateQualityScore(existingDecisions) };
    }

    // Stage 2: Gap analysis with core file impact
    this.think(
      `CONVENTIONS GAP: No existing decisions found for ${decisionType}. This creates a critical gap in conventions.md that impacts team consistency.`,
      { stage: 'GAP_IDENTIFICATION', impact: 'team_consistency' }
    );

    // Stage 3: Enhanced question generation for conventions.md
    const questions = this.generateContextualQuestions(decisionType, context);
    const enhancedQuestions = this.enhanceQuestionsForConventions(questions, context);

    this.think(
      `DECISION CAPTURE PREP: Generated ${enhancedQuestions.length} high-quality questions designed for comprehensive conventions.md documentation.`,
      { stage: 'QUESTION_GENERATION', questions: enhancedQuestions, target: 'conventions.md' }
    );

    return {
      action: 'capture_decision',
      questions: enhancedQuestions,
      core_file_priority: 'high',
      expected_quality: 'comprehensive'
    };
  }

  /**
   * Reasoning for symbol index updates
   * Enhanced with core file focus
   */
  reasonAboutSymbolUpdate(newFunctions, newConnections, context) {
    this.think(
      `SYMBOL INDEX UPDATE: Processing ${newFunctions.length} new functions, ${newConnections.length} new connections for symbol-index.md.`,
      { stage: 'SYMBOL_ANALYSIS', coreFile: 'symbol-index.md' }
    );

    // Enhanced impact analysis focusing on symbol-index.md quality
    const impact = this.analyzeSymbolImpact(newFunctions, newConnections);
    this.think(
      `SYMBOL INDEX IMPACT: ${impact.architectural_changes} architectural changes, ${impact.new_patterns} patterns detected. Assessing symbol-index.md update priority.`,
      { stage: 'IMPACT_ASSESSMENT', impact, priority: this.calculateUpdatePriority(impact) }
    );

    // Enhanced pattern detection with symbol-index focus
    const patterns = this.detectEmergingPatterns(newFunctions, newConnections);
    if (patterns.length > 0) {
      this.think(
        `SYMBOL INDEX PATTERNS: Detected ${patterns.map(p => p.name).join(', ')}. These patterns strengthen symbol-index.md as a navigation tool.`,
        { stage: 'PATTERN_DETECTION', patterns, benefit: 'navigation_enhancement' }
      );
    }

    // Check for symbol-index.md structure improvements
    const structureImprovements = this.assessStructureImprovements(newFunctions, newConnections);
    if (structureImprovements.length > 0) {
      this.think(
        `STRUCTURE ENHANCEMENT: Identified ${structureImprovements.length} ways these additions improve symbol-index.md organization.`,
        { stage: 'STRUCTURE_IMPROVEMENT', improvements: structureImprovements }
      );
    }

    return {
      update_needed: true,
      patterns_to_document: patterns,
      impact_assessment: impact,
      structure_improvements: structureImprovements,
      core_file_quality_score: this.calculateSymbolIndexQuality(newFunctions, newConnections)
    };
  }

  /**
   * Reasoning for drift detection
   */
  reasonAboutDrift(driftReport) {
    this.think(
      `Analyzing drift report: ${driftReport.issues.length} potential issues detected.`,
      { stage: 'DRIFT_ANALYSIS' }
    );

    const criticalIssues = driftReport.issues.filter(i => i.severity === 'critical');
    const warningIssues = driftReport.issues.filter(i => i.severity === 'warning');

    if (criticalIssues.length > 0) {
      this.think(
        `CRITICAL DRIFT DETECTED: ${criticalIssues.length} critical issues found. Immediate action required to prevent institutional memory corruption.`,
        { stage: 'CRITICAL_ALERT', criticalIssues }
      );
    }

    if (warningIssues.length > 0) {
      this.think(
        `Warning-level drift detected: ${warningIssues.length} issues that could lead to future problems if not addressed.`,
        { stage: 'WARNING_ASSESSMENT', warningIssues }
      );
    }

    // Prioritize resolution
    const resolutionPlan = this.prioritizeResolution(driftReport.issues);
    this.think(
      `Resolution plan created: ${resolutionPlan.length} steps prioritized by impact and urgency.`,
      { stage: 'RESOLUTION_PLANNING', plan: resolutionPlan }
    );

    return {
      requires_immediate_action: criticalIssues.length > 0,
      resolution_plan: resolutionPlan,
      estimated_effort: this.estimateResolutionEffort(resolutionPlan)
    };
  }

  /**
   * Helper methods for analysis
   */
  analyzeConflicts(decisions) {
    // Simplified conflict detection
    const conflicts = [];
    for (let i = 0; i < decisions.length; i++) {
      for (let j = i + 1; j < decisions.length; j++) {
        if (this.decisionsConflict(decisions[i], decisions[j])) {
          conflicts.push({ decision1: decisions[i], decision2: decisions[j] });
        }
      }
    }
    return conflicts;
  }

  decisionsConflict(d1, d2) {
    // Simple heuristic - same scope but different standards
    return d1.scope === d2.scope && d1.standard !== d2.standard;
  }

  generateContextualQuestions(decisionType, context) {
    const baseQuestions = {
      'authentication': [
        'What authentication method should be used? (JWT, sessions, OAuth2, etc.)',
        'What security level is required? (basic, 2FA, enterprise)',
        'How should tokens be stored and managed?',
        'What are the session timeout requirements?'
      ],
      'database': [
        'Which database system should be used?',
        'What are the ACID requirements?',
        'What are the scaling expectations?',
        'What backup and recovery strategy is needed?'
      ],
      'frontend': [
        'Which frontend framework should be used?',
        'What browser support is required?',
        'What are the performance requirements?',
        'What accessibility standards must be met?'
      ]
    };

    return baseQuestions[decisionType] || [
      'What standard should be adopted?',
      'What is the rationale for this choice?',
      'Where does this apply?',
      'What are the constraints or requirements?'
    ];
  }

  analyzeSymbolImpact(newFunctions, newConnections) {
    return {
      architectural_changes: newConnections.filter(c => c.type === 'architectural').length,
      new_patterns: this.countNewPatterns(newFunctions),
      complexity_increase: newFunctions.length + newConnections.length
    };
  }

  detectEmergingPatterns(newFunctions, newConnections) {
    // Simplified pattern detection
    const patterns = [];

    // Detect service patterns
    const serviceConnections = newConnections.filter(c => c.type === 'service_call');
    if (serviceConnections.length >= 3) {
      patterns.push({
        name: 'Service Integration Pattern',
        description: 'Multiple service integrations detected',
        usage: 'Use for microservice communication'
      });
    }

    return patterns;
  }

  countNewPatterns(newFunctions) {
    // Simplified - count unique function prefixes as patterns
    const prefixes = new Set(newFunctions.map(f => f.name.split(/[A-Z]/)[0]));
    return prefixes.size;
  }

  prioritizeResolution(issues) {
    return issues
      .sort((a, b) => {
        // Critical first, then by impact
        if (a.severity === 'critical' && b.severity !== 'critical') return -1;
        if (b.severity === 'critical' && a.severity !== 'critical') return 1;
        return (b.impact || 0) - (a.impact || 0);
      })
      .map((issue, index) => ({
        priority: index + 1,
        issue,
        action: this.determineResolutionAction(issue)
      }));
  }

  determineResolutionAction(issue) {
    if (issue.type === 'outdated_convention') {
      return 'update_convention';
    } else if (issue.type === 'missing_symbol') {
      return 'update_symbol_index';
    } else {
      return 'manual_review';
    }
  }

  estimateResolutionEffort(plan) {
    const effortMap = {
      'update_convention': 15,
      'update_symbol_index': 10,
      'manual_review': 30
    };

    return plan.reduce((total, step) => {
      return total + (effortMap[step.action] || 20);
    }, 0);
  }

  /**
   * Get reasoning summary
   */
  getReasoningSummary() {
    return {
      total_thoughts: this.thoughtLog.length,
      stages_covered: [...new Set(this.thoughtLog.map(t => t.context.stage))],
      recent_thoughts: this.thoughtLog.slice(-5),
      current_context: this.currentContext
    };
  }

  /**
   * Clear thought log
   */
  clearThoughts() {
    this.thoughtLog = [];
    this.currentContext = null;
  }

  /**
   * ENHANCED CORE FILE REASONING METHODS
   */

  assessDecisionQuality(decisions) {
    const issues = [];

    for (const decision of decisions) {
      if (!decision.rationale || decision.rationale === 'Not specified') {
        issues.push(`Decision "${decision.title}" lacks proper rationale`);
      }
      if (!decision.scope || decision.scope.includes('[') || decision.scope.includes('be decided')) {
        issues.push(`Decision "${decision.title}" has undefined scope`);
      }
      if (!decision.standard || decision.standard.includes('[') || decision.standard.includes('be decided')) {
        issues.push(`Decision "${decision.title}" has undefined standard`);
      }
    }

    return issues;
  }

  calculateQualityScore(decisions) {
    if (decisions.length === 0) return 0;

    let totalScore = 0;
    for (const decision of decisions) {
      let score = 100;

      // Deduct points for missing or template content
      if (!decision.rationale || decision.rationale === 'Not specified') score -= 25;
      if (!decision.scope || decision.scope.includes('[')) score -= 25;
      if (!decision.standard || decision.standard.includes('[')) score -= 25;
      if (!decision.title || decision.title.includes('[')) score -= 25;

      totalScore += score;
    }

    return Math.round(totalScore / decisions.length);
  }

  enhanceQuestionsForConventions(questions, context) {
    const enhanced = [...questions];

    // Add core file specific questions
    enhanced.push('How should this decision be documented for future team reference?');
    enhanced.push('What examples or code snippets would help explain this standard?');
    enhanced.push('Are there any migration steps needed for existing code?');
    enhanced.push('What related decisions should be cross-referenced?');

    // Add context-specific enhancements
    if (context.scope === 'enterprise' || context.scale === 'enterprise') {
      enhanced.push('What compliance or audit requirements does this decision address?');
      enhanced.push('How does this align with enterprise architecture standards?');
    }

    if (context.team_size && context.team_size > 5) {
      enhanced.push('How will this decision be communicated to all team members?');
      enhanced.push('What training or documentation is needed for adoption?');
    }

    return enhanced;
  }

  calculateUpdatePriority(impact) {
    let priority = 'medium';

    if (impact.architectural_changes > 2) priority = 'high';
    if (impact.new_patterns > 1) priority = 'high';
    if (impact.complexity_increase > 10) priority = 'high';

    if (impact.architectural_changes === 0 && impact.new_patterns === 0) priority = 'low';

    return priority;
  }

  assessStructureImprovements(newFunctions, newConnections) {
    const improvements = [];

    // Check for new architectural layers
    const layers = new Set();
    newFunctions.forEach(func => {
      if (func.file) {
        const path = func.file.split('/');
        if (path.length > 2) layers.add(path[1]); // e.g., 'services', 'components'
      }
    });

    if (layers.size > 1) {
      improvements.push('Multi-layer architecture detection - enhances symbol-index structure');
    }

    // Check for service patterns
    const serviceConnections = newConnections.filter(conn =>
      conn.type && conn.type.toLowerCase().includes('service')
    );
    if (serviceConnections.length > 0) {
      improvements.push('Service pattern emergence - creates new symbol-index section opportunity');
    }

    // Check for data flow patterns
    const dataFlows = newConnections.filter(conn =>
      conn.purpose && conn.purpose.toLowerCase().includes('data')
    );
    if (dataFlows.length > 2) {
      improvements.push('Data flow pattern detection - suggests symbol-index data section');
    }

    return improvements;
  }

  calculateSymbolIndexQuality(newFunctions, newConnections) {
    let qualityScore = 80; // Base score

    // Quality indicators
    const hasGoodDocumentation = newFunctions.every(func =>
      func.purpose && func.purpose.length > 10 && !func.purpose.includes('[')
    );
    if (hasGoodDocumentation) qualityScore += 10;

    const hasFilePaths = newFunctions.every(func => func.file && func.file.includes('/'));
    if (hasFilePaths) qualityScore += 5;

    const hasConnectionPurposes = newConnections.every(conn =>
      conn.purpose && conn.purpose.length > 5
    );
    if (hasConnectionPurposes) qualityScore += 5;

    // Complexity bonus - more complex additions are typically more valuable
    if (newFunctions.length + newConnections.length > 5) qualityScore += 5;

    return Math.min(qualityScore, 100);
  }
}

module.exports = ThinkTool;