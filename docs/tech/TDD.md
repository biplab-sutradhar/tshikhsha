## Overview

[Team.shiksha 2.0](https://team.shiksha/) is a thriving learning community designed for students, freshers, and working professionals. It fosters skill development by simulating a corporate work environment, providing hands-on projects and real-world tasks similar to those encountered in the industry. 

Application introduces features that enable users of all types to engage with the community and pursue their passions. It helps users understand their current skill level and guides them on how to progress further by providing a structured roadmap and regular feedback at defined intervals.

### Jump To 

- [Architecture](#architecture)
- [API Design](#api-design)
- [Data Model](#data-model)
- [Security and Authentication](#security-and-authentication)
- [Scalability & Performance](#scalability--performance)
- [Deployment Strategy](#deployment-strategy)
- [Failure Handling & Monitoring](#failure-handling--monitoring)

## Architecture
TBC

## API Design

The API layer serves as the backbone of the application, enabling seamless communication between the frontend and backend systems. Below are the key aspects of the API design:

### Design Principles
- **RESTful Architecture**: The APIs follow REST principles to ensure scalability and simplicity.
- **Versioning**: All APIs are versioned (e.g., `/v1/`) to maintain backward compatibility.

### Example
TBC

## Data Model

Data modeling occurs at three main levels, each with increasing specificity as you move from conceptual to physical. These levels represent different stages in the database design process.

### Conceptual Data Model
A conceptual data model is a high-level overview that identifies the main entities and their relationships without implementation details.

```mermaid
erDiagram
    USERS }o--|| PROJECTS : "user_id, project_id"
    PROJECTS ||--o{ DISCORD_ROLE : "project_id, discord_role_id"
    USERS ||--o{ EVENTS : created_by
    SNAPSHOTS }|--|{ USERS : "user_id, lead_id"
    SNAPSHOTS ||--|| PROJECTS : project_id
    INTERVIEWS }|--|{ USERS : "interviewee_id, interviewer_id"
    REQUESTS }|--|{ USERS : user_id
    DISCORD_ROLE
```

### Logical Data Model
A logical data model expands on the conceptual model by adding attributes, defining keys, and normalizing relationships, but remains independent of any specific database technology.

> [!NOTE]
> Audit table will be added for keeping the audit information for destructive or intensive tasks, which is not present in this diagram as this table might not be related to any table present here.

```mermaid
erDiagram
    USERS {
        id(PK) STRING
        name STRING
        email STRING
        bio STRING
        linkedin STRING
        discord STRING
        twitter STRING
        oauth_type(ENUM) STRING
        metadata_info JSON
        last_active TIMESTAMP
        photo STRING
        is_profile_completed BOOLEAN
        is_deleted BOOLEAN
        is_active BOOLEAN
        created_on TIMESTAMP
        updated_on TIMESTAMP
        created_by STRING
        updated_by STRING
    }
    PROJECTS {
        id(PK) STRING
        name STRING
        description STRING
        live_link STRING
        github_team STRING
        repository STRING
        total_contributor INT
        metadata_info JSON
        is_deleted BOOLEAN
        is_active BOOLEAN
        created_on TIMESTAMP
        updated_on TIMESTAMP
        created_by STRING
        updated_by STRING
    }
    DISCORD_ROLE {
        id(PK) STRING
        name STRING
        description STRING
        is_deleted BOOLEAN
        is_active BOOLEAN
        created_on TIMESTAMP
        updated_on TIMESTAMP
        created_by STRING
        updated_by STRING
    }
    EVENTS {
        id(PK) STRING
        title STRING
        description STRING
        host STRING
        metadata_info JSON
        start_time TIMESTAMP
        event_link STRING
        is_exclusive BOOLEAN
        is_deleted BOOLEAN
        is_active BOOLEAN
        created_on TIMESTAMP
        updated_on TIMESTAMP
        created_by STRING
        updated_by STRING
    }
    SNAPSHOTS {
        id(PK) STRING
        user_id(FK) STRING
        lead_id(FK) STRING
        status(ENUM) STRING
        description STRING
        project_id STRING
        comment STRING
        metadata_info JSON
        is_deleted BOOLEAN
        is_active BOOLEAN
        created_on TIMESTAMP
        updated_on TIMESTAMP
        created_by STRING
        updated_by STRING
    }
    INTERVIEWS {
        id(PK) STRING
        interviewee_id(FK) STRING
        interviewer_id(FK) STRING
        interview_date_time TIMESTAMP
        status(ENUM) STRING
        for_role STRING
        feedback STRING
        cooldown_end_on TIMESTAMP
        metadata_info JSON
        is_deleted BOOLEAN
        is_active BOOLEAN
        created_on TIMESTAMP
        updated_on TIMESTAMP
        created_by STRING
        updated_by STRING
    }
    REQUESTS {
        id(PK) STRING
        user_id(FK) STRING
        request_type STRING
        status(ENUM) STRING
        approved_by STRING
        justification STRING
        metadata_info JSON
        is_deleted BOOLEAN
        is_active BOOLEAN
        created_on TIMESTAMP
        updated_on TIMESTAMP
        created_by STRING
        updated_by STRING
    }
    USER_PROJECT_MAP {
        id(PK) STRING
        user_id(FK) STRING
        project_id(FK) STRING
        is_deleted BOOLEAN
        is_active BOOLEAN
        created_on TIMESTAMP
        updated_on TIMESTAMP
        created_by STRING
        updated_by STRING
    }
    PROJECT_DISCORD_MAP {
        id(PK) STRING
        project_id(FK) STRING
        discord_role_id(FK) STRING
        is_deleted BOOLEAN
        is_active BOOLEAN
        created_on TIMESTAMP
        updated_on TIMESTAMP
        created_by STRING
        updated_by STRING
    }

    USERS ||--o{ USER_PROJECT_MAP : user_id
    PROJECTS ||--o{ USER_PROJECT_MAP : project_id
    PROJECTS ||--o{ PROJECT_DISCORD_MAP : project_id
    DISCORD_ROLE ||--o{ PROJECT_DISCORD_MAP : discord_role_id
    USERS ||--o{ EVENTS : created_by
    SNAPSHOTS }|--|{ USERS : "user_id, lead_id"
    SNAPSHOTS ||--|| PROJECTS : project_id
    INTERVIEWS }|--|{ USERS : "interviewee_id, interviewer_id"
    REQUESTS }|--|{ USERS : user_id
```

### Physical Data Model
A physical data model translates the logical model into a specific database implementation with detailed specifications for storage and performance optimization. The below database physical model is for MySQL.

```mermaid
erDiagram
    USERS {
        id(PK) VARCHAR(36)
        name VARCHAR(100)
        email VARCHAR(100) "NOT NULL"
        bio VARCHAR(300)
        linkedin VARCHAR(100)
        discord VARCHAR(100)
        twitter VARCHAR(100)
        oauth_type(ENUM) VARCHAR(20) "NOT NULL"
        metadata_info JSON "DEFAULT {}"
        last_active TIMESTAMP
        photo VARCHAR(100)
        is_profile_completed BOOLEAN "DEFAULT FALSE"
        is_deleted BOOLEAN "DEFAULT FALSE"
        is_active BOOLEAN "DEFAULT TRUE"
        created_on TIMESTAMP "DEFAULT CURRENT_TIMESTAMP()"
        updated_on TIMESTAMP "DEFAULT CURRENT_TIMESTAMP()"
        created_by(FK) VARCHAR(36)
        updated_by(FK) VARCHAR(36)
    }

    PROJECTS {
        id(PK) VARCHAR(36)
        name VARCHAR(100) "NOT NULL"
        description VARCHAR(300)
        live_link VARCHAR(100)
        github_team VARCHAR(100) "NOT NULL"
        repository VARCHAR(100) "NOT NULL"
        total_contributor INT "DEFAULT 0"
        metadata_info JSON "DEFAULT {}"
        is_deleted BOOLEAN "DEFAULT FALSE"
        is_active BOOLEAN "DEFAULT TRUE"
        created_on TIMESTAMP "DEFAULT CURRENT_TIMESTAMP()"
        updated_on TIMESTAMP "DEFAULT CURRENT_TIMESTAMP()"
        created_by(FK) VARCHAR(36)
        updated_by(FK) VARCHAR(36)
    }

    DISCORD_ROLE {
        id(PK) VARCHAR(36)
        name VARCHAR(100) "NOT NULL"
        description VARCHAR(300)
        is_deleted BOOLEAN "DEFAULT FALSE"
        is_active BOOLEAN "DEFAULT TRUE"
        created_on TIMESTAMP "DEFAULT CURRENT_TIMESTAMP()"
        updated_on TIMESTAMP "DEFAULT CURRENT_TIMESTAMP()"
        created_by(FK) VARCHAR(36)
        updated_by(FK) VARCHAR(36)
    }

    EVENTS {
        id(PK) VARCHAR(36)
        title VARCHAR(100) "NOT NULL"
        description VARCHAR(500)
        host VARCHAR(100)
        metadata_info JSON "DEFAULT {}"
        start_time TIMESTAMP "NOT NULL"
        event_link VARCHAR(100) "NOT NULL"
        is_exclusive BOOLEAN "DEFAULT FALSE"
        is_deleted BOOLEAN "DEFAULT FALSE"
        is_active BOOLEAN "DEFAULT TRUE"
        created_on TIMESTAMP "DEFAULT CURRENT_TIMESTAMP()"
        updated_on TIMESTAMP "DEFAULT CURRENT_TIMESTAMP()"
        created_by(FK) VARCHAR(36)
        updated_by(FK) VARCHAR(36)
    }

    SNAPSHOTS {
        id(PK) VARCHAR(36)
        user_id(FK) VARCHAR(36)
        lead_id(FK) VARCHAR(36)
        status(ENUM) VARCHAR(100) "DEFAULT PENDING"
        description VARCHAR(500) "NOT NULL"
        project_id(FK) VARCHAR(36)
        comment VARCHAR(3000)
        metadata_info JSON "DEFAULT {}"
        is_deleted BOOLEAN "DEFAULT FALSE"
        is_active BOOLEAN "DEFAULT TRUE"
        created_on TIMESTAMP "DEFAULT CURRENT_TIMESTAMP()"
        updated_on TIMESTAMP "DEFAULT CURRENT_TIMESTAMP()"
        created_by(FK) VARCHAR(36)
        updated_by(FK) VARCHAR(36)
    }

    INTERVIEWS {
        id(PK) VARCHAR(36)
        interviewee_id(FK) VARCHAR(36)
        interviewer_id(FK) VARCHAR(36)
        interview_date_time TIMESTAMP
        status(ENUM) VARCHAR(100) "DEFAULT PENDING"
        for_role VARCHAR(100) "NOT NULL"
        feedback VARCHAR(3000)
        cooldown_end_on TIMESTAMP
        metadata_info JSON "DEFAULT {}"
        is_deleted BOOLEAN "DEFAULT FALSE"
        is_active BOOLEAN "DEFAULT TRUE"
        created_on TIMESTAMP "DEFAULT CURRENT_TIMESTAMP()"
        updated_on TIMESTAMP "DEFAULT CURRENT_TIMESTAMP()"
        created_by(FK) VARCHAR(36)
        updated_by(FK) VARCHAR(36)
    }

    REQUESTS {
        id(PK) VARCHAR(36)
        user_id(FK) VARCHAR(36)
        request_type(ENUM) VARCHAR(100) "NOT NULL"
        status(ENUM) VARCHAR(100) "DEFAULT PENDING"
        approved_by(FK) VARCHAR(100)
        justification VARCHAR(300) "NOT NULL"
        metadata_info JSON "DEFAULT {}"
        is_deleted BOOLEAN "DEFAULT FALSE"
        is_active BOOLEAN "DEFAULT TRUE"
        created_on TIMESTAMP "DEFAULT CURRENT_TIMESTAMP()"
        updated_on TIMESTAMP "DEFAULT CURRENT_TIMESTAMP()"
        created_by(FK) VARCHAR(36)
        updated_by(FK) VARCHAR(36)
    }

    USER_PROJECT_MAP {
        id(PK) VARCHAR(36)
        user_id(FK) VARCHAR(36)
        project_id(FK) VARCHAR(36)
        is_deleted BOOLEAN "DEFAULT FALSE"
        is_active BOOLEAN "DEFAULT TRUE"
        created_on TIMESTAMP "DEFAULT CURRENT_TIMESTAMP()"
        updated_on TIMESTAMP "DEFAULT CURRENT_TIMESTAMP()"
        created_by(FK) VARCHAR(36)
        updated_by(FK) VARCHAR(36)
    }

    PROJECT_DISCORD_MAP {
        id(PK) VARCHAR(36)
        project_id(FK) VARCHAR(36)
        discord_role_id(FK) VARCHAR(36)
        is_deleted BOOLEAN "DEFAULT FALSE"
        is_active BOOLEAN "DEFAULT TRUE"
        created_on TIMESTAMP "DEFAULT CURRENT_TIMESTAMP()"
        updated_on TIMESTAMP "DEFAULT CURRENT_TIMESTAMP()"
        created_by(FK) VARCHAR(36)
        updated_by(FK) VARCHAR(36)
    }

    USERS ||--o{ USER_PROJECT_MAP : user_id
    PROJECTS ||--o{ USER_PROJECT_MAP : project_id
    PROJECTS ||--o{ PROJECT_DISCORD_MAP : project_id
    DISCORD_ROLE ||--o{ PROJECT_DISCORD_MAP : discord_role_id
    USERS ||--o{ EVENTS : created_by
    SNAPSHOTS }|--|{ USERS : "user_id, lead_id"
    SNAPSHOTS ||--|| PROJECTS : project_id
    INTERVIEWS }|--|{ USERS : "interviewee_id, interviewer_id"
    REQUESTS }|--|{ USERS : user_id
```

### Entity-Relationship Diagram
An Entity-Relationship diagram (ERD) is a conceptual, logical or physcial representation that shows Entities (objects or concepts), Relationships between entities, Attributes of entities, and Cardinality of relationships. ER diagrams are typically created early in the design process and focus on business concepts rather than implementation details. Diagram provided in the `Physical Data Model` section can be considered as the ER diagram.

## Security and Authentication

Security and authentication are critical components of any technical system. Our authentication system will use OAuth with the following identity providers:
- [Google OAuth](https://developers.google.com/identity/protocols/oauth2)
- [Discord OAuth](https://discord.com/developers/docs/topics/oauth2)
- [GitHub OAuth](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)

This provides several advantages:

- Leverages established security infrastructure of major platforms
- Reduces password fatigue for users
- Simplifies onboarding with familiar login options
- Delegates account security concerns to trusted providers

Some security considerations are given below:

### Token Management

- Access Tokens: Short-lived JWTs (15 minutes) with appropriate scopes
- Refresh Tokens: Longer-lived(30 days) tokens stored securely to obtain new access tokens

### Rate Limiting

- Implementation of rate limiting to prevent resource consumption and expliotation.
- IP address based server side rate limiting.
- Rate limit headers in responses.

## Scalability & Performance
TBC

## Deployment Strategy
TBC

## Failure Handling & Monitoring
TBC
