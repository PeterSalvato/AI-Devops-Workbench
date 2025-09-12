#!/usr/bin/env python3
"""
Methodology Validator for Development Agent System

Validates that agents follow their specified development methodologies and frameworks:
- Clean Architecture principles validation
- SOLID principles adherence checking  
- Security framework compliance (OWASP, NIST)
- UX design methodology validation
- Development best practices verification

Ensures agents maintain expertise integrity and methodology consistency.
"""

import json
import re
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import logging

logger = logging.getLogger(__name__)

class MethodologyType(Enum):
    """Types of development methodologies"""
    CLEAN_ARCHITECTURE = "clean_architecture"
    SOLID_PRINCIPLES = "solid_principles"
    OWASP_SECURITY = "owasp_security"
    NIST_CYBERSECURITY = "nist_cybersecurity"
    UX_DESIGN_THINKING = "ux_design_thinking"
    REST_API_DESIGN = "rest_api_design"
    AGILE_DEVELOPMENT = "agile_development"
    TEST_DRIVEN_DEVELOPMENT = "tdd"
    DOMAIN_DRIVEN_DESIGN = "ddd"
    MICROSERVICES_PATTERNS = "microservices_patterns"

class ValidationSeverity(Enum):
    """Validation issue severity levels"""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"

@dataclass
class ValidationIssue:
    """Individual methodology validation issue"""
    severity: ValidationSeverity
    methodology: MethodologyType
    issue_type: str
    description: str
    recommendation: str
    affected_content: str = ""
    line_reference: Optional[int] = None

@dataclass
class MethodologyValidationResult:
    """Complete validation result for an agent response"""
    agent_name: str
    methodology_claimed: str
    validation_score: float  # 0.0 to 1.0
    overall_compliance: str  # excellent, good, fair, poor
    issues: List[ValidationIssue] = field(default_factory=list)
    strengths: List[str] = field(default_factory=list)
    improvement_areas: List[str] = field(default_factory=list)
    methodology_consistency: bool = True
    expert_framework_adherence: float = 0.0

