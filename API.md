
# MYBLOG PROJECT API DOCUMANTATION

All endpoints are prefixed with /api/ and Authentication is handled via token authentication


## Authentication and User Endpoints

#### Register User

```http
  POST /api/users/register/
```
Register a new user and return the user details along with an authentication token

`Request Body:`

```JSON
{
  "username": "new_user",
  "password": "password123",
  "first_name": "First",
  "last_name": "Last",
  "email": "email@example.com"
}
```

`Response:`

```JSON
{
  "user": {
    "id": 1,
    "first_name": "First",
    "last_name": "Last",
    "email": "email@example.com",
    "username": "new_user"
  },
  "token": "generated_auth_token"
}
```


#### Login User

```http
  POST /api/users/login/
```

Authenticate a user and return an authentication token.

`Request Body:`

```JSON
{
  "username": "existing_user",
  "password": "password123"
}

```

`Response:`

```JSON
{
  "user_id": 1,
  "username": "existing_user",
  "token": "generated_auth_token"
}

```

#### Logout User

```http
  POST /api/users/logout/
```

Logout the authenticated user and delete their authentication token.

`Response:`

```JSON
{
  "details": "Logged out successfully."
}
```

#### User List

```http
  GET /api/users/
```

Retrieve a list of all users.

`Request Body:`

```JSON
[
  {
    "id": 1,
    "first_name": "First",
    "last_name": "Last",
    "email": "email@example.com",
    "username": "user1"
  },
  ...
]
```

#### Retrieve User

```http
  GET /api/users/{id}/
```

 Retrieve details of a specific user by ID.

`Request Body:`

```JSON
{
  "id": 1,
  "first_name": "First",
  "last_name": "Last",
  "email": "email@example.com",
  "username": "user1"
}

```

------------------------------------------------------------


## Post Endpoints

#### List Posts

```http
  GET /api/posts/
```
Retrieve a list of all posts.

`Response:`

```JSON
[
  {
    "id": 1,
    "title": "Post Title",
    "content": "Post content",
    "author": 1,
    "created_at": "2023-07-01T12:34:56Z",
    "updated_at": "2023-07-01T12:34:56Z"
  },
  ...
]
```

* `author`: Filter by author ID.
```http
  GET  /api/posts/?author=1
```

* `created_at`: Filter by specific creation date (YYYY-MM-DD).
```http
  GET  /api/posts/?created_at=2023-07-01
```

* `created_at__gte`: Filter posts created on or after a specific date (YYYY-MM-DD).
```http
  GET  /api/posts/?created_at__gt=2023-07-01
```

* `created_at__lte`: Filter posts created on or before a specific date (YYYY-MM-DD).
```http
  GET  /api/posts/?created_at__lt=2023-07-01
```
* Filter with author and created
```http
  GET  /api/posts/?author=1&created_at__gt=2023-07-01
```

* Filter with start date and end date

```http
  GET  /api/posts/?created_at__gte=<start_date>&created_at__lte=<end_date>

  GET /api/posts/?created_at__gte=2023-07-01&created_at__lte=2023-07-31
```

`Response:`

```JSON
[
  {
    "id": 1,
    "title": "Post Title",
    "content": "Post content",
    "author": 1,
    "created_at": "2023-07-01T12:34:56Z",
    "updated_at": "2023-07-01T12:34:56Z"
  },
  ...
]

```


#### Create Post

```http
  POST /api/posts/
```
Create a new post.

`Request Body:`

```JSON
{
  "title": "New Post",
  "content": "Post content"
}


```

`Response:`

```JSON
{
  "id": 1,
  "title": "New Post",
  "content": "Post content",
  "author": 1,
  "created_at": "2023-07-01T12:34:56Z",
  "updated_at": "2023-07-01T12:34:56Z"
}

```

#### Retrieve Post

```http
  GET /api/posts/{id}/
```

Retrieve details of a specific post by ID.

`Response:`

```JSON
{
  "id": 1,
  "title": "Post Title",
  "content": "Post content",
  "author": 1,
  "created_at": "2023-07-01T12:34:56Z",
  "updated_at": "2023-07-01T12:34:56Z"
}

```

#### Update Post

```http
  PUT or PATCH /api/posts/{id}/
```

Update details of a specific post by ID.

`Request Body:`

```JSON
{
  "title": "Updated Post Title",
  "content": "Updated post content"
}

```

`Response:`

```JSON
{
  "id": 1,
  "title": "Updated Post Title",
  "content": "Updated post content",
  "author": 1,
  "created_at": "2023-07-01T12:34:56Z",
  "updated_at": "2023-07-01T12:34:56Z"
}

```

#### Delete Post

```http
  DELETE /api/posts/{id}/
```

Delete a specific post by ID.

`Response:`

```JSON
204 No Content
```

------------------------------------------------------------


## Comment Endpoints

#### List Comments

```http
  GET /api/comments/
```
Retrieve a list of all comments.

`Response:`

```JSON
[
  {
    "id": 1,
    "post": 1,
    "author": 1,
    "content": "Comment content",
    "created_at": "2023-07-01T12:34:56Z",
    "updated_at": "2023-07-01T12:34:56Z"
  },
  ...
]

```

#### Create Comment

```http
  POST /api/comments/
```
Create a new comment.

`Request Body:`

```JSON
{
  "post": 1,
  "content": "Comment content"
}

```

`Response:`

```JSON
{
  "id": 1,
  "post": 1,
  "author": 1,
  "content": "Comment content",
  "created_at": "2023-07-01T12:34:56Z",
  "updated_at": "2023-07-01T12:34:56Z"
}


```

#### Retrieve Comment

```http
  GET api/comments/{id}/
```

Retrieve details of a specific comment by ID.

`Response:`

```JSON
{
  "id": 1,
  "post": 1,
  "author": 1,
  "content": "Comment content",
  "created_at": "2023-07-01T12:34:56Z",
  "updated_at": "2023-07-01T12:34:56Z"
}

```

#### Update Comment

```http
  PUT or PATCH /api/comments/{id}/
```

Update details of a specific comment by ID.

`Request Body:`

```JSON
{
  "content": "Updated comment content"
}

```

`Response:`

```JSON
{
  "id": 1,
  "post": 1,
  "author": 1,
  "content": "Updated comment content",
  "created_at": "2023-07-01T12:34:56Z",
  "updated_at": "2023-07-01T12:34:56Z"
}


```

#### Delete Comment

```http
  DELETE /api/comments/{id}/
```

Delete a specific comment by ID.

`Response:`

```JSON
204 No Content
```
