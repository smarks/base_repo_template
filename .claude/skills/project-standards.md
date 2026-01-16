## Code Reuse (Strictly Enforced)
- Before writing any new function, search the codebase for similar logic
- If you find similar code, refactor it into a shared utility in `common/`
- Templates: use `{% include %}` and `{% block %}` inheritance, never duplicate HTML
- Views: use mixins in `common/mixins.py` for shared behavior
- Forms: inherit from base form classes when fields repeat

# Project Development Standards

## Python Conventions
- Python 3.11+ features are acceptable
- Type hints on all function signatures and return types
- Docstrings in Google format for public functions and classes
- Use dataclasses or Pydantic for data structures, not plain dicts
- Prefer pathlib over os.path
- Use f-strings, not .format() or %

## Django Patterns
- Class-based views for anything beyond trivial endpoints
- Django REST Framework for APIs with ViewSets
- Fat models, thin views—business logic belongs in models or services
- Use Django's ORM; raw SQL only when performance requires it
- Migrations should be atomic and reversible when possible
- Settings split: base.py, local.py, production.py
- Environment variables via django-environ or python-decouple

## Database
- PostgreSQL assumed
- Indexes on foreign keys and frequently queried fields
- Use select_related/prefetch_related to avoid N+1 queries
- Explicit db_index=True on model fields that get filtered

## Testing
- pytest with pytest-django, not unittest
- Fixtures over setUp methods
- Factory Boy for test data
- Tests mirror source structure in tests/ directory
- Aim for testing behavior, not implementation

## Code Style
- Black for formatting (line length 88)
- isort for import sorting (black-compatible profile)
- ruff for linting
- After writing or modifying code, run `ruff check --fix` to autofix lint errors
- No wildcard imports
- Imports grouped: stdlib, third-party, local

## Git
- Conventional commits: fix:, docs:, refactor:, test:, chore:
- Feature branches off main
- Squash commits on merge when appropriate
- Meaningful commit messages that explain why, not just what

## Documentation
- README.md with setup instructions
- API endpoints documented (OpenAPI/Swagger preferred)
- Complex logic gets inline comments explaining intent

## Error Handling
- Specific exceptions, not bare except:
- Log errors with context (logger.exception preferred)
- User-facing errors should be helpful, not technical

## Security
- No secrets in code—use environment variables
- Input validation on all user data
- CSRF protection enabled
- SQL injection prevention via ORM (no raw string interpolation)