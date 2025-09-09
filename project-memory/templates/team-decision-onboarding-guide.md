# Team Decision Making Onboarding Guide

*Get your team up and running with systematic convention decisions in 2 weeks*

## Week 1: Foundation Setup

### Day 1: Framework Introduction (1 hour)
**Goal**: Team understands the AI DevOps Framework and decision-making approach

**Team Lead Tasks**:
- [ ] Present framework overview (15 min)
- [ ] Show conventions.md structure and purpose (10 min)  
- [ ] Demonstrate individual preferences setup (15 min)
- [ ] Explain team vs individual hierarchy (10 min)
- [ ] Q&A and initial concerns (10 min)

**Key Message**: "We're moving from ad-hoc decisions to systematic team conventions. Individual preferences still matter, but team decisions come first."

**Materials Needed**:
- Framework README.md walkthrough
- Example conventions.md from similar team
- Individual preference template

### Day 2-3: Critical Decision Identification (2 hours)
**Goal**: Identify what decisions your team needs to make first

**Activity**: Team Decision Audit
```markdown
## Current State Assessment

**Technology Stack Gaps** (What we haven't standardized):
- [ ] Backend framework: [Current mix of approaches]
- [ ] Frontend framework: [Current mix of approaches]  
- [ ] Database choices: [Current inconsistencies]
- [ ] Testing frameworks: [Current variations]

**Process Inconsistencies** (Where we work differently):
- [ ] Git workflows: [Different branching strategies in use]
- [ ] Code review practices: [Inconsistent approval processes]
- [ ] Deployment approaches: [Different methods per project]
- [ ] Documentation standards: [Varying levels of docs]

**Style Conflicts** (Where we disagree or vary):
- [ ] Naming conventions: [CamelCase vs snake_case debates]
- [ ] Function organization: [File structure differences]  
- [ ] Comment styles: [Some heavy, some minimal]
- [ ] Error handling: [Different exception patterns]

**Tool Fragmentation** (Where we use different tools):
- [ ] Code editors: [VS Code vs others]
- [ ] Package managers: [npm vs yarn vs pnpm]
- [ ] Linting/formatting: [Different ESLint configs]
- [ ] Local development: [Docker vs native vs cloud]
```

**Output**: Prioritized list of decisions needed for team consistency

### Day 4-5: Decision Authority Setup (1 hour)
**Goal**: Establish who makes what decisions and how

**Team Authority Matrix**:
```markdown
| Decision Type | Final Authority | Required Input | Timeline |
|---------------|-----------------|-----------------|----------|
| Architecture | [Technical Lead Name] | All senior devs | 1-2 weeks |
| Security | [Security Lead/Tech Lead] | Tech lead + team | 1 week |
| Process | Team majority vote | All team members | 2 weeks |
| Style/Tools | [Tech Lead with team input] | Team preferences | 1 week |
| Emergency | [On-call lead] | Document after | 24 hours |
```

**Team Lead Selection** (if not already clear):
- Technical Lead: [Name] - Architecture and tech stack decisions
- Process Lead: [Name] - Workflow and team process decisions  
- Security Lead: [Name/Tech Lead] - Security standards and reviews

## Week 2: First Decision Cycle

### Day 6-8: Priority Decision #1 - Backend Technology
**Goal**: Make your first team decision using the systematic process

**Using the Framework**:
1. **Create proposal** using convention-decision-templates.md
2. **Team discussion** for 2-3 days
3. **Vote using** team-decision-voting-system.md process  
4. **Document decision** with decision-documentation-format.md
5. **Update conventions.md** with new team standard

**Example First Decision** - Backend Framework:
```markdown
## Backend Technology Decision Workshop

**Problem**: Team using mix of Node.js Express, Python Flask, and considering FastAPI

**Proposed Process**:
- Day 6: Technical Lead presents options with pros/cons research
- Day 7-8: Team discussion via Slack/GitHub with input collection
- Day 8 end: Team vote using agreed voting method
- Day 9: Decision documented and conventions.md updated

**Decision Template Used**: convention-decision-templates.md > Technology Stack Decision
**Voting Method**: Based on team size (2-5: in-person, 6+: GitHub Discussion)
**Documentation**: Full decision record in project-memory/decisions/
```

### Day 9-10: First Decision Implementation
**Goal**: Turn decision into active convention and verify Claude compliance

