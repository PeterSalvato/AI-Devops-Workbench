# Codebase Symbol Index & Dependencies

*Maintains an index of codebase structure, function dependencies, and interconnections. This context enables Claude to understand existing code and make changes without breaking integrations.*

**Key Function**: This maintains an index of your codebase structure, function dependencies, and interconnections - providing Claude with the context needed to understand and modify existing code without breaking integrations.

**Updated**: 2024-09-09 (automatically maintained by Claude during development sessions)

## Core Service Architecture

### Authentication Service (`src/auth-service/core.ts`)
**Dependencies**:
- **Database**: `userRepository` (PostgreSQL user tables)
- **Cache**: `redisClient` (session storage)
- **Email**: `emailService` (verification emails)
- **Crypto**: `bcrypt`, `jsonwebtoken` libraries

**Exports**:
- `authenticateUser()` → Used by API middleware (MOVED from src/services/auth/ on 2024-09-09)
- `generateTokens()` → Used by login/refresh endpoints  
- `validateSession()` → Used by protected routes
- `revokeSession()` → Used by logout functionality

**Integration Points**:
- **API Gateway**: All `/auth/*` routes depend on this service
- **User Service**: Calls `validateSession()` for user data requests
- **Admin Service**: Requires admin role validation through this service

### User Management Service (`src/services/users/`)
**Dependencies**:
- **Auth Service**: `validateSession()` for permission checks
- **Database**: `userRepository`, `profileRepository`
- **Storage**: `s3Client` for profile images
- **Validation**: `userValidationSchemas`

**Exports**:
- `getUserProfile()` → Used by frontend user dashboard
- `updateUserProfile()` → Used by profile edit forms
- **deleteUser()** → Used by admin panel and GDPR compliance
- `listUsers()` → Used by admin user management interface

**Integration Points**:
- **Frontend Dashboard**: Directly consumes user profile data
- **Admin Panel**: Uses user management functions with role validation
- **Audit Service**: Receives user action events for compliance logging

## Agent Coordination Discoveries

### Successful Coordination Patterns
*[Discovered during actual project work - populated by Claude]*

**Pattern**: [Name of coordination approach]
- **Agents involved**: [Which agents participated]
- **Project context**: [What project/feature this worked on]
- **Coordination method**: [How they worked together]  
- **Success indicators**: [Why this approach was effective]
- **Reusability**: [When this pattern applies to future projects]

### Agent Dependency Mapping
*[Updated as dependencies are discovered during coordination]*

**Agent Dependencies Discovered**:
- **[Agent Name] → [Required Input From]**: [Specific dependency discovered]
- **[Agent Name] ↔ [Coordination With]**: [Bi-directional coordination needed]
- **[Agent Name] → [Provides To]**: [What this agent delivers to others]

### Cross-Agent Integration Points
*[Documented as integration challenges and solutions are discovered]*

**Integration Point**: [Specific coordination challenge]
- **Agents involved**: [Which agents needed to coordinate]
- **Challenge**: [What made coordination difficult]
- **Solution pattern**: [How coordination was achieved]
- **Future application**: [When to use this coordination approach]

## Connection Network Evolution

### Agent Relationship Strengths
*[Mapped as relationships prove effective or problematic]*

**Strong Coordination Pairs**:
- **[Agent A] + [Agent B]**: [Why they work well together]
- **[Agent C] + [Agent D]**: [What makes their coordination effective]

**Challenging Coordination Points**:  
- **[Agent X] ↔ [Agent Y]**: [What coordination challenges exist]
- **Resolution approach**: [How to handle this coordination challenge]

### Communication Flow Discoveries
*[Documented as effective communication patterns emerge]*

**Effective Communication Patterns**:
- **[Situation]**: [What type of project/challenge]  
- **Communication flow**: [How agents should communicate for this situation]
- **Key handoff points**: [Critical information transfer moments]
- **Success metrics**: [How to know communication is working]

## Project-Specific Pattern Learnings

### Authentication System Patterns
*[Example - to be populated with actual learnings]*

### API Development Patterns  
*[To be populated as API projects are completed]*

### Frontend Integration Patterns
*[To be populated as UI projects are completed]*

### Security Implementation Patterns
*[To be populated as security projects are completed]*

## Institutional Memory

### Repeated Decision Patterns
*[Track which human decisions tend to repeat across projects]*

**Decision Pattern**: [Type of recurring decision]
- **Frequency**: [How often this decision type occurs]
- **Common choice**: [What humans typically decide]
- **Context factors**: [When humans choose differently]
- **Convention status**: [Whether this is now codified]

### Agent Capability Evolution
*[Document how agent effectiveness changes over time]*

**Agent Improvement Observations**:
- **[Agent Name]**: [How performance/coordination has improved]
- **Coordination enhancement**: [How multi-agent work has gotten better]
- **Pattern recognition**: [What coordination patterns are becoming automatic]

---

*This document grows through actual project experience. Each coordination session adds discovered patterns, successful relationships, and integration solutions that improve future multi-agent collaboration.*