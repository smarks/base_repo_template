# Tarmar Folio

Django authentication project with user registration, login, and profile management.

## Setup

After cloning, install dependencies and pre-commit hooks:
```bash
uv sync
uv run pre-commit install
bd init  # Initialize task tracking (one time)
```

## Commands
```bash
./run dev         # Start development server (http://127.0.0.1:8000)
./run test        # Run all tests
./run lint        # Lint and auto-fix with ruff
./run format      # Format code with ruff
./run check       # Run all pre-commit checks
./run migrate     # Run database migrations
./run update-cov  # Update coverage threshold
```

## Task Tracking (Beads)
```bash
bd ready                        # Show tasks ready to work on (no blockers)
bd list                         # List all tasks
bd create "title" -p 1 -t task  # Create task (priority 0-3, 0=highest)
bd show bd-xxxx                 # View task details
bd update bd-xxxx --status in_progress  # Start work
bd update bd-xxxx --notes "what you did" # Add progress notes
bd close bd-xxxx --reason "done"         # Complete task
bd stats                        # Project progress
```

- **Use `bd` for all task tracking**, not markdown TODOs or comments
- Before starting work, run `bd ready` to see available tasks
- Update task status and notes as you work
- When blocked, use `bd update bd-xxxx --status blocked --notes "reason"`

## Project Structure
- `accounts/` - Authentication app (models, views, forms, templates)
- `characters/` - Character creation and management
- `character_export/` - PDF/Markdown export functionality
- `reference/` - Rules reference system (content in `reference/content/`)
- `common/` - Shared utilities (helpers, decorators, mixins)
- `pillars_folio/` - Django project settings
- `templates/` - Shared templates (base.html)
- `static/` - Shared static files
- `tests.py` - All project tests

## Rules
- **DRY is mandatory.** Before writing new code, search for existing implementations. If similar code exists anywhere in the codebase, extract and generalize it. Never copy-paste-modify. Never write the same logic twice.
- **Do not delete or disable tests.** All existing tests must be preserved and passing.
- **All tests must pass.** Run `./run test` before committing.
- Pre-commit hooks run automatically: ruff lint, ruff format, pyright, pytest with coverage.
- **Coverage threshold auto-updates.** When coverage increases, the threshold in `pyproject.toml` automatically updates to the new value. Coverage cannot drop below the current threshold.
- Use `uv` for dependency management (`uv add <package>`).
- **Single source of truth.** Never define the same thing in two places. CI runs pre-commit hooks (not duplicated checks). Config lives in one file. If something needs to stay in sync, make one generate/call the other.
- **All editable fields should auto-save** when focus is lost.

## File Hygiene
- **Never create files with spaces or numeric suffixes** (e.g., `file 2.py`, `folder 2/`). These indicate accidental duplicates - fix the root cause instead.
- **Before creating any file**, search for existing files with similar names or content.
- **Never copy directory trees.** If content exists elsewhere, import or reference it.
- **After file operations**, run `git status` to catch unintended changes before committing.
- **Content locations are fixed:**
  - Reference content: `reference/content/` only
  - Templates: `templates/` (root) for shared, `<app>/templates/<app>/` for app-specific
  - Static files: `static/` (root) for shared, `<app>/static/<app>/` for app-specific
- **Clean up after migrations.** When moving content, delete the source files.

## User Model Fields
| Field | Required | Max Length |
|-------|----------|------------|
| username | Yes | 25 |
| password | Yes | 128 |
| real_name | No | 100 |
| email | No | 254 |
| phone | No | 20 |
| discord | No | 50 |
| preferred_contact | No | - |

## Roles
Users can have any combination of roles:
| Role | Field | Default |
|------|-------|---------|
| Admin | `is_role_admin` | False |
| DM | `is_dm` | False |
| Player | `is_player` | True |

- New users automatically get the Player role upon registration
- Users can have multiple roles (e.g., Admin + DM + Player)

## Database Configuration
- **Development**: SQLite (default, no configuration needed)
- **Production**: PostgreSQL (set `DATABASE_URL` environment variable)
```bash
# Production PostgreSQL
export DATABASE_URL=postgres://user:password@host:port/dbname
uv sync --group prod  # Install psycopg
```

## URL Routes
- `/` - Home page
- `/accounts/register/` - Registration
- `/accounts/login/` - Login
- `/accounts/logout/` - Logout (POST only)
- `/accounts/profile/` - Editable profile (requires auth, auto-saves on blur, admins can edit roles)
- `/accounts/profile/update-field/` - API endpoint for auto-save (POST, JSON)
- `/admin/` - Django admin