**Implementation Checklist**:
- [ ] Decision documented in project-memory/decisions/YYYY-MM-tech-backend.md
- [ ] Convention added to project-memory/conventions.md with examples
- [ ] Team notified via preferred communication channel
- [ ] Development tools updated (package.json, linting, etc.)
- [ ] Claude tested with new convention (ask for backend recommendation)

**Convention Format Example**:
```markdown
## Backend Development Standards  
**Decision Made**: 2024-09-09 (Team technology selection)
**Technology**: Node.js + Express + TypeScript + PostgreSQL
**Rationale**: Team JavaScript expertise, unified language stack, mature ecosystem
**Apply To**: All new backend services starting [date]

```typescript
// Standardized API response format
interface APIResponse<T> {
  success: boolean;
  data?: T;
  error?: { code: string; message: string; };
  timestamp: string;
}
```

**Migration Plan**: Existing Python services remain, new development uses Node.js
**Review Date**: 6 months - assess team satisfaction and project outcomes
```

### Day 11-12: Second Priority Decision
**Goal**: Demonstrate the process works smoothly and build team confidence

**Suggested Second Decision**: Code Style Standards
- Lower stakes than architecture
- Immediate visible impact  
- Easy to implement and enforce
- Good practice for voting/consensus process

**Process Acceleration**:
- Use lessons learned from first decision
- Apply templates more efficiently
- Focus on decision quality over process perfection

## Onboarding Success Metrics

### Week 1 Success Indicators
- [ ] **Team understands framework**: No major conceptual questions remaining
- [ ] **Individual preferences setup**: Each developer has personal-conventions.md configured  
- [ ] **Decision priorities clear**: Team agrees on what needs standardizing first
- [ ] **Authority established**: No confusion about who decides what

### Week 2 Success Indicators  
- [ ] **First decision completed**: Full process from problem → documentation → implementation
- [ ] **Convention active**: Claude properly applies new team standard
- [ ] **Team confidence**: Process felt systematic rather than chaotic
- [ ] **Second decision smoother**: Less process overhead, focus on content

### 30-Day Follow-up Indicators
- [ ] **Decisions being followed**: Team actually uses established conventions
- [ ] **Framework integrated**: Decision-making feels natural, not forced
- [ ] **Individual/team balance working**: Developers understand when each applies
- [ ] **Quality improvement visible**: More consistency in code/process

## Common Onboarding Challenges

### Challenge: "This feels like too much overhead"
**Response**: 
- Start with decisions causing current pain/conflict
- Use quick decision format for low-impact choices
- Show time saved by avoiding repeated "how should we..." discussions

### Challenge: "What if we make the wrong decision?"
**Response**:
- Emphasize review dates and amendment process
- Show rollback plans in decision documentation
- Frame as "best decision with current information" not "perfect decision"

### Challenge: "Individual developers lose autonomy"  
**Response**:
- Clarify team decisions only apply where standardization helps
- Show individual preferences still apply for personal productivity tools
- Demonstrate pattern elevation process (individual → team when valuable)

### Challenge: "Too many meetings/discussions"
**Response**:
- Use asynchronous tools (GitHub Discussions, Slack polls)
- Set clear timelines to avoid endless discussion
- Template approaches to reduce decision overhead

## Team Size Adaptations

### Small Team (2-5 developers)
**Simplifications**:
- Fewer formal voting requirements
- More in-person/synchronous decisions  
- Technical Lead can make more decisions unilaterally
- Lighter documentation for obvious choices

**Timeline**: Can complete onboarding in 1 week

### Medium Team (6-12 developers)  
**Standard Process**: Follow guide as written
**Timeline**: 2 weeks as outlined

### Large Team (13+ developers)
**Extensions**:
- Add working groups for complex decisions
- More structured RFC process for major choices
- Longer discussion timelines  
- More formal voting platforms

**Timeline**: 3-4 weeks with extended discussion phases

## Post-Onboarding: Monthly Decision Hygiene

### Monthly Team Decision Review (30 minutes)
**Agenda**:
- Review decisions made this month
- Assess effectiveness of existing conventions
- Identify new decisions needed  
- Update conventions.md if needed

**Questions**:
- Which conventions are team actually following?
- Where are we still making ad-hoc decisions?  
- What's working well vs. causing friction?
- Any individual patterns worth elevating to team standard?

### Quarterly Convention Assessment (1 hour)
- Full review of all active conventions  
- Decision effectiveness metrics
- Framework process improvements
- New team member feedback integration

---

*This guide gets teams from chaos to systematic decision-making in 2 weeks, with ongoing processes to maintain decision quality and convention effectiveness.*