class DevelopmentMethodologyValidator:
    """
    Comprehensive validator for development methodology adherence
    
    Validates that agents consistently apply their claimed expert methodologies
    and provide technically sound recommendations following established frameworks.
    """
    
    def __init__(self):
        self.methodology_frameworks = self._initialize_methodology_frameworks()
        self.validation_history: List[MethodologyValidationResult] = []
        self.agent_methodology_tracking: Dict[str, Dict[str, Any]] = {}
    
    def _initialize_methodology_frameworks(self) -> Dict[MethodologyType, Dict[str, Any]]:
        """Initialize comprehensive methodology validation frameworks"""
        
        return {
            MethodologyType.CLEAN_ARCHITECTURE: {
                "core_principles": [
                    "independence_of_frameworks",
                    "testability",
                    "independence_of_ui",
                    "independence_of_database",
                    "independence_of_external_agency"
                ],
                "layer_structure": [
                    "entities", "use_cases", "interface_adapters", "frameworks_drivers"
                ],
                "dependency_rule": "dependencies_point_inward",
                "required_concepts": [
                    "separation_of_concerns", "dependency_inversion", "business_logic_isolation",
                    "testable_architecture", "framework_independence"
                ],
                "anti_patterns": [
                    "business_logic_in_ui", "database_logic_in_business",
                    "tight_framework_coupling", "circular_dependencies"
                ],
                "validation_keywords": [
                    "clean architecture", "dependency inversion", "business logic",
                    "use case", "entity", "adapter", "boundary", "isolation"
                ]
            },
            
            MethodologyType.SOLID_PRINCIPLES: {
                "principles": {
                    "single_responsibility": {
                        "description": "A class should have one reason to change",
                        "keywords": ["single responsibility", "one reason to change", "cohesion"],
                        "anti_patterns": ["god class", "swiss army knife", "multiple responsibilities"]
                    },
                    "open_closed": {
                        "description": "Open for extension, closed for modification",
                        "keywords": ["open closed", "extension", "modification", "polymorphism"],
                        "anti_patterns": ["modification of existing code", "breaking changes"]
                    },
                    "liskov_substitution": {
                        "description": "Objects should be replaceable with instances of subtypes",
                        "keywords": ["substitution", "inheritance", "polymorphism", "contract"],
                        "anti_patterns": ["violated contracts", "strengthened preconditions"]
                    },
                    "interface_segregation": {
                        "description": "Clients shouldn't depend on interfaces they don't use",
                        "keywords": ["interface segregation", "client specific", "minimal interface"],
                        "anti_patterns": ["fat interface", "interface pollution", "unused methods"]
                    },
                    "dependency_inversion": {
                        "description": "Depend on abstractions, not concretions",
                        "keywords": ["dependency inversion", "abstraction", "dependency injection"],
                        "anti_patterns": ["concrete dependencies", "tight coupling", "direct instantiation"]
                    }
                },
                "implementation_patterns": [
                    "dependency_injection", "factory_pattern", "strategy_pattern",
                    "observer_pattern", "adapter_pattern"
                ]
            },
            
            MethodologyType.OWASP_SECURITY: {
                "top_10_2021": {
                    "A01_broken_access_control": {
                        "description": "Restrictions on authenticated users not properly enforced",
                        "mitigations": ["principle_of_least_privilege", "deny_by_default", "rate_limiting"],
                        "keywords": ["access control", "authorization", "privilege", "permissions"]
                    },
                    "A02_cryptographic_failures": {
                        "description": "Failures related to cryptography leading to sensitive data exposure",
                        "mitigations": ["encryption_at_rest", "encryption_in_transit", "secure_key_management"],
                        "keywords": ["encryption", "cryptography", "sensitive data", "key management"]
                    },
                    "A03_injection": {
                        "description": "Application vulnerable to injection attacks",
                        "mitigations": ["parameterized_queries", "input_validation", "output_encoding"],
                        "keywords": ["injection", "sql injection", "input validation", "parameterized"]
                    },
                    "A04_insecure_design": {
                        "description": "Risks related to design and architectural flaws",
                        "mitigations": ["secure_design_patterns", "threat_modeling", "secure_development"],
                        "keywords": ["secure design", "threat modeling", "security architecture"]
                    },
                    "A05_security_misconfiguration": {
                        "description": "Insecure default configurations, incomplete configurations",
                        "mitigations": ["security_hardening", "configuration_management", "minimal_platform"],
                        "keywords": ["configuration", "hardening", "security settings", "defaults"]
                    }
                },
                "security_principles": [
                    "defense_in_depth", "principle_of_least_privilege", "fail_securely",
                    "secure_by_default", "separation_of_duties", "complete_mediation"
                ],
                "validation_categories": [
                    "authentication", "authorization", "input_validation", "output_encoding",
                    "session_management", "cryptography", "error_handling", "logging"
                ]
            },
            
            MethodologyType.NIST_CYBERSECURITY: {
                "framework_functions": {
                    "identify": {
                        "categories": ["asset_management", "business_environment", "governance", "risk_assessment"],
                        "keywords": ["identify", "inventory", "risk assessment", "governance"]
                    },
                    "protect": {
                        "categories": ["identity_management", "awareness_training", "data_security", "protective_technology"],
                        "keywords": ["protect", "access control", "data protection", "training"]
                    },
                    "detect": {
                        "categories": ["anomalies_events", "security_monitoring", "detection_processes"],
                        "keywords": ["detect", "monitoring", "logging", "anomaly detection"]
                    },
                    "respond": {
                        "categories": ["response_planning", "communications", "analysis", "mitigation"],
                        "keywords": ["respond", "incident response", "mitigation", "communications"]
                    },
                    "recover": {
                        "categories": ["recovery_planning", "improvements", "communications"],
                        "keywords": ["recover", "backup", "recovery", "business continuity"]
                    }
                }
            },
            
            MethodologyType.UX_DESIGN_THINKING: {
                "design_thinking_process": [
                    "empathize", "define", "ideate", "prototype", "test"
                ],
                "don_norman_principles": [
                    "visibility", "feedback", "constraints", "mapping", "consistency", "affordance"
                ],
                "usability_heuristics": [
                    "visibility_of_system_status", "match_system_real_world", "user_control_freedom",
                    "consistency_standards", "error_prevention", "recognition_vs_recall",
                    "flexibility_efficiency", "aesthetic_minimalist_design", "error_recovery",
                    "help_documentation"
                ],
                "user_centered_design": [
                    "user_research", "persona_development", "user_journey_mapping",
                    "usability_testing", "accessibility", "inclusive_design"
                ],
                "validation_keywords": [
                    "user experience", "usability", "accessibility", "user research",
                    "user testing", "persona", "journey mapping", "design thinking"
                ]
            },
            
            MethodologyType.REST_API_DESIGN: {
                "rest_principles": [
                    "client_server", "stateless", "cacheable", "uniform_interface", 
                    "layered_system", "code_on_demand"
                ],
                "http_methods": {
                    "GET": "retrieve_resource",
                    "POST": "create_resource", 
                    "PUT": "update_replace_resource",
                    "PATCH": "partial_update_resource",
                    "DELETE": "remove_resource"
                },
                "status_codes": {
                    "2xx": "success",
                    "3xx": "redirection", 
                    "4xx": "client_error",
                    "5xx": "server_error"
                },
                "design_principles": [
                    "resource_based", "stateless_communication", "hypermedia_as_engine",
                    "self_descriptive_messages", "consistent_naming", "proper_http_methods"
                ],
                "best_practices": [
                    "consistent_naming", "proper_status_codes", "versioning_strategy",
                    "error_handling", "pagination", "filtering", "documentation"
                ]
            },
            
            MethodologyType.MICROSERVICES_PATTERNS: {
                "core_patterns": [
                    "database_per_service", "api_gateway", "circuit_breaker",
                    "service_discovery", "event_sourcing", "cqrs", "saga_pattern"
                ],
                "decomposition_patterns": [
                    "decompose_by_business_capability", "decompose_by_subdomain",
                    "self_contained_service", "service_per_team"
                ],
                "data_management": [
                    "database_per_service", "shared_databases_anti_pattern",
                    "eventual_consistency", "distributed_transactions"
                ],
                "communication_patterns": [
                    "synchronous_messaging", "asynchronous_messaging",
                    "service_mesh", "api_gateway", "message_broker"
                ],
                "observability": [
                    "distributed_tracing", "centralized_logging", "metrics_aggregation",
                    "health_check_api", "service_monitoring"
                ]
            }
        }
    
    async def validate_agent_methodology(self, 
                                       agent_response: Dict[str, Any], 
                                       claimed_methodology: str,
                                       agent_name: str) -> MethodologyValidationResult:
        """
        Comprehensive validation of agent methodology adherence
        
        Args:
            agent_response: The agent's response to validate
            claimed_methodology: The methodology the agent claims to follow
            agent_name: Name of the agent being validated
            
        Returns:
            MethodologyValidationResult with detailed validation feedback
        """
        
        logger.info(f"Validating {agent_name} methodology adherence: {claimed_methodology}")
        
        # Initialize validation result
        result = MethodologyValidationResult(
            agent_name=agent_name,
            methodology_claimed=claimed_methodology,
            validation_score=0.0,
            overall_compliance="unknown"
        )
        
        # Determine methodology type from claimed methodology
        methodology_type = self._map_methodology_string_to_type(claimed_methodology)
        
        if not methodology_type:
            result.issues.append(ValidationIssue(
                severity=ValidationSeverity.WARNING,
                methodology=MethodologyType.CLEAN_ARCHITECTURE,  # Default
                issue_type="unknown_methodology",
                description=f"Cannot validate unknown methodology: {claimed_methodology}",
                recommendation="Specify a recognized development methodology"
            ))
            result.validation_score = 0.5
            result.overall_compliance = "fair"
            return result
        
        # Perform specific methodology validation
        if methodology_type == MethodologyType.CLEAN_ARCHITECTURE:
            await self._validate_clean_architecture(agent_response, result)
        elif methodology_type == MethodologyType.SOLID_PRINCIPLES:
            await self._validate_solid_principles(agent_response, result)
        elif methodology_type == MethodologyType.OWASP_SECURITY:
            await self._validate_owasp_security(agent_response, result)
        elif methodology_type == MethodologyType.NIST_CYBERSECURITY:
            await self._validate_nist_cybersecurity(agent_response, result)
        elif methodology_type == MethodologyType.UX_DESIGN_THINKING:
            await self._validate_ux_design_thinking(agent_response, result)
        elif methodology_type == MethodologyType.REST_API_DESIGN:
            await self._validate_rest_api_design(agent_response, result)
        elif methodology_type == MethodologyType.MICROSERVICES_PATTERNS:
            await self._validate_microservices_patterns(agent_response, result)
        else:
            await self._validate_generic_methodology(agent_response, result, methodology_type)
        
        # Calculate overall scores and compliance
        result.validation_score = self._calculate_validation_score(result)
        result.overall_compliance = self._determine_compliance_level(result.validation_score)
        result.expert_framework_adherence = self._calculate_framework_adherence(result)
        
        # Update tracking
        self._update_agent_tracking(agent_name, result)
        
        # Add to validation history
        self.validation_history.append(result)
        
        logger.info(f"Validation complete - Score: {result.validation_score:.2f}, Compliance: {result.overall_compliance}")
        
        return result
    
    def _map_methodology_string_to_type(self, methodology_string: str) -> Optional[MethodologyType]:
        """Map methodology string to MethodologyType enum"""
        
        methodology_lower = methodology_string.lower()
        
        if "clean architecture" in methodology_lower:
            return MethodologyType.CLEAN_ARCHITECTURE
        elif "solid" in methodology_lower:
            return MethodologyType.SOLID_PRINCIPLES
        elif "owasp" in methodology_lower:
            return MethodologyType.OWASP_SECURITY
        elif "nist" in methodology_lower:
            return MethodologyType.NIST_CYBERSECURITY
        elif any(keyword in methodology_lower for keyword in ["ux", "design thinking", "user experience"]):
            return MethodologyType.UX_DESIGN_THINKING
        elif "rest" in methodology_lower or "api" in methodology_lower:
            return MethodologyType.REST_API_DESIGN
        elif "microservices" in methodology_lower:
            return MethodologyType.MICROSERVICES_PATTERNS
        elif "tdd" in methodology_lower or "test driven" in methodology_lower:
            return MethodologyType.TEST_DRIVEN_DEVELOPMENT
        elif "ddd" in methodology_lower or "domain driven" in methodology_lower:
            return MethodologyType.DOMAIN_DRIVEN_DESIGN
        else:
            return None
    
    async def _validate_clean_architecture(self, agent_response: Dict[str, Any], result: MethodologyValidationResult):
        """Validate Clean Architecture methodology adherence"""
        
        framework = self.methodology_frameworks[MethodologyType.CLEAN_ARCHITECTURE]
        response_text = self._extract_full_response_text(agent_response).lower()
        
        # Check for core principles
        principles_mentioned = 0
        for principle in framework["core_principles"]:
            if any(keyword in response_text for keyword in principle.split("_")):
                principles_mentioned += 1
                result.strengths.append(f"Mentions {principle.replace('_', ' ')}")
        
        if principles_mentioned == 0:
            result.issues.append(ValidationIssue(
                severity=ValidationSeverity.ERROR,
                methodology=MethodologyType.CLEAN_ARCHITECTURE,
                issue_type="missing_core_principles",
                description="No Clean Architecture core principles mentioned",
                recommendation="Include discussion of framework independence, testability, UI independence, etc."
            ))
        elif principles_mentioned < 3:
            result.issues.append(ValidationIssue(
                severity=ValidationSeverity.WARNING,
                methodology=MethodologyType.CLEAN_ARCHITECTURE,
                issue_type="insufficient_principle_coverage",
                description=f"Only {principles_mentioned}/5 core principles mentioned",
                recommendation="Provide more comprehensive Clean Architecture guidance"
            ))
        
        # Check for required concepts
        concepts_mentioned = 0
        for concept in framework["required_concepts"]:
            concept_words = concept.replace("_", " ")
            if concept_words in response_text:
                concepts_mentioned += 1
                result.strengths.append(f"Addresses {concept_words}")
        
        if concepts_mentioned < 2:
            result.issues.append(ValidationIssue(
                severity=ValidationSeverity.WARNING,
                methodology=MethodologyType.CLEAN_ARCHITECTURE,
                issue_type="missing_key_concepts",
                description="Insufficient Clean Architecture concepts discussed",
                recommendation="Include separation of concerns, dependency inversion, business logic isolation"
            ))
        
        # Check for anti-patterns warning
        anti_pattern_warnings = 0
        for anti_pattern in framework["anti_patterns"]:
            anti_pattern_words = anti_pattern.replace("_", " ")
            if anti_pattern_words in response_text or "avoid" in response_text:
                anti_pattern_warnings += 1
        
        if anti_pattern_warnings == 0:
            result.improvement_areas.append("Include warnings about Clean Architecture anti-patterns")
        
        # Check for layer structure understanding
        if any(layer in response_text for layer in framework["layer_structure"]):
            result.strengths.append("Demonstrates layer structure understanding")
        else:
            result.improvement_areas.append("Explain Clean Architecture layer structure")
    
    async def _validate_solid_principles(self, agent_response: Dict[str, Any], result: MethodologyValidationResult):
        """Validate SOLID principles methodology adherence"""
        
        framework = self.methodology_frameworks[MethodologyType.SOLID_PRINCIPLES]
        response_text = self._extract_full_response_text(agent_response).lower()
        
        # Check each SOLID principle
        principles_covered = 0
        for principle_name, principle_data in framework["principles"].items():
            
            principle_mentioned = False
            for keyword in principle_data["keywords"]:
                if keyword in response_text:
                    principle_mentioned = True
                    break
            
            if principle_mentioned:
                principles_covered += 1
                result.strengths.append(f"Addresses {principle_name.replace('_', ' ')} principle")
            
            # Check for anti-pattern warnings
            for anti_pattern in principle_data["anti_patterns"]:
                if anti_pattern in response_text or "avoid" in response_text:
                    result.strengths.append(f"Warns against {anti_pattern}")
        
        if principles_covered == 0:
            result.issues.append(ValidationIssue(
                severity=ValidationSeverity.CRITICAL,
                methodology=MethodologyType.SOLID_PRINCIPLES,
                issue_type="no_solid_principles",
                description="No SOLID principles mentioned in response",
                recommendation="Agent claiming SOLID methodology must discuss relevant principles"
            ))
        elif principles_covered < 3:
            result.issues.append(ValidationIssue(
                severity=ValidationSeverity.WARNING,
                methodology=MethodologyType.SOLID_PRINCIPLES,
                issue_type="incomplete_solid_coverage",
                description=f"Only {principles_covered}/5 SOLID principles covered",
                recommendation="Provide more comprehensive SOLID principles guidance"
            ))
        
        # Check for implementation patterns
        patterns_mentioned = 0
        for pattern in framework["implementation_patterns"]:
            if pattern.replace("_", " ") in response_text:
                patterns_mentioned += 1
                result.strengths.append(f"Mentions {pattern.replace('_', ' ')}")
        
        if patterns_mentioned == 0:
            result.improvement_areas.append("Include SOLID implementation patterns (DI, Factory, Strategy, etc.)")
    
    async def _validate_owasp_security(self, agent_response: Dict[str, Any], result: MethodologyValidationResult):
        """Validate OWASP security methodology adherence"""
        
        framework = self.methodology_frameworks[MethodologyType.OWASP_SECURITY]
        response_text = self._extract_full_response_text(agent_response).lower()
        
        # Check for OWASP Top 10 coverage
        top10_mentioned = 0
        for vuln_id, vuln_data in framework["top_10_2021"].items():
            
            vuln_mentioned = False
            for keyword in vuln_data["keywords"]:
                if keyword in response_text:
                    vuln_mentioned = True
                    break
            
            if vuln_mentioned:
                top10_mentioned += 1
                result.strengths.append(f"Addresses {vuln_id.replace('_', ' ')}")
                
                # Check for specific mitigations
                mitigations_mentioned = 0
                for mitigation in vuln_data["mitigations"]:
                    if mitigation.replace("_", " ") in response_text:
                        mitigations_mentioned += 1
                        result.strengths.append(f"Provides {mitigation.replace('_', ' ')} guidance")
                
                if mitigations_mentioned == 0:
                    result.improvement_areas.append(f"Include specific mitigations for {vuln_id}")
        
        if top10_mentioned == 0:
            result.issues.append(ValidationIssue(
                severity=ValidationSeverity.ERROR,
                methodology=MethodologyType.OWASP_SECURITY,
                issue_type="no_owasp_coverage",
                description="No OWASP Top 10 vulnerabilities addressed",
                recommendation="Security analysis should reference relevant OWASP Top 10 items"
            ))
        
        # Check for security principles
        principles_mentioned = 0
        for principle in framework["security_principles"]:
            if principle.replace("_", " ") in response_text:
                principles_mentioned += 1
                result.strengths.append(f"Applies {principle.replace('_', ' ')} principle")
        
        if principles_mentioned == 0:
            result.improvement_areas.append("Include fundamental security principles (defense in depth, least privilege, etc.)")
        
        # Check validation categories
        categories_covered = 0
        for category in framework["validation_categories"]:
            if category in response_text:
                categories_covered += 1
        
        if categories_covered < 3:
            result.improvement_areas.append("Cover more security validation categories (auth, input validation, crypto, etc.)")
    
    async def _validate_nist_cybersecurity(self, agent_response: Dict[str, Any], result: MethodologyValidationResult):
        """Validate NIST Cybersecurity Framework adherence"""
        
        framework = self.methodology_frameworks[MethodologyType.NIST_CYBERSECURITY]
        response_text = self._extract_full_response_text(agent_response).lower()
        
        # Check for framework functions coverage
        functions_mentioned = 0
        for function_name, function_data in framework["framework_functions"].items():
            
            function_mentioned = False
            for keyword in function_data["keywords"]:
                if keyword in response_text:
                    function_mentioned = True
                    break
            
            if function_mentioned:
                functions_mentioned += 1
                result.strengths.append(f"Addresses NIST {function_name.upper()} function")
                
                # Check for specific categories
                categories_mentioned = 0
                for category in function_data["categories"]:
                    if category.replace("_", " ") in response_text:
                        categories_mentioned += 1
                
                if categories_mentioned > 0:
                    result.strengths.append(f"Covers {categories_mentioned} {function_name} categories")
        
        if functions_mentioned == 0:
            result.issues.append(ValidationIssue(
                severity=ValidationSeverity.WARNING,
                methodology=MethodologyType.NIST_CYBERSECURITY,
                issue_type="no_nist_functions",
                description="No NIST Cybersecurity Framework functions addressed",
                recommendation="Reference relevant NIST framework functions (Identify, Protect, Detect, Respond, Recover)"
            ))
        elif functions_mentioned < 3:
            result.improvement_areas.append("Consider broader NIST framework coverage across multiple functions")
    
    async def _validate_ux_design_thinking(self, agent_response: Dict[str, Any], result: MethodologyValidationResult):
        """Validate UX Design Thinking methodology adherence"""
        
        framework = self.methodology_frameworks[MethodologyType.UX_DESIGN_THINKING]
        response_text = self._extract_full_response_text(agent_response).lower()
        
        # Check for design thinking process
        process_steps_mentioned = 0
        for step in framework["design_thinking_process"]:
            if step in response_text:
                process_steps_mentioned += 1
                result.strengths.append(f"References {step} phase of design thinking")
        
        if process_steps_mentioned == 0:
            result.improvement_areas.append("Include design thinking process steps (empathize, define, ideate, prototype, test)")
        
        # Check for Don Norman principles
        norman_principles = 0
        for principle in framework["don_norman_principles"]:
            if principle in response_text:
                norman_principles += 1
                result.strengths.append(f"Applies {principle} principle")
        
        if norman_principles == 0:
            result.improvement_areas.append("Reference Don Norman's design principles")
        
        # Check for usability heuristics
        heuristics_mentioned = 0
        for heuristic in framework["usability_heuristics"]:
            heuristic_words = heuristic.replace("_", " ")
            if any(word in response_text for word in heuristic_words.split()):
                heuristics_mentioned += 1
        
        if heuristics_mentioned > 3:
            result.strengths.append(f"Addresses {heuristics_mentioned} usability heuristics")
        elif heuristics_mentioned == 0:
            result.improvement_areas.append("Include usability heuristics and guidelines")
        
        # Check for user-centered design elements
        ucd_elements = 0
        for element in framework["user_centered_design"]:
            element_words = element.replace("_", " ")
            if element_words in response_text:
                ucd_elements += 1
                result.strengths.append(f"Includes {element_words}")
        
        if ucd_elements == 0:
            result.issues.append(ValidationIssue(
                severity=ValidationSeverity.WARNING,
                methodology=MethodologyType.UX_DESIGN_THINKING,
                issue_type="missing_user_centered_design",
                description="No user-centered design elements mentioned",
                recommendation="Include user research, personas, journey mapping, or usability testing"
            ))
    
    async def _validate_rest_api_design(self, agent_response: Dict[str, Any], result: MethodologyValidationResult):
        """Validate REST API design methodology adherence"""
        
        framework = self.methodology_frameworks[MethodologyType.REST_API_DESIGN]
        response_text = self._extract_full_response_text(agent_response).lower()
        
        # Check for REST principles
        principles_mentioned = 0
        for principle in framework["rest_principles"]:
            principle_words = principle.replace("_", " ")
            if principle_words in response_text:
                principles_mentioned += 1
                result.strengths.append(f"Addresses {principle_words} principle")
        
        if principles_mentioned == 0:
            result.issues.append(ValidationIssue(
                severity=ValidationSeverity.WARNING,
                methodology=MethodologyType.REST_API_DESIGN,
                issue_type="missing_rest_principles",
                description="No REST architectural principles mentioned",
                recommendation="Include REST principles (stateless, cacheable, uniform interface, etc.)"
            ))
        
        # Check for HTTP methods discussion
        methods_mentioned = 0
        for method in framework["http_methods"].keys():
            if method.lower() in response_text:
                methods_mentioned += 1
        
        if methods_mentioned > 0:
            result.strengths.append(f"Discusses {methods_mentioned} HTTP methods")
        else:
            result.improvement_areas.append("Include HTTP methods usage (GET, POST, PUT, DELETE)")
        
        # Check for status codes
        if any(code in response_text for code in ["200", "201", "400", "401", "404", "500"]):
            result.strengths.append("References HTTP status codes")
        else:
            result.improvement_areas.append("Include HTTP status code guidance")
        
        # Check for best practices
        practices_mentioned = 0
        for practice in framework["best_practices"]:
            practice_words = practice.replace("_", " ")
            if practice_words in response_text:
                practices_mentioned += 1
                result.strengths.append(f"Includes {practice_words} best practice")
        
        if practices_mentioned < 2:
            result.improvement_areas.append("Include more REST API best practices")
    
    async def _validate_microservices_patterns(self, agent_response: Dict[str, Any], result: MethodologyValidationResult):
        """Validate Microservices patterns methodology adherence"""
        
        framework = self.methodology_frameworks[MethodologyType.MICROSERVICES_PATTERNS]
        response_text = self._extract_full_response_text(agent_response).lower()
        
        # Check for core patterns
        patterns_mentioned = 0
        for pattern in framework["core_patterns"]:
            pattern_words = pattern.replace("_", " ")
            if pattern_words in response_text:
                patterns_mentioned += 1
                result.strengths.append(f"Mentions {pattern_words} pattern")
        
        if patterns_mentioned == 0:
            result.issues.append(ValidationIssue(
                severity=ValidationSeverity.WARNING,
                methodology=MethodologyType.MICROSERVICES_PATTERNS,
                issue_type="missing_core_patterns",
                description="No microservices patterns mentioned",
                recommendation="Include core patterns like API gateway, circuit breaker, service discovery"
            ))
        
        # Check for decomposition strategy
        decomposition_mentioned = 0
        for pattern in framework["decomposition_patterns"]:
            pattern_words = pattern.replace("_", " ")
            if pattern_words in response_text:
                decomposition_mentioned += 1
        
        if decomposition_mentioned > 0:
            result.strengths.append("Addresses service decomposition strategy")
        else:
            result.improvement_areas.append("Include service decomposition strategy")
        
        # Check for data management
        data_patterns = 0
        for pattern in framework["data_management"]:
            pattern_words = pattern.replace("_", " ")
            if pattern_words in response_text:
                data_patterns += 1
        
        if data_patterns > 0:
            result.strengths.append("Addresses microservices data management")
        else:
            result.improvement_areas.append("Include data management patterns (database per service, etc.)")
        
        # Check for observability
        observability_mentioned = 0
        for pattern in framework["observability"]:
            pattern_words = pattern.replace("_", " ")
            if pattern_words in response_text:
                observability_mentioned += 1
        
        if observability_mentioned > 0:
            result.strengths.append(f"Includes {observability_mentioned} observability patterns")
        else:
            result.improvement_areas.append("Include observability patterns (tracing, logging, monitoring)")
    
    async def _validate_generic_methodology(self, agent_response: Dict[str, Any], result: MethodologyValidationResult, methodology_type: MethodologyType):
        """Generic validation for methodologies not specifically implemented"""
        
        response_text = self._extract_full_response_text(agent_response).lower()
        
        # Basic validation checks
        if len(response_text) < 100:
            result.issues.append(ValidationIssue(
                severity=ValidationSeverity.WARNING,
                methodology=methodology_type,
                issue_type="insufficient_detail",
                description="Response lacks sufficient detail for methodology validation",
                recommendation="Provide more comprehensive methodology-based guidance"
            ))
        
        # Check for methodology-specific keywords
        methodology_name = methodology_type.value.replace("_", " ")
        if methodology_name not in response_text:
            result.issues.append(ValidationIssue(
                severity=ValidationSeverity.WARNING,
                methodology=methodology_type,
                issue_type="methodology_not_referenced",
                description=f"Claimed methodology '{methodology_name}' not explicitly referenced",
                recommendation=f"Reference {methodology_name} principles and practices"
            ))
        
        result.improvement_areas.append(f"Provide more specific {methodology_name} guidance")
    
    def _extract_full_response_text(self, agent_response: Dict[str, Any]) -> str:
        """Extract all text content from agent response"""
        
        text_parts = []
        
        # Extract from result
        if 'result' in agent_response:
            result = agent_response['result']
            if isinstance(result, dict):
                for value in result.values():
                    if isinstance(value, str):
                        text_parts.append(value)
                    elif isinstance(value, (list, dict)):
                        text_parts.append(str(value))
            else:
                text_parts.append(str(result))
        
        # Extract from technical decisions
        if 'technical_decisions' in agent_response:
            for decision in agent_response['technical_decisions']:
                if isinstance(decision, dict):
                    text_parts.append(str(decision))
                else:
                    text_parts.append(str(decision))
        
        # Extract from recommendations
        if 'recommendations' in agent_response:
            recommendations = agent_response['recommendations']
            if isinstance(recommendations, dict):
                for value in recommendations.values():
                    text_parts.append(str(value))
            else:
                text_parts.append(str(recommendations))
        
        return " ".join(text_parts)
    
    def _calculate_validation_score(self, result: MethodologyValidationResult) -> float:
        """Calculate overall validation score"""
        
        base_score = 1.0
        
        # Deduct points for issues
        for issue in result.issues:
            if issue.severity == ValidationSeverity.CRITICAL:
                base_score -= 0.3
            elif issue.severity == ValidationSeverity.ERROR:
                base_score -= 0.2
            elif issue.severity == ValidationSeverity.WARNING:
                base_score -= 0.1
            elif issue.severity == ValidationSeverity.INFO:
                base_score -= 0.05
        
        # Add points for strengths (up to 0.2 bonus)
        strength_bonus = min(0.2, len(result.strengths) * 0.05)
        base_score += strength_bonus
        
        # Ensure score is between 0 and 1
        return max(0.0, min(1.0, base_score))
    
    def _determine_compliance_level(self, validation_score: float) -> str:
        """Determine compliance level based on validation score"""
        
        if validation_score >= 0.9:
            return "excellent"
        elif validation_score >= 0.75:
            return "good"
        elif validation_score >= 0.6:
            return "fair"
        else:
            return "poor"
    
    def _calculate_framework_adherence(self, result: MethodologyValidationResult) -> float:
        """Calculate how well the agent adheres to their claimed framework"""
        
        # Base adherence on validation score and issue severity
        critical_issues = sum(1 for issue in result.issues if issue.severity == ValidationSeverity.CRITICAL)
        error_issues = sum(1 for issue in result.issues if issue.severity == ValidationSeverity.ERROR)
        
        if critical_issues > 0:
            return max(0.3, result.validation_score - 0.4)
        elif error_issues > 1:
            return max(0.5, result.validation_score - 0.2)
        else:
            return result.validation_score
    
    def _update_agent_tracking(self, agent_name: str, result: MethodologyValidationResult):
        """Update agent performance tracking"""
        
        if agent_name not in self.agent_methodology_tracking:
            self.agent_methodology_tracking[agent_name] = {
                'total_validations': 0,
                'average_score': 0.0,
                'methodology_consistency': True,
                'common_issues': {},
                'strengths_count': {},
                'claimed_methodologies': set()
            }
        
        tracking = self.agent_methodology_tracking[agent_name]
        tracking['total_validations'] += 1
        
        # Update average score
        prev_avg = tracking['average_score']
        total = tracking['total_validations']
        tracking['average_score'] = (prev_avg * (total - 1) + result.validation_score) / total
        
        # Track claimed methodologies
        tracking['claimed_methodologies'].add(result.methodology_claimed)
        
        # Check methodology consistency
        if len(tracking['claimed_methodologies']) > 1:
            tracking['methodology_consistency'] = False
        
        # Track common issues
        for issue in result.issues:
            issue_key = f"{issue.issue_type}_{issue.severity.value}"
            tracking['common_issues'][issue_key] = tracking['common_issues'].get(issue_key, 0) + 1
        
        # Track strengths
        for strength in result.strengths:
            tracking['strengths_count'][strength] = tracking['strengths_count'].get(strength, 0) + 1
    
    def get_agent_methodology_report(self, agent_name: str) -> Dict[str, Any]:
        """Get comprehensive methodology validation report for an agent"""
        
        if agent_name not in self.agent_methodology_tracking:
            return {"error": f"No validation history found for agent: {agent_name}"}
        
        tracking = self.agent_methodology_tracking[agent_name]
        
        # Get recent validations for this agent
        recent_validations = [
            result for result in self.validation_history[-10:] 
            if result.agent_name == agent_name
        ]
        
        return {
            'agent_name': agent_name,
            'validation_summary': {
                'total_validations': tracking['total_validations'],
                'average_validation_score': tracking['average_score'],
                'methodology_consistency': tracking['methodology_consistency'],
                'claimed_methodologies': list(tracking['claimed_methodologies'])
            },
            'performance_trends': {
                'recent_scores': [v.validation_score for v in recent_validations[-5:]],
                'recent_compliance': [v.overall_compliance for v in recent_validations[-5:]],
                'improvement_trend': self._calculate_improvement_trend(recent_validations)
            },
            'common_issues': dict(sorted(tracking['common_issues'].items(), key=lambda x: x[1], reverse=True)[:5]),
            'top_strengths': dict(sorted(tracking['strengths_count'].items(), key=lambda x: x[1], reverse=True)[:5]),
            'recommendations': self._generate_agent_recommendations(tracking, recent_validations)
        }
    
    def _calculate_improvement_trend(self, recent_validations: List[MethodologyValidationResult]) -> str:
        """Calculate if agent's methodology adherence is improving"""
        
        if len(recent_validations) < 3:
            return "insufficient_data"
        
        scores = [v.validation_score for v in recent_validations]
        
        # Simple trend analysis
        first_half = scores[:len(scores)//2]
        second_half = scores[len(scores)//2:]
        
        avg_first = sum(first_half) / len(first_half)
        avg_second = sum(second_half) / len(second_half)
        
        if avg_second > avg_first + 0.1:
            return "improving"
        elif avg_second < avg_first - 0.1:
            return "declining"
        else:
            return "stable"
    
    def _generate_agent_recommendations(self, tracking: Dict[str, Any], recent_validations: List[MethodologyValidationResult]) -> List[str]:
        """Generate improvement recommendations for agent"""
        
        recommendations = []
        
        # Score-based recommendations
        if tracking['average_score'] < 0.7:
            recommendations.append("Focus on improving methodology adherence - current average score is below good threshold")
        
        # Consistency recommendations
        if not tracking['methodology_consistency']:
            recommendations.append("Maintain consistency in claimed methodology across consultations")
        
        # Issue-based recommendations
        for issue_key, count in list(tracking['common_issues'].items())[:3]:
            issue_type, severity = issue_key.split('_', 1)
            recommendations.append(f"Address recurring {severity} issue: {issue_type.replace('_', ' ')}")
        
        # Recent trend recommendations
        if recent_validations:
            recent_issues = [issue.issue_type for v in recent_validations[-3:] for issue in v.issues]
            if len(recent_issues) > 5:
                recommendations.append("Recent validations show increased issues - review methodology application")
        
        return recommendations
    
    def get_system_methodology_health(self) -> Dict[str, Any]:
        """Get overall system methodology validation health"""
        
        if not self.validation_history:
            return {"status": "no_data", "message": "No validation history available"}
        
        recent_validations = self.validation_history[-20:]
        
        # Calculate system-wide metrics
        avg_score = sum(v.validation_score for v in recent_validations) / len(recent_validations)
        compliance_distribution = {}
        for v in recent_validations:
            compliance_distribution[v.overall_compliance] = compliance_distribution.get(v.overall_compliance, 0) + 1
        
        # Issue analysis
        all_issues = [issue for v in recent_validations for issue in v.issues]
        issue_severity_counts = {}
        issue_type_counts = {}
        
        for issue in all_issues:
            issue_severity_counts[issue.severity.value] = issue_severity_counts.get(issue.severity.value, 0) + 1
            issue_type_counts[issue.issue_type] = issue_type_counts.get(issue.issue_type, 0) + 1
        
        return {
            'system_health_score': avg_score,
            'total_validations': len(self.validation_history),
            'recent_validations_analyzed': len(recent_validations),
            'compliance_distribution': compliance_distribution,
            'average_issues_per_validation': len(all_issues) / len(recent_validations),
            'issue_severity_breakdown': issue_severity_counts,
            'most_common_issues': dict(sorted(issue_type_counts.items(), key=lambda x: x[1], reverse=True)[:5]),
            'methodology_coverage': {
                methodology.value: sum(1 for v in recent_validations if methodology.value in v.methodology_claimed.lower()) 
                for methodology in MethodologyType
            },
            'agent_performance_summary': {
                agent: {
                    'average_score': tracking['average_score'],
                    'total_validations': tracking['total_validations'],
                    'methodology_consistency': tracking['methodology_consistency']
                } for agent, tracking in self.agent_methodology_tracking.items()
            }
        }

# Example usage and testing
async def main():
    """Example usage of the methodology validator"""
    
    validator = DevelopmentMethodologyValidator()
    
    # Example agent response for validation
    agent_response = {
        'metadata': {
            'agent_name': 'senior-architect',
            'methodology_applied': 'Clean Architecture + SOLID principles',
            'confidence': 0.9
        },
        'result': {
            'architectural_recommendation': 'Implement clean architecture with clear separation of concerns, dependency inversion, and business logic isolation. Use entities, use cases, and interface adapters to maintain framework independence and testability.',
            'technology_stack_guidance': 'Choose frameworks that support dependency injection and follow single responsibility principle',
            'design_patterns': 'Apply adapter pattern for external integrations and strategy pattern for business rules'
        },
        'technical_decisions': [
            {
                'decision': 'Architecture Pattern',
                'recommendation': 'Clean Architecture with dependency inversion for better testability'
            },
            {
                'decision': 'Design Patterns',
                'recommendation': 'Use SOLID principles throughout - single responsibility for each component'
            }
        ],
        'recommendations': {
            'implementation_approach': 'Start with entities and use cases, then build adapters for UI and database',
            'testing_strategy': 'Framework-independent business logic enables comprehensive unit testing'
        }
    }
    
    print("🔍 Starting Methodology Validation")
    print("=" * 60)
    
    # Validate the agent's methodology adherence
    result = await validator.validate_agent_methodology(
        agent_response=agent_response,
        claimed_methodology="Clean Architecture + SOLID principles",
        agent_name="senior-architect"
    )
    
    print(f"\n📊 Validation Results for {result.agent_name}")
    print(f"Methodology: {result.methodology_claimed}")
    print(f"Validation Score: {result.validation_score:.2f}/1.0")
    print(f"Overall Compliance: {result.overall_compliance}")
    print(f"Framework Adherence: {result.expert_framework_adherence:.2f}")
    
    # Display issues
    if result.issues:
        print(f"\n⚠️  Issues Found ({len(result.issues)}):")
        for issue in result.issues:
            print(f"  • [{issue.severity.value.upper()}] {issue.issue_type}: {issue.description}")
            print(f"    Recommendation: {issue.recommendation}")
    else:
        print("\n✅ No validation issues found")
    
    # Display strengths
    if result.strengths:
        print(f"\n💪 Methodology Strengths ({len(result.strengths)}):")
        for strength in result.strengths:
            print(f"  • {strength}")
    
    # Display improvement areas
    if result.improvement_areas:
        print(f"\n🎯 Improvement Areas ({len(result.improvement_areas)}):")
        for area in result.improvement_areas:
            print(f"  • {area}")
    
    # Get agent report
    print("\n" + "=" * 60)
    agent_report = validator.get_agent_methodology_report("senior-architect")
    
    print(f"\n📈 Agent Methodology Report:")
    print(f"Total Validations: {agent_report['validation_summary']['total_validations']}")
    print(f"Average Score: {agent_report['validation_summary']['average_validation_score']:.2f}")
    print(f"Methodology Consistent: {agent_report['validation_summary']['methodology_consistency']}")
    
    # System health
    system_health = validator.get_system_methodology_health()
    print(f"\n🏥 System Methodology Health:")
    print(f"Overall Health Score: {system_health['system_health_score']:.2f}")
    print(f"Total System Validations: {system_health['total_validations']}")
    
    print("\n" + "=" * 60)
    print("🏁 Methodology Validation Complete")

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())