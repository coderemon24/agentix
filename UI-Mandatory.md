## Mandatory UI/UX Implementation Guidelines

Implement every requested feature as a complete, working end-to-end feature, including backend logic, database changes, routes, authorization, frontend pages, reusable UI components, validation, loading states, and error handling.

### 1. Audit the Existing UI First
- Inspect the existing dashboard layout, sidebar, navigation, header, breadcrumbs, page structure, components, CSS, JavaScript, and frontend technology before making changes.
- Identify the project's existing UI framework and conventions. Reuse the existing stack instead of introducing a new frontend framework or UI library without approval.
- Preserve the current Super Admin dashboard and existing working screens.
- Do not redesign unrelated pages or replace the existing admin template.

### 2. UI Design Consistency
- Follow the existing dashboard's design system, including colors, typography, spacing, buttons, cards, tables, forms, icons, borders, and responsive breakpoints.
- Build a clean, professional, education-management dashboard suitable for real school administrators and staff.
- Use consistent page headers, action buttons, breadcrumbs, content spacing, and form layouts.
- Reuse existing layouts and components. Create reusable components only where they provide clear value.
- Avoid unnecessary animations, decorative effects, excessive colors, and inconsistent UI patterns.

### 3. Required UI for Every CRUD Module
When a feature requires CRUD operations, implement all applicable screens and interactions:
- **List page:** page title, breadcrumbs, relevant summary cards, search, filters, pagination, and a clear primary action.
- **Create page:** properly labeled fields, required-field indicators, sensible defaults, help text where useful, and validation feedback.
- **Edit page:** prefilled existing data, update action, and clear error handling.
- **Details page:** organized information with relevant actions and status indicators.
- **Delete/archive:** confirmation dialog, appropriate authorization, and clear success/error feedback.
- Use a modal or drawer instead of a separate page only when it matches the existing project conventions and the form is suitable for that pattern.

Do not create unnecessary pages or summary cards that do not provide meaningful value for the specific module.

### 4. Forms, Tables, and Interactions
- Use appropriate input types, select boxes, date pickers, searchable dropdowns, and file upload controls based on existing project conventions.
- Preserve old input after validation errors and show field-specific error messages.
- Tables must have readable column labels, sensible alignment, status badges where appropriate, and responsive behavior.
- Implement working search, filters, sorting, pagination, bulk actions, and export controls only when required.
- Dependent fields must work correctly; for example, selecting a class should load its relevant sections.
- Every visible button, dropdown, link, and form must have a real, functional action. Do not leave placeholder buttons or fake interactions.

### 5. UI States and Feedback
Implement the states relevant to each screen:
- Loading or processing state.
- Empty state with a useful message and next action.
- Validation errors.
- Success and failure notifications.
- Disabled states while processing.
- Confirmation before destructive operations.
- Permission-denied and unavailable-record states.
- Appropriate handling of network or server errors.

Prevent accidental duplicate submissions and preserve entered data when an operation fails where practical.

### 6. Responsive Design and Accessibility
- Ensure screens work on desktop, tablet, and mobile.
- Make navigation, tables, forms, dialogs, and action buttons usable on smaller screens.
- Use proper labels, keyboard-accessible controls, visible focus states, and accessible dialog behavior.
- Avoid horizontal overflow except where a data table reasonably requires horizontal scrolling.

### 7. Authorization and Data Integrity
- Never rely on hiding UI elements as the only security mechanism. Enforce permissions and tenant isolation on the backend too.
- Only show actions that the current user is authorized to perform.
- Do not expose another school's records through dropdowns, search results, URLs, or frontend state.
- Validate all submitted data on the server, even when client-side validation exists.

### 8. Navigation and Integration
- Add new pages to the existing sidebar/navigation in the correct section.
- Use the existing route names, layouts, middleware, and authentication conventions wherever possible.
- Ensure page titles, breadcrumbs, navigation active states, and redirects work correctly.
- Preserve existing working workflows and avoid unrelated changes.

### 9. Implementation and Verification
- Implement the frontend and backend together; do not stop after creating models, migrations, APIs, or controllers.
- Inspect the final changes for broken routes, missing views, incorrect permissions, nonfunctional buttons, console errors, and styling regressions.
- Run relevant automated tests and available frontend build/lint checks.
- Verify the main user flows, validation failures, empty states, and unauthorized access.
- Report which pages and interactions were implemented, which checks passed, and any remaining limitations.
- Do not claim that a UI or test works unless it has actually been verified.
