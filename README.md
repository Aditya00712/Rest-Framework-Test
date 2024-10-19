# Rest-Framework-Test
## CRUD Operations

### 1. Create a Task
- **Endpoint**: `POST /api/tasks/`
- **Request Body**:
    ```json
    {
      "title": "Task Title",
      "description": "Task Description",
      "due_date": "YYYY-MM-DD",
      "status": true
    }
### 2. Read Tasks
- **List All Tasks**: 
    - **Endpoint**: `GET /api/tasks/`
- **Retrieve a Specific Task**:
    - **Endpoint**: `GET /api/tasks/{id}/`

### 3. Update a Task
- **Endpoint**: `PUT /api/tasks/{id}/`
- **Request Body**:
    ```json
    {
      "title": "Updated Task Title",
      "description": "Updated Task Description",
      "due_date": "YYYY-MM-DD",
      "status": false
    }
  
### 4. Delete a Task
- **Endpoint**: `DELETE /api/tasks/{id}/`


### 5 .Test the Search Functionality
To search for tasks, you can now make a GET request with query parameters. Here’s how you can use it:
Search by Title:
GET /api/tasks/?search=your_task_title


### 6.Testing the Validation
To test this, you can try creating or updating a task with a due date set to a past date:
Create a Task with Past Due Date:

POST /api/tasks/
Request Body:
{
  "title": "Sample Task",
  "description": "This task has a past due date",
  "due_date": "2022-01-01",         # Example of a past date
  "status": false
}
