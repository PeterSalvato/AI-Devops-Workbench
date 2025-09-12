# Convention-Driven Workflow Example

Real demonstration of how the convention discovery system works with a typical development request.

## Example Request: "Build user authentication with 2FA"

### **Step 1: Context Loading**
```
✅ Reading project-memory/conventions.md...
✅ Reading project-memory/symbol-index.md...  
✅ Reading .output/PROJECT_ITINERARY.md...
```

### **Step 2: Workplan Analysis**
```
ANALYZING REQUEST: "Build user authentication with 2FA"

REQUIRED CONVENTIONS IDENTIFIED:
🏗️ Architecture: Authentication method, Session management
🔒 Security: Password policies, 2FA approach, Token expiration  
📊 Database: User data storage, Audit logging
🌐 API: Authentication endpoints, Error handling
📱 Frontend: Login UI, Session state management
```

### **Step 3: Convention Gap Analysis**
```
CHECKING EXISTING CONVENTIONS (project-memory/conventions.md):

✅ DOCUMENTED:
- Database Technology: PostgreSQL (decided 2025-01-10)
- API Style: REST with JSON responses (decided 2025-01-05)
- Frontend Framework: React 18 with TypeScript (decided 2025-01-08)

❌ MISSING CONVENTIONS NEEDED:
- Authentication method (JWT vs Sessions vs OAuth)
- 2FA approach (TOTP vs SMS vs Email)  
- Password security policies
- Token/session expiration times
- User data schema patterns
```

### **Step 4: Convention Discovery**
```
🛑 PAUSING DEVELOPMENT - Missing Convention Decisions Required

I need to establish 4 key conventions before implementing authentication:

## Authentication Convention Decisions Required

🏗️ **Authentication Method**
Which approach should we use for this project and all future authentication?

A) **JWT Tokens** (stateless, scalable, mobile-friendly)
   - Pro: Scalable, works across services, mobile apps
   - Con: Token revocation complexity, larger payload

B) **Session-based** (server-side state, simpler revocation)  
   - Pro: Easy revocation, smaller cookies, familiar pattern
   - Con: Server state, scaling challenges, CSRF considerations

C) **OAuth Integration** (delegate to Google/GitHub/etc.)
   - Pro: No password management, established security
   - Con: Third-party dependency, integration complexity

🔒 **2FA Security Approach**  
How should we handle two-factor authentication?

A) **TOTP (Time-based)** - Google Authenticator, Authy apps
B) **SMS Codes** - Text message verification  
C) **Email Codes** - Email-based verification

🔐 **Security Policies**
What password and session policies should we enforce?

- Password requirements: Length, complexity, special characters?
- Session duration: 15 minutes, 1 hour, 24 hours, "remember me"?
- Failed login handling: Lockout after how many attempts?

🗄️ **User Data Schema**
How should we structure user authentication data?

- User table structure: email, username, both as login?
- Audit logging: Track login attempts, password changes?
- Profile data: Separate user profile table or combined?

**IMPACT**: These decisions will:
- Define security posture for entire application
- Establish patterns for all future authentication features  
- Determine integration complexity with frontend and mobile
- Set compliance baseline for audit and regulatory requirements

Please make these decisions so I can implement consistent authentication across your project.
```

### **Step 5: User Decisions**
```
USER RESPONSE:
"Let's go with JWT tokens for scalability, TOTP for 2FA since it's most secure, 
passwords need 12+ chars with special characters, 15-minute token expiration 
with refresh tokens, lock account after 5 failed attempts, and use separate 
user and profile tables for flexibility."
```

### **Step 6: Convention Codification**
```
✅ UPDATING project-memory/conventions.md:

## Convention Decision: Authentication Architecture - 2025-01-14

**Context**: User authentication system implementation with 2FA support

**Decision**: JWT-based authentication with TOTP 2FA
- **Authentication Method**: JWT tokens with refresh token pattern
- **2FA Approach**: TOTP (Time-based One-Time Password) using authenticator apps
- **Password Policy**: Minimum 12 characters, require special characters and numbers
- **Token Expiration**: 15-minute access tokens, 7-day refresh tokens
- **Security Controls**: Account lockout after 5 failed attempts, unlock after 30 minutes
- **Data Architecture**: Separate users and user_profiles tables for flexibility

**Decision Maker**: [User] **Date**: 2025-01-14  
**Scope**: Organization-wide - applies to all authentication features

**Implementation Notes**: 
- Use bcrypt for password hashing (cost factor 12)
- TOTP secret generation using crypto.randomBytes(32)
- JWT signed with RS256 (RSA + SHA256)
- Refresh token rotation on use
- Audit log all authentication events

**Dependencies**: 
- Database schema design
- Frontend state management patterns
- API error handling standards

**Review Date**: 2025-07-14 (6 months)

✅ CONVENTIONS SAVED - Ready to implement with consistent patterns
```

### **Step 7: Implementation with Conventions**
```
🚀 IMPLEMENTING AUTHENTICATION SYSTEM

APPLYING ESTABLISHED CONVENTIONS:
✅ Database: PostgreSQL with separate users/profiles tables
✅ API: REST endpoints with JWT authentication  
✅ Frontend: React with JWT state management
✅ Security: OWASP-compliant password policies + TOTP 2FA
✅ Architecture: Clean Architecture patterns with dependency injection

COORDINATING MULTI-AGENT IMPLEMENTATION:
→ Senior Architect: Database schema design with JWT patterns
→ Security Consultant: TOTP implementation with audit logging
→ Backend Builder: JWT middleware and authentication endpoints
→ Frontend Builder: Login components with 2FA workflow

DELIVERABLES:
- Production-ready authentication system
- Complete test suite with security validation
- Documentation with implementation decisions
- Future authentication requests use these same patterns automatically
```

## Key Benefits Demonstrated

### **Institutional Memory Building**
- **First Request**: Establishes foundational authentication conventions
- **Future Requests**: "Add social login" automatically uses JWT + TOTP patterns
- **Team Consistency**: All developers follow same authentication approach
- **Decision Rationale**: Why choices were made is preserved for future reference

### **Smart Convention Discovery**  
- **Context-Aware**: Only asked about authentication-relevant decisions
- **Impact-Focused**: Explained how each choice affects implementation
- **Efficient**: Grouped related decisions together
- **Future-Proof**: Decisions apply to similar features automatically

### **Enterprise Governance**
- **User Control**: Developer made all architectural decisions
- **Full Transparency**: Complete audit trail of decisions and rationale  
- **Consistent Application**: Conventions automatically applied to implementation
- **Quality Assurance**: Security and architecture patterns enforced systematically

This workflow transforms from "vibecoding" to systematic engineering with persistent institutional memory.