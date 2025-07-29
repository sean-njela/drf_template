<div align="center">
    <!-- <img src="https://raw.githubusercontent.com/sean-njela/drf_template/refs/heads/main/static/logo.png" data-canonical-src="/logo.png" width="130" height="130" /> -->

# DRF starter template

A comprehensive and easy-to-use starting point for your new API with **Django** and **DRF**.

<!-- [![Test Status](https://github.com/sean-njela/drf_template/actions/workflows/test.yml/badge.svg)](https://github.com/sean-njela/drf_template/actions/workflows/test.yml)
[![CodeQL Advanced](https://github.com/sean-njela/drf_template/actions/workflows/codeql.yml/badge.svg)](https://github.com/sean-njela/drf_template/actions/workflows/codeql.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/sean-njela/drf_template?tab=MIT-1-ov-file#readme) -->

</div>

## ✨ Key Features

This template is packed with features to help you build amazing APIs:

- **User Authentication:** Secure token-based authentication with `django-rest-knox`.
- **Background Tasks:** Asynchronous task processing with `Celery` and `Redis`.
- **API Documentation:** Automatic OpenAPI 3 schema generation with `drf-spectacular`.
- **Centralized Logging:** Structured JSON logging for easy monitoring.
- **Custom User Model:** Email-based authentication for a modern user experience.
- **And much more!** Explore the documentation to discover all the features.
- **AI Tools:** Useful prompts to enhance your development experience with GitHub Copilot, Gemini CLI agent, and Roo Code.

## Quick Start

### Prerequisites

- 💻 VS Code
- 🐋 Docker
- 🐳 Docker Compose

### Setup Steps

1. Use [GitHub's template feature](https://github.com/new?template_name=django-starter-template&template_owner=wilfredinni) (recommended) or clone repository
2. Open in VS Code
3. Check [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree) in the sidebar for setup guidance
4. Run `CTL/CMD + Shift + p` and select `Reopen in container`
5. Create superuser: `python manage.py createsuperuser`
6. Start server: `python manage.py runserver`

## 📖 Explore the Documentation

This documentation is your guide to building amazing applications with the Django Starter Template. Use the navigation on the left to explore the different sections.

- **[Development](https://sean-njela.github.io/drf_template/development):** Learn about the development workflow, including how to run tests, and use the scripts.
- **[AI Tools](https://sean-njela.github.io/drf_template/ai_tools):** Explore useful prompts to enhance your development experience with GitHub Copilot.
- **[Project Structure](https://sean-njela.github.io/drf_template/project_structure):** Get an overview of the project's directory structure.
- **[Project Settings](https://sean-njela.github.io/drf_template/settings):** Understand the available settings and how to configure your project.
- **[Dependencies](https://sean-njela.github.io/drf_template/dependencies):** See a list of all the project's dependencies.
- **[Authentication](https://sean-njela.github.io/drf_template/authentication):** Learn how to use the authentication and user management endpoints.
- **[Core App](https://sean-njela.github.io/drf_template/core_endpoints):** Discover the core functionalities and API endpoints.
- **[Logging](https://sean-njela.github.io/drf_template/logging):** Understand the logging system and how to use it.
- **[Celery Tasks](https://sean-njela.github.io/drf_template/tasks):** Learn how to create and manage background tasks.
- **[Rate Limiting](https://sean-njela.github.io/drf_template/rate_limiting):** Configure rate limiting to protect your API.
- **[Database Seeding](https://sean-njela.github.io/drf_template/database_seeding):** Learn how to seed your database with initial data.
- **[Testing](https://sean-njela.github.io/drf_template/testing):** Understand how to run and write tests for your project.
- **[Environment Setup](https://sean-njela.github.io/drf_template/environment_setup):** Learn how to set up your development environment.

```bash
├── apps/                   # All Django apps go here
│   ├── __init__.py
│   ├── users/              # Sample app
│   │   ├── __init__.py
│   │   ├── 0-facade.py     # Booking facade interface for external clients
│   │   ├── models.py       # Django ORM models
│   │   ├── serializers.py  # DRF serializers
│   │   ├── views.py        # DRF views
│   │   ├── urls.py         # App-specific URL routes
│   │   ├── services.py     # Business/application logic
│   │   ├── permissions.py  # Custom DRF permissions (optional)
│   │   ├── validators.py   # Custom field/data validators (optional)
│   │   ├── domain.py       # (Optional) Pure logic & rules
│   │   ├── repositories.py # (Optional) Data access layer
│   │   ├── models.py       # Django ORM models
│   │   ├── tasks.py        # Background jobs (Celery, etc.)
│   │   └── tests/          # Unit tests for this app
│   │       ├── __init__.py
│   │       ├── test_views.py
│   │       ├── test_services.py
│   │       ├── test_domain.py
│   │       └── test_models.py

│   └── another_app/        # Add more apps as needed

```

OR

```bash

apps/
├── __init__.py
├── users/                            # Bounded context / domain module
│   ├── __init__.py

│   ├── facades/                      # (0) Public interface for internal/external use (e.g. other apps)
│   │   ├── __init__.py
│   │   └── user_facade.py            # Clean API for external/internal calls (e.g., register_user(...))

│   ├── presentation/                 # (1) Presentation layer (DRF-related)
│   │   ├── __init__.py
│   │   ├── views.py                  # DRF API views (controllers)
│   │   ├── serializers.py            # DRF serializers (DTOs)
│   │   └── urls.py                   # DRF routing

│   ├── application/                  # (2) Application layer (use cases, commands, service orchestration)
│   │   ├── __init__.py
│   │   ├── services.py               # Use case orchestration (e.g. register_user())
│   │   ├── commands/                 # Optionally break out per command/use case
│   │   │   ├── __init__.py
│   │   │   └── create_user.py        # E.g., command handler for user creation
│   │   ├── events/                   # Domain events (used for decoupling)
│   │   │   ├── __init__.py
│   │   │   └── user_registered.py    # E.g., event raised after user is created

│   ├── domain/                       # (3) Domain layer: business rules and contracts
│   │   ├── __init__.py
│   │   ├── entities.py               # Core domain models (User, etc.)
│   │   ├── value_objects.py          # VOs like EmailAddress, PasswordHash, etc.
│   │   ├── policies.py               # Business rules/policies (e.g. PasswordPolicy)
│   │   └── interfaces/               # Abstract interfaces for services
│   │       ├── __init__.py
│   │       └── email_service.py      # Interface contract for sending email

│   ├── infrastructure/              # (4) Infra implementations (external services, APIs, adapters)
│   │   ├── __init__.py
│   │   ├── email_service.py         # Implements email_service interface
│   │   └── external_api.py          # E.g. 3rd-party auth, external billing, etc.

│   ├── data/                        # (5) Data access and persistence
│   │   ├── __init__.py
│   │   ├── models.py               # Django ORM models
│   │   └── repositories.py        # Data mappers/repositories (hide model logic behind interfaces)

│   └── tests/                      # Tests organized by architectural concern
│       ├── __init__.py
│       ├── test_views.py          # Presentation layer tests
│       ├── test_services.py       # Application use case tests
│       ├── test_repositories.py   # Data access logic tests
│       └── test_entities.py       # Pure domain model tests

│   └── another_app/              # Add more apps with same structure

```

| Command                     | Description                                                | Notes                                                  |
| --------------------------- | ---------------------------------------------------------- | ------------------------------------------------------ |
| `runserver`                 | Starts the Django development server                       | Use `--port` to specify custom port: `runserver 8001`  |
| `migrate`                   | Applies migrations to the database                         | Required after model changes                           |
| `makemigrations`            | Creates new migration files from model changes             | Doesn’t affect DB yet                                  |
| `shell`                     | Opens a Python shell with Django context                   | Use `shell_plus` (from `django-extensions`) for extras |
| `createsuperuser`           | Creates an admin user                                      | Prompts for username, email, password                  |
| `flush`                     | Deletes all data from DB and resets PKs                    | **Keeps schema**, asks for confirmation                |
| `loaddata`                  | Loads data from fixtures (e.g. JSON)                       | `loaddata users.json`                                  |
| `dumpdata`                  | Dumps DB data to JSON                                      | `dumpdata app.Model > file.json`                       |
| `check`                     | Checks project for issues (e.g. configs)                   | Use before deployment                                  |
| `collectstatic`             | Collects static files into one directory                   | Used in production                                     |
| `test`                      | Runs tests                                                 | Discover and run all `tests.py` or test modules        |
| `startapp`                  | Creates a new Django app directory                         | `startapp myapp`                                       |
| `startproject`              | Creates a new Django project                               | Usually only used once                                 |
| `showmigrations`            | Lists all migrations and their status                      | Shows which ones are applied                           |
| `sqlmigrate`                | Shows SQL of a migration                                   | `sqlmigrate appname 0001_initial`                      |
| `makemessages`              | Extracts translatable strings                              | Use for internationalization (i18n)                    |
| `compilemessages`           | Compiles `.po` to `.mo` files                              | Needed after translating strings                       |
| `dbshell`                   | Opens DB shell                                             | Depends on DB driver setup                             |
| `diffsettings`              | Shows differences from Django default settings             | Useful for debugging settings overrides                |
| `inspectdb`                 | Generates models from an existing DB                       | Great for legacy DBs                                   |
| `clear_cache`               | (custom) Clears cache if implemented                       | Not built-in; depends on your setup                    |
| `changepassword <username>` | Changes password of a user                                 | Useful when you forgot the admin password              |
| `showurls`                  | (via `django-extensions`) Lists all URL patterns           | Optional but very useful                               |
| `graph_models`              | (via `django-extensions`) Generates a graph of your models | Install `pygraphviz` or `pydot`                        |

---

### ✅ Bonus: Useful Custom Aliases

If you use `django-extensions` (highly recommended for dev), you also get:

```bash
python manage.py shell_plus
python manage.py runscript <script_name>
python manage.py show_urls
python manage.py export_emails

```
