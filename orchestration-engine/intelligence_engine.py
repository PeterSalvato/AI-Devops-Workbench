#!/usr/bin/env python3
"""
Intelligence Engine for Enhanced Development Agent System
Advanced overlap detection, conflict resolution, and code quality optimization
"""

import json
import asyncio
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import logging

logger = logging.getLogger(__name__)

class ConflictType(Enum):
    """Types of conflicts between development agents"""
    ARCHITECTURE_DISAGREEMENT = "architecture_disagreement"
    TECHNOLOGY_CHOICE_CONFLICT = "technology_choice_conflict"
    SECURITY_VS_PERFORMANCE = "security_vs_performance"
    IMPLEMENTATION_APPROACH_CONFLICT = "implementation_approach_conflict"
    DESIGN_PATTERN_DISAGREEMENT = "design_pattern_disagreement"
    SCOPE_OVERLAP = "scope_overlap"

class ConflictSeverity(Enum):
    """Severity levels for development conflicts"""
    LOW = "low"           # Minor preference differences
    MODERATE = "moderate" # Significant but resolvable differences
    HIGH = "high"         # Major disagreements requiring decision
    CRITICAL = "critical" # Fundamental conflicts blocking progress

class QualityMetricType(Enum):
    """Types of code quality metrics"""
    CODE_COMPLEXITY = "code_complexity"
    TEST_COVERAGE = "test_coverage"
    TECHNICAL_DEBT = "technical_debt"
    SECURITY_SCORE = "security_score"
    PERFORMANCE_INDEX = "performance_index"
    MAINTAINABILITY = "maintainability"
    DOCUMENTATION_COVERAGE = "documentation_coverage"

@dataclass
class AgentOverlap:
    """Detected overlap between development agents"""
    agents: List[str]
    overlap_type: str
    overlap_areas: List[str]
    confidence: float
    resolution_strategy: str
    impact_assessment: Dict[str, Any]
    
    # Development-specific fields
    code_areas_affected: List[str] = field(default_factory=list)
    architectural_impact: str = ""
    technical_risk_level: str = "low"

@dataclass
class ConflictAnalysis:
    """Advanced conflict analysis for development decisions"""
    conflict_id: str
    agents_involved: List[str]
    conflict_type: ConflictType
    severity: ConflictSeverity
    description: str
    root_cause: str
    
    # Development-specific conflict data
    technical_areas: List[str] = field(default_factory=list)
    architecture_impact: str = ""
    performance_implications: Dict[str, Any] = field(default_factory=dict)
    security_implications: Dict[str, Any] = field(default_factory=dict)
    resolution_options: List[Dict[str, Any]] = field(default_factory=list)
    stakeholder_input_required: bool = False

@dataclass
class QualityMetrics:
    """Code quality and technical metrics"""
    metric_type: QualityMetricType
    score: float  # 0.0 to 1.0
    threshold: float = 0.8
    status: str = "unknown"  # pass, fail, warning
    details: Dict[str, Any] = field(default_factory=dict)
    improvement_suggestions: List[str] = field(default_factory=list)

@dataclass
class TechnicalDecisionPoint:
    """Critical technical decision requiring resolution"""
    decision_id: str
    title: str
    description: str
    options: List[Dict[str, Any]]
    agents_involved: List[str]
    impact_analysis: Dict[str, Any]
    recommendation: Optional[Dict[str, Any]] = None
    stakeholder_approval_required: bool = False

