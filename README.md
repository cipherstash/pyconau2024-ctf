# PyCon 2024 Capture the Flag (CTF)

Welcome to the PyCon 2024 Capture the Flag game! This environment uses [PostgreSQL](https://www.postgresql.org/) and [CipherStash](https://cipherstash.com/) to encrypt data in use.
The database has been initialized with [Encrypt Query Language](https://github.com/cipherstash/encrypt-query-language) (EQL) and seeded with the encrypted flag.
The Python applications uses the [eqlpy](https://github.com/cipherstash/eqlpy) library to interact with the EQL payloads.

## Requirements

- [Docker](https://www.docker.com/) installed and running
- [Docker Compose](https://docs.docker.com/compose/) installed
- Python 3.x for interacting with the application
- Keys provided at the CipherStash booth

## Environment overview

This environment includes:

1. PostgreSQL database: Runs on `localhost:5432`.
2. CipherStash Proxy: Intercepts database traffic to handle encryption and decryption, running on `localhost:6432`.

To successfully query and decrypt data:

- All database traffic must go through the CipherStash Proxy.
- Use the provided encryption keys to access decrypted results.

You can view the previously executed SQL commands to initialize the database [here](sql/init.sql).

## Getting started

### 1. Clone the repo

```bash
git clone https://github.com/cipherstash/pyconau2024-ctf.git
cd pyconau2024-ctf
```

### 2. Start the environment

Run the following command to start PostgreSQL and the CipherStash Proxy:

```bash
docker compose up --build
```

This will:

- Start the PostgreSQL database (`localhost:5432`) and initialize the database with the seeded data.
- Start the CipherStash Proxy (`localhost:6432`).

### 3. Running the Python application

To run the Python application, run the following command:

```bash
python3 -m venv .venv
source .venv/bin/activate
python main.py
```

The application will query the database and print the results to the console.
If this is the first time running the application, you should see the following output:

```bash
Ciphertext: ...
```

Once you solve the challenge, you should see the following output:

```bash
Plaintext: ...
```

### 4. Obtain your keys

Visit the CipherStash booth to receive your decryption keys.
They will provide you a link to download the contents for your `.envrc` file.

---

## How to solve the challenge

1. Open the `.envrc` file and update the values with your keys.
1. Update the Python application to query the database via the Proxy.
2. Run the application to query the database and view the plaintext decrypted results.

## Flag submission

Once the challenge is solved, submit the flag to [this form](https://forms.gle/sQkc9WktakrJeekUA).

> Hint: The flag is the plaintext value of the `key` column in the `pycon_cta` table.

## Troubleshooting

- Can’t connect to the database?
  - Ensure the Proxy is running (`localhost:6432`).
  - Check your application’s connection settings.
- Decryption issues?
  - Verify you’re using the correct keys from the CipherStash booth.
  - Ensure database traffic is routed through the Proxy.

## Support

For help, visit the CipherStash booth to connect with our team.

---

Have fun and good luck decrypting the flag! 🚩
