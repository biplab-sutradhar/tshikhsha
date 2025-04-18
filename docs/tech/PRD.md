## Point of Contact (POC)

- `Title`: [Team.shiksha 2.0](https://team.shiksha/)
- `Date and Version`: 17th March, v1
- `Product (POC)`: Sunny, Anoop
- `Design (POC)`: Chandresh, Sayantan
- `Tech (POC)`: Sunny, Anoop
- `Stack`: [React](https://react.dev/), [FastAPI](https://fastapi.tiangolo.com/), [MySQL](https://www.mysql.com/)
- `CI/CD`: [GitHub Actions](https://docs.github.com/en/actions/writing-workflows/quickstart)
- `Deployment Platform`: [Vercel](https://vercel.com/), [Railway](http://railway.com/)
- `Test Requirement`: Unit testing should have coverage > 90%

## Why

- Enhanced UI for new and existing users.
- Get information on how to use channels.
- Learn about upcoming and previous events/sessions.
- Learn about projects, tech stack, and join projects.
- Receive feedback on your open-source contributions.
- Request exclusive events based on upvotes.

## Measure

- Total number of users.
- Number of active users.
- Percentage of users onboarded after release.
- End-user feedback.
- Number of recruiters onboarded.

## Who are the users:

- Existing Discord members.
- New members: students, working professionals, or recruiters.

## User personas:
- `Member`: New members who join are by default a member. They can see how to navigate in the TeamShiksha server using different channels.
- `Contributor`: Members can be converted to contributors if they join projects. NOTE: Before joining the project, members need to make sure they meet the eligibility criteria.
- `Recruiter`: Members can be converted to recruiters after verification from the admins. Once they get access, they should be able to see top performers from the project sections, reviews, PRs, and other information too.
- `Admin`: Users can approve the promotion of members to Contributor/Recruiter/Admin or they can also directly promote folks to any position. They can view metrics of the website, like the total number of users, active users, traffic, and percentage increase in users compared to the previous week. They can also add events directly from the website (this will automatically be created on Discord).

## Solution

- Allow users to onboard the server and understand the use of all the channels.
- Allow users to become contributors by joining projects based on their interests, eligibility, and requirements. Contributors can also request feedback based on their work done for improvement.
- Allow recruiters to hire from our pool of contributors, based on the metrics provided on the recruiter dashboard.
- Allow admins to create non-exclusive/exclusive events, set the minimum number of upvotes (for exclusive events), add/remove users from personas, approve persona promotions, and view recruiters and contributor pool.
- Mock interview for active members.

## Tentative timeline

- **April**: Finalize design and wireframes, set up the development environment, and complete authentication (OAuth for GitHub, Google, Discord).
- **May**: Develop the onboarding flow for members and contributors, including eligibility checks and project joining functionality.
- **June**: Build the recruiter dashboard, including metrics for contributors and top performers.
- **July**: Implement admin functionalities, such as event creation, persona promotions, and metrics dashboard.
- **August**: Conduct internal testing, ensure unit test coverage > 90%, and fix bugs.
- **September**: Perform user acceptance testing (UAT), deploy to production, and onboard initial users.

Total time: 6 months. Release `30th September 2025`.

## Dependencies

- Oauth from GitHub, Google, Discord.
- Design/Wireframes.
- Email service.
- Active contributors.
