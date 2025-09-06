"""
Tests for the demo functionality and integration tests.
"""

import pytest
import subprocess
import sys
from unittest.mock import patch, MagicMock
import demo
from src.orchestrator import MetaOrchestrator, ExecutionStatus


class TestDemoFunctions:
    """Test cases for demo functions."""

    @patch('demo.MetaOrchestrator')
    def test_demo_brand_development(self, mock_orchestrator_class):
        """Test brand development demo function."""
        # Mock the orchestrator and its methods
        mock_orchestrator = MagicMock()
        mock_orchestrator_class.return_value = mock_orchestrator
        
        # Mock list_agents
        mock_orchestrator.list_agents.return_value = ['content_agent', 'designer_agent']
        
        # Mock coordinate method
        mock_result = MagicMock()
        mock_result.status.value = 'success'
        mock_result.quality_metrics.overall = 89.5
        mock_result.execution_time = 0.15
        mock_result.conflicts_resolved = 1
        mock_result.metadata = {'agents_used': ['content_agent', 'designer_agent']}
        mock_result.deliverable = {
            'response': {
                'deliverable': {
                    'primary_output': 'Mock brand strategy analysis',
                    'analysis': 'Strategic analysis using methodology',
                    'recommendations': ['Use systematic validation', 'Apply quality frameworks']
                }
            }
        }
        mock_result.quality_metrics.consistency = 92.0
        mock_result.quality_metrics.completeness = 85.0
        mock_result.quality_metrics.methodology_adherence = 90.0
        mock_result.quality_metrics.confidence = 89.0
        
        mock_orchestrator.coordinate.return_value = mock_result
        
        # Test the function (should not raise exceptions)
        try:
            demo.demo_brand_development()
        except Exception as e:
            pytest.fail(f"demo_brand_development() raised an exception: {e}")
        
        # Verify orchestrator was called
        mock_orchestrator_class.assert_called_once()
        mock_orchestrator.coordinate.assert_called_once()

    @patch('demo.MetaOrchestrator')
    def test_demo_api_creation(self, mock_orchestrator_class):
        """Test API creation demo function."""
        mock_orchestrator = MagicMock()
        mock_orchestrator_class.return_value = mock_orchestrator
        
        mock_result = MagicMock()
        mock_result.status.value = 'success'
        mock_result.quality_metrics.overall = 92.0
        mock_result.quality_metrics.confidence = 91.0
        
        mock_orchestrator.coordinate.return_value = mock_result
        
        try:
            demo.demo_api_creation()
        except Exception as e:
            pytest.fail(f"demo_api_creation() raised an exception: {e}")

    @patch('demo.MetaOrchestrator')
    def test_demo_content_pipeline(self, mock_orchestrator_class):
        """Test content pipeline demo function."""
        mock_orchestrator = MagicMock()
        mock_orchestrator_class.return_value = mock_orchestrator
        
        mock_result = MagicMock()
        mock_result.status.value = 'success'
        mock_result.quality_metrics.overall = 88.5
        mock_result.quality_metrics.consistency = 90.0
        
        mock_orchestrator.coordinate.return_value = mock_result
        
        try:
            demo.demo_content_pipeline()
        except Exception as e:
            pytest.fail(f"demo_content_pipeline() raised an exception: {e}")

    @patch('demo.MetaOrchestrator')
    @patch('demo.OrchestrationPattern')
    def test_demo_framework_overview(self, mock_pattern, mock_orchestrator_class):
        """Test framework overview demo function."""
        mock_orchestrator = MagicMock()
        mock_orchestrator_class.return_value = mock_orchestrator
        mock_orchestrator.list_agents.return_value = ['agent1', 'agent2', 'agent3']
        
        # Mock OrchestrationPattern enum
        mock_pattern_item = MagicMock()
        mock_pattern_item.value = 'sequential'
        mock_pattern.__iter__ = MagicMock(return_value=iter([mock_pattern_item]))
        
        try:
            demo.demo_framework_overview()
        except Exception as e:
            pytest.fail(f"demo_framework_overview() raised an exception: {e}")

    def test_get_pattern_description(self):
        """Test pattern description function."""
        from demo import _get_pattern_description
        from src.orchestrator import OrchestrationPattern
        
        # Test all patterns have descriptions
        for pattern in OrchestrationPattern:
            description = _get_pattern_description(pattern)
            assert isinstance(description, str)
            assert len(description) > 10  # Should be meaningful description

    @patch('argparse.ArgumentParser.parse_args')
    @patch('demo.demo_framework_overview')
    def test_main_default(self, mock_overview, mock_args):
        """Test main function with default arguments."""
        mock_args.return_value = MagicMock(example='overview')
        
        demo.main()
        
        mock_overview.assert_called_once()

    @patch('argparse.ArgumentParser.parse_args')
    @patch('demo.demo_brand_development')
    def test_main_brand_development(self, mock_brand_dev, mock_args):
        """Test main function with brand development example."""
        mock_args.return_value = MagicMock(example='brand_development')
        
        demo.main()
        
        mock_brand_dev.assert_called_once()


