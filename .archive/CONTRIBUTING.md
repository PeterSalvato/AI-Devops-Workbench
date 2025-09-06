# Contributing to AI DevOps Framework

We welcome contributions to make AI development more systematic and production-ready! 

## How to Contribute

### **Areas Where We Need Help**

1. **Example Agents** - Create more demo agents showing different capabilities
2. **Documentation** - Improve guides, examples, and explanations
3. **Framework Integrations** - Connect with LangChain, AutoGPT, etc.
4. **Testing** - Add test coverage and validation frameworks
5. **Performance** - Optimize orchestration and agent coordination

### **What We're NOT Looking For**

- Production agent configurations (these remain proprietary)
- Expert methodology implementations (available through consulting)
- Client-specific workflows or customizations

## Getting Started

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Make your changes**
4. **Add tests** if applicable
5. **Update documentation** as needed
6. **Submit a pull request**

## Development Guidelines

### **Code Style**
- Follow PEP 8 for Python code
- Use descriptive variable and function names
- Add docstrings for all public functions
- Keep functions focused and small

### **Agent Development**
- Use the standard JSON schema format (see `src/agents/examples/`)
- Include clear capability descriptions
- Provide example usage
- Add quality validation logic

### **Documentation**
- Write clear, concise explanations
- Include code examples
- Test all examples before submitting
- Use consistent formatting

## Testing

Run the test suite before submitting:

```bash
python -m pytest tests/
python -m pytest tests/ --cov=src
```

## Bug Reports

When reporting bugs, please include:

1. **Clear description** of the issue
2. **Steps to reproduce** the problem
3. **Expected vs actual behavior**
4. **Environment details** (Python version, OS, etc.)
5. **Minimal code example** if possible

## Feature Requests

For feature requests:

1. **Explain the problem** you're trying to solve
2. **Describe your proposed solution**
3. **Consider backwards compatibility**
4. **Be open to alternative approaches**

## Questions?

- **Framework questions**: Open an issue
- **Implementation help**: Check the documentation first
- **Consulting/production needs**: Open an issue or discussion

## Recognition

Contributors will be:
- Added to the README contributors section
- Mentioned in release notes
- Invited to provide feedback on major changes

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping make AI development more systematic and production-ready!