# Codebase Symbol Index & Dependencies

*Index of codebase structure, function dependencies, and system connections. This provides context for understanding and modifying code without breaking integrations.*

**Updated**: 2025-09-20 (initialized for corporate team)

## Core System Architecture

### Main Components
*[To be populated as system components are identified and documented]*

**Component**: [Name]
- **Location**: `[file path]`
- **Purpose**: [What this component does]
- **Dependencies**: [What it depends on]
- **Used By**: [What uses this component]

## Function Index

### Core Functions
*[To be populated as functions are created and documented]*

**Function**: [functionName]
- **Location**: `[file]:[line number]`
- **Purpose**: [What the function does]
- **Parameters**: [Input parameters]
- **Returns**: [Return value/type]
- **Dependencies**: [What it calls or requires]

## System Connections

### Integration Points
*[To be populated as system integrations are built]*

**Connection**: [ComponentA] → [ComponentB]
- **Type**: [API call, database query, file operation, etc.]
- **Purpose**: [Why this connection exists]
- **Data Flow**: [What data flows between components]
- **Dependencies**: [What this connection requires]

## Discovered Patterns

### Development Patterns
*[To be populated as successful patterns are discovered]*

**Pattern**: [PatternName]
- **Context**: [When this pattern was discovered]
- **Description**: [What the pattern involves]
- **Usage**: [When to apply this pattern]
- **Examples**: [Where this pattern is used]

## External Dependencies

### Third-Party Libraries
*[To be populated as external dependencies are added]*

**Library**: [LibraryName]
- **Version**: [Version used]
- **Purpose**: [Why this library is used]
- **Components Using**: [Which parts of system use it]
- **Documentation**: [Link to library docs]

---

*This document grows through development work. Each function created, integration built, and pattern discovered gets documented here to maintain institutional knowledge of the codebase structure.*
### authenticateUser
- **Location**: `src/auth/auth-service.js:N/A`
- **Purpose**: Validates user credentials using JWT
- **Parameters**: See function signature
- **Returns**: See function documentation
- **Dependencies**: jsonwebtoken, bcrypt
- **Added**: 2025-09-20
- **Context**: Development session

### authorizeRequest
- **Location**: `src/auth/auth-middleware.js:N/A`
- **Purpose**: Middleware for request authorization
- **Parameters**: See function signature
- **Returns**: See function documentation
- **Dependencies**: auth-service
- **Added**: 2025-09-20
- **Context**: Development session

### refreshToken
- **Location**: `src/auth/token-service.js:N/A`
- **Purpose**: Refreshes expired JWT tokens
- **Parameters**: See function signature
- **Returns**: See function documentation
- **Dependencies**: jsonwebtoken
- **Added**: 2025-09-20
- **Context**: Development session

### LoginForm → AuthService
- **Connection Type**: service_call
- **Purpose**: User login authentication
- **Data Flow**: See implementation
- **Dependencies**: Direct connection
- **Added**: 2025-09-20
- **Context**: Development session

### API Gateway → AuthMiddleware
- **Connection Type**: service_call
- **Purpose**: Request authorization check
- **Data Flow**: See implementation
- **Dependencies**: Direct connection
- **Added**: 2025-09-20
- **Context**: Development session

### TokenService → AuthService
- **Connection Type**: service_call
- **Purpose**: Token refresh validation
- **Data Flow**: See implementation
- **Dependencies**: Direct connection
- **Added**: 2025-09-20
- **Context**: Development session

### authenticateUser
- **Location**: `src/auth/auth-service.js:N/A`
- **Purpose**: Validates user credentials using JWT
- **Parameters**: See function signature
- **Returns**: See function documentation
- **Dependencies**: jsonwebtoken, bcrypt
- **Added**: 2025-09-20
- **Context**: Development session

### authorizeRequest
- **Location**: `src/auth/auth-middleware.js:N/A`
- **Purpose**: Middleware for request authorization
- **Parameters**: See function signature
- **Returns**: See function documentation
- **Dependencies**: auth-service
- **Added**: 2025-09-20
- **Context**: Development session

### refreshToken
- **Location**: `src/auth/token-service.js:N/A`
- **Purpose**: Refreshes expired JWT tokens
- **Parameters**: See function signature
- **Returns**: See function documentation
- **Dependencies**: jsonwebtoken
- **Added**: 2025-09-20
- **Context**: Development session

### LoginForm → AuthService
- **Connection Type**: service_call
- **Purpose**: User login authentication
- **Data Flow**: See implementation
- **Dependencies**: Direct connection
- **Added**: 2025-09-20
- **Context**: Development session

### API Gateway → AuthMiddleware
- **Connection Type**: service_call
- **Purpose**: Request authorization check
- **Data Flow**: See implementation
- **Dependencies**: Direct connection
- **Added**: 2025-09-20
- **Context**: Development session

### TokenService → AuthService
- **Connection Type**: service_call
- **Purpose**: Token refresh validation
- **Data Flow**: See implementation
- **Dependencies**: Direct connection
- **Added**: 2025-09-20
- **Context**: Development session

### Service Integration Pattern
**Discovered**: 2025-09-20
**Pattern**: Multiple service integrations detected
**Usage**: Use for microservice communication
**Integration Points**: N/A
