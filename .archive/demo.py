#!/usr/bin/env python3
"""
AI DevOps Framework Demo

Demonstrates the framework's development orchestration capabilities with specialized agents.
Run: python demo.py --example full_stack_development
"""

import argparse
import json
import logging
from pathlib import Path
from src.orchestrator import MetaOrchestrator, OrchestrationPattern

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def demo_full_stack_development():
    """Demonstrate full-stack feature development orchestration."""
    print("\nDemo: Full-Stack Feature Development Orchestration")
    print("=" * 60)
    
    orchestrator = MetaOrchestrator()
    
    # List available agents
    agents = orchestrator.list_agents()
    print(f"Available agents: {', '.join(agents)}")
    
    # Full-stack development request
    request = {
        "objective": "Build user authentication system with JWT tokens and role-based access",
        "agents": ["backend_agent", "frontend_agent", "security_agent"],
        "pattern": "consultation_then_production",
        "quality_threshold": 90,
        "context": {
            "technical_requirements": {
                "backend": "Node.js with Express and PostgreSQL",
                "frontend": "React with TypeScript",
                "authentication": "JWT tokens with refresh mechanism",
                "authorization": "Role-based access control (RBAC)"
            },
            "security_constraints": {
                "compliance": ["OWASP Top 10", "Password security standards"],
                "data_protection": "Encrypted password storage with bcrypt",
                "session_management": "Secure token expiry and rotation"
            },
            "performance_targets": {
                "response_time": "< 200ms for auth endpoints",
                "security": "No vulnerabilities in OWASP scan",
                "test_coverage": "> 85%"
            }
        }
    }
    
    # Execute orchestration
    print(f"\nExecuting orchestration...")
    result = orchestrator.coordinate(request)
    
    # Display results
    print(f"\nResults:")
    print(f"Status: {result.status.value}")
    print(f"Quality Score: {result.quality_metrics.overall:.1f}/100")
    print(f"Execution Time: {result.execution_time:.2f}s")
    agents_used = result.metadata.get('agents_used', ['Unknown'])
    print(f"Agents Used: {', '.join(agents_used)}")
    print(f"Conflicts Resolved: {result.conflicts_resolved}")
    
    if result.deliverable and 'response' in result.deliverable:
        response = result.deliverable['response']
        if 'deliverable' in response:
            print(f"\nPrimary Output:")
            print(f"  {response['deliverable']['primary_output']}")
            
            if 'analysis' in response['deliverable']:
                print(f"\nAnalysis:")
                print(f"  {response['deliverable']['analysis']}")
                
            if 'recommendations' in response['deliverable']:
                print(f"\nRecommendations:")
                for i, rec in enumerate(response['deliverable']['recommendations'], 1):
                    print(f"  {i}. {rec}")
    
    print(f"\nQuality Breakdown:")
    metrics = result.quality_metrics
    print(f"  Consistency: {metrics.consistency:.1f}%")
    print(f"  Completeness: {metrics.completeness:.1f}%") 
    print(f"  Methodology: {metrics.methodology_adherence:.1f}%")
    print(f"  Confidence: {metrics.confidence:.1f}%")


def demo_secure_api_development():
    """Demonstrate secure API development orchestration."""
    print("\nDemo: Secure API Development Orchestration")
    print("=" * 55)
    
    orchestrator = MetaOrchestrator()
    
    request = {
        "objective": "Build secure payment processing API with comprehensive security testing",
        "agents": ["backend_agent", "security_agent", "pentesting_agent"],
        "pattern": "hierarchical_validation", 
        "quality_threshold": 95,
        "context": {
            "technical_environment": {
                "primary_language": "Python",
                "frameworks": ["FastAPI", "SQLAlchemy", "Redis"],
                "deployment": "Kubernetes with auto-scaling"
            },
            "requirements": {
                "performance": {"response_time": "<50ms", "throughput": "1000 req/s"},
                "security": ["JWT authentication", "Rate limiting", "GDPR compliance"]
            }
        }
    }
    
    result = orchestrator.coordinate(request)
    
    print(f"Development Results:")
    print(f"Status: {result.status.value}")
    print(f"Quality Score: {result.quality_metrics.overall:.1f}/100")
    print(f"Architecture Confidence: {result.quality_metrics.confidence:.1f}%")
    
    if result.status.value == 'success':
        print("Production-ready implementation generated with comprehensive testing")
    else:
        print("Implementation requires review before production deployment")


