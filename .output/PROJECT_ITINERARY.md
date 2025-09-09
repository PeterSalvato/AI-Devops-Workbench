# Project Itinerary

*Active project tracking for the AI DevOps Framework*

## Current Projects in Progress

*No active projects currently*

---

## Project Status Definitions

### 🟢 Active Projects
**Status: `ACTIVE`** - Currently being worked on with assigned team leads and specialists
- Team leads dispatched and managing specialists  
- Regular progress updates and coordination
- Expected completion timeline defined

### 🟡 Planning Projects  
**Status: `PLANNING`** - Requirements gathered, consultation phase in progress
- Human requirements documented
- Consultation team leads analyzing and designing
- Implementation strategy being developed

### 🔵 Queued Projects
**Status: `QUEUED`** - Approved projects waiting for resource availability
- Human requirements documented and approved
- Waiting for consultation team lead availability
- Priority order established

### 🟣 Blocked Projects
**Status: `BLOCKED`** - Projects waiting for external dependencies or decisions
- Waiting for human approval on major decisions
- External dependency or integration blockers
- Resource or timeline constraint issues

### ✅ Completed Projects
**Status: `COMPLETED`** - Fully delivered and validated projects
- All quality gates passed
- Production-ready deliverables in `.output/project-name/`
- Final validation and sign-off completed

---

## Project Entry Template

```markdown
### Project: [Project Name]
**Status**: [PLANNING/ACTIVE/QUEUED/BLOCKED/COMPLETED]
**Priority**: [High/Medium/Low]
**Started**: [Date]
**Expected Completion**: [Date/TBD]

**Assigned Team Leads**:
- Senior Architect: [Assigned/Not Needed]
- Security Consultant: [Assigned/Not Needed]  
- UX Strategist: [Assigned/Not Needed]

**Active Specialists**:
- Backend Builder: [Status]
- Frontend Builder: [Status]
- Security Implementer: [Status]
- CSS Specialist: [Status]

**Current Phase**: [Requirements/Analysis/Design/Implementation/Validation/Complete]

**Progress Summary**:
- [Brief progress update]
- [Current blockers or issues]
- [Next steps]

**Output Location**: `.output/project-name/`

---
```

## Role-Based Usage Instructions

### 👤 Human Decision Maker (Level 1) - How to Use This Document

**Daily/Weekly Review:**
- **Scan project statuses** to understand current workload and progress
- **Review blocked projects** - these need your decisions or approvals
- **Check high-priority active projects** for timeline concerns
- **Identify resource bottlenecks** when multiple projects compete for same specialists

**When Adding New Projects:**
- Tell Claude: *"Add [project name] to the itinerary with [priority level]"*
- Provide clear requirements and timeline expectations
- Specify if this project should take priority over existing work

**When Projects Are Blocked:**
- Review the blocker description in the project entry
- Make required business decisions or provide approvals
- Tell Claude: *"Unblock [project name] - [your decision/approval]"*

**Priority Management:**
- Tell Claude: *"Reprioritize projects - [project A] is now High priority"*
- Approve resource reallocation when specialists are needed elsewhere
- Set timeline expectations: *"[Project name] needs to be completed by [date]"*

---

### 🤖 Claude Meta-Orchestrator (Level 2) - How to Use This Document

**Session Start:**
- **Always read PROJECT_ITINERARY.md first** to understand current project landscape
- **Update status** of any projects worked on in previous sessions
- **Check for resource conflicts** before assigning new specialists
- **Review blocked projects** and determine if any can be unblocked

**When Starting New Projects:**
1. Add project to itinerary as `QUEUED` with human-provided requirements
2. Create project repository structure in `.output/project-name/`
3. Analyze project needs and assign consultation team leads
4. Update status to `PLANNING` with team lead assignments

**During Project Execution:**
- **Update project phases** as teams progress (Requirements → Analysis → Design → Implementation → Validation)
- **Track specialist assignments** and dispatch status
- **Monitor cross-project dependencies** and coordination needs
- **Document blockers immediately** with clear escalation needs

**Session End:**
- **Update all active project statuses** with current progress
- **Document any new blockers** discovered during the session
- **Update expected completion dates** based on progress
- **Note any quality concerns** or resource needs

**Conflict Resolution:**
- **Resource conflicts**: Document in itinerary, escalate to human for priority decisions
- **Technical conflicts**: Work with team leads, document resolution in session logs
- **Timeline conflicts**: Update expectations, escalate if human decision needed

---

### 🎯 Consultation Team Leads (Level 3) - How to Use This Document

**Project Assignment:**
- **Review project entry** to understand scope, requirements, and timeline
- **Check resource availability** for your team specialists
- **Coordinate with other team leads** on shared dependencies
- **Update your assignment status** through Claude meta-orchestrator

**During Analysis/Design Phase:**
- **Request project status updates** through Claude when milestones are completed
- **Identify specialist needs** and resource requirements for implementation
- **Document dependencies** on other teams or external factors
- **Escalate blockers** that prevent progress

**When Dispatching Specialists:**
- **Confirm specialist availability** before assignment
- **Provide clear specifications** and quality requirements
- **Establish check-in cadence** for progress monitoring
- **Coordinate integration points** with other teams

**Quality Validation:**
- **Update project status** when validation phases complete
- **Document quality concerns** that need escalation
- **Sign off on specialist work** before project completion
- **Recommend project status changes** (ACTIVE → COMPLETED)

---

### 🔧 Production Specialists (Level 4) - How to Use This Document

**Assignment Notification:**
- **Review project entry** to understand your role and scope
- **Check timeline expectations** and delivery requirements
- **Understand integration points** with other specialists
- **Confirm availability** and resource needs with team lead

**During Implementation:**
- **Request status updates** through your team lead when milestones are reached
- **Report blockers immediately** that prevent progress (dependencies, requirements clarity, resource needs)
- **Coordinate with other specialists** on shared interfaces and integration
- **Escalate quality concerns** or technical issues through team lead

**Progress Communication:**
- **Provide regular updates** to team lead on implementation progress
- **Document technical decisions** in project session logs
- **Request clarification** on requirements or specifications when needed
- **Report completion** of assigned work for team lead validation

### Project Lifecycle Management:
1. **New Project Request** → Add as `QUEUED` with human requirements
2. **Resource Assignment** → Move to `PLANNING` with consultation team leads
3. **Implementation Start** → Move to `ACTIVE` with specialists dispatched
4. **External Blockers** → Move to `BLOCKED` with escalation to human
5. **Quality Validation** → Final validation phase before `COMPLETED`
6. **Project Delivery** → Move to `COMPLETED` with final deliverables

### Resource Conflict Resolution:
- **Senior Architect**: Can manage multiple projects simultaneously (analysis/coordination)
- **Security Consultant**: Can manage multiple projects simultaneously (analysis/validation)
- **Production Specialists**: Generally one active project per specialist
- **Cross-project coordination**: Senior architect coordinates shared integration points

---

*This itinerary is maintained by Claude meta-orchestrator and provides visibility into active development work across the AI DevOps Framework.*