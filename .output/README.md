# Project Output Directory

This directory contains the actual projects and deliverables created through AI agent orchestration.

## Structure

Each project gets its own subdirectory with organized outputs:

```
.output/
├── project-name/
│   ├── code/                    # Implementation files
│   ├── documentation/           # Generated docs
│   ├── analysis/               # Consultation outputs
│   ├── decisions/              # Architecture and design decisions
│   └── session-log.md          # Record of agent coordination
├── another-project/
│   └── ...
└── shared/
    ├── templates/              # Reusable patterns
    ├── components/             # Shared code components
    └── learnings/              # Cross-project insights
```

## Project Creation

When Claude starts a new development task:

1. **Creates project directory**: `.output/project-name/`
2. **Sets up structure**: Code, docs, analysis, decisions folders
3. **Initializes session log**: Records agent coordination and decisions
4. **Applies orchestration**: Consultation → production workflow
5. **Delivers organized output**: All artifacts in appropriate folders

## Session Logging

Each project maintains a `session-log.md` that records:
- Agent coordination decisions
- Quality validation results
- Conflict resolutions
- Architecture choices and rationale
- Lessons learned for future projects

## Cross-Project Learning

The `shared/` directory captures:
- **Templates**: Successful patterns for reuse
- **Components**: Reusable code artifacts  
- **Learnings**: Insights that improve future orchestration

This creates an **institutional memory** that makes each project better than the last.

## Workbench Benefits

- **Organized output** - No more scattered files
- **Project isolation** - Clean separation between different work
- **Audit trail** - Complete record of how decisions were made
- **Learning capture** - Patterns and insights for future use
- **Portfolio building** - Collection of systematically developed projects