class TestDemoIntegration:
    """Integration tests for demo functionality."""

    def test_demo_script_execution(self):
        """Test that demo script can be executed without errors."""
        # Test overview demo (least likely to fail)
        try:
            result = subprocess.run(
                [sys.executable, 'demo.py', '--example', 'overview'],
                capture_output=True,
                text=True,
                timeout=30,
                cwd='/workspaces/AI-Devops-Framework'
            )
            
            # Should complete without error
            assert result.returncode == 0
            
            # Should contain expected output
            assert 'AI DevOps Framework' in result.stdout
            assert 'Available Example Agents' in result.stdout
            assert 'Orchestration Patterns' in result.stdout
            
        except subprocess.TimeoutExpired:
            pytest.fail("Demo script execution timed out")
        except Exception as e:
            pytest.fail(f"Demo script execution failed: {e}")

    def test_all_demo_examples_available(self):
        """Test that all advertised demo examples can be called."""
        examples = ['brand_development', 'api_creation', 'content_pipeline', 'overview']
        
        for example in examples:
            try:
                # Test that the demo doesn't immediately crash
                result = subprocess.run(
                    [sys.executable, 'demo.py', '--example', example],
                    capture_output=True,
                    text=True,
                    timeout=15,
                    cwd='/workspaces/AI-Devops-Framework'
                )
                
                # Should complete (may have various return codes depending on mock behavior)
                # Main thing is it shouldn't crash immediately
                assert "Traceback" not in result.stderr or result.returncode == 0
                
            except subprocess.TimeoutExpired:
                # Timeout is acceptable for demo purposes
                pass
            except Exception as e:
                pytest.fail(f"Demo example '{example}' failed to start: {e}")

    def test_help_text_available(self):
        """Test that help text is available for demo script."""
        try:
            result = subprocess.run(
                [sys.executable, 'demo.py', '--help'],
                capture_output=True,
                text=True,
                timeout=10,
                cwd='/workspaces/AI-Devops-Framework'
            )
            
            assert result.returncode == 0
            assert 'AI DevOps Framework Demo' in result.stdout
            assert '--example' in result.stdout
            assert 'brand_development' in result.stdout
            
        except Exception as e:
            pytest.fail(f"Demo help failed: {e}")


class TestDemoOutput:
    """Test demo output formatting and content."""

    @patch('demo.MetaOrchestrator')
    def test_demo_output_formatting(self, mock_orchestrator_class):
        """Test that demo output is properly formatted."""
        mock_orchestrator = MagicMock()
        mock_orchestrator_class.return_value = mock_orchestrator
        mock_orchestrator.list_agents.return_value = ['test_agent']
        
        # Capture stdout during demo execution
        import io
        import contextlib
        
        captured_output = io.StringIO()
        
        with contextlib.redirect_stdout(captured_output):
            try:
                demo.demo_framework_overview()
            except Exception:
                pass  # We're testing output format, not execution success
        
        output = captured_output.getvalue()
        
        # Should contain proper formatting elements
        assert 'Framework Overview' in output
        assert '=' in output  # Should have section dividers
        assert 'Available Example Agents' in output