class IntelligenceEngine:
    """
    Advanced intelligence engine for development agent coordination
    
    Capabilities:
    - Code quality analysis and optimization recommendations
    - Technical debt detection and prioritization
    - Architecture conflict resolution
    - Development methodology validation
    - Performance vs security trade-off analysis
    """
    
    def __init__(self):
        self.conflict_history: List[ConflictAnalysis] = []
        self.quality_metrics_history: List[QualityMetrics] = []
        self.technical_decisions: List[TechnicalDecisionPoint] = []
        self.agent_performance_tracking: Dict[str, Dict[str, Any]] = {}
        
        # Development-specific intelligence components
        self.code_quality_standards = self._initialize_quality_standards()
        self.architecture_patterns = self._initialize_architecture_patterns()
        self.security_frameworks = self._initialize_security_frameworks()
    
    def _initialize_quality_standards(self) -> Dict[str, Any]:
        """Initialize code quality standards and thresholds"""
        return {
            "code_complexity": {
                "cyclomatic_complexity_max": 10,
                "function_length_max": 50,
                "class_size_max": 500,
                "parameter_count_max": 5
            },
            "test_coverage": {
                "minimum_coverage": 0.8,
                "critical_path_coverage": 0.95,
                "integration_test_coverage": 0.7
            },
            "technical_debt": {
                "max_debt_ratio": 0.1,
                "critical_issues_max": 0,
                "code_duplication_max": 0.05
            },
            "security": {
                "vulnerability_scan_required": True,
                "security_review_required": True,
                "dependency_audit_required": True
            },
            "documentation": {
                "api_documentation_required": True,
                "code_comment_coverage": 0.6,
                "readme_completeness": True
            }
        }
    
    def _initialize_architecture_patterns(self) -> Dict[str, Any]:
        """Initialize known architecture patterns and their characteristics"""
        return {
            "microservices": {
                "complexity": "high",
                "scalability": "excellent",
                "team_overhead": "high",
                "technology_flexibility": "excellent",
                "suitable_for": ["large_teams", "complex_domains", "independent_deployment"]
            },
            "monolith": {
                "complexity": "low",
                "scalability": "limited",
                "team_overhead": "low",
                "technology_flexibility": "limited",
                "suitable_for": ["small_teams", "simple_domains", "rapid_prototyping"]
            },
            "modular_monolith": {
                "complexity": "medium",
                "scalability": "good",
                "team_overhead": "medium",
                "technology_flexibility": "medium",
                "suitable_for": ["medium_teams", "evolving_domains", "migration_path"]
            },
            "serverless": {
                "complexity": "medium",
                "scalability": "excellent",
                "team_overhead": "low",
                "technology_flexibility": "limited",
                "suitable_for": ["event_driven", "variable_load", "cost_optimization"]
            }
        }
    
    def _initialize_security_frameworks(self) -> Dict[str, Any]:
        """Initialize security frameworks and requirements"""
        return {
            "owasp_top_10": {
                "injection_attacks": {"severity": "critical", "mitigation": "input_validation"},
                "broken_authentication": {"severity": "critical", "mitigation": "secure_auth_framework"},
                "sensitive_data_exposure": {"severity": "high", "mitigation": "encryption_at_rest_transit"},
                "xml_external_entities": {"severity": "high", "mitigation": "disable_xml_parsing"},
                "broken_access_control": {"severity": "critical", "mitigation": "role_based_access"},
                "security_misconfiguration": {"severity": "high", "mitigation": "security_hardening"},
                "cross_site_scripting": {"severity": "high", "mitigation": "output_encoding"},
                "insecure_deserialization": {"severity": "high", "mitigation": "secure_serialization"},
                "vulnerable_components": {"severity": "high", "mitigation": "dependency_scanning"},
                "insufficient_logging": {"severity": "medium", "mitigation": "comprehensive_logging"}
            },
            "threat_modeling": {
                "stride_framework": ["spoofing", "tampering", "repudiation", "information_disclosure", "denial_of_service", "elevation_of_privilege"],
                "attack_surface_analysis": True,
                "risk_assessment_required": True
            }
        }
    
    async def analyze_agent_responses(self, 
                                    agent_responses: List[Dict[str, Any]], 
                                    request_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Comprehensive analysis of agent responses for conflicts, quality, and optimization
        """
        
        analysis_results = {
            "overlap_analysis": await self._detect_agent_overlaps(agent_responses),
            "conflict_analysis": await self._analyze_conflicts(agent_responses, request_context),
            "quality_assessment": await self._assess_code_quality(agent_responses, request_context),
            "technical_decision_points": await self._identify_decision_points(agent_responses),
            "optimization_opportunities": await self._identify_optimizations(agent_responses),
            "consensus_recommendations": await self._generate_consensus_recommendations(agent_responses)
        }
        
        # Update intelligence engine state
        await self._update_intelligence_state(analysis_results, agent_responses, request_context)
        
        return analysis_results
    
    async def _detect_agent_overlaps(self, agent_responses: List[Dict[str, Any]]) -> List[AgentOverlap]:
        """Detect overlapping expertise and recommendations between agents"""
        
        overlaps = []
        
        for i, response1 in enumerate(agent_responses):
            for j, response2 in enumerate(agent_responses[i+1:], i+1):
                
                agent1_name = response1.get('metadata', {}).get('agent_name', f'agent_{i}')
                agent2_name = response2.get('metadata', {}).get('agent_name', f'agent_{j}')
                
                overlap_areas = self._find_overlap_areas(response1, response2)
                
                if overlap_areas:
                    confidence = self._calculate_overlap_confidence(response1, response2, overlap_areas)
                    
                    overlap = AgentOverlap(
                        agents=[agent1_name, agent2_name],
                        overlap_type=self._classify_overlap_type(overlap_areas),
                        overlap_areas=overlap_areas,
                        confidence=confidence,
                        resolution_strategy=self._determine_resolution_strategy(agent1_name, agent2_name, overlap_areas),
                        impact_assessment=self._assess_overlap_impact(response1, response2, overlap_areas),
                        code_areas_affected=self._identify_affected_code_areas(response1, response2),
                        architectural_impact=self._assess_architectural_impact(response1, response2),
                        technical_risk_level=self._assess_technical_risk(response1, response2, overlap_areas)
                    )
                    
                    overlaps.append(overlap)
        
        return overlaps
    
    def _find_overlap_areas(self, response1: Dict[str, Any], response2: Dict[str, Any]) -> List[str]:
        """Find specific areas where agent responses overlap"""
        
        overlap_areas = []
        
        # Check technical decisions overlap
        decisions1 = response1.get('technical_decisions', [])
        decisions2 = response2.get('technical_decisions', [])
        
        for decision1 in decisions1:
            for decision2 in decisions2:
                if self._decisions_overlap(decision1, decision2):
                    overlap_areas.append(f"technical_decision: {decision1.get('decision', 'unknown')}")
        
        # Check result content overlap
        result1 = str(response1.get('result', {})).lower()
        result2 = str(response2.get('result', {})).lower()
        
        # Common development topics that might overlap
        development_topics = [
            'architecture', 'database', 'api', 'security', 'performance', 
            'testing', 'deployment', 'frontend', 'backend', 'authentication',
            'authorization', 'caching', 'monitoring', 'logging'
        ]
        
        for topic in development_topics:
            if topic in result1 and topic in result2:
                overlap_areas.append(f"domain_expertise: {topic}")
        
        # Check recommendation overlap
        recommendations1 = response1.get('recommendations', {})
        recommendations2 = response2.get('recommendations', {})
        
        if isinstance(recommendations1, dict) and isinstance(recommendations2, dict):
            common_keys = set(recommendations1.keys()) & set(recommendations2.keys())
            for key in common_keys:
                overlap_areas.append(f"recommendation_area: {key}")
        
        return overlap_areas
    
    def _decisions_overlap(self, decision1: Dict[str, Any], decision2: Dict[str, Any]) -> bool:
        """Check if two technical decisions overlap"""
        
        decision1_text = f"{decision1.get('decision', '')} {decision1.get('recommendation', '')}".lower()
        decision2_text = f"{decision2.get('decision', '')} {decision2.get('recommendation', '')}".lower()
        
        # Simple keyword overlap detection - could be more sophisticated
        words1 = set(decision1_text.split())
        words2 = set(decision2_text.split())
        
        overlap_ratio = len(words1 & words2) / max(len(words1), len(words2), 1)
        return overlap_ratio > 0.3
    
    def _classify_overlap_type(self, overlap_areas: List[str]) -> str:
        """Classify the type of overlap detected"""
        
        if any('technical_decision' in area for area in overlap_areas):
            return 'decision_overlap'
        elif any('domain_expertise' in area for area in overlap_areas):
            return 'expertise_overlap'
        elif any('recommendation_area' in area for area in overlap_areas):
            return 'recommendation_overlap'
        else:
            return 'general_overlap'
    
    def _calculate_overlap_confidence(self, response1: Dict[str, Any], response2: Dict[str, Any], overlap_areas: List[str]) -> float:
        """Calculate confidence level in overlap detection"""
        
        # Base confidence on number and type of overlaps
        base_confidence = min(0.9, len(overlap_areas) * 0.2)
        
        # Boost confidence for high-quality responses
        quality1 = response1.get('metadata', {}).get('confidence', 0.5)
        quality2 = response2.get('metadata', {}).get('confidence', 0.5)
        quality_boost = (quality1 + quality2) / 2 * 0.2
        
        return min(1.0, base_confidence + quality_boost)
    
    def _determine_resolution_strategy(self, agent1: str, agent2: str, overlap_areas: List[str]) -> str:
        """Determine strategy for resolving agent overlap"""
        
        # Agent hierarchy for conflict resolution
        agent_hierarchy = {
            'senior-architect': 5,
            'security-consultant': 4,
            'ux-strategist': 3,
            'backend-builder': 2,
            'frontend-builder': 2
        }
        
        priority1 = agent_hierarchy.get(agent1, 1)
        priority2 = agent_hierarchy.get(agent2, 1)
        
        if priority1 > priority2:
            return f"defer_to_{agent1}"
        elif priority2 > priority1:
            return f"defer_to_{agent2}"
        elif 'security' in str(overlap_areas).lower():
            return "security_priority"
        elif 'architecture' in str(overlap_areas).lower():
            return "architecture_priority"
        else:
            return "consensus_building"
    
    def _assess_overlap_impact(self, response1: Dict[str, Any], response2: Dict[str, Any], overlap_areas: List[str]) -> Dict[str, Any]:
        """Assess the impact of agent overlap"""
        
        return {
            'development_delay_risk': 'medium' if len(overlap_areas) > 2 else 'low',
            'decision_complexity': 'high' if any('technical_decision' in area for area in overlap_areas) else 'medium',
            'coordination_overhead': len(overlap_areas) * 0.1,
            'quality_impact': 'positive' if len(overlap_areas) <= 2 else 'neutral',
            'areas_needing_clarification': overlap_areas
        }
    
    def _identify_affected_code_areas(self, response1: Dict[str, Any], response2: Dict[str, Any]) -> List[str]:
        """Identify code areas affected by agent overlap"""
        
        affected_areas = []
        
        # Extract mentioned code areas from responses
        result1_text = str(response1.get('result', {})).lower()
        result2_text = str(response2.get('result', {})).lower()
        
        code_areas = [
            'authentication', 'authorization', 'database', 'api', 'frontend',
            'backend', 'middleware', 'routing', 'validation', 'testing',
            'configuration', 'logging', 'monitoring', 'deployment'
        ]
        
        for area in code_areas:
            if area in result1_text and area in result2_text:
                affected_areas.append(area)
        
        return affected_areas
    
    def _assess_architectural_impact(self, response1: Dict[str, Any], response2: Dict[str, Any]) -> str:
        """Assess architectural impact of agent overlap"""
        
        # Look for architecture-related keywords
        combined_text = f"{response1.get('result', {})} {response2.get('result', {})}".lower()
        
        if any(keyword in combined_text for keyword in ['architecture', 'design', 'pattern', 'structure']):
            return 'significant - architectural decisions affected'
        elif any(keyword in combined_text for keyword in ['database', 'api', 'integration']):
            return 'moderate - component design affected'
        else:
            return 'minimal - implementation details only'
    
    def _assess_technical_risk(self, response1: Dict[str, Any], response2: Dict[str, Any], overlap_areas: List[str]) -> str:
        """Assess technical risk level from overlap"""
        
        risk_indicators = 0
        
        # High-risk overlap areas
        high_risk_areas = ['security', 'architecture', 'database', 'authentication']
        for area_desc in overlap_areas:
            if any(high_risk in area_desc.lower() for high_risk in high_risk_areas):
                risk_indicators += 2
        
        # Medium-risk overlap areas
        medium_risk_areas = ['api', 'performance', 'integration']
        for area_desc in overlap_areas:
            if any(medium_risk in area_desc.lower() for medium_risk in medium_risk_areas):
                risk_indicators += 1
        
        if risk_indicators >= 4:
            return 'high'
        elif risk_indicators >= 2:
            return 'medium'
        else:
            return 'low'
    
    async def _analyze_conflicts(self, agent_responses: List[Dict[str, Any]], request_context: Dict[str, Any]) -> List[ConflictAnalysis]:
        """Analyze conflicts between agent recommendations"""
        
        conflicts = []
        
        for i, response1 in enumerate(agent_responses):
            for j, response2 in enumerate(agent_responses[i+1:], i+1):
                
                conflict = await self._detect_response_conflict(response1, response2, request_context)
                if conflict:
                    conflicts.append(conflict)
        
        return conflicts
    
    async def _detect_response_conflict(self, response1: Dict[str, Any], response2: Dict[str, Any], context: Dict[str, Any]) -> Optional[ConflictAnalysis]:
        """Detect specific conflicts between two agent responses"""
        
        agent1 = response1.get('metadata', {}).get('agent_name', 'unknown')
        agent2 = response2.get('metadata', {}).get('agent_name', 'unknown')
        
        # Check for explicit conflicts mentioned in responses
        conflicts1 = response1.get('potential_conflicts', {})
        conflicts2 = response2.get('potential_conflicts', {})
        
        if conflicts1 or conflicts2:
            conflict_type, severity = self._classify_conflict(conflicts1, conflicts2, response1, response2)
            
            if severity != ConflictSeverity.LOW:
                conflict_id = f"conflict_{agent1}_{agent2}_{len(self.conflict_history)}"
                
                return ConflictAnalysis(
                    conflict_id=conflict_id,
                    agents_involved=[agent1, agent2],
                    conflict_type=conflict_type,
                    severity=severity,
                    description=self._generate_conflict_description(response1, response2, conflict_type),
                    root_cause=self._identify_conflict_root_cause(response1, response2, conflict_type),
                    technical_areas=self._identify_technical_conflict_areas(response1, response2),
                    architecture_impact=self._assess_conflict_architecture_impact(response1, response2),
                    performance_implications=self._analyze_performance_implications(response1, response2),
                    security_implications=self._analyze_security_implications(response1, response2),
                    resolution_options=self._generate_resolution_options(response1, response2, conflict_type),
                    stakeholder_input_required=self._requires_stakeholder_input(conflict_type, severity)
                )
        
        return None
    
    def _classify_conflict(self, conflicts1: Dict[str, Any], conflicts2: Dict[str, Any], response1: Dict[str, Any], response2: Dict[str, Any]) -> Tuple[ConflictType, ConflictSeverity]:
        """Classify conflict type and severity"""
        
        # Analyze conflict content
        all_conflicts = {**conflicts1, **conflicts2}
        conflict_text = str(all_conflicts).lower()
        
        # Determine conflict type
        if 'architecture' in conflict_text or 'design' in conflict_text:
            conflict_type = ConflictType.ARCHITECTURE_DISAGREEMENT
        elif 'technology' in conflict_text or 'framework' in conflict_text:
            conflict_type = ConflictType.TECHNOLOGY_CHOICE_CONFLICT
        elif 'security' in conflict_text and 'performance' in conflict_text:
            conflict_type = ConflictType.SECURITY_VS_PERFORMANCE
        elif 'implementation' in conflict_text or 'approach' in conflict_text:
            conflict_type = ConflictType.IMPLEMENTATION_APPROACH_CONFLICT
        elif 'pattern' in conflict_text:
            conflict_type = ConflictType.DESIGN_PATTERN_DISAGREEMENT
        else:
            conflict_type = ConflictType.SCOPE_OVERLAP
        
        # Determine severity
        severity_indicators = 0
        
        # Check for high-impact areas
        if any(keyword in conflict_text for keyword in ['security', 'architecture', 'database']):
            severity_indicators += 2
        
        # Check for blocking language
        if any(keyword in conflict_text for keyword in ['cannot', 'incompatible', 'conflicts', 'contradicts']):
            severity_indicators += 2
        
        # Check for performance/scalability impacts
        if any(keyword in conflict_text for keyword in ['performance', 'scalability', 'bottleneck']):
            severity_indicators += 1
        
        if severity_indicators >= 4:
            severity = ConflictSeverity.CRITICAL
        elif severity_indicators >= 2:
            severity = ConflictSeverity.HIGH
        elif severity_indicators >= 1:
            severity = ConflictSeverity.MODERATE
        else:
            severity = ConflictSeverity.LOW
        
        return conflict_type, severity
    
    def _generate_conflict_description(self, response1: Dict[str, Any], response2: Dict[str, Any], conflict_type: ConflictType) -> str:
        """Generate human-readable conflict description"""
        
        agent1 = response1.get('metadata', {}).get('agent_name', 'Agent 1')
        agent2 = response2.get('metadata', {}).get('agent_name', 'Agent 2')
        
        if conflict_type == ConflictType.ARCHITECTURE_DISAGREEMENT:
            return f"{agent1} and {agent2} have conflicting architectural recommendations"
        elif conflict_type == ConflictType.TECHNOLOGY_CHOICE_CONFLICT:
            return f"{agent1} and {agent2} recommend different technology choices"
        elif conflict_type == ConflictType.SECURITY_VS_PERFORMANCE:
            return f"Security requirements from {agent1} conflict with performance goals from {agent2}"
        elif conflict_type == ConflictType.IMPLEMENTATION_APPROACH_CONFLICT:
            return f"{agent1} and {agent2} suggest incompatible implementation approaches"
        elif conflict_type == ConflictType.DESIGN_PATTERN_DISAGREEMENT:
            return f"{agent1} and {agent2} recommend different design patterns"
        else:
            return f"{agent1} and {agent2} have overlapping scope with conflicting recommendations"
    
    def _identify_conflict_root_cause(self, response1: Dict[str, Any], response2: Dict[str, Any], conflict_type: ConflictType) -> str:
        """Identify the root cause of the conflict"""
        
        if conflict_type == ConflictType.ARCHITECTURE_DISAGREEMENT:
            return "Different architectural philosophies and trade-off priorities"
        elif conflict_type == ConflictType.TECHNOLOGY_CHOICE_CONFLICT:
            return "Varying technology expertise and preference frameworks"
        elif conflict_type == ConflictType.SECURITY_VS_PERFORMANCE:
            return "Fundamental trade-off between security requirements and performance optimization"
        elif conflict_type == ConflictType.IMPLEMENTATION_APPROACH_CONFLICT:
            return "Different implementation methodologies and development practices"
        elif conflict_type == ConflictType.DESIGN_PATTERN_DISAGREEMENT:
            return "Varying interpretation of appropriate design patterns for the context"
        else:
            return "Unclear agent responsibility boundaries and scope definitions"
    
    def _identify_technical_conflict_areas(self, response1: Dict[str, Any], response2: Dict[str, Any]) -> List[str]:
        """Identify specific technical areas affected by conflict"""
        
        areas = []
        
        # Extract technical areas from responses
        technical_decisions1 = response1.get('technical_decisions', [])
        technical_decisions2 = response2.get('technical_decisions', [])
        
        for decision1 in technical_decisions1:
            decision_area = decision1.get('decision', '').lower()
            for decision2 in technical_decisions2:
                if decision1.get('decision') == decision2.get('decision'):
                    if decision1.get('recommendation') != decision2.get('recommendation'):
                        areas.append(decision_area)
        
        return areas
    
    def _assess_conflict_architecture_impact(self, response1: Dict[str, Any], response2: Dict[str, Any]) -> str:
        """Assess architectural impact of conflict"""
        
        # Check if architectural decisions are involved
        arch_keywords = ['architecture', 'design', 'pattern', 'structure', 'component']
        
        combined_text = f"{response1.get('result', {})} {response2.get('result', {})}".lower()
        
        arch_mentions = sum(1 for keyword in arch_keywords if keyword in combined_text)
        
        if arch_mentions >= 3:
            return "high - fundamental architectural decisions affected"
        elif arch_mentions >= 1:
            return "medium - architectural components affected"
        else:
            return "low - implementation details only"
    
    def _analyze_performance_implications(self, response1: Dict[str, Any], response2: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze performance implications of conflict"""
        
        perf_keywords = ['performance', 'speed', 'latency', 'throughput', 'optimization', 'bottleneck']
        combined_text = f"{response1.get('result', {})} {response2.get('result', {})}".lower()
        
        perf_impact = sum(1 for keyword in perf_keywords if keyword in combined_text)
        
        return {
            'impact_level': 'high' if perf_impact >= 2 else 'medium' if perf_impact >= 1 else 'low',
            'areas_affected': [keyword for keyword in perf_keywords if keyword in combined_text],
            'optimization_required': perf_impact >= 2,
            'performance_testing_needed': perf_impact >= 1
        }
    
    def _analyze_security_implications(self, response1: Dict[str, Any], response2: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze security implications of conflict"""
        
        security_keywords = ['security', 'authentication', 'authorization', 'encryption', 'vulnerability', 'threat']
        combined_text = f"{response1.get('result', {})} {response2.get('result', {})}".lower()
        
        security_impact = sum(1 for keyword in security_keywords if keyword in combined_text)
        
        return {
            'impact_level': 'critical' if security_impact >= 3 else 'high' if security_impact >= 2 else 'medium' if security_impact >= 1 else 'low',
            'security_areas_affected': [keyword for keyword in security_keywords if keyword in combined_text],
            'security_review_required': security_impact >= 1,
            'threat_model_update_needed': security_impact >= 2
        }
    
    def _generate_resolution_options(self, response1: Dict[str, Any], response2: Dict[str, Any], conflict_type: ConflictType) -> List[Dict[str, Any]]:
        """Generate options for resolving the conflict"""
        
        agent1 = response1.get('metadata', {}).get('agent_name', 'Agent 1')
        agent2 = response2.get('metadata', {}).get('agent_name', 'Agent 2')
        
        options = []
        
        # Standard resolution options based on conflict type
        if conflict_type == ConflictType.ARCHITECTURE_DISAGREEMENT:
            options = [
                {
                    'option': 'senior_architect_decision',
                    'description': f'Senior architect makes final architectural decision',
                    'pros': ['Clear decision authority', 'Architectural consistency'],
                    'cons': ['May not consider all specialized perspectives'],
                    'implementation_effort': 'low'
                },
                {
                    'option': 'hybrid_approach',
                    'description': f'Combine elements from both {agent1} and {agent2} approaches',
                    'pros': ['Incorporates multiple perspectives', 'Potentially optimal solution'],
                    'cons': ['Increased complexity', 'Potential inconsistencies'],
                    'implementation_effort': 'medium'
                },
                {
                    'option': 'prototype_evaluation',
                    'description': 'Build small prototypes to evaluate both approaches',
                    'pros': ['Data-driven decision', 'Validates assumptions'],
                    'cons': ['Additional development time', 'Resource overhead'],
                    'implementation_effort': 'high'
                }
            ]
        elif conflict_type == ConflictType.SECURITY_VS_PERFORMANCE:
            options = [
                {
                    'option': 'security_priority',
                    'description': 'Prioritize security requirements, optimize performance within constraints',
                    'pros': ['Security compliance maintained', 'Risk mitigation'],
                    'cons': ['Potential performance limitations'],
                    'implementation_effort': 'medium'
                },
                {
                    'option': 'performance_priority',
                    'description': 'Prioritize performance, implement security measures that don\'t impact performance',
                    'pros': ['Optimal performance maintained', 'User experience preserved'],
                    'cons': ['Security risks may remain', 'Compliance challenges'],
                    'implementation_effort': 'medium'
                },
                {
                    'option': 'balanced_approach',
                    'description': 'Find middle ground with acceptable performance and security',
                    'pros': ['Balanced solution', 'Stakeholder compromise'],
                    'cons': ['May not fully optimize either aspect'],
                    'implementation_effort': 'high'
                }
            ]
        else:
            # Generic resolution options
            options = [
                {
                    'option': f'defer_to_{agent1}',
                    'description': f'Accept {agent1} recommendations',
                    'pros': [f'{agent1} domain expertise'],
                    'cons': [f'May miss {agent2} insights'],
                    'implementation_effort': 'low'
                },
                {
                    'option': f'defer_to_{agent2}',
                    'description': f'Accept {agent2} recommendations',
                    'pros': [f'{agent2} domain expertise'],
                    'cons': [f'May miss {agent1} insights'],
                    'implementation_effort': 'low'
                },
                {
                    'option': 'consensus_building',
                    'description': 'Facilitate discussion to build consensus',
                    'pros': ['Collaborative solution', 'Buy-in from all agents'],
                    'cons': ['Time-intensive', 'May not reach agreement'],
                    'implementation_effort': 'medium'
                }
            ]
        
        return options
    
    def _requires_stakeholder_input(self, conflict_type: ConflictType, severity: ConflictSeverity) -> bool:
        """Determine if stakeholder input is required for conflict resolution"""
        
        if severity == ConflictSeverity.CRITICAL:
            return True
        elif severity == ConflictSeverity.HIGH and conflict_type in [ConflictType.ARCHITECTURE_DISAGREEMENT, ConflictType.SECURITY_VS_PERFORMANCE]:
            return True
        else:
            return False
    
    async def _assess_code_quality(self, agent_responses: List[Dict[str, Any]], request_context: Dict[str, Any]) -> List[QualityMetrics]:
        """Assess code quality based on agent responses and recommendations"""
        
        quality_metrics = []
        
        # Analyze each quality metric type
        for metric_type in QualityMetricType:
            metric = await self._calculate_quality_metric(metric_type, agent_responses, request_context)
            if metric:
                quality_metrics.append(metric)
        
        return quality_metrics
    
    async def _calculate_quality_metric(self, metric_type: QualityMetricType, agent_responses: List[Dict[str, Any]], request_context: Dict[str, Any]) -> Optional[QualityMetrics]:
        """Calculate a specific quality metric"""
        
        # This is a simplified implementation - in practice would analyze actual code
        if metric_type == QualityMetricType.CODE_COMPLEXITY:
            return self._assess_code_complexity(agent_responses, request_context)
        elif metric_type == QualityMetricType.SECURITY_SCORE:
            return self._assess_security_score(agent_responses, request_context)
        elif metric_type == QualityMetricType.TEST_COVERAGE:
            return self._assess_test_coverage(agent_responses, request_context)
        elif metric_type == QualityMetricType.TECHNICAL_DEBT:
            return self._assess_technical_debt(agent_responses, request_context)
        elif metric_type == QualityMetricType.MAINTAINABILITY:
            return self._assess_maintainability(agent_responses, request_context)
        else:
            return None
    
    def _assess_code_complexity(self, agent_responses: List[Dict[str, Any]], request_context: Dict[str, Any]) -> QualityMetrics:
        """Assess code complexity based on agent recommendations"""
        
        complexity_indicators = 0
        complexity_details = {}
        improvement_suggestions = []
        
        # Analyze responses for complexity indicators
        for response in agent_responses:
            result_text = str(response.get('result', {})).lower()
            
            if 'complex' in result_text or 'complicated' in result_text:
                complexity_indicators += 1
            
            if 'microservices' in result_text:
                complexity_indicators += 2
                complexity_details['architecture_complexity'] = 'high'
            elif 'monolith' in result_text:
                complexity_details['architecture_complexity'] = 'low'
            
            # Look for complexity-related technical decisions
            for decision in response.get('technical_decisions', []):
                decision_text = str(decision).lower()
                if any(keyword in decision_text for keyword in ['complex', 'intricate', 'sophisticated']):
                    complexity_indicators += 1
        
        # Calculate complexity score (inverted - lower complexity is better)
        base_score = max(0.1, 1.0 - (complexity_indicators * 0.2))
        
        # Add improvement suggestions
        if complexity_indicators >= 3:
            improvement_suggestions.extend([
                "Consider simplifying architecture design",
                "Implement clear component boundaries",
                "Review complexity of business logic"
            ])
        
        status = "pass" if base_score >= 0.6 else "warning" if base_score >= 0.4 else "fail"
        
        return QualityMetrics(
            metric_type=QualityMetricType.CODE_COMPLEXITY,
            score=base_score,
            threshold=0.6,
            status=status,
            details={
                'complexity_indicators': complexity_indicators,
                **complexity_details
            },
            improvement_suggestions=improvement_suggestions
        )
    
    def _assess_security_score(self, agent_responses: List[Dict[str, Any]], request_context: Dict[str, Any]) -> QualityMetrics:
        """Assess security score based on security consultant recommendations"""
        
        security_score = 0.5  # Base score
        security_details = {}
        improvement_suggestions = []
        
        # Find security consultant response
        security_response = None
        for response in agent_responses:
            if response.get('metadata', {}).get('agent_name') == 'security-consultant':
                security_response = response
                break
        
        if security_response:
            result = security_response.get('result', {})
            
            # Look for security analysis components
            if 'security_analysis' in result:
                security_score += 0.2
                security_details['security_analysis_complete'] = True
            
            if 'threat_model' in result:
                security_score += 0.2
                security_details['threat_modeling_complete'] = True
            
            if 'compliance_requirements' in result:
                security_score += 0.1
                security_details['compliance_addressed'] = True
            
            # Check security-related technical decisions
            for decision in security_response.get('technical_decisions', []):
                if 'security' in decision.get('decision', '').lower():
                    security_score += 0.1
        else:
            # No security consultant involved - potential risk
            security_score = 0.3
            improvement_suggestions.append("Include security consultant in development process")
        
        # Cap at 1.0
        security_score = min(1.0, security_score)
        
        status = "pass" if security_score >= 0.8 else "warning" if security_score >= 0.6 else "fail"
        
        if security_score < 0.8:
            improvement_suggestions.extend([
                "Conduct comprehensive security analysis",
                "Implement threat modeling",
                "Review security technical decisions"
            ])
        
        return QualityMetrics(
            metric_type=QualityMetricType.SECURITY_SCORE,
            score=security_score,
            threshold=0.8,
            status=status,
            details=security_details,
            improvement_suggestions=improvement_suggestions
        )
    
    def _assess_test_coverage(self, agent_responses: List[Dict[str, Any]], request_context: Dict[str, Any]) -> QualityMetrics:
        """Assess test coverage expectations based on agent recommendations"""
        
        test_score = 0.0
        test_details = {}
        improvement_suggestions = []
        
        # Look for testing-related recommendations
        for response in agent_responses:
            result_text = str(response.get('result', {})).lower()
            
            if 'test' in result_text:
                test_score += 0.2
            
            if 'unit test' in result_text:
                test_score += 0.2
                test_details['unit_testing_mentioned'] = True
            
            if 'integration test' in result_text:
                test_score += 0.2
                test_details['integration_testing_mentioned'] = True
            
            if 'coverage' in result_text:
                test_score += 0.2
                test_details['coverage_requirements_mentioned'] = True
            
            # Check for testing in technical decisions
            for decision in response.get('technical_decisions', []):
                if 'test' in decision.get('decision', '').lower():
                    test_score += 0.2
        
        test_score = min(1.0, test_score)
        
        status = "pass" if test_score >= 0.6 else "warning" if test_score >= 0.4 else "fail"
        
        if test_score < 0.6:
            improvement_suggestions.extend([
                "Include comprehensive testing strategy",
                "Define unit testing requirements",
                "Establish integration testing approach",
                "Set test coverage targets"
            ])
        
        return QualityMetrics(
            metric_type=QualityMetricType.TEST_COVERAGE,
            score=test_score,
            threshold=0.6,
            status=status,
            details=test_details,
            improvement_suggestions=improvement_suggestions
        )
    
    def _assess_technical_debt(self, agent_responses: List[Dict[str, Any]], request_context: Dict[str, Any]) -> QualityMetrics:
        """Assess technical debt risk based on agent recommendations"""
        
        debt_risk = 0.0
        debt_details = {}
        improvement_suggestions = []
        
        # Look for technical debt indicators
        for response in agent_responses:
            result_text = str(response.get('result', {})).lower()
            
            # Negative indicators (increase debt risk)
            if 'quick fix' in result_text or 'temporary' in result_text:
                debt_risk += 0.2
                debt_details['temporary_solutions_mentioned'] = True
            
            if 'legacy' in result_text and 'maintain' in result_text:
                debt_risk += 0.1
                debt_details['legacy_maintenance_required'] = True
            
            if 'workaround' in result_text:
                debt_risk += 0.2
                debt_details['workarounds_mentioned'] = True
            
            # Positive indicators (reduce debt risk)
            if 'refactor' in result_text or 'clean' in result_text:
                debt_risk -= 0.1
                debt_details['refactoring_mentioned'] = True
            
            if 'best practices' in result_text or 'clean code' in result_text:
                debt_risk -= 0.1
                debt_details['best_practices_mentioned'] = True
        
        # Invert score - lower debt risk is better
        debt_score = max(0.0, 1.0 - debt_risk)
        
        status = "pass" if debt_score >= 0.7 else "warning" if debt_score >= 0.5 else "fail"
        
        if debt_score < 0.7:
            improvement_suggestions.extend([
                "Avoid temporary solutions and workarounds",
                "Plan for code refactoring",
                "Follow clean code principles",
                "Document technical debt for future resolution"
            ])
        
        return QualityMetrics(
            metric_type=QualityMetricType.TECHNICAL_DEBT,
            score=debt_score,
            threshold=0.7,
            status=status,
            details=debt_details,
            improvement_suggestions=improvement_suggestions
        )
    
    def _assess_maintainability(self, agent_responses: List[Dict[str, Any]], request_context: Dict[str, Any]) -> QualityMetrics:
        """Assess maintainability based on agent recommendations"""
        
        maintainability_score = 0.5  # Base score
        maintainability_details = {}
        improvement_suggestions = []
        
        # Look for maintainability indicators
        for response in agent_responses:
            result_text = str(response.get('result', {})).lower()
            
            # Positive maintainability indicators
            if 'documentation' in result_text:
                maintainability_score += 0.1
                maintainability_details['documentation_mentioned'] = True
            
            if 'modular' in result_text or 'component' in result_text:
                maintainability_score += 0.1
                maintainability_details['modular_design_mentioned'] = True
            
            if 'clean' in result_text and 'code' in result_text:
                maintainability_score += 0.1
                maintainability_details['clean_code_mentioned'] = True
            
            if 'pattern' in result_text:
                maintainability_score += 0.1
                maintainability_details['design_patterns_mentioned'] = True
            
            if 'standard' in result_text or 'convention' in result_text:
                maintainability_score += 0.1
                maintainability_details['standards_mentioned'] = True
            
            # Look for maintainability in technical decisions
            for decision in response.get('technical_decisions', []):
                decision_text = str(decision).lower()
                if any(keyword in decision_text for keyword in ['maintainable', 'clean', 'modular', 'standard']):
                    maintainability_score += 0.1
        
        maintainability_score = min(1.0, maintainability_score)
        
        status = "pass" if maintainability_score >= 0.7 else "warning" if maintainability_score >= 0.5 else "fail"
        
        if maintainability_score < 0.7:
            improvement_suggestions.extend([
                "Include comprehensive documentation requirements",
                "Design for modularity and component reuse",
                "Follow clean code principles and standards",
                "Implement consistent design patterns"
            ])
        
        return QualityMetrics(
            metric_type=QualityMetricType.MAINTAINABILITY,
            score=maintainability_score,
            threshold=0.7,
            status=status,
            details=maintainability_details,
            improvement_suggestions=improvement_suggestions
        )
    
    async def _identify_decision_points(self, agent_responses: List[Dict[str, Any]]) -> List[TechnicalDecisionPoint]:
        """Identify critical technical decisions that require resolution"""
        
        decision_points = []
        decision_counter = 0
        
        # Collect all technical decisions from agents
        all_decisions = {}
        
        for response in agent_responses:
            agent_name = response.get('metadata', {}).get('agent_name', 'unknown')
            technical_decisions = response.get('technical_decisions', [])
            
            for decision in technical_decisions:
                decision_key = decision.get('decision', f'decision_{decision_counter}')
                
                if decision_key not in all_decisions:
                    all_decisions[decision_key] = []
                
                all_decisions[decision_key].append({
                    'agent': agent_name,
                    'recommendation': decision.get('recommendation', ''),
                    'response': response
                })
                
                decision_counter += 1
        
        # Analyze decisions for conflicts or critical importance
        for decision_key, decision_data in all_decisions.items():
            if len(decision_data) > 1:  # Multiple agents weighed in
                
                # Check for conflicting recommendations
                recommendations = [d['recommendation'] for d in decision_data]
                unique_recommendations = list(set(recommendations))
                
                if len(unique_recommendations) > 1:
                    # Conflicting recommendations - critical decision point
                    decision_point = TechnicalDecisionPoint(
                        decision_id=f"decision_{len(decision_points)}",
                        title=f"Technical Decision: {decision_key}",
                        description=f"Multiple agents provided conflicting recommendations for {decision_key}",
                        options=[
                            {
                                'option': rec,
                                'supporting_agents': [d['agent'] for d in decision_data if d['recommendation'] == rec],
                                'rationale': rec
                            } for rec in unique_recommendations
                        ],
                        agents_involved=[d['agent'] for d in decision_data],
                        impact_analysis=self._analyze_decision_impact(decision_key, decision_data),
                        stakeholder_approval_required=self._requires_stakeholder_approval(decision_key, decision_data)
                    )
                    
                    decision_points.append(decision_point)
        
        return decision_points
    
    def _analyze_decision_impact(self, decision_key: str, decision_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze the impact of a technical decision"""
        
        # Assess impact based on decision type and agent involvement
        high_impact_keywords = ['architecture', 'database', 'security', 'framework']
        medium_impact_keywords = ['api', 'performance', 'testing', 'deployment']
        
        decision_text = f"{decision_key} {str(decision_data)}".lower()
        
        impact_level = 'low'
        if any(keyword in decision_text for keyword in high_impact_keywords):
            impact_level = 'high'
        elif any(keyword in decision_text for keyword in medium_impact_keywords):
            impact_level = 'medium'
        
        return {
            'impact_level': impact_level,
            'affected_components': self._identify_affected_components(decision_text),
            'development_effort': self._estimate_development_effort(decision_text),
            'risk_level': self._assess_decision_risk(decision_text),
            'reversibility': self._assess_decision_reversibility(decision_text)
        }
    
    def _identify_affected_components(self, decision_text: str) -> List[str]:
        """Identify components affected by decision"""
        
        components = []
        component_keywords = {
            'frontend': ['frontend', 'ui', 'interface', 'react', 'vue', 'angular'],
            'backend': ['backend', 'api', 'server', 'service'],
            'database': ['database', 'db', 'storage', 'sql', 'nosql'],
            'security': ['security', 'auth', 'encryption', 'permission'],
            'infrastructure': ['deployment', 'infrastructure', 'devops', 'ci/cd']
        }
        
        for component, keywords in component_keywords.items():
            if any(keyword in decision_text for keyword in keywords):
                components.append(component)
        
        return components
    
    def _estimate_development_effort(self, decision_text: str) -> str:
        """Estimate development effort for decision"""
        
        high_effort_keywords = ['architecture', 'refactor', 'migration', 'integration']
        medium_effort_keywords = ['implementation', 'development', 'configuration']
        
        if any(keyword in decision_text for keyword in high_effort_keywords):
            return 'high'
        elif any(keyword in decision_text for keyword in medium_effort_keywords):
            return 'medium'
        else:
            return 'low'
    
    def _assess_decision_risk(self, decision_text: str) -> str:
        """Assess risk level of decision"""
        
        high_risk_keywords = ['security', 'architecture', 'database', 'migration']
        medium_risk_keywords = ['performance', 'integration', 'api']
        
        if any(keyword in decision_text for keyword in high_risk_keywords):
            return 'high'
        elif any(keyword in decision_text for keyword in medium_risk_keywords):
            return 'medium'
        else:
            return 'low'
    
    def _assess_decision_reversibility(self, decision_text: str) -> str:
        """Assess how easily decision can be reversed"""
        
        irreversible_keywords = ['database', 'architecture', 'migration', 'framework']
        hard_to_reverse_keywords = ['integration', 'api', 'security']
        
        if any(keyword in decision_text for keyword in irreversible_keywords):
            return 'difficult'
        elif any(keyword in decision_text for keyword in hard_to_reverse_keywords):
            return 'moderate'
        else:
            return 'easy'
    
    def _requires_stakeholder_approval(self, decision_key: str, decision_data: List[Dict[str, Any]]) -> bool:
        """Determine if decision requires stakeholder approval"""
        
        # High-impact decisions requiring stakeholder input
        stakeholder_keywords = ['architecture', 'security', 'budget', 'timeline', 'framework', 'database']
        
        decision_text = f"{decision_key} {str(decision_data)}".lower()
        
        return any(keyword in decision_text for keyword in stakeholder_keywords)
    
    async def _identify_optimizations(self, agent_responses: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Identify optimization opportunities from agent responses"""
        
        optimizations = {
            'performance_optimizations': [],
            'security_enhancements': [],
            'code_quality_improvements': [],
            'architecture_optimizations': [],
            'development_process_improvements': []
        }
        
        for response in agent_responses:
            agent_name = response.get('metadata', {}).get('agent_name', 'unknown')
            result_text = str(response.get('result', {})).lower()
            
            # Performance optimizations
            if 'performance' in result_text or 'optimization' in result_text:
                optimizations['performance_optimizations'].append({
                    'agent': agent_name,
                    'opportunity': self._extract_performance_opportunities(result_text),
                    'impact': 'medium'
                })
            
            # Security enhancements
            if 'security' in result_text and agent_name == 'security-consultant':
                optimizations['security_enhancements'].append({
                    'agent': agent_name,
                    'opportunity': self._extract_security_opportunities(result_text),
                    'impact': 'high'
                })
            
            # Code quality improvements
            if any(keyword in result_text for keyword in ['clean', 'refactor', 'quality', 'best practices']):
                optimizations['code_quality_improvements'].append({
                    'agent': agent_name,
                    'opportunity': self._extract_quality_opportunities(result_text),
                    'impact': 'medium'
                })
            
            # Architecture optimizations
            if 'architecture' in result_text or 'design' in result_text:
                optimizations['architecture_optimizations'].append({
                    'agent': agent_name,
                    'opportunity': self._extract_architecture_opportunities(result_text),
                    'impact': 'high'
                })
        
        return optimizations
    
    def _extract_performance_opportunities(self, text: str) -> str:
        """Extract performance optimization opportunities from text"""
        if 'caching' in text:
            return "Implement caching strategy for improved performance"
        elif 'database' in text:
            return "Optimize database queries and indexing"
        elif 'api' in text:
            return "Optimize API response times and payload sizes"
        else:
            return "General performance optimization opportunities identified"
    
    def _extract_security_opportunities(self, text: str) -> str:
        """Extract security enhancement opportunities from text"""
        if 'authentication' in text:
            return "Enhance authentication mechanisms and security"
        elif 'encryption' in text:
            return "Implement comprehensive encryption strategy"
        elif 'vulnerability' in text:
            return "Address identified security vulnerabilities"
        else:
            return "General security enhancement opportunities identified"
    
    def _extract_quality_opportunities(self, text: str) -> str:
        """Extract code quality improvement opportunities from text"""
        if 'testing' in text:
            return "Improve testing coverage and quality"
        elif 'documentation' in text:
            return "Enhance code documentation and comments"
        elif 'refactor' in text:
            return "Refactor code for better maintainability"
        else:
            return "General code quality improvement opportunities identified"
    
    def _extract_architecture_opportunities(self, text: str) -> str:
        """Extract architecture optimization opportunities from text"""
        if 'modular' in text:
            return "Improve system modularity and component design"
        elif 'scalability' in text:
            return "Enhance system scalability and performance"
        elif 'integration' in text:
            return "Optimize system integration patterns"
        else:
            return "General architecture optimization opportunities identified"
    
    async def _generate_consensus_recommendations(self, agent_responses: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Generate consensus recommendations from all agent responses"""
        
        consensus = {
            'high_confidence_recommendations': [],
            'moderate_confidence_recommendations': [],
            'conflicting_areas': [],
            'unanimous_decisions': [],
            'majority_decisions': [],
            'overall_confidence': 0.0
        }
        
        # Analyze confidence levels
        confidences = []
        for response in agent_responses:
            confidence = response.get('metadata', {}).get('confidence', 0.5)
            confidences.append(confidence)
        
        consensus['overall_confidence'] = sum(confidences) / len(confidences) if confidences else 0.0
        
        # Extract recommendations by confidence level
        for response in agent_responses:
            agent_name = response.get('metadata', {}).get('agent_name', 'unknown')
            confidence = response.get('metadata', {}).get('confidence', 0.5)
            
            rec_item = {
                'agent': agent_name,
                'recommendation': self._extract_primary_recommendation(response),
                'confidence': confidence
            }
            
            if confidence >= 0.8:
                consensus['high_confidence_recommendations'].append(rec_item)
            elif confidence >= 0.6:
                consensus['moderate_confidence_recommendations'].append(rec_item)
        
        # Identify unanimous vs majority decisions
        consensus['unanimous_decisions'] = self._find_unanimous_decisions(agent_responses)
        consensus['majority_decisions'] = self._find_majority_decisions(agent_responses)
        
        return consensus
    
    def _extract_primary_recommendation(self, response: Dict[str, Any]) -> str:
        """Extract primary recommendation from agent response"""
        
        result = response.get('result', {})
        
        # Try to get the most important recommendation
        if isinstance(result, dict):
            for key in ['primary_recommendation', 'architectural_recommendation', 'security_analysis', 'consultation_output']:
                if key in result:
                    return str(result[key])
        
        return str(result)
    
    def _find_unanimous_decisions(self, agent_responses: List[Dict[str, Any]]) -> List[str]:
        """Find decisions that all agents agree on"""
        
        # This is a simplified implementation
        unanimous = []
        
        # Look for common themes in all responses
        common_keywords = ['security', 'testing', 'documentation', 'best practices']
        
        for keyword in common_keywords:
            appears_in_all = True
            for response in agent_responses:
                response_text = str(response.get('result', {})).lower()
                if keyword not in response_text:
                    appears_in_all = False
                    break
            
            if appears_in_all:
                unanimous.append(f"All agents emphasize {keyword}")
        
        return unanimous
    
    def _find_majority_decisions(self, agent_responses: List[Dict[str, Any]]) -> List[str]:
        """Find decisions that majority of agents agree on"""
        
        majority = []
        
        # Look for themes appearing in majority of responses
        common_keywords = ['performance', 'scalability', 'maintainability', 'integration']
        
        for keyword in common_keywords:
            count = 0
            for response in agent_responses:
                response_text = str(response.get('result', {})).lower()
                if keyword in response_text:
                    count += 1
            
            if count > len(agent_responses) / 2:
                majority.append(f"Majority of agents ({count}/{len(agent_responses)}) emphasize {keyword}")
        
        return majority
    
    async def _update_intelligence_state(self, analysis_results: Dict[str, Any], agent_responses: List[Dict[str, Any]], request_context: Dict[str, Any]):
        """Update intelligence engine state with analysis results"""
        
        # Update conflict history
        conflicts = analysis_results.get('conflict_analysis', [])
        self.conflict_history.extend(conflicts)
        
        # Update quality metrics history
        quality_metrics = analysis_results.get('quality_assessment', [])
        self.quality_metrics_history.extend(quality_metrics)
        
        # Update technical decisions
        decision_points = analysis_results.get('technical_decision_points', [])
        self.technical_decisions.extend(decision_points)
        
        # Update agent performance tracking
        for response in agent_responses:
            agent_name = response.get('metadata', {}).get('agent_name', 'unknown')
            confidence = response.get('metadata', {}).get('confidence', 0.5)
            
            if agent_name not in self.agent_performance_tracking:
                self.agent_performance_tracking[agent_name] = {
                    'total_consultations': 0,
                    'average_confidence': 0.0,
                    'successful_consultations': 0,
                    'conflict_involvement': 0
                }
            
            perf = self.agent_performance_tracking[agent_name]
            perf['total_consultations'] += 1
            perf['average_confidence'] = (perf['average_confidence'] * (perf['total_consultations'] - 1) + confidence) / perf['total_consultations']
            
            if response.get('status') == 'success':
                perf['successful_consultations'] += 1
            
            # Check if agent was involved in conflicts
            for conflict in conflicts:
                if agent_name in conflict.agents_involved:
                    perf['conflict_involvement'] += 1
        
        logger.info(f"Updated intelligence engine state - Conflicts: {len(self.conflict_history)}, Quality metrics: {len(self.quality_metrics_history)}")
    
    def get_intelligence_summary(self) -> Dict[str, Any]:
        """Get summary of intelligence engine state and insights"""
        
        return {
            'total_conflicts_analyzed': len(self.conflict_history),
            'total_quality_assessments': len(self.quality_metrics_history),
            'total_technical_decisions': len(self.technical_decisions),
            'agent_performance_summary': {
                agent: {
                    'consultations': perf['total_consultations'],
                    'success_rate': perf['successful_consultations'] / max(1, perf['total_consultations']),
                    'average_confidence': perf['average_confidence'],
                    'conflict_rate': perf['conflict_involvement'] / max(1, perf['total_consultations'])
                } for agent, perf in self.agent_performance_tracking.items()
            },
            'conflict_type_distribution': self._get_conflict_type_distribution(),
            'quality_metrics_summary': self._get_quality_metrics_summary(),
            'system_health_score': self._calculate_system_health_score()
        }
    
    def _get_conflict_type_distribution(self) -> Dict[str, int]:
        """Get distribution of conflict types"""
        
        distribution = {}
        for conflict in self.conflict_history:
            conflict_type = conflict.conflict_type.value
            distribution[conflict_type] = distribution.get(conflict_type, 0) + 1
        
        return distribution
    
    def _get_quality_metrics_summary(self) -> Dict[str, Any]:
        """Get summary of quality metrics"""
        
        if not self.quality_metrics_history:
            return {}
        
        summary = {}
        for metric in self.quality_metrics_history:
            metric_type = metric.metric_type.value
            if metric_type not in summary:
                summary[metric_type] = {
                    'average_score': 0.0,
                    'pass_rate': 0.0,
                    'total_assessments': 0
                }
            
            summary[metric_type]['total_assessments'] += 1
            summary[metric_type]['average_score'] += metric.score
            if metric.status == 'pass':
                summary[metric_type]['pass_rate'] += 1
        
        # Calculate averages
        for metric_type, data in summary.items():
            total = data['total_assessments']
            data['average_score'] /= total
            data['pass_rate'] /= total
        
        return summary
    
    def _calculate_system_health_score(self) -> float:
        """Calculate overall system health score"""
        
        if not self.agent_performance_tracking:
            return 0.5
        
        # Calculate based on agent performance
        total_success_rate = 0
        total_confidence = 0
        total_agents = len(self.agent_performance_tracking)
        
        for perf in self.agent_performance_tracking.values():
            success_rate = perf['successful_consultations'] / max(1, perf['total_consultations'])
            total_success_rate += success_rate
            total_confidence += perf['average_confidence']
        
        avg_success_rate = total_success_rate / total_agents
        avg_confidence = total_confidence / total_agents
        
        # Weight success rate higher than confidence
        health_score = (avg_success_rate * 0.7) + (avg_confidence * 0.3)
        
        return health_score

# Example usage and testing
async def main():
    """Example usage of the intelligence engine"""
    
    engine = IntelligenceEngine()
    
    # Example agent responses for analysis
    agent_responses = [
        {
            'metadata': {'agent_name': 'senior-architect', 'confidence': 0.9},
            'status': 'success',
            'result': {
                'architectural_recommendation': 'Implement microservices architecture with API gateway',
                'technology_stack_guidance': 'Use Node.js with TypeScript for consistency'
            },
            'technical_decisions': [
                {'decision': 'Architecture Pattern', 'recommendation': 'Microservices'},
                {'decision': 'API Design', 'recommendation': 'RESTful with OpenAPI spec'}
            ],
            'potential_conflicts': {
                'complexity': 'Microservices add operational complexity'
            }
        },
        {
            'metadata': {'agent_name': 'security-consultant', 'confidence': 0.85},
            'status': 'success',
            'result': {
                'security_analysis': 'Implement OAuth2 with JWT tokens and rate limiting',
                'threat_model': 'API security and data protection requirements'
            },
            'technical_decisions': [
                {'decision': 'Authentication', 'recommendation': 'OAuth2 + JWT'},
                {'decision': 'API Security', 'recommendation': 'Rate limiting + input validation'}
            ],
            'potential_conflicts': {
                'performance': 'Security measures may impact API performance'
            }
        }
    ]
    
    request_context = {
        'objective': 'Build secure microservices API',
        'project_type': 'feature'
    }
    
    print("🧠 Starting Intelligence Engine Analysis")
    print("=" * 60)
    
    # Analyze agent responses
    analysis = await engine.analyze_agent_responses(agent_responses, request_context)
    
    print("\n📊 Analysis Results:")
    
    # Display overlap analysis
    overlaps = analysis['overlap_analysis']
    print(f"\nAgent Overlaps Detected: {len(overlaps)}")
    for overlap in overlaps:
        print(f"  • {' & '.join(overlap.agents)}: {overlap.overlap_type} (confidence: {overlap.confidence:.2f})")
    
    # Display conflicts
    conflicts = analysis['conflict_analysis']
    print(f"\nConflicts Identified: {len(conflicts)}")
    for conflict in conflicts:
        print(f"  • {conflict.conflict_type.value}: {conflict.description} ({conflict.severity.value})")
    
    # Display quality assessment
    quality_metrics = analysis['quality_assessment']
    print(f"\nQuality Assessment:")
    for metric in quality_metrics:
        print(f"  • {metric.metric_type.value}: {metric.score:.2f} ({metric.status})")
        if metric.improvement_suggestions:
            for suggestion in metric.improvement_suggestions:
                print(f"    - {suggestion}")
    
    # Display technical decision points
    decision_points = analysis['technical_decision_points']
    print(f"\nTechnical Decision Points: {len(decision_points)}")
    for decision in decision_points:
        print(f"  • {decision.title}")
        print(f"    Impact: {decision.impact_analysis['impact_level']}")
        print(f"    Options: {len(decision.options)}")
    
    # Display consensus recommendations
    consensus = analysis['consensus_recommendations']
    print(f"\nConsensus Analysis:")
    print(f"  Overall Confidence: {consensus['overall_confidence']:.2f}")
    print(f"  High Confidence Recommendations: {len(consensus['high_confidence_recommendations'])}")
    print(f"  Unanimous Decisions: {len(consensus['unanimous_decisions'])}")
    
    # Display intelligence summary
    summary = engine.get_intelligence_summary()
    print(f"\n🏥 System Health Score: {summary['system_health_score']:.2f}")
    
    print("\n" + "=" * 60)
    print("🏁 Intelligence Engine Analysis Complete")

if __name__ == "__main__":
    asyncio.run(main())