# Portfolio Optimization Web App

## Setup Instructions

1. **Install Python 3.10.11**
2. **Create Virtual Environment & Install Dependencies**
   - Use the batch script or run:
     - `uv venv .venv --python 3.10.11`
     - `uv pip install -r requirements.txt`
3. **Run the App**
   - Activate the environment and run:
     - `python app.py`

## Project Structure
- `app/` - Application modules
- `templates/` - HTML templates
- `static/css/` - Stylesheets
- `static/js/` - JavaScript
- `tests/` - Test suite
- `scripts/` - Utilities, PRD, setup scripts

## Environment Management
- All dependencies pinned in requirements.txt and pyproject.toml
- Use uv for dependency management

## Features
- Portfolio optimization using Monte Carlo simulation
- Interactive Bokeh visualizations (efficient frontier, asset weights)
- Responsive Flask web UI
- Robust error handling and logging (Rich)
- Fully tested with pytest (unit, integration, visualization)

## Testing
- Run all tests:
  - `pytest --maxfail=2 --disable-warnings -v`
- Test coverage includes data loading, optimization, visualization, Flask routes, and session handling.
- All tests must pass before deployment.

## Deployment

### Deploying to Render

1. **Connect your GitHub repository to Render**
2. Render will auto-detect your Python project and use your `requirements.txt` and `Procfile`/`render.yaml`.
3. Ensure your `Procfile` contains:
   ```
   web: gunicorn "app:create_app()"
   ```
   Or use the provided `render.yaml` for infrastructure-as-code deployment.
4. Set environment variables (e.g., `SECRET_KEY`) in the Render dashboard for security.
5. On deployment, Render will run `uv pip install -r requirements.txt` and launch the app using Gunicorn.

**Notes:**
- No Heroku-specific configuration is needed.
- The app uses the Flask application factory pattern for maximum flexibility.
- For static files, ensure the `/static` directory is present and referenced in your templates.
  2. Push to your deployment platform (Heroku, Render, etc.).
  3. Static files and templates are served by Flask; Bokeh output is generated as HTML.

## Code Quality
- All core modules and functions have Google-style docstrings.
- Linting via ruff (see pyproject.toml).
- Logging and error handling via Rich for clear diagnostics.
