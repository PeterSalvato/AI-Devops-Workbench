"""
Tests for the MetaOrchestrator class and related functionality.
"""

import pytest
import time
from unittest.mock import patch, MagicMock
from src.orchestrator import (
    MetaOrchestrator, 
    OrchestrationPattern, 
    ExecutionStatus,
    QualityMetrics,
    OrchestrationResult
)


class TestMetaOrchestrator:
    """Test cases for MetaOrchestrator."""

    def test_initialization(self, temp_agents_dir):
        """Test orchestrator initialization."""
        orchestrator = MetaOrchestrator(agents_dir=temp_agents_dir)
        
        assert orchestrator.agent_loader is not None
        assert orchestrator.quality_validator is not None
        assert orchestrator.conflict_resolver is not None
        assert orchestrator.logger is not None

    def test_list_agents(self, orchestrator):
        """Test listing available agents."""
        agents = orchestrator.list_agents()
        
        assert isinstance(agents, list)
        assert "test_agent" in agents

    def test_coordinate_basic_request(self, orchestrator, sample_orchestration_request):
        """Test basic orchestration coordination."""
        result = orchestrator.coordinate(sample_orchestration_request)
        
        assert isinstance(result, OrchestrationResult)
        assert isinstance(result.status, ExecutionStatus)
        assert isinstance(result.quality_metrics, QualityMetrics)
        assert isinstance(result.execution_time, float)
        assert result.execution_time > 0

    def test_coordinate_with_invalid_agents(self, orchestrator):
        """Test coordination with non-existent agents."""
        request = {
            "objective": "Test with invalid agents",
            "agents": ["nonexistent_agent"],
            "pattern": "sequential"
        }
        
        result = orchestrator.coordinate(request)
        
        assert result.status == ExecutionStatus.FAILED
        assert "error" in result.deliverable

    def test_coordinate_multiple_agents(self, orchestrator):
        """Test coordination with multiple agents."""
        request = {
            "objective": "Multi-agent test",
            "agents": ["test_agent", "test_agent"],  # Use same agent twice for testing
            "pattern": "sequential",
            "quality_threshold": 80.0
        }
        
        result = orchestrator.coordinate(request)
        
        assert isinstance(result, OrchestrationResult)
        assert len(result.agent_outputs) <= 2  # Should have outputs from agents
        assert result.conflicts_resolved >= 0

    def test_orchestration_patterns(self, orchestrator, sample_orchestration_request):
        """Test different orchestration patterns."""
        patterns = [
            OrchestrationPattern.SEQUENTIAL,
            OrchestrationPattern.MAPREDUCE,
            OrchestrationPattern.CONSENSUS,
            OrchestrationPattern.HIERARCHICAL
        ]
        
        for pattern in patterns:
            request = sample_orchestration_request.copy()
            request["pattern"] = pattern.value
            
            result = orchestrator.coordinate(request)
            
            assert isinstance(result, OrchestrationResult)
            assert result.metadata["pattern"] == pattern.value

    def test_quality_threshold_validation(self, orchestrator, sample_orchestration_request):
        """Test quality threshold handling."""
        # Test with high threshold
        request = sample_orchestration_request.copy()
        request["quality_threshold"] = 95.0
        
        result = orchestrator.coordinate(request)
        
        assert isinstance(result, OrchestrationResult)
        # Result might be partial or failed due to high threshold
        assert result.status in [ExecutionStatus.SUCCESS, ExecutionStatus.PARTIAL, ExecutionStatus.FAILED]

    def test_error_handling(self, orchestrator):
        """Test error handling in orchestration."""
        # Test with malformed request
        malformed_request = {
            "invalid_field": "test"
        }
        
        result = orchestrator.coordinate(malformed_request)
        
        assert result.status == ExecutionStatus.FAILED
        assert "error" in result.metadata or "error" in result.deliverable

    def test_execution_metadata(self, orchestrator, sample_orchestration_request):
        """Test that execution metadata is properly recorded."""
        result = orchestrator.coordinate(sample_orchestration_request)
        
        assert "objective" in result.metadata
        assert "agents_used" in result.metadata
        assert "pattern" in result.metadata
        assert "quality_threshold" in result.metadata
        
        assert result.metadata["objective"] == sample_orchestration_request["objective"]

    @patch('time.time')
    def test_execution_timing(self, mock_time, orchestrator, sample_orchestration_request):
        """Test execution timing measurement."""
        # Mock time to return predictable values
        mock_time.side_effect = [1000.0, 1001.5]  # 1.5 second execution
        
        result = orchestrator.coordinate(sample_orchestration_request)
        
        assert result.execution_time == 1.5

    def test_coordinate_with_context(self, orchestrator):
        """Test coordination with rich context."""
        request = {
            "objective": "Context-aware test",
            "agents": ["test_agent"],
            "pattern": "sequential",
            "context": {
                "business_context": {"industry": "technology"},
                "technical_context": {"platform": "python"},
                "stakeholder_context": {"primary_user": "developers"}
            }
        }
        
        result = orchestrator.coordinate(request)
        
        assert isinstance(result, OrchestrationResult)
        assert result.status in [ExecutionStatus.SUCCESS, ExecutionStatus.PARTIAL]


class TestQualityMetrics:
    """Test cases for QualityMetrics."""

    def test_quality_metrics_creation(self, quality_metrics):
        """Test QualityMetrics initialization."""
        assert quality_metrics.overall == 85.5
        assert quality_metrics.consistency == 90.0
        assert quality_metrics.completeness == 82.0
        assert quality_metrics.methodology_adherence == 88.0
        assert quality_metrics.confidence == 85.0

    def test_passes_threshold_default(self, quality_metrics):
        """Test passes_threshold with default threshold."""
        assert quality_metrics.passes_threshold()  # 85.5 >= 85.0

    def test_passes_threshold_custom(self, quality_metrics):
        """Test passes_threshold with custom threshold."""
        assert quality_metrics.passes_threshold(80.0)  # 85.5 >= 80.0
        assert not quality_metrics.passes_threshold(90.0)  # 85.5 < 90.0

    def test_passes_threshold_edge_cases(self):
        """Test passes_threshold edge cases."""
        metrics = QualityMetrics(85.0, 85.0, 85.0, 85.0, 85.0)
        assert metrics.passes_threshold(85.0)  # Exactly equal
        assert not metrics.passes_threshold(85.1)  # Just above


class TestOrchestrationResult:
    """Test cases for OrchestrationResult."""

    def test_orchestration_result_structure(self, quality_metrics):
        """Test OrchestrationResult structure."""
        result = OrchestrationResult(
            status=ExecutionStatus.SUCCESS,
            deliverable={"output": "test"},
            quality_metrics=quality_metrics,
            agent_outputs=[{"agent": "test"}],
            conflicts_resolved=1,
            execution_time=1.23,
            metadata={"test": "metadata"}
        )
        
        assert result.status == ExecutionStatus.SUCCESS
        assert result.deliverable == {"output": "test"}
        assert result.quality_metrics == quality_metrics
        assert result.agent_outputs == [{"agent": "test"}]
        assert result.conflicts_resolved == 1
        assert result.execution_time == 1.23
        assert result.metadata == {"test": "metadata"}