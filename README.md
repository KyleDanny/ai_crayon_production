# ai_crayon_production

## AI Model

- Claude 3.5 Sonnet (vscode)
- GPT o1 (site & vscode)
- DeepSeek Coder (site & vscode)

## AI Prompt

"Create a web application using Django that manages a list of crayon providers. The application will display details about each provider, including the types of crayons they offer (e.g., standard, premium, eco-friendly) and their current pricing. Additionally, include a checkmark to indicate whether the provider offers bulk discounts. The application should have a superuser for administrative tasks.

The project will be set up on a Mac, starting from an empty Git repository. The Django project will be named "crayon_production", and it should be designed to handle the needs of a business that creates and sells crayons to various providers."

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the development server:

```bash
python manage.py runserver
```

http://127.0.0.1:8000/admin/providers/provider/

## Admin Page

http://127.0.0.1:8000/admin/providers/provider/

## Crayon Providers Page

http://127.0.0.1:8000/providers/

## Feedback

### Pros of Using AI for Code

- Fast: Gets you started quickly with boilerplate code.

- Helpful: Explains stuff and suggests fixes.

- Less Errors: Follows best practices, so fewer mistakes.

- Customizable: Tailors code to your needs (e.g., Mac setup, crayon business).

- Always Available: Helps anytime, even when humans can’t.

- Can switch between models to see which one is best for the task.

### Cons of Using AI for Code

- Not Perfect: Can give incomplete or buggy solutions (like your rendering issue).

- Debugging Hassle: Fixing AI’s mistakes can take extra time.

- Generic: Doesn’t always "get" your specific problem.

- Prompt-Dependent: Needs clear instructions to work well.

- Time Sink: Tweaking and debugging can eat up time.

- No Creativity: Struggles with unique or creative solutions.

### Your Experience

- Good: AI saved time setting up Django and gave debugging tips.

- Not So Good: The rendering issue took extra effort to fix.

### When to Use AI

For quick setups, learning, or standard tasks.

Not for super complex or unique problems.

### Takeaway

AI’s great for speeding things up and learning, but always double-check its work and use your own skills for the tricky stuff. 😊
