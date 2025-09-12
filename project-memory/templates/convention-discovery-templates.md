# Convention Discovery Templates

Templates for systematically identifying and documenting missing conventions for different types of development requests.

## Architecture & Backend Conventions

### **Authentication Systems**
```markdown
## Authentication Convention Decisions Required

I need the following convention decisions before implementing authentication:

🏗️ **Authentication Method**
- JWT tokens (stateless, scalable)
- Session-based (server-side state)  
- OAuth integration (Google, GitHub, etc.)

🔒 **Security Configuration**
- Token expiration: 15min, 1hr, 24hr, custom?
- Password requirements: complexity rules?
- Rate limiting: attempts per IP/user?

📊 **Data Storage**
- User data location: database table structure?
- Session storage: Redis, database, memory?
- Audit logging: security events tracking?

**Impact**: These decisions affect security posture, scalability, and integration patterns for all future authentication features.
```

### **Database & Data Architecture**
```markdown
## Database Convention Decisions Required

🗄️ **Database Technology**
- PostgreSQL (ACID compliance, JSON support)
- MySQL (performance, widespread support)
- MongoDB (document flexibility)

🏗️ **Architecture Pattern**
- Single database (simple, consistent)
- Database per service (microservices)
- Read replicas (performance scaling)

📋 **Data Conventions**
- Naming: camelCase, snake_case, PascalCase?
- Timestamps: UTC storage, timezone handling?
- IDs: UUIDs, auto-increment, custom format?

**Impact**: Database decisions affect performance, scalability, and development patterns across all data-driven features.
```

## Frontend & UI Conventions

### **React/Frontend Framework**
```markdown
## Frontend Convention Decisions Required

⚛️ **Framework & Architecture**
- React version: 17, 18, latest?
- State management: Context, Redux, Zustand?
- Routing: React Router, Next.js, custom?

🎨 **Styling Approach**
- CSS approach: CSS Modules, Styled Components, Tailwind?
- Component library: Material-UI, Ant Design, custom?
- Responsive strategy: mobile-first, desktop-first?

🧪 **Development Patterns**
- Component structure: containers/presentational?
- Testing approach: Jest, React Testing Library, Cypress?
- Bundle strategy: Webpack, Vite, Create React App?

**Impact**: Frontend conventions ensure consistent user experience and development patterns across all UI components.
```

### **UI/UX Design System**
```markdown
## Design System Convention Decisions Required

🎨 **Visual Design Standards**
- Color palette: primary, secondary, accent colors?
- Typography: font families, size scale, weights?
- Spacing system: 4px, 8px grid, custom scale?

♿ **Accessibility Requirements**
- WCAG compliance level: AA, AAA?
- Screen reader support: required features?
- Keyboard navigation: tab order, shortcuts?

📱 **Responsive Design**
- Breakpoints: mobile, tablet, desktop definitions?
- Layout patterns: flexbox, grid, hybrid?
- Device support: minimum browser versions?

**Impact**: Design system decisions create consistent user experience and accessibility compliance across all interfaces.
```

## API & Integration Conventions

### **API Design Standards**
```markdown
## API Convention Decisions Required

🌐 **API Architecture**
- Style: REST, GraphQL, RPC?
- Versioning: URL path, headers, query params?
- Authentication: JWT, API keys, OAuth?

📊 **Data Format Standards**
- Response format: JSON, JSON-API, custom?
- Date formats: ISO 8601, Unix timestamps?
- Error handling: status codes, error objects?

🔒 **Security & Performance**
- Rate limiting: requests per minute/hour?
- CORS policy: allowed origins, methods?
- Caching strategy: ETags, cache headers?

**Impact**: API conventions ensure consistent integration patterns and developer experience across all services.
```

## Security & Compliance Conventions

### **Security Framework**
```markdown
## Security Convention Decisions Required

🔐 **Security Standards**
- Framework: OWASP Top 10, NIST, custom?
- Encryption: algorithms, key management?
- Audit requirements: logging, monitoring?

🛡️ **Access Control**
- Authorization model: RBAC, ABAC, custom?
- Permission granularity: resource, action level?
- Multi-factor auth: TOTP, SMS, email?

📋 **Compliance Requirements**
- Data protection: GDPR, CCPA, industry-specific?
- Retention policies: data lifecycle, deletion?
- Third-party integrations: security vetting?

**Impact**: Security conventions establish non-negotiable baseline for all application security and compliance requirements.
```

## DevOps & Deployment Conventions

### **Deployment & Infrastructure**
```markdown
## DevOps Convention Decisions Required

🚀 **Deployment Strategy**
- Platform: AWS, Azure, GCP, on-premise?
- Containerization: Docker, Kubernetes, serverless?
- CI/CD pipeline: GitHub Actions, Jenkins, custom?

🔧 **Environment Management**
- Environments: dev, staging, prod, others?
- Configuration: environment variables, config files?
- Secrets management: HashiCorp Vault, cloud native?

📊 **Monitoring & Observability**
- Logging: structured, centralized, retention?
- Metrics: application, infrastructure, business?
- Alerting: thresholds, escalation, on-call?

**Impact**: DevOps conventions establish operational consistency and reliability patterns for all deployments.
```

## Convention Decision Format

### **Template for Documenting Decisions**
```markdown
## Convention Decision: [Feature Area] - [Date]

**Context**: [What development work required this decision]

**Options Considered**:
1. **Option A**: [Description, pros/cons]
2. **Option B**: [Description, pros/cons]  
3. **Option C**: [Description, pros/cons]

**Decision**: [Chosen option with rationale]

**Decision Maker**: [Who made the decision]

**Scope**: [This project only / All similar projects / Organization-wide]

**Implementation Notes**: [Any specific implementation guidance]

**Dependencies**: [Other conventions or systems this affects]

**Review Date**: [When to reconsider this decision]
```

## Usage Instructions

1. **Identify Feature Type** - Match user request to relevant template
2. **Present Missing Conventions** - Show user only the gaps in their current conventions
3. **Request Specific Decisions** - Ask targeted questions from relevant template
4. **Document Immediately** - Use decision format to codify choices
5. **Reference in Future** - Apply established conventions to similar requests

These templates ensure systematic convention discovery while avoiding overwhelming users with irrelevant decisions.