"""
Tests for the AgentLoader class.
"""

import json
import pytest
from pathlib import Path
from src.orchestrator import AgentLoader


class TestAgentLoader:
    """Test cases for AgentLoader."""

    def test_initialization_default_path(self):
        """Test AgentLoader initialization with default path."""
        loader = AgentLoader()
        
        assert loader.agents_dir is not None
        assert isinstance(loader.agents_dir, Path)
        assert loader.loaded_agents == {}

    def test_initialization_custom_path(self, temp_agents_dir):
        """Test AgentLoader initialization with custom path."""
        loader = AgentLoader(temp_agents_dir)
        
        assert loader.agents_dir == temp_agents_dir
        assert loader.loaded_agents == {}

    def test_load_agent_success(self, temp_agents_dir):
        """Test successful agent loading."""
        loader = AgentLoader(temp_agents_dir)
        
        config = loader.load_agent("test_agent")
        
        assert isinstance(config, dict)
        assert "agent_identity" in config
        assert "capabilities" in config
        assert "methodology" in config
        assert "input_schema" in config
        assert "output_schema" in config
        
        # Verify agent is cached
        assert "test_agent" in loader.loaded_agents

    def test_load_agent_not_found(self, temp_agents_dir):
        """Test loading non-existent agent."""
        loader = AgentLoader(temp_agents_dir)
        
        with pytest.raises(FileNotFoundError):
            loader.load_agent("nonexistent_agent")

    def test_load_agent_invalid_format(self, temp_agents_dir):
        """Test loading agent with invalid JSON format."""
        # Create invalid agent file
        examples_dir = temp_agents_dir / "examples"
        invalid_agent_path = examples_dir / "invalid_agent.json"
        
        with open(invalid_agent_path, "w") as f:
            f.write("invalid json content")
        
        loader = AgentLoader(temp_agents_dir)
        
        with pytest.raises(json.JSONDecodeError):
            loader.load_agent("invalid_agent")

    def test_load_agent_missing_required_keys(self, temp_agents_dir):
        """Test loading agent with missing required keys."""
        # Create agent with missing required key
        examples_dir = temp_agents_dir / "examples"
        incomplete_agent_path = examples_dir / "incomplete_agent.json"
        
        incomplete_config = {
            "agent_identity": {"name": "test"},
            # Missing other required keys
        }
        
        with open(incomplete_agent_path, "w") as f:
            json.dump(incomplete_config, f)
        
        loader = AgentLoader(temp_agents_dir)
        
        with pytest.raises(ValueError, match="missing required key"):
            loader.load_agent("incomplete_agent")

    def test_list_available_agents(self, temp_agents_dir):
        """Test listing available agents."""
        loader = AgentLoader(temp_agents_dir)
        
        agents = loader.list_available_agents()
        
        assert isinstance(agents, list)
        assert "test_agent" in agents
        assert all(agent.endswith("_agent") for agent in agents)

    def test_list_available_agents_empty_directory(self, tmp_path):
        """Test listing agents from empty directory."""
        empty_agents_dir = tmp_path / "empty_agents"
        empty_agents_dir.mkdir()
        
        loader = AgentLoader(empty_agents_dir)
        
        agents = loader.list_available_agents()
        
        assert isinstance(agents, list)
        assert len(agents) == 0

    def test_list_available_agents_no_examples_directory(self, tmp_path):
        """Test listing agents when examples directory doesn't exist."""
        no_examples_dir = tmp_path / "no_examples"
        no_examples_dir.mkdir()
        
        loader = AgentLoader(no_examples_dir)
        
        agents = loader.list_available_agents()
        
        assert isinstance(agents, list)
        assert len(agents) == 0

    def test_agent_caching(self, temp_agents_dir):
        """Test that loaded agents are properly cached."""
        loader = AgentLoader(temp_agents_dir)
        
        # Load agent first time
        config1 = loader.load_agent("test_agent")
        
        # Load same agent second time
        config2 = loader.load_agent("test_agent")
        
        # Should be same content (cached)
        assert config1 == config2
        assert len(loader.loaded_agents) == 1

    def test_multiple_agent_loading(self, temp_agents_dir):
        """Test loading multiple different agents."""
        # Create a second test agent
        examples_dir = temp_agents_dir / "examples"
        second_agent_path = examples_dir / "second_agent.json"
        
        second_config = {
            "agent_identity": {"name": "second-agent", "type": "producer"},
            "capabilities": {"primary": [], "secondary": [], "specialized": []},
            "methodology": {"framework": "test", "process": []},
            "input_schema": {},
            "output_schema": {}
        }
        
        with open(second_agent_path, "w") as f:
            json.dump(second_config, f)
        
        loader = AgentLoader(temp_agents_dir)
        
        # Load both agents
        config1 = loader.load_agent("test_agent")
        config2 = loader.load_agent("second_agent")
        
        assert config1 != config2
        assert len(loader.loaded_agents) == 2
        assert "test_agent" in loader.loaded_agents
        assert "second_agent" in loader.loaded_agents

    def test_agent_validation_comprehensive(self, temp_agents_dir):
        """Test comprehensive agent configuration validation."""
        # Create agent with all required sections properly formatted
        examples_dir = temp_agents_dir / "examples"
        valid_agent_path = examples_dir / "valid_comprehensive_agent.json"
        
        comprehensive_config = {
            "agent_identity": {
                "name": "comprehensive-agent",
                "type": "consultant",
                "expertise": "Comprehensive testing",
                "version": "1.0.0"
            },
            "capabilities": {
                "primary": ["Analysis", "Strategy"],
                "secondary": ["Communication", "Planning"],
                "specialized": ["Advanced Analytics"]
            },
            "methodology": {
                "framework": "Comprehensive Analysis Framework",
                "process": [
                    {"phase": "Discovery", "activities": ["Research", "Analysis"]},
                    {"phase": "Strategy", "activities": ["Planning", "Design"]}
                ]
            },
            "input_schema": {
                "objective": "string",
                "context": "object"
            },
            "output_schema": {
                "response": {
                    "status": "string",
                    "deliverable": "object",
                    "quality_assessment": "object"
                }
            }
        }
        
        with open(valid_agent_path, "w") as f:
            json.dump(comprehensive_config, f, indent=2)
        
        loader = AgentLoader(temp_agents_dir)
        
        # Should load without error
        config = loader.load_agent("valid_comprehensive_agent")
        
        assert config["agent_identity"]["name"] == "comprehensive-agent"
        assert len(config["capabilities"]["primary"]) == 2
        assert len(config["methodology"]["process"]) == 2