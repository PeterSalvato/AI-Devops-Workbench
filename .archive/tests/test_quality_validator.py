"""
Tests for the QualityValidator class.
"""

import pytest
from src.orchestrator import QualityValidator, QualityMetrics


class TestQualityValidator:
    """Test cases for QualityValidator."""

    def test_initialization_default_thresholds(self):
        """Test QualityValidator initialization with default thresholds."""
        validator = QualityValidator()
        
        expected_thresholds = {
            'overall': 85.0,
            'consistency': 90.0,
            'completeness': 85.0,
            'methodology_adherence': 85.0,
            'confidence': 80.0
        }
        
        assert validator.thresholds == expected_thresholds

    def test_initialization_custom_thresholds(self):
        """Test QualityValidator initialization with custom thresholds."""
        custom_thresholds = {
            'overall': 90.0,
            'consistency': 95.0,
            'completeness': 88.0
        }
        
        validator = QualityValidator(custom_thresholds)
        
        # Should use custom values where provided, defaults for others
        assert validator.thresholds['overall'] == 90.0
        assert validator.thresholds['consistency'] == 95.0
        assert validator.thresholds['completeness'] == 88.0
        # Should still have defaults for non-specified thresholds

    def test_validate_output_basic(self, sample_agent_config):
        """Test basic output validation."""
        validator = QualityValidator()
        
        sample_output = {
            "response": {
                "status": "success",
                "deliverable": {
                    "primary_output": "Test analysis complete",
                    "analysis": "Comprehensive testing performed"
                },
                "quality_assessment": {
                    "methodology_validation": "confirmed"
                },
                "metadata": {
                    "methodology_applied": "Test Framework",
                    "implementation_confidence": 85
                }
            }
        }
        
        metrics = validator.validate_output(sample_output, sample_agent_config)
        
        assert isinstance(metrics, QualityMetrics)
        assert isinstance(metrics.overall, float)
        assert isinstance(metrics.consistency, float)
        assert isinstance(metrics.completeness, float)
        assert isinstance(metrics.methodology_adherence, float)
        assert isinstance(metrics.confidence, float)
        
        # All scores should be between 0 and 100
        assert 0 <= metrics.overall <= 100
        assert 0 <= metrics.consistency <= 100
        assert 0 <= metrics.completeness <= 100
        assert 0 <= metrics.methodology_adherence <= 100
        assert 0 <= metrics.confidence <= 100

    def test_validate_consistency(self, sample_agent_config):
        """Test consistency validation logic."""
        validator = QualityValidator()
        
        # Test output with response and deliverable (should score well)
        good_output = {
            "response": {
                "deliverable": {"content": "test"}
            }
        }
        
        score = validator._validate_consistency(good_output, sample_agent_config)
        assert score == 92.0  # Expected demo score for good structure
        
        # Test output without proper structure (should score poorly)
        bad_output = {"invalid": "structure"}
        
        score = validator._validate_consistency(bad_output, sample_agent_config)
        assert score == 60.0  # Expected demo score for bad structure

    def test_validate_completeness(self, sample_agent_config):
        """Test completeness validation logic."""
        validator = QualityValidator()
        
        # Mock agent config with expected output schema
        agent_config = {
            "output_schema": {
                "response": {
                    "status": "string",
                    "deliverable": "object"
                }
            }
        }
        
        # Test complete output
        complete_output = {
            "response": {
                "status": "success",
                "deliverable": {"content": "test"}
            }
        }
        
        score = validator._validate_completeness(complete_output, agent_config)
        assert score == 95.0  # Expected score for complete output
        
        # Test incomplete output
        incomplete_output = {
            "response": {
                "status": "success"
                # Missing deliverable
            }
        }
        
        score = validator._validate_completeness(incomplete_output, agent_config)
        assert score == 70.0  # Expected score for incomplete output

    def test_validate_methodology(self, sample_agent_config):
        """Test methodology validation logic."""
        validator = QualityValidator()
        
        # Test output with methodology metadata
        good_output = {
            "response": {
                "metadata": {
                    "methodology_applied": "Test Framework"
                }
            }
        }
        
        score = validator._validate_methodology(good_output, sample_agent_config)
        assert score == 88.0  # Expected score for methodology presence
        
        # Test output without methodology metadata
        bad_output = {
            "response": {
                "metadata": {}
            }
        }
        
        score = validator._validate_methodology(bad_output, sample_agent_config)
        assert score == 65.0  # Expected score for missing methodology

    def test_extract_confidence(self):
        """Test confidence extraction logic."""
        validator = QualityValidator()
        
        # Test output with confidence score
        output_with_confidence = {
            "response": {
                "metadata": {
                    "implementation_confidence": 90
                }
            }
        }
        
        confidence = validator._extract_confidence(output_with_confidence)
        assert confidence == 90.0
        
        # Test output without confidence score
        output_without_confidence = {
            "response": {
                "metadata": {}
            }
        }
        
        confidence = validator._extract_confidence(output_without_confidence)
        assert confidence == 75.0  # Expected default confidence

    def test_validate_output_edge_cases(self, sample_agent_config):
        """Test output validation with edge cases."""
        validator = QualityValidator()
        
        # Test empty output
        empty_output = {}
        metrics = validator.validate_output(empty_output, sample_agent_config)
        
        assert isinstance(metrics, QualityMetrics)
        assert metrics.overall > 0  # Should still return some score
        
        # Test None output (should handle gracefully)
        none_output = None
        try:
            metrics = validator.validate_output(none_output, sample_agent_config)
            # Should either work or raise a clear exception
            assert isinstance(metrics, QualityMetrics)
        except (TypeError, AttributeError):
            # Expected behavior for None input
            pass

    def test_quality_metrics_calculation(self, sample_agent_config):
        """Test that quality metrics are calculated correctly."""
        validator = QualityValidator()
        
        # Create predictable output
        test_output = {
            "response": {
                "deliverable": {"content": "test"},  # Good consistency
                "metadata": {
                    "methodology_applied": "framework",  # Good methodology
                    "implementation_confidence": 80  # Explicit confidence
                }
            }
        }
        
        # Mock the agent config to have predictable output schema
        mock_config = {
            "output_schema": {
                "response": {
                    "deliverable": "object"
                }
            }
        }
        
        metrics = validator.validate_output(test_output, mock_config)
        
        # Verify calculation: (consistency + completeness + methodology + confidence) / 4
        expected_overall = (92.0 + 95.0 + 88.0 + 80.0) / 4.0
        assert abs(metrics.overall - expected_overall) < 0.1  # Allow for small float differences
        
        assert metrics.consistency == 92.0
        assert metrics.completeness == 95.0
        assert metrics.methodology_adherence == 88.0
        assert metrics.confidence == 80.0

    def test_threshold_comparison(self):
        """Test quality threshold comparison functionality."""
        # Create metrics with known values
        metrics = QualityMetrics(
            overall=87.5,
            consistency=90.0,
            completeness=85.0,
            methodology_adherence=88.0,
            confidence=85.0
        )
        
        # Test various thresholds
        assert metrics.passes_threshold(85.0)  # 87.5 > 85.0
        assert metrics.passes_threshold(87.5)  # 87.5 == 87.5
        assert not metrics.passes_threshold(90.0)  # 87.5 < 90.0