def demo_code_review_pipeline():
    """Demonstrate code review orchestration with multiple domain experts."""
    print("\nDemo: Multi-Agent Code Review Pipeline")
    print("=" * 50)
    
    orchestrator = MetaOrchestrator()
    
    request = {
        "objective": "Review pull request: Payment processing endpoint with security validation",
        "agents": ["security_agent", "backend_agent", "frontend_agent"],
        "pattern": "consensus_validation",
        "quality_threshold": 90,
        "context": {
            "code_review": {
                "pr_description": "Add Stripe payment processing with JWT auth", 
                "files_changed": ["payment_service.py", "auth_middleware.js", "payment_form.tsx"],
                "complexity": "High - handles sensitive payment data"
            },
            "validation_criteria": {
                "security": ["OWASP compliance", "PCI DSS standards", "Input validation"],
                "performance": ["Response time < 500ms", "Database query optimization"],
                "maintainability": ["Code clarity", "Error handling", "Test coverage > 80%"]
            }
        }
    }
    
    result = orchestrator.coordinate(request)
    
    print(f"Code Review Results:")
    print(f"Status: {result.status.value}")
    print(f"Overall Quality Score: {result.quality_metrics.overall:.1f}/100") 
    print(f"Security Score: {result.security_metrics.overall:.1f}/100")
    print(f"Agent Consensus: {result.quality_metrics.consistency:.1f}%")
    
    if result.quality_metrics.overall >= 90:
        print("✅ Pull request approved - meets production quality standards")
    else:
        print("❌ Pull request requires changes before approval")


def demo_development_overview():
    """Show development orchestration framework capabilities overview."""
    print("\nAI DevOps Framework - Development Orchestration Overview") 
    print("=" * 65)
    
    orchestrator = MetaOrchestrator()
    agents = orchestrator.list_agents()
    
    print(f"Available Development Agents: {len(agents)}")
    for agent in agents:
        print(f"  - {agent}")
    
    print(f"\nDevelopment Orchestration Patterns:")
    for pattern in OrchestrationPattern:
        print(f"  - {pattern.value}: {_get_pattern_description(pattern)}")
    
    print(f"\nKey Development Features:")
    features = [
        "Systematic code quality validation with measurable metrics",
        "Multi-agent conflict resolution for technical decisions",
        "Production-ready orchestration patterns",
        "Comprehensive agent persona and methodology frameworks",
        "Extensible architecture for custom agent development"
    ]
    for feature in features:
        print(f"  - {feature}")
    
    print(f"\nThis demonstrates systematic AI development beyond 'vibecoding'")


def _get_pattern_description(pattern: OrchestrationPattern) -> str:
    """Get description for orchestration pattern."""
    descriptions = {
        OrchestrationPattern.SEQUENTIAL: "Step-by-step agent execution with validation",
        OrchestrationPattern.MAPREDUCE: "Parallel processing with result aggregation", 
        OrchestrationPattern.CONSENSUS: "Multi-agent agreement with conflict resolution",
        OrchestrationPattern.HIERARCHICAL: "Complex task decomposition and coordination"
    }
    return descriptions.get(pattern, "Advanced orchestration pattern")


def main():
    """Run framework demonstrations."""
    parser = argparse.ArgumentParser(description="AI DevOps Framework Demo")
    parser.add_argument(
        "--example", 
        choices=["full_stack_development", "secure_api_development", "code_review_pipeline", "development_overview"],
        default="development_overview",
        help="Development workflow demo to run"
    )
    
    args = parser.parse_args()
    
    print("AI DevOps Framework - Production-Ready AI Orchestration")
    print("From 'Vibecoding' to Systematic Engineering")
    print("https://github.com/PeterSalvato/AI-Devops-Framework")
    
    if args.example == "full_stack_development":
        demo_full_stack_development()
    elif args.example == "secure_api_development":
        demo_secure_api_development()
    elif args.example == "code_review_pipeline":
        demo_code_review_pipeline()
    else:
        demo_development_overview()
    
    print(f"\nLearn More:")
    print(f"  Agent Development Guide: docs/agent-development-guide.md")
    print(f"  Why NOT Vibecoding: docs/why-not-vibecoding.md") 
    print(f"  System Architecture: docs/conventions.md")
    print(f"  Component Mapping: docs/symbol-index.md")
    
    print(f"\nNeed production implementation? Open an issue or discussion on GitHub")


if __name__ == "__main__":
    main()