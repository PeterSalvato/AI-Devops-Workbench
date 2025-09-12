#!/usr/bin/env python3
"""
Meta-Orchestrator for Enhanced Development Agent System

Implements sophisticated multi-agent coordination for development workflows:
- Development task planning and decomposition  
- Technical agent coordination and results synthesis
- Code quality validation and architectural decision making
- Error handling and fallback strategies for development processes

Adapted from agentic AI best practices for development-focused workflows.
"""

import json
import yaml
import asyncio
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass, field
from enum import Enum
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OrchestrationPattern(Enum):
    """Development workflow orchestration patterns"""
    SEQUENTIAL = "sequential"          # Architecture → Implementation → Testing → Deployment
    MAPREDUCE = "mapreduce"           # Parallel analysis with result aggregation  
    CONSENSUS = "consensus"           # Multiple experts reaching technical agreement
    HIERARCHICAL = "hierarchical"    # Senior architect delegates to specialists

class TaskStatus(Enum):
    """Development task execution status"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    PARTIAL = "partial"
    BLOCKED = "blocked"               # Waiting for dependencies or decisions

@dataclass
class DevelopmentRequest:
    """Structured development consultation request"""
    objective: str                    # What needs to be built or analyzed
    context: Dict[str, Any] = field(default_factory=dict)
    constraints: Dict[str, Any] = field(default_factory=dict)
    output_format: str = "consultation"
    success_criteria: str = ""
    
    # Development-specific fields
    project_type: str = "feature"     # feature, bug_fix, refactor, architecture
    technical_requirements: Dict[str, Any] = field(default_factory=dict)
    quality_gates: List[str] = field(default_factory=list)
    
    def to_yaml(self) -> str:
        """Convert to YAML format for agent communication"""
        data = {
            "consultation_request": {
                "objective": self.objective,
                "context": self.context,
                "constraints": self.constraints,
                "output_format": self.output_format,
                "success_criteria": self.success_criteria,
                "project_type": self.project_type,
                "technical_requirements": self.technical_requirements,
                "quality_gates": self.quality_gates
            }
        }
        return yaml.dump(data, default_flow_style=False)

@dataclass
class AgentResponse:
    """Structured agent response for development workflows"""
    status: str
    result: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    recommendations: Dict[str, Any] = field(default_factory=dict)
    scope_boundaries: Dict[str, Any] = field(default_factory=dict)
    potential_conflicts: Dict[str, Any] = field(default_factory=dict)
    errors: str = ""
    
    # Development-specific response fields
    code_quality_metrics: Dict[str, Any] = field(default_factory=dict)
    technical_decisions: List[Dict[str, Any]] = field(default_factory=list)
    implementation_risks: List[str] = field(default_factory=list)
    
    @classmethod
    def from_yaml(cls, yaml_str: str) -> 'AgentResponse':
        """Parse agent response from YAML"""
        data = yaml.safe_load(yaml_str)
        response_data = data.get('response', {})
        return cls(
            status=response_data.get('status', 'failed'),
            result=response_data.get('result', {}),
            metadata=response_data.get('metadata', {}),
            recommendations=response_data.get('recommendations', {}),
            scope_boundaries=response_data.get('scope_boundaries', {}),
            potential_conflicts=response_data.get('potential_conflicts', {}),
            errors=response_data.get('errors', ''),
            code_quality_metrics=response_data.get('code_quality_metrics', {}),
            technical_decisions=response_data.get('technical_decisions', []),
            implementation_risks=response_data.get('implementation_risks', [])
        )

class DevelopmentMetaOrchestrator:
    """
    Primary orchestrator for development agent coordination
    
    Core responsibilities:
    - Development task analysis and decomposition
    - Technical agent coordination and routing
    - Code quality validation and architectural oversight
    - Multi-agent result synthesis and conflict resolution
    - Development workflow management and quality gates
    """
    
    def __init__(self, agents_directory: str = "../agents", registry_file: str = "../enhanced-agent-registry.json"):
        self.agents_directory = Path(agents_directory)
        self.registry_file = Path(registry_file)
        self.conversation_history: List[Dict[str, Any]] = []
        self.active_agents: Dict[str, Dict[str, Any]] = {}
        self.quality_metrics: Dict[str, Any] = {}
        
        # Development-specific orchestrator state
        self.technical_decisions: List[Dict[str, Any]] = []
        self.architecture_constraints: Dict[str, Any] = {}
        self.code_quality_gates: List[str] = []
        
        # Load agent registry and validate agents
        self._load_agent_registry()
        self._validate_agent_compatibility()
    
    def _load_agent_registry(self):
        """Load the enhanced agent registry"""
        try:
            if self.registry_file.exists():
                with open(self.registry_file, 'r') as f:
                    self.registry = json.load(f)
                logger.info(f"Loaded {len(self.registry.get('agents', {}))} agents from registry")
            else:
                logger.warning("Agent registry not found, creating minimal registry")
                self.registry = self._create_minimal_registry()
        except Exception as e:
            logger.error(f"Failed to load agent registry: {e}")
            self.registry = self._create_minimal_registry()
    
    def _create_minimal_registry(self) -> Dict[str, Any]:
        """Create minimal registry for development agents"""
        return {
            "registry_metadata": {
                "version": "1.0.0",
                "architecture_type": "Enhanced Development Agents",
                "communication_protocol": "Structured YAML input/output schemas",
                "orchestration_patterns": ["sequential", "mapreduce", "consensus", "hierarchical"]
            },
            "agents": {},
            "development_workflows": {
                "feature_development": {
                    "pattern": "sequential",
                    "agents": ["senior-architect", "security-consultant", "backend-builder", "frontend-builder"],
                    "description": "Full feature development from architecture to implementation"
                },
                "code_review": {
                    "pattern": "parallel", 
                    "agents": ["security-consultant", "senior-architect"],
                    "description": "Multi-perspective code quality and security review"
                },
                "architecture_decision": {
                    "pattern": "consensus",
                    "agents": ["senior-architect", "security-consultant", "ux-strategist"],
                    "description": "Collaborative architectural decision making"
                }
            }
        }
    
    def _validate_agent_compatibility(self):
        """Validate that agents follow enhanced JSON format"""
        compatible_agents = {}
        agent_files = list(self.agents_directory.glob("enhanced-*.json"))
        
        for agent_file in agent_files:
            try:
                with open(agent_file, 'r') as f:
                    agent_data = json.load(f)
                
                # Validate required enhanced agent structure
                required_sections = ['agent_identity', 'input_schema', 'output_schema', 'orchestration_integration']
                if all(section in agent_data for section in required_sections):
                    agent_name = agent_data['agent_identity']['name']
                    compatible_agents[agent_name] = agent_data
                    logger.info(f"Validated enhanced agent: {agent_name}")
                else:
                    logger.warning(f"Agent {agent_file.name} missing required enhanced structure")
                    
            except Exception as e:
                logger.error(f"Failed to validate agent {agent_file.name}: {e}")
        
        self.active_agents = compatible_agents
        logger.info(f"Loaded {len(compatible_agents)} compatible enhanced agents")
    
    async def process_development_request(self, request: DevelopmentRequest) -> Dict[str, Any]:
        """
        Main orchestration method for development requests
        
        Steps:
        1. Analyze development requirements and select appropriate pattern
        2. Determine required agents based on task complexity
        3. Execute orchestration pattern (sequential, parallel, consensus, hierarchical)
        4. Synthesize results and resolve any conflicts
        5. Validate against quality gates and technical standards
        6. Return comprehensive development guidance
        """
        
        try:
            logger.info(f"Processing development request: {request.objective}")
            
            # Step 1: Task analysis and pattern selection
            orchestration_plan = await self._analyze_development_task(request)
            
            # Step 2: Agent selection and coordination
            selected_agents = self._select_agents_for_task(orchestration_plan)
            
            # Step 3: Execute orchestration pattern
            if orchestration_plan['pattern'] == OrchestrationPattern.SEQUENTIAL:
                results = await self._execute_sequential_workflow(request, selected_agents)
            elif orchestration_plan['pattern'] == OrchestrationPattern.MAPREDUCE:
                results = await self._execute_parallel_analysis(request, selected_agents)
            elif orchestration_plan['pattern'] == OrchestrationPattern.CONSENSUS:
                results = await self._execute_consensus_decision(request, selected_agents)
            elif orchestration_plan['pattern'] == OrchestrationPattern.HIERARCHICAL:
                results = await self._execute_hierarchical_delegation(request, selected_agents)
            else:
                results = await self._execute_fallback_workflow(request, selected_agents)
            
            # Step 4: Result synthesis and conflict resolution
            synthesized_response = await self._synthesize_development_results(results, request)
            
            # Step 5: Quality validation
            validated_response = self._validate_development_quality(synthesized_response, request)
            
            # Step 6: Update conversation history and technical decisions
            self._update_development_context(request, validated_response)
            
            return validated_response
            
        except Exception as e:
            logger.error(f"Development orchestration failed: {e}")
            return self._create_error_response(str(e), request)
    
    async def _analyze_development_task(self, request: DevelopmentRequest) -> Dict[str, Any]:
        """Analyze development request and determine optimal orchestration pattern"""
        
        # Analyze task complexity and requirements
        task_complexity = self._assess_task_complexity(request)
        required_expertise = self._determine_required_expertise(request)
        coordination_needs = self._assess_coordination_needs(request, required_expertise)
        
        # Select orchestration pattern based on analysis
        if len(required_expertise) == 1:
            pattern = OrchestrationPattern.SEQUENTIAL
        elif task_complexity['conflicts_likely'] or 'architecture_decision' in request.objective.lower():
            pattern = OrchestrationPattern.CONSENSUS
        elif task_complexity['parallel_work_possible']:
            pattern = OrchestrationPattern.MAPREDUCE
        elif 'senior-architect' in required_expertise and len(required_expertise) > 2:
            pattern = OrchestrationPattern.HIERARCHICAL
        else:
            pattern = OrchestrationPattern.SEQUENTIAL
        
        return {
            'pattern': pattern,
            'complexity': task_complexity,
            'required_expertise': required_expertise,
            'coordination_strategy': coordination_needs,
            'estimated_steps': len(required_expertise)
        }
    
    def _assess_task_complexity(self, request: DevelopmentRequest) -> Dict[str, Any]:
        """Assess development task complexity"""
        complexity_indicators = {
            'multiple_systems': any(keyword in request.objective.lower() 
                                  for keyword in ['integration', 'microservice', 'api', 'database']),
            'security_critical': any(keyword in request.objective.lower() 
                                   for keyword in ['security', 'auth', 'permission', 'encryption']),
            'ui_component': any(keyword in request.objective.lower() 
                              for keyword in ['frontend', 'ui', 'interface', 'component']),
            'architecture_change': any(keyword in request.objective.lower() 
                                     for keyword in ['architecture', 'design', 'refactor', 'restructure']),
            'performance_critical': any(keyword in request.objective.lower() 
                                      for keyword in ['performance', 'optimization', 'scaling', 'speed']),
            'conflicts_likely': len(request.technical_requirements) > 3 or len(request.constraints) > 2,
            'parallel_work_possible': 'analysis' in request.objective.lower() or 'review' in request.objective.lower()
        }
        
        complexity_score = sum(complexity_indicators.values())
        
        return {
            **complexity_indicators,
            'complexity_score': complexity_score,
            'complexity_level': 'high' if complexity_score >= 4 else 'medium' if complexity_score >= 2 else 'low'
        }
    
    def _determine_required_expertise(self, request: DevelopmentRequest) -> List[str]:
        """Determine which agents are needed for the development task"""
        required_agents = []
        
        # Always include senior architect for complex tasks
        if any(keyword in request.objective.lower() 
               for keyword in ['architecture', 'design', 'system', 'integration']):
            required_agents.append('senior-architect')
        
        # Security consultant for security-related tasks
        if any(keyword in request.objective.lower() 
               for keyword in ['security', 'auth', 'permission', 'encryption', 'vulnerability']):
            required_agents.append('security-consultant')
        
        # UX strategist for user-facing features
        if any(keyword in request.objective.lower() 
               for keyword in ['ui', 'ux', 'user', 'interface', 'frontend']):
            required_agents.append('ux-strategist')
        
        # Backend builder for server-side work
        if any(keyword in request.objective.lower() 
               for keyword in ['api', 'backend', 'server', 'database', 'microservice']):
            required_agents.append('backend-builder')
        
        # Frontend builder for client-side work
        if any(keyword in request.objective.lower() 
               for keyword in ['frontend', 'ui', 'react', 'vue', 'angular', 'component']):
            required_agents.append('frontend-builder')
        
        # Default to senior architect if no specific expertise identified
        if not required_agents:
            required_agents.append('senior-architect')
        
        return list(set(required_agents))  # Remove duplicates
    
    def _assess_coordination_needs(self, request: DevelopmentRequest, required_expertise: List[str]) -> Dict[str, Any]:
        """Assess how agents need to coordinate"""
        return {
            'sequential_dependencies': len(required_expertise) > 1,
            'parallel_analysis_beneficial': 'review' in request.objective.lower(),
            'consensus_required': len(required_expertise) > 2 and 'decision' in request.objective.lower(),
            'hierarchical_coordination': 'senior-architect' in required_expertise and len(required_expertise) > 2
        }
    
    def _select_agents_for_task(self, orchestration_plan: Dict[str, Any]) -> List[str]:
        """Select and validate agents for the task"""
        required_agents = orchestration_plan['required_expertise']
        available_agents = []
        
        for agent_name in required_agents:
            if agent_name in self.active_agents:
                available_agents.append(agent_name)
            else:
                logger.warning(f"Required agent '{agent_name}' not available, looking for alternatives")
                # Could add fallback agent selection logic here
        
        if not available_agents:
            logger.warning("No required agents available, defaulting to senior-architect")
            available_agents = ['senior-architect'] if 'senior-architect' in self.active_agents else []
        
        return available_agents
    
    async def _execute_sequential_workflow(self, request: DevelopmentRequest, agents: List[str]) -> List[AgentResponse]:
        """Execute agents in sequence, passing context between them"""
        results = []
        accumulated_context = request.context.copy()
        
        for agent_name in agents:
            try:
                logger.info(f"Executing agent: {agent_name}")
                
                # Update request context with previous results
                updated_request = DevelopmentRequest(
                    objective=request.objective,
                    context=accumulated_context,
                    constraints=request.constraints,
                    output_format=request.output_format,
                    success_criteria=request.success_criteria,
                    project_type=request.project_type,
                    technical_requirements=request.technical_requirements,
                    quality_gates=request.quality_gates
                )
                
                response = await self._consult_agent(agent_name, updated_request)
                results.append(response)
                
                # Accumulate context for next agent
                if response.status == 'success':
                    accumulated_context.update({
                        f"{agent_name}_recommendations": response.recommendations,
                        f"{agent_name}_decisions": response.technical_decisions,
                        f"{agent_name}_constraints": response.scope_boundaries
                    })
                
            except Exception as e:
                logger.error(f"Agent {agent_name} execution failed: {e}")
                error_response = AgentResponse(status='failed', errors=str(e))
                results.append(error_response)
        
        return results
    
    async def _execute_parallel_analysis(self, request: DevelopmentRequest, agents: List[str]) -> List[AgentResponse]:
        """Execute agents in parallel and aggregate results"""
        tasks = []
        
        for agent_name in agents:
            task = self._consult_agent(agent_name, request)
            tasks.append(task)
        
        try:
            results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # Convert exceptions to error responses
            processed_results = []
            for i, result in enumerate(results):
                if isinstance(result, Exception):
                    error_response = AgentResponse(status='failed', errors=str(result))
                    processed_results.append(error_response)
                else:
                    processed_results.append(result)
            
            return processed_results
            
        except Exception as e:
            logger.error(f"Parallel execution failed: {e}")
            return [AgentResponse(status='failed', errors=str(e))]
    
    async def _execute_consensus_decision(self, request: DevelopmentRequest, agents: List[str]) -> List[AgentResponse]:
        """Execute agents and build consensus on conflicting recommendations"""
        # First get all agent responses in parallel
        responses = await self._execute_parallel_analysis(request, agents)
        
        # Analyze for conflicts and attempt consensus building
        conflicts = self._detect_response_conflicts(responses)
        
        if conflicts:
            logger.info("Conflicts detected, attempting consensus resolution")
            consensus_responses = await self._resolve_conflicts_through_consensus(
                request, agents, responses, conflicts
            )
            return consensus_responses
        
        return responses
    
    async def _execute_hierarchical_delegation(self, request: DevelopmentRequest, agents: List[str]) -> List[AgentResponse]:
        """Senior architect coordinates and delegates to specialists"""
        # Senior architect must be present for hierarchical pattern
        if 'senior-architect' not in agents:
            logger.warning("Hierarchical pattern requires senior-architect, falling back to sequential")
            return await self._execute_sequential_workflow(request, agents)
        
        # First consult senior architect for coordination strategy
        architect_response = await self._consult_agent('senior-architect', request)
        
        if architect_response.status != 'success':
            logger.error("Senior architect consultation failed, falling back to parallel")
            return await self._execute_parallel_analysis(request, agents)
        
        # Use architect recommendations to coordinate other agents
        specialist_agents = [agent for agent in agents if agent != 'senior-architect']
        
        # Update request with architect's guidance
        guided_request = DevelopmentRequest(
            objective=request.objective,
            context={
                **request.context,
                'architect_guidance': architect_response.result,
                'technical_direction': architect_response.technical_decisions
            },
            constraints=request.constraints,
            output_format=request.output_format,
            success_criteria=request.success_criteria,
            project_type=request.project_type,
            technical_requirements=request.technical_requirements,
            quality_gates=request.quality_gates
        )
        
        # Execute specialists with architect guidance
        specialist_responses = await self._execute_parallel_analysis(guided_request, specialist_agents)
        
        # Return architect response first, followed by specialist responses
        return [architect_response] + specialist_responses
    
    async def _execute_fallback_workflow(self, request: DevelopmentRequest, agents: List[str]) -> List[AgentResponse]:
        """Fallback workflow when pattern selection fails"""
        logger.info("Using fallback workflow - simple sequential execution")
        return await self._execute_sequential_workflow(request, agents)
    
    async def _consult_agent(self, agent_name: str, request: DevelopmentRequest) -> AgentResponse:
        """Simulate agent consultation (placeholder for actual agent execution)"""
        
        if agent_name not in self.active_agents:
            return AgentResponse(
                status='failed',
                errors=f"Agent '{agent_name}' not available"
            )
        
        agent_config = self.active_agents[agent_name]
        
        try:
            # This is a placeholder - in actual implementation, this would:
            # 1. Format request according to agent's input_schema
            # 2. Execute the agent (possibly via Claude API call with agent persona)
            # 3. Parse response according to agent's output_schema
            # 4. Validate response against agent's methodology requirements
            
            logger.info(f"Consulting {agent_name} with methodology: {agent_config['agent_identity']['methodology']}")
            
            # Placeholder response based on agent type
            if agent_name == 'senior-architect':
                result = {
                    'architectural_recommendation': f"System design analysis for: {request.objective}",
                    'technology_stack_guidance': "Technology recommendations based on requirements",
                    'design_patterns': "Recommended architectural patterns",
                    'scalability_considerations': "Performance and scaling guidance"
                }
                technical_decisions = [
                    {'decision': 'Architecture Pattern', 'recommendation': 'Microservices vs Monolith analysis'},
                    {'decision': 'Technology Stack', 'recommendation': 'Framework and library selections'}
                ]
            elif agent_name == 'security-consultant':
                result = {
                    'security_analysis': f"Security assessment for: {request.objective}",
                    'threat_model': "Identified security threats and mitigations",
                    'compliance_requirements': "Regulatory and security compliance needs"
                }
                technical_decisions = [
                    {'decision': 'Security Controls', 'recommendation': 'Authentication and authorization approach'},
                    {'decision': 'Data Protection', 'recommendation': 'Encryption and data handling requirements'}
                ]
            else:
                result = {
                    'consultation_output': f"{agent_name} analysis of: {request.objective}",
                    'recommendations': f"Specialized guidance from {agent_name}"
                }
                technical_decisions = []
            
            return AgentResponse(
                status='success',
                result=result,
                metadata={
                    'agent_name': agent_name,
                    'methodology_applied': agent_config['agent_identity']['methodology'],
                    'confidence': 0.85,
                    'processing_time': '2.3s'
                },
                recommendations={
                    'follow_up_actions': f"Implement {agent_name} recommendations",
                    'next_consultations': []
                },
                technical_decisions=technical_decisions,
                implementation_risks=[f"Risk assessment from {agent_name}"]
            )
            
        except Exception as e:
            logger.error(f"Agent {agent_name} consultation failed: {e}")
            return AgentResponse(status='failed', errors=str(e))
    
    def _detect_response_conflicts(self, responses: List[AgentResponse]) -> List[Dict[str, Any]]:
        """Detect conflicts between agent responses"""
        conflicts = []
        
        # Simple conflict detection - in practice this would be more sophisticated
        for i, response1 in enumerate(responses):
            for j, response2 in enumerate(responses[i+1:], i+1):
                if response1.potential_conflicts and response2.potential_conflicts:
                    # Check for overlapping conflict areas
                    conflicts.append({
                        'agents': [f"agent_{i}", f"agent_{j}"],
                        'conflict_type': 'methodology_difference',
                        'description': 'Conflicting technical recommendations detected'
                    })
        
        return conflicts
    
    async def _resolve_conflicts_through_consensus(self, 
                                                 request: DevelopmentRequest, 
                                                 agents: List[str], 
                                                 responses: List[AgentResponse], 
                                                 conflicts: List[Dict[str, Any]]) -> List[AgentResponse]:
        """Attempt to resolve conflicts through consensus building"""
        
        # Placeholder for consensus resolution - would involve:
        # 1. Identifying specific areas of disagreement
        # 2. Re-consulting agents with conflict information
        # 3. Applying domain authority weights from orchestration_integration
        # 4. Building compromise solutions or presenting choices to user
        
        logger.info("Applying consensus resolution (placeholder implementation)")
        
        # For now, return original responses with conflict annotations
        for response in responses:
            if not response.potential_conflicts:
                response.potential_conflicts = {}
            response.potential_conflicts['consensus_attempted'] = True
        
        return responses
    
    async def _synthesize_development_results(self, results: List[AgentResponse], request: DevelopmentRequest) -> Dict[str, Any]:
        """Synthesize multi-agent results into comprehensive development guidance"""
        
        successful_results = [r for r in results if r.status == 'success']
        failed_results = [r for r in results if r.status == 'failed']
        
        if not successful_results:
            return {
                'status': 'failed',
                'error': 'No agents provided successful consultations',
                'failed_agents': len(failed_results)
            }
        
        # Aggregate all technical decisions
        all_technical_decisions = []
        all_recommendations = {}
        all_implementation_risks = []
        combined_quality_metrics = {}
        
        for result in successful_results:
            all_technical_decisions.extend(result.technical_decisions)
            all_implementation_risks.extend(result.implementation_risks)
            
            # Merge recommendations
            if result.recommendations:
                agent_name = result.metadata.get('agent_name', 'unknown')
                all_recommendations[agent_name] = result.recommendations
            
            # Merge quality metrics
            if result.code_quality_metrics:
                combined_quality_metrics.update(result.code_quality_metrics)
        
        synthesized_response = {
            'status': 'success',
            'synthesis_summary': {
                'total_agents_consulted': len(results),
                'successful_consultations': len(successful_results),
                'failed_consultations': len(failed_results),
                'consensus_level': 'high' if len(failed_results) == 0 else 'medium'
            },
            'technical_guidance': {
                'primary_recommendations': self._extract_primary_recommendations(successful_results),
                'technical_decisions': all_technical_decisions,
                'implementation_approach': self._synthesize_implementation_approach(successful_results),
                'quality_requirements': combined_quality_metrics
            },
            'risk_assessment': {
                'implementation_risks': list(set(all_implementation_risks)),
                'mitigation_strategies': self._generate_mitigation_strategies(all_implementation_risks),
                'confidence_level': self._calculate_confidence_level(successful_results)
            },
            'next_steps': {
                'immediate_actions': self._prioritize_immediate_actions(all_recommendations),
                'follow_up_consultations': self._suggest_follow_up_consultations(successful_results, request),
                'quality_gates': self._define_quality_gates(successful_results, request)
            },
            'detailed_agent_responses': [
                {
                    'agent': r.metadata.get('agent_name', 'unknown'),
                    'methodology': r.metadata.get('methodology_applied', 'unknown'),
                    'key_recommendations': r.result,
                    'confidence': r.metadata.get('confidence', 0.0)
                } for r in successful_results
            ]
        }
        
        return synthesized_response
    
    def _extract_primary_recommendations(self, results: List[AgentResponse]) -> List[str]:
        """Extract the most important recommendations across all agents"""
        primary_recommendations = []
        
        for result in results:
            agent_name = result.metadata.get('agent_name', 'unknown')
            if result.result:
                # Extract key recommendation based on agent type
                if agent_name == 'senior-architect':
                    primary_recommendations.append(
                        result.result.get('architectural_recommendation', f"{agent_name} provided technical guidance")
                    )
                elif agent_name == 'security-consultant':
                    primary_recommendations.append(
                        result.result.get('security_analysis', f"{agent_name} provided security guidance")
                    )
                else:
                    primary_recommendations.append(
                        result.result.get('consultation_output', f"{agent_name} provided specialized guidance")
                    )
        
        return primary_recommendations
    
    def _synthesize_implementation_approach(self, results: List[AgentResponse]) -> str:
        """Synthesize implementation approach from multiple agent perspectives"""
        approaches = []
        
        for result in results:
            agent_name = result.metadata.get('agent_name', 'unknown')
            if agent_name == 'senior-architect':
                approaches.append("Architecture-driven development with clear component boundaries")
            elif agent_name == 'security-consultant':
                approaches.append("Security-first implementation with comprehensive threat mitigation")
            elif agent_name == 'backend-builder':
                approaches.append("API-first backend development with clean architecture principles")
            elif agent_name == 'frontend-builder':
                approaches.append("Component-driven frontend development with accessibility focus")
        
        if approaches:
            return " | ".join(approaches)
        return "Standard development approach with quality focus"
    
    def _generate_mitigation_strategies(self, risks: List[str]) -> List[str]:
        """Generate mitigation strategies for identified risks"""
        strategies = []
        
        for risk in set(risks):  # Remove duplicates
            if 'security' in risk.lower():
                strategies.append("Implement comprehensive security testing and code review")
            elif 'performance' in risk.lower():
                strategies.append("Conduct performance testing and optimization analysis")
            elif 'integration' in risk.lower():
                strategies.append("Develop integration testing strategy and API contracts")
            else:
                strategies.append(f"Mitigate risk: {risk}")
        
        return strategies
    
    def _calculate_confidence_level(self, results: List[AgentResponse]) -> float:
        """Calculate overall confidence level from agent responses"""
        confidences = [r.metadata.get('confidence', 0.5) for r in results]
        return sum(confidences) / len(confidences) if confidences else 0.5
    
    def _prioritize_immediate_actions(self, recommendations: Dict[str, Any]) -> List[str]:
        """Prioritize immediate actions from agent recommendations"""
        actions = []
        
        # Extract follow-up actions from each agent's recommendations
        for agent_name, agent_recommendations in recommendations.items():
            if isinstance(agent_recommendations, dict) and 'follow_up_actions' in agent_recommendations:
                actions.append(f"{agent_name}: {agent_recommendations['follow_up_actions']}")
        
        return actions if actions else ["Begin implementation based on technical guidance"]
    
    def _suggest_follow_up_consultations(self, results: List[AgentResponse], request: DevelopmentRequest) -> List[str]:
        """Suggest follow-up consultations based on results and request"""
        suggestions = []
        
        consulted_agents = {r.metadata.get('agent_name') for r in results}
        
        # Suggest missing critical agents based on request
        if 'security' in request.objective.lower() and 'security-consultant' not in consulted_agents:
            suggestions.append("security-consultant - for security analysis")
        
        if ('ui' in request.objective.lower() or 'frontend' in request.objective.lower()) and 'ux-strategist' not in consulted_agents:
            suggestions.append("ux-strategist - for user experience guidance")
        
        return suggestions
    
    def _define_quality_gates(self, results: List[AgentResponse], request: DevelopmentRequest) -> List[str]:
        """Define quality gates based on agent recommendations"""
        gates = []
        
        for result in results:
            agent_name = result.metadata.get('agent_name', 'unknown')
            if agent_name == 'security-consultant':
                gates.append("Security review and vulnerability assessment")
            elif agent_name == 'senior-architect':
                gates.append("Architecture compliance and design review")
            elif agent_name in ['backend-builder', 'frontend-builder']:
                gates.append("Code quality review and testing validation")
        
        # Add standard gates
        gates.extend(["Unit test coverage >= 80%", "Integration testing complete", "Code review approved"])
        
        return list(set(gates))  # Remove duplicates
    
    def _validate_development_quality(self, response: Dict[str, Any], request: DevelopmentRequest) -> Dict[str, Any]:
        """Validate response meets development quality standards"""
        
        quality_checks = {
            'has_technical_guidance': bool(response.get('technical_guidance')),
            'has_implementation_approach': bool(response.get('technical_guidance', {}).get('implementation_approach')),
            'has_risk_assessment': bool(response.get('risk_assessment')),
            'has_next_steps': bool(response.get('next_steps')),
            'meets_success_criteria': self._check_success_criteria(response, request.success_criteria)
        }
        
        quality_score = sum(quality_checks.values()) / len(quality_checks)
        
        response['quality_validation'] = {
            'quality_checks': quality_checks,
            'quality_score': quality_score,
            'validation_passed': quality_score >= 0.8,
            'validation_timestamp': self._get_timestamp()
        }
        
        if quality_score < 0.8:
            logger.warning(f"Quality validation failed with score: {quality_score}")
            response['quality_warnings'] = [
                f"Quality check failed: {check}" for check, passed in quality_checks.items() if not passed
            ]
        
        return response
    
    def _check_success_criteria(self, response: Dict[str, Any], criteria: str) -> bool:
        """Check if response meets specified success criteria"""
        if not criteria:
            return True
        
        # Simple keyword matching - could be more sophisticated
        criteria_lower = criteria.lower()
        response_text = str(response).lower()
        
        criteria_keywords = criteria_lower.split()
        matches = sum(1 for keyword in criteria_keywords if keyword in response_text)
        
        return matches >= len(criteria_keywords) * 0.5  # At least 50% keyword match
    
    def _update_development_context(self, request: DevelopmentRequest, response: Dict[str, Any]):
        """Update orchestrator context with development decisions and learnings"""
        
        # Update conversation history
        self.conversation_history.append({
            'timestamp': self._get_timestamp(),
            'request_objective': request.objective,
            'project_type': request.project_type,
            'agents_consulted': [
                agent['agent'] for agent in response.get('detailed_agent_responses', [])
            ],
            'technical_decisions': response.get('technical_guidance', {}).get('technical_decisions', []),
            'quality_score': response.get('quality_validation', {}).get('quality_score', 0.0)
        })
        
        # Update technical decisions registry
        if 'technical_guidance' in response:
            technical_decisions = response['technical_guidance'].get('technical_decisions', [])
            self.technical_decisions.extend(technical_decisions)
        
        # Update quality metrics
        if 'quality_validation' in response:
            self.quality_metrics[request.objective] = response['quality_validation']
        
        logger.info(f"Updated development context - Total decisions: {len(self.technical_decisions)}")
    
    def _create_error_response(self, error_message: str, request: DevelopmentRequest) -> Dict[str, Any]:
        """Create standardized error response"""
        return {
            'status': 'failed',
            'error': error_message,
            'request_objective': request.objective,
            'timestamp': self._get_timestamp(),
            'fallback_recommendations': [
                "Review request parameters and try again",
                "Ensure required agents are available",
                "Check system logs for detailed error information"
            ]
        }
    
    def _get_timestamp(self) -> str:
        """Get current timestamp for logging"""
        import datetime
        return datetime.datetime.now().isoformat()
    
    def get_orchestrator_status(self) -> Dict[str, Any]:
        """Get current orchestrator status and metrics"""
        return {
            'active_agents': list(self.active_agents.keys()),
            'total_conversations': len(self.conversation_history),
            'total_technical_decisions': len(self.technical_decisions),
            'average_quality_score': self._calculate_average_quality_score(),
            'orchestration_patterns_used': self._get_pattern_usage_stats(),
            'system_health': 'operational' if self.active_agents else 'degraded'
        }
    
    def _calculate_average_quality_score(self) -> float:
        """Calculate average quality score across all requests"""
        if not self.quality_metrics:
            return 0.0
        
        scores = [metrics['quality_score'] for metrics in self.quality_metrics.values()]
        return sum(scores) / len(scores)
    
    def _get_pattern_usage_stats(self) -> Dict[str, int]:
        """Get usage statistics for orchestration patterns"""
        # Placeholder - would track pattern usage in actual implementation
        return {
            'sequential': 0,
            'mapreduce': 0,
            'consensus': 0,
            'hierarchical': 0
        }

# Main execution and testing
async def main():
    """Example usage of the development meta-orchestrator"""
    
    orchestrator = DevelopmentMetaOrchestrator()
    
    # Example development request
    request = DevelopmentRequest(
        objective="Design and implement a user authentication system with OAuth2 integration",
        context={
            "existing_system": "Node.js API with Express",
            "user_base": "10,000+ users",
            "compliance_requirements": ["GDPR", "SOC2"]
        },
        constraints={
            "timeline": "4 weeks",
            "team_size": "3 developers",
            "budget": "limited"
        },
        success_criteria="Secure, scalable authentication system with social login support",
        project_type="feature",
        technical_requirements={
            "oauth_providers": ["Google", "GitHub"],
            "session_management": "JWT tokens",
            "database": "PostgreSQL"
        },
        quality_gates=["Security review", "Performance testing", "Integration testing"]
    )
    
    print("🚀 Starting Development Meta-Orchestrator Example")
    print(f"Request: {request.objective}")
    print("=" * 80)
    
    # Process the development request
    result = await orchestrator.process_development_request(request)
    
    print("\n📊 Orchestration Results:")
    print(f"Status: {result['status']}")
    
    if result['status'] == 'success':
        print(f"\nAgents Consulted: {result['synthesis_summary']['successful_consultations']}")
        print(f"Confidence Level: {result['risk_assessment']['confidence_level']:.2f}")
        
        print("\n🔧 Primary Recommendations:")
        for rec in result['technical_guidance']['primary_recommendations']:
            print(f"  • {rec}")
        
        print("\n⚠️  Implementation Risks:")
        for risk in result['risk_assessment']['implementation_risks']:
            print(f"  • {risk}")
        
        print("\n✅ Next Steps:")
        for step in result['next_steps']['immediate_actions']:
            print(f"  • {step}")
        
        print("\n🎯 Quality Gates:")
        for gate in result['next_steps']['quality_gates']:
            print(f"  • {gate}")
    
    else:
        print(f"❌ Error: {result.get('error', 'Unknown error')}")
    
    print("\n" + "=" * 80)
    print("🏁 Development Meta-Orchestrator Example Complete")

if __name__ == "__main__":
    asyncio.run(main())