"""
Test configuration and fixtures for AI DevOps Framework tests.
"""

import json
import pytest
from pathlib import Path
from typing import Dict, Any
from src.orchestrator import MetaOrchestrator, QualityMetrics, ExecutionStatus


@pytest.fixture
def sample_agent_config():
    """Sample agent configuration for testing."""
    return {
        "agent_identity": {
            "name": "test-agent",
            "type": "consultant",
            "expertise": "Test automation and quality assurance",
            "version": "1.0.0",
            "persona": {
                "personality": "Systematic and detail-oriented",
                "communication_style": "Clear and precise",
                "approach": "Test-first development methodology",
                "values": ["Quality", "Reliability", "Automation"]
            }
        },
        "capabilities": {
            "primary": ["Test planning", "Quality validation", "Process automation"],
            "secondary": ["Documentation", "Training", "Tool integration"],
            "specialized": ["Performance testing", "Security validation"]
        },
        "methodology": {
            "framework": "Test-Driven Quality Assurance",
            "process": [
                {
                    "phase": "Analysis",
                    "activities": ["Requirement analysis", "Test planning"]
                },
                {
                    "phase": "Execution", 
                    "activities": ["Test implementation", "Quality validation"]
                }
            ]
        },
        "input_schema": {
            "objective": "string",
            "context": "object",
            "constraints": "object"
        },
        "output_schema": {
            "response": {
                "status": "string",
                "deliverable": "object",
                "quality_assessment": "object",
                "metadata": "object"
            }
        }
    }


@pytest.fixture
def sample_orchestration_request():
    """Sample orchestration request for testing."""
    return {
        "objective": "Test framework orchestration capabilities",
        "agents": ["test_agent"],
        "pattern": "sequential",
        "quality_threshold": 85.0,
        "context": {
            "test_environment": "pytest",
            "validation_required": True
        }
    }


@pytest.fixture
def temp_agents_dir(tmp_path):
    """Temporary agents directory with test agent."""
    agents_dir = tmp_path / "agents"
    examples_dir = agents_dir / "examples"
    examples_dir.mkdir(parents=True)
    
    # Create test agent file
    test_agent = {
        "agent_identity": {
            "name": "test-agent",
            "type": "consultant",
            "expertise": "Test automation"
        },
        "capabilities": {
            "primary": ["Testing", "Validation"],
            "secondary": ["Documentation"],
            "specialized": ["Automation"]
        },
        "methodology": {
            "framework": "Test Framework",
            "process": []
        },
        "input_schema": {"objective": "string"},
        "output_schema": {"response": {"status": "string"}}
    }
    
    with open(examples_dir / "test_agent.json", "w") as f:
        json.dump(test_agent, f, indent=2)
    
    return agents_dir


@pytest.fixture
def quality_metrics():
    """Sample quality metrics for testing."""
    return QualityMetrics(
        overall=85.5,
        consistency=90.0,
        completeness=82.0,
        methodology_adherence=88.0,
        confidence=85.0
    )


@pytest.fixture
def orchestrator(temp_agents_dir):
    """MetaOrchestrator instance with test configuration."""
    return MetaOrchestrator(agents_dir=temp_agents_dir)