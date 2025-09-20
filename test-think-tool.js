#!/usr/bin/env node

/**
 * Test Script for Think Tool Integration
 *
 * Tests complex decision scenarios to validate structured reasoning
 */

const InstitutionalMemoryEnforcer = require('./institutional-memory-enforcer.js');

async function testComplexScenarios() {
  const enforcer = new InstitutionalMemoryEnforcer();

  console.log('🧪 Testing Think Tool with Complex Scenarios\n');

  // Test 1: Authentication decision with conflicts
  console.log('=== Test 1: Authentication Decision with Potential Conflicts ===');

  // Simulate existing conflicting decisions
  const mockConflictingDecisions = [
    {
      title: 'API Authentication',
      standard: 'JWT tokens',
      scope: 'Backend API',
      date: '2024-01-15'
    },
    {
      title: 'Web Authentication',
      standard: 'Session cookies',
      scope: 'Frontend web app',
      date: '2024-02-10'
    }
  ];

  try {
    // This should trigger conflict analysis
    const result1 = await enforcer.checkForExistingDecision('authentication', {
      scope: 'Full-stack application',
      requirements: ['security', 'scalability']
    });

    console.log('Result:', JSON.stringify(result1, null, 2));
    console.log('Reasoning Summary:', enforcer.thinkTool.getReasoningSummary());
  } catch (error) {
    console.log('Expected - checking non-existent decisions');
  }

  console.log('\n=== Test 2: Symbol Index Update with Pattern Detection ===');

  // Test 2: Complex development results
  const complexDevelopmentResults = {
    newFunctions: [
      {
        name: 'authenticateUser',
        file: 'src/auth/auth-service.js',
        purpose: 'Validates user credentials using JWT',
        dependencies: ['jsonwebtoken', 'bcrypt']
      },
      {
        name: 'authorizeRequest',
        file: 'src/auth/auth-middleware.js',
        purpose: 'Middleware for request authorization',
        dependencies: ['auth-service']
      },
      {
        name: 'refreshToken',
        file: 'src/auth/token-service.js',
        purpose: 'Refreshes expired JWT tokens',
        dependencies: ['jsonwebtoken']
      }
    ],
    newConnections: [
      {
        from: 'LoginForm',
        to: 'AuthService',
        type: 'service_call',
        purpose: 'User login authentication'
      },
      {
        from: 'API Gateway',
        to: 'AuthMiddleware',
        type: 'service_call',
        purpose: 'Request authorization check'
      },
      {
        from: 'TokenService',
        to: 'AuthService',
        type: 'service_call',
        purpose: 'Token refresh validation'
      }
    ],
    context: {
      feature: 'authentication_system',
      complexity: 'high',
      architectural_impact: 'major'
    }
  };

  const updateResult = await enforcer.updateSymbolIndexAfterDevelopment(complexDevelopmentResults);
  console.log('Update Result:', JSON.stringify(updateResult, null, 2));

  console.log('\n=== Test 3: Drift Detection with Multiple Issues ===');

  // Test 3: Drift detection with complex issues
  const mockDriftIssues = [
    {
      type: 'INVALID_CODE_REFERENCES',
      severity: 'critical',
      count: 5,
      details: ['Missing function: oldAuthFunction', 'Broken import: ./old-module'],
      impact: 10
    },
    {
      type: 'STALE_CONVENTIONS',
      severity: 'warning',
      count: 3,
      details: ['Database choice outdated', 'Frontend framework changed'],
      impact: 3
    },
    {
      type: 'CONVENTION_CONFLICTS',
      severity: 'critical',
      count: 2,
      details: ['Auth method conflict', 'API versioning conflict'],
      impact: 6
    }
  ];

  // Simulate drift analysis
  const driftReport = { driftDetected: true, issues: mockDriftIssues };
  const driftReasoning = enforcer.thinkTool.reasonAboutDrift(driftReport);

  console.log('Drift Reasoning:', JSON.stringify(driftReasoning, null, 2));

  console.log('\n=== Test 4: Decision Generation for Missing Convention ===');

  // Test 4: Generate questions for missing decisions
  const questions = enforcer.thinkTool.generateContextualQuestions('database', {
    scale: 'enterprise',
    performance: 'high',
    compliance: 'required'
  });

  console.log('Generated Questions:', questions);

  console.log('\n=== Final Reasoning Summary ===');
  const finalSummary = enforcer.thinkTool.getReasoningSummary();
  console.log(JSON.stringify(finalSummary, null, 2));

  console.log('\n✅ Think Tool Testing Complete');
}

// Run tests
testComplexScenarios().catch(console.error);