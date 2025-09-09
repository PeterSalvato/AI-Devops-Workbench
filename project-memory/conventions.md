# Team Conventions & Architectural Decisions

*Team-wide architectural decisions and coding standards that Claude applies consistently across all development work. These conventions are shared across all team members and take precedence over individual preferences.*

**Priority**: HIGHEST - Team conventions override individual preferences  
**Scope**: All team members must follow these decisions  
**Updates**: Requires team consensus or technical lead approval  
**Updated**: 2024-09-09 (automatically maintained by Claude during development sessions)

## Technology Stack Preferences

### Backend Development Standards
**Decision Made**: 2024-08-15 (E-commerce project)  
**Technology**: Node.js + Express + TypeScript + PostgreSQL  
**Rationale**: Team expertise, mature ecosystem, TypeScript safety  
**Apply To**: All backend services and APIs  

```typescript
// Standardized API response format
interface APIResponse<T> {
  success: boolean;
  data?: T;
  error?: {
    code: string;
    message: string;
    details?: any;
  };
  timestamp: string;
}
```

### Frontend Development Standards
**Decision Made**: 2024-08-10 (Customer portal project)  
**Technology**: React + TypeScript + Next.js + Tailwind CSS  
**Rationale**: SSR performance needs, design system compatibility  
**Apply To**: All user-facing applications  

```typescript
// Component structure standard
interface ComponentProps {
  className?: string;
  children?: React.ReactNode;
  testId?: string;
}
```

### Database Standards
**Decision Made**: 2024-08-15 (E-commerce architecture)  
**Pattern**: PostgreSQL primary + Redis caching, database-per-service  
**Rationale**: Data consistency + service autonomy + proven reliability  
**Apply To**: All microservices data architecture  

```sql
-- Naming conventions
-- Tables: snake_case (user_accounts, order_items)
-- Indexes: idx_tablename_columnname
-- Foreign keys: fk_tablename_referencedtable
```

## Security Standards

### Authentication Requirements  
**Decision Made**: 2024-09-06 (User auth system)  
**Standard**: JWT + OAuth2 + TOTP 2FA for admin roles  
**Implementation**: 15-min access tokens, 30-day refresh with rotation  
**Apply To**: All authentication systems  

```typescript
// JWT payload standard
interface JWTPayload {
  userId: string;
  email: string;
  role: 'admin' | 'user' | 'guest';
  permissions: string[];
  mfaVerified: boolean;
  iat: number;
  exp: number;
}
```

### API Security Requirements
**Decision Made**: 2024-09-01 (Partner API project)  
**Standard**: OAuth2 client credentials + comprehensive rate limiting + audit logging  
**Rate Limits**: 1000 req/hr per API key, 100 req/min per endpoint  
**Apply To**: All external-facing APIs  

### Frontend Security Standards
**Decision Made**: 2024-08-20 (Customer web app)  
**Standard**: Content Security Policy + SameSite cookies + security headers  
**CSP**: Strict with nonce-based script loading  
**Apply To**: All customer-facing applications

### Password Security Standards
**Decision Made**: 2024-09-09 (Password complexity implementation)  
**Standard**: Minimum 12 characters with uppercase, lowercase, numbers, and special characters  
**Implementation**: Centralized validatePasswordComplexity() function with configurable rules  
**Apply To**: All authentication systems and password change functionality  

```typescript
// Password complexity standard
const DEFAULT_PASSWORD_RULES = {
  minLength: 12,
  requireUppercase: true,
  requireLowercase: true, 
  requireNumbers: true,
  requireSpecialChars: true
};
```

## Code Quality Standards

### Code Style Preferences  
**Decision Made**: 2024-07-20 (Team standardization)  
**Standards**: Prettier + ESLint + strict TypeScript  
**Naming**: camelCase variables, PascalCase components, UPPER_SNAKE_CASE constants  
**Apply To**: All JavaScript/TypeScript code  

```typescript
// File naming conventions
// Components: UserProfile.tsx
// Utilities: dateUtils.ts  
// Constants: API_ENDPOINTS.ts
// Types: userTypes.ts

// Function naming standard
const calculateTotalPrice = (items: CartItem[]): number => {
  // Implementation
};

// Component naming standard  
const UserProfileCard: React.FC<UserProfileProps> = ({ user }) => {
  // Implementation
};
```

### Testing Requirements
**Decision Made**: 2024-08-05 (Quality improvement initiative)  
**Standards**: Jest + Testing Library, 80% coverage minimum  
**Structure**: Separate test files, descriptive test names  
**Apply To**: All production code  

```typescript
// Test file naming: UserProfile.test.tsx
describe('UserProfile Component', () => {
  it('should display user name when user data is provided', () => {
    // Test implementation
  });

  it('should handle missing user data gracefully', () => {
    // Test implementation  
  });
});
```

### Documentation Requirements
**Decision Made**: 2024-08-25 (Team onboarding improvement)  
**Standards**: JSDoc for functions, README for modules, API docs for endpoints  
**Level**: Public APIs documented, complex logic explained  
**Apply To**: All shared code and modules  

```typescript
/**
 * Calculates the total price including tax and discounts
 * @param items - Array of cart items to calculate total for
 * @param taxRate - Tax rate as decimal (0.08 for 8%)
 * @param discountCode - Optional discount code to apply
 * @returns Total price with tax and discounts applied
 */
const calculateTotal = (
  items: CartItem[], 
  taxRate: number, 
  discountCode?: string
): number => {
  // Implementation
};
```

## Development Process Standards

### Git Workflow Preferences  
**Decision Made**: 2024-07-15 (Team collaboration improvement)  
**Standard**: Feature branches + PR reviews + squash merging  
**Branch Naming**: feature/TICKET-123-description, bugfix/issue-description  
**Apply To**: All repositories  

```bash
# Branch naming examples
git checkout -b feature/AUTH-456-implement-2fa
git checkout -b bugfix/payment-validation-error  
git checkout -b hotfix/security-vulnerability-fix
```

### Error Handling Standards
**Decision Made**: 2024-09-03 (Production reliability improvement)  
**Standard**: Structured error objects, comprehensive logging, user-friendly messages  
**Logging**: Winston with structured JSON, correlation IDs  
**Apply To**: All backend services and critical frontend functions  

```typescript
// Error handling standard
class APIError extends Error {
  constructor(
    public code: string,
    message: string,
    public statusCode: number = 500,
    public details?: any
  ) {
    super(message);
    this.name = 'APIError';
  }
}

// Usage example
try {
  await processPayment(paymentData);
} catch (error) {
  logger.error('Payment processing failed', {
    correlationId,
    userId,
    error: error.message,
    details: error.details
  });
  
  throw new APIError(
    'PAYMENT_FAILED', 
    'Unable to process payment at this time',
    400,
    { originalError: error.message }
  );
}
```

---

*This conventions file is automatically updated by Claude when you make architectural decisions during development. It ensures consistent application of your preferences across all projects, preventing "vibecoding" and maintaining enterprise-grade consistency.*

---

*This document is automatically updated based on project learnings and coordination experiences. Last updated: [Date will be auto-updated by Claude during sessions]*