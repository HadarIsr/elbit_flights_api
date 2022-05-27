# Elbit Flight Api

## Elbit backend home assignment - Hadar Israeli

### About 

is a web application written in `python` using `fastapi` api framework.


### Entities

The service includes basic main model:

* Flight


### API Methods Examples

* Get **all** flights number:
  
  ```bash
  curl -X 'GET' \
  'http://127.0.0.1:8080/flights_number/' \
  -H 'accept: application/json'
  ```
  
* Get flights number from **given** country

  ```bash
  curl -X 'GET' \
  'http://127.0.0.1:8080/flights_number/?county=Germany' \
  -H 'accept: application/json'
  ```
  
- Get **all inbound** flights:
  
  ```bash
   curl -X 'GET' \
    'http://127.0.0.1:8080/flights_number/inbound' \
    -H 'accept: application/json'
  ```

- Get **inbound** flights from **given** country:
  
  ```bash
   curl -X 'GET' \
    'http://127.0.0.1:8080/flights_number/inbound?county=spain' \
    -H 'accept: application/json'
  ```
  
- Get **all outbound** flights:
  
  ```bash
   curl -X 'GET' \
    'http://127.0.0.1:8080/flights_number/outbound' \
    -H 'accept: application/json'
  ```

- Get **outbound** flights from **given** country:
  
  ```bash
   curl -X 'GET' \
    'http://127.0.0.1:8080/flights_number/outbound?county=spain' \
    -H 'accept: application/json'
  ```
  
- Get **delayed** flights:
  
  ```bash
   curl -X 'GET' \
    'http://127.0.0.1:8080/flights_delayed' \
    -H 'accept: application/json'
  ```
  
- Get most popular destination:
  
  ```bash
   curl -X 'GET' \
    'http://127.0.0.1:8080/most_popular_destination' \
    -H 'accept: application/json'
  ```

- Get two flights one from Israel and one to Israel that someone 
can take for a quick getaway

  ```bash
   curl -X 'GET' \
    'http://127.0.0.1:8080/flights_soon' \
    -H 'accept: application/json'
  ```
  
  
### Installation Guide



1. To build the docker file run
    ```shell
    docker build -t hadar-elbit-image path/to/dockerfile
   ```

2. After the build is completed you can start the server by running the command
   
   ```shell
    docker run -d --rm --name hadar-elbit-container -p 8080:8080 hadar-elbit-image
   ```
3. You can send requests to the server using curl
    ```shell
   curl -GET   http://127.0.0.1:8080
    ```

@Hadar Israeli