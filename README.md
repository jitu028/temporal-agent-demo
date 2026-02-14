# Python Temporal Agent Demo

This repository contains a Python Temporal Agent demo application. The aim of this demo is to showcase the capabilities of Temporal Workflow with a focus on building robust and scalable applications.

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Running the Demo

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jitu028/temporal-agent-demo.git
   cd temporal-agent-demo
   ```

2. **Start Docker Compose**:
   ```bash
   docker-compose up
   ```

This command will build and start the necessary services defined in the `docker-compose.yml` file.

### Architecture
- This demo consists of the following components:
  - Temporal Server: Manages the workflow executions.
  - Worker: Processes the workflows and activities.
  - The Python Client: Interacts with the Temporal Server to start and manage workflows.

### Folder Structure
```
├── docker-compose.yml
├── worker
│   ├── main.py
│   └── requirements.txt
├── client
│   ├── main.py
│   └── requirements.txt
└── README.md
```

## Contributing

Feel free to submit pull requests if you have improvements or additional features to add to the demo.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Temporal](https://temporal.io/): The framework used for workflow orchestration.
- [Docker](https://www.docker.com/): For containerization.

---

This README is updated with the objective of making it easier for users to quickly understand how to utilize this Python Temporal Agent demo application.