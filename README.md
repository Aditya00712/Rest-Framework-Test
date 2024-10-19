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
