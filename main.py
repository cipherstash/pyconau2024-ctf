import psycopg2

def fetch_data_from_db():
  # Database connection parameters
  host = "localhost"
  port = 5432
  database = "postgres"
  user = "postgres"
  password = "postgres"

  try:
    # Connect to PostgreSQL database
    connection = psycopg2.connect(
      host=host,
      port=port,
      database=database,
      user=user,
      password=password
    )

    cursor = connection.cursor()
      
    # Execute the query
    query = "SELECT * FROM pycon_cta;"
    cursor.execute(query)
      
    # Fetch and print all results
    results = cursor.fetchall()
    for row in results:
      print(row)
  
  except Exception as error:
    print(f"An error occurred: {error}")
  
  finally:
    if cursor:
      cursor.close()
    if connection:
      connection.close()

if __name__ == "__main__":
  fetch_data_from_db()
