# Roadmap: AI-Powered Marketing Tool for Small Businesses

## End Goal (MVP)
A functional web application that allows small business owners to create marketing campaigns by inputting basic info (e.g., business type, budget), uses AI to generate ad copy and targeting suggestions, saves campaigns to a database, and lets users retrieve results. The MVP should be deployable, testable with real users, and provide enough value to validate the concept for potential scaling or an exit.

---

## High-Level Phases

### Phase 0: Project Setup & Foundation
- **Goal**: Establish a scalable project structure, set up development environment, and confirm basic functionality.
- **Tasks**:
  - Set up GitHub repo with `create-skeleton` branch.
  - Choose Git Bash as the primary terminal for consistency.
  - Define enterprise-grade project structure (`app/`, `controllers/`, `models/`, `services/`, etc.).
  - Implement basic Flask app with SQLite database.
  - Add `/campaign` endpoint to accept POST requests (e.g., `{"business": "coffee shop", "budget": 200}`) and save to DB.
  - Test with Postman to confirm functionality.
- **Status**: **Completed**.
- **Deliverables**:
  - Project skeleton with modular structure.
  - Working `/campaign` POST endpoint.
  - SQLite database (`campaigns.db`) storing campaigns.

---

### Phase 1: Core Functionality
- **Goal**: Build the essential features for the MVP—create, store, and retrieve campaigns with mock AI outputs.
- **Tasks**:
  1. Add `/results` Endpoint:
     - GET endpoint (`/results/<campaign_id>`) to fetch a campaign by ID and return mock AI-generated ad copy and targeting.
     - Use Flask-SQLAlchemy’s `query.get_or_404()` for clean error handling.
  2. Set Up Error Handling:
     - Add global error handlers for 400, 404, 500 errors in `app/__init__.py`.
     - Ensure consistent JSON error responses.
  3. Add Basic Logging:
     - Implement file-based logging (`app.log`) with rotation for debugging.
     - Log startup, errors, and key events.
  4. Prep `services/` Layer:
     - Create `services/ai_service.py` with mock methods for ad copy and targeting.
     - Wire it into the `/results` endpoint to keep controllers thin.
- **Status**: **In Progress**.
- **Deliverables**:
  - `/results` endpoint returning mock AI outputs.
  - Global error handling and logging.
  - `services/` layer ready for real AI integration.

---

### Phase 2: AI Integration
- **Goal**: Replace mock AI outputs with real API calls to generate ad copy and targeting suggestions.
- **Tasks**:
  1. Integrate OpenAI API:
     - Sign up for OpenAI API, get API key.
     - Update `services/ai_service.py` to call OpenAI for ad copy generation (e.g., "Generate 5 ad headlines for a coffee shop").
     - Handle API errors, rate limits, and costs (budget $5-10 for testing).
  2. Integrate Google Ads API (or Trends Data):
     - Use Google Ads API or scrape trends data (e.g., from X) for targeting suggestions (e.g., "25-45, local").
     - Update `services/ai_service.py` to process and return targeting.
  3. Enhance Campaign Model:
     - Add fields to `models/campaign.py` (e.g., `created_at`, `status`, `ad_copy`, `targeting`) to store AI results.
     - Update `/campaign` and `/results` to save and retrieve these fields.
- **Status**: **Not Started**.
- **Deliverables**:
  - Real AI-generated ad copy via OpenAI API.
  - Targeting suggestions based on data (Google Ads API or trends).
  - Updated DB schema to store AI outputs.

---

### Phase 3: Polish & Testing
- **Goal**: Add user-friendly features, ensure reliability, and prepare for beta testing.
- **Tasks**:
  1. Basic UI:
     - Add a minimal frontend (HTML + JS) for users to input data and view results.
     - Use Flask’s `render_template` to serve a simple page.
  2. Unit Tests:
     - Set up `pytest` in `tests/` folder.
     - Write tests for endpoints (`/campaign`, `/results`), models, and services.
  3. Input Validation:
     - Add stricter validation on `/campaign` (e.g., budget > 0, business not empty).
     - Return meaningful error messages.
  4. Beta Testing Prep:
     - Deploy to a free/low-cost host (e.g., Heroku, Railway) for testing.
     - Recruit 50-100 beta users via X or small biz forums.
- **Status**: **Not Started**.
- **Deliverables**:
  - Simple UI for campaign creation and results viewing.
  - Test suite covering key components.
  - Deployed app for beta testing.

---

### Phase 4: MVP Launch
- **Goal**: Launch the MVP to a small audience, gather feedback, and validate the concept.
- **Tasks**:
  1. Deployment:
     - Finalize deployment setup (e.g., Heroku with Gunicorn, SQLite → PostgreSQL if needed).
     - Add environment variables for API keys (OpenAI, Google Ads).
  2. User Onboarding:
     - Add basic user signup/login (Flask-Login or similar).
     - Allow users to save and view their campaigns.
  3. Feedback Collection:
     - Add a feedback form or track usage (e.g., via Google Analytics or Mixpanel).
     - Iterate based on user input (e.g., tweak AI prompts, UI).
  4. Performance Metrics:
     - Measure user engagement (e.g., campaigns created, results viewed).
     - Assess AI output quality (manual review or user ratings).
- **Status**: **Not Started**.
- **Deliverables**:
  - Live MVP with 50-100 active users.
  - Feedback loop established.
  - Metrics to validate concept for scaling or exit.

---

## Timeline (Rough Estimate)
Assuming iterative work with potential external commitments:
- **Phase 0**: Done.
- **Phase 1**: 1-2 weeks (in progress).
- **Phase 2**: 1-2 weeks (AI integration can be tricky with API quirks).
- **Phase 3**: 2-3 weeks (UI and testing take time).
- **Phase 4**: 1-2 weeks (deployment and feedback collection).
- **Total**: ~6-9 weeks for MVP, depending on pace and hiccups.

---

## Current Progress Snapshot
- **Where We Are**: In Phase 1—core functionality.
  - Project structure set up with plural naming (`controllers/`, etc.).
  - `/campaign` endpoint working (POST), saving to SQLite.
  - Git Bash as terminal, Postman for testing.
- **Next Immediate Step**: Add `/results` endpoint, error handling, logging, and prep `services/` layer.

---

## Progress Checklist
- [x] **Phase 0: Project Setup**
  - [x] Set up GitHub repo and structure
  - [x] `/campaign` endpoint with SQLite
- [ ] **Phase 1: Core Functionality** (In Progress)
  - [x] `/campaign` endpoint
  - [ ] `/results` endpoint
  - [ ] Error handling, logging, `services/` layer
- [ ] **Phase 2: AI Integration**
- [ ] **Phase 3: Polish & Testing**
- [ ] **Phase 4: MVP Launch**

---

## Notes
- This roadmap can be updated as we progress or pivot.
- Track progress by checking off tasks in the "Progress Checklist" section.
- Refer to commits and branches (`create-skeleton`) for implementation details.