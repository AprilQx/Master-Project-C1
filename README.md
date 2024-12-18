# dual_autodiff


Dual number automatic differentiation package for Python.

## Documentation

Full documentation is available at: 

## Quick Start
```python
from dual_autodiff import Dual

x = Dual(2.0, 1.0)
y = x * x 
print(f"Value: {y.real}")     # 4.0
print(f"Derivative: {y.dual}") # 4.0
```

## Installation

```bash
pip install -e .
```

# Appendix: Declaration of AI Tool Usage

As required by the course policy on AI tool usage, I declare the following use of AI assistance in this project:

Areas where AI assistance was utilized:
1. Initial project structure consultation and best practices review
2. Documentation string templates and formatting suggestions
3. Code review feedback
4. Test case identification and coverage suggestions

I confirm that:
- All AI-generated suggestions were carefully reviewed and validated before use
- No direct code generation was used for core functionality
- The mathematical implementation and logic were developed independently
- I maintain complete understanding of all project components
- All code has been independently tested and verified

The use of AI tools was limited to supportive purposes only and not as a substitute for my own understanding or implementation. I take full responsibility for all work submitted and can explain any aspect of the implementation in detail.
