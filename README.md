This project includes Web application based on FastAPI, PostgreSQL, SQLAlchemy and prepared for Docker Compose. Application can create item, gets all items, get item by id and get random item.

Tools    

SQLAlchemy is a popular Object-Relational Mapping (ORM) library for Python. It is widely used due to its support for multiple database backends thus offering database portability and simplifying complex SQL operations.

PostgreSQL is an open-source relational database management system that is used for storing and managing data.    

FastAPI is a modern web framework built on top of the asynchronous Starlette framework. It leverages Python’s type hints and the Pydantic library for automatic request and response validation, serialization, and interactive API documentation generation.

You need to create .env file with following variables for db connection:
| variable  | value     |
|-----------|-----------|
| USER_NAME | *required |
| PASSWORD  | *required |
| HOST      | *required |
| PORT      | *required | 
| DATABASE  | *required |

You need to create db_password.txt and db_name.txt for db service in compose.yaml
Example: db_password.txt contains only one string with password without paired or single quotes.