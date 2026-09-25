# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a small REST API with FastAPI by defining routes, returning JSON data, and accepting validated client requests.

## 📝 Tasks

### 🛠️ Create a FastAPI Application

#### Description
Complete the starter code to create a FastAPI application for a school library. Run the application with Uvicorn and verify that the interactive documentation opens at `/docs`.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Start successfully with `uvicorn starter-code:app --reload`
- Return a welcome message from the `GET /` route
- Include a short description for the API in the application configuration


### 🛠️ Add Book GET Endpoints

#### Description
Use the provided in-memory list of books to create endpoints that let a client view all books and find one book by its ID.

#### Requirements
Completed program should:

- Return the complete book list from `GET /books`
- Return one book from `GET /books/{book_id}`
- Return HTTP status `404` with a useful message when a requested book does not exist
- Return book data as JSON objects with an ID, title, author, and availability value

Example request:

```text
GET /books/1
```

Example response:

```json
{
  "id": 1,
  "title": "The Giver",
  "author": "Lois Lowry",
  "available": true
}
```


### 🛠️ Add a Book with a POST Endpoint

#### Description
Define a Pydantic request model and use it to accept a new book from a client. Store valid books in the in-memory list and return the created book.

#### Requirements
Completed program should:

- Define a request model with `title`, `author`, and `available` fields
- Add a new book from `POST /books`
- Assign a unique numeric ID to each new book
- Return the created book with HTTP status `201`
- Let FastAPI reject requests that are missing required fields or use incorrect field types

Example request body:

```json
{
  "title": "A Wrinkle in Time",
  "author": "Madeleine L'Engle",
  "available": true
}
```