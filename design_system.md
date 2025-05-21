# NovaFlow Design System

## Product Details
*   **Product name:** NovaFlow
*   **One-sentence value prop:** Streamline your creative collaboration.
*   **Primary user persona:** Design teams and solo creators.
*   **Key screen(s) to design:** Landing page + Project Dashboard

## Visual Vibe
Apple-esque minimalism – soft shadows, ample whitespace, pastel blues/greys/purples, rounded 2xl corners.

## Design Tokens

### Color Palette

| Name       | Hex Code | Tailwind Utility      | Usage Notes                                     |
|------------|----------|-----------------------|-------------------------------------------------|
| Primary    | `#A0AECF` | `bg-primary-500`      | Buttons, primary actions, key highlights        |
| Secondary  | `#BAD6FB` | `bg-secondary-500`    | Secondary actions, accents, decorative elements |
| Accent     | `#D8BFD8` | `bg-accent-500`       | Special highlights, call-to-actions (sparingly) |
| Neutral    | `#E5E7EB` | `bg-neutral-200`      | Borders, dividers, disabled states              |
| Background | `#F9FAFB` | `bg-background`       | Main page backgrounds                           |
| Text       | `#374151` | `text-gray-700`       | Primary text content                            |
| Text Light | `#6B7280` | `text-gray-500`       | Secondary text, captions, helper text           |
| Pastel Blue| `#BFDBFE` | `bg-blue-200`         | Backgrounds, decorative elements                |
| Pastel Grey| `#D1D5DB` | `bg-gray-300`         | UI controls, subtle backgrounds                 |
| Pastel Purple| `#DDD6FE`| `bg-purple-200`       | Accents, illustrations                          |

### Typography Scale

| Element/Usage | Font Family                                                                                                                              | Font Size (Tailwind) | Font Weight (Tailwind) |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------|----------------------|------------------------|
| Heading 1     | `ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, ...` | `text-4xl`           | `font-bold`            |
| Heading 2     | `ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, ...` | `text-3xl`           | `font-semibold`        |
| Heading 3     | `ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, ...` | `text-2xl`           | `font-semibold`        |
| Body          | `ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, ...` | `text-base`          | `font-normal`          |
| Caption       | `ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, ...` | `text-sm`            | `font-normal`          |
| Button Text   | `ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, ...` | `text-base`          | `font-medium`          |

### Spacing & Radius Tokens

| Type           | Token Name/Tailwind Class | Value (Example) | Usage Notes                                       |
|----------------|---------------------------|-----------------|---------------------------------------------------|
| Padding        | `p-2`                     | `0.5rem (8px)`  | Small elements, icons                             |
| Padding        | `p-4`                     | `1rem (16px)`   | Standard padding for containers, cards            |
| Padding        | `p-6`                     | `1.5rem (24px)` | Larger containers, sections                       |
| Padding        | `p-8`                     | `2rem (32px)`   | Page-level padding, significant visual separation |
| Margin         | `m-2`                     | `0.5rem (8px)`  | Small spacing between elements                    |
| Margin         | `m-4`                     | `1rem (16px)`   | Standard spacing between components               |
| Margin         | `m-8`                     | `2rem (32px)`   | Large spacing, section separation                 |
| Margin         | `m-16`                    | `4rem (64px)`   | Major visual breaks                               |
| Corner Radius  | `rounded-md`              | `0.375rem (6px)`| Smaller elements, inputs                          |
| Corner Radius  | `rounded-lg`              | `0.5rem (8px)`  | Standard cards, containers                        |
| Corner Radius  | `rounded-xl`              | `0.75rem (12px)`| Larger cards, prominent containers                |
| Corner Radius  | `rounded-2xl`             | `1rem (16px)`   | Key elements, hero sections, modal dialogs        |
| Corner Radius  | `rounded-full`            | `9999px`        | Circular elements, avatars                        |
