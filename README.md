# BD2-T2
API de Gestión de Biblioteca con Litestar y SQLAlchemy


### Rodolfo Cifuentes 🤓
- Estudiante de Ingeniería Informática
- [Rodolfo Cifuentes](https://github.com/Fitooooooooo)
- **rcifuent@umag.cl**

### Descripción del Proyecto y Decisiones de Diseño

Este proyecto extiende una API REST base para la gestión de una biblioteca, aplicando conocimientos avanzados en el desarrollo de APIs con Litestar y SQLAlchemy.

**Principales cambios y decisiones:**

*   **Nuevos Modelos:** Se introdujeron los modelos `Category` y `Review`. Para `Category`, se implementó una relación muchos a muchos con `Book` a través de una tabla de asociación (`book_categories`), permitiendo una clasificación flexible de los libros.
*   **Actualización de Modelos Existentes:** Se enriquecieron los modelos `Book`, `User` y `Loan` con nuevos campos para añadir más detalle y lógica de negocio, como el manejo de stock, información de contacto de usuarios, y estados de préstamos (`ACTIVE`, `RETURNED`, `OVERDUE`) mediante un `Enum` para mayor robustez.
*   **Lógica de Negocio en Repositorios:** Se centralizó la lógica de negocio compleja en los repositorios correspondientes (`BookRepository` y `LoanRepository`). Esto permite mantener los controladores más limpios y enfocados en manejar las peticiones HTTP, mientras que la lógica de acceso y manipulación de datos reside en una capa separada.
*   **Validaciones y DTOs:** Se utilizaron DTOs (`Data Transfer Objects`) para cada modelo, configurando los campos a excluir o incluir en operaciones de lectura, creación y actualización. Las validaciones específicas (formato de email, rangos de valores) se implementaron a nivel de controlador para proporcionar feedback inmediato al cliente.
*   **Migraciones con Alembic:** Cada cambio en la estructura de la base de datos fue gestionado a través de migraciones generadas con Alembic, asegurando un versionado claro y la capacidad de replicar la base de datos de forma consistente.

### Cumplimiento de Requerimientos

| Requerimiento | Estado | Observación |
| :--- | :--- | :--- |
| 1. Crear modelo `Category` | Cumplido | Se implementó el modelo, la relación M-M, DTOs y el CRUD completo. |
| 2. Crear modelo `Review` | Cumplido | Se implementó el modelo, DTOs y el CRUD con las validaciones de rating y límite de reseñas por usuario. |
| 3. Actualizar modelo `Book` | Cumplido | Se añadieron los nuevos campos y se implementaron las validaciones de stock y lenguaje en los endpoints. |
| 4. Actualizar modelo `User` | Cumplido | Se añadieron los nuevos campos, se ajustaron los DTOs para seguridad y se implementó la validación de formato de email. |
| 5. Actualizar modelo `Loan` | Cumplido | Se añadió el `Enum` `LoanStatus` y los nuevos campos. La lógica de `due_date` se implementó en el endpoint de creación. |
| 6. Métodos en `BookRepository` | Cumplido | Se implementaron todos los métodos solicitados y se crearon los endpoints correspondientes en el `BookController`. |
| 7. Métodos en `LoanRepository` | Cumplido | Se implementaron todos los métodos de lógica de negocio y se crearon los endpoints específicos en el `LoanController`. |
| 8. Base de datos inicial | Cumplido | Se creó un script `seed.py` para poblar la base de datos y se generó el respaldo `initial_data.sql` mediante `pg_dump`. |