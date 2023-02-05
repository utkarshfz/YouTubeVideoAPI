
# YouTubeVideoAPI 

YouTubeVideoAPI exposes endpoint to fetch paginated response about youtube video details based on a fixed query string.



## Author

- Utkarsh Verma
    - utkarshofficio@gmail.com
    - +91 9934661467

## Deployment

To deploy this project run

```bash
  sudo docker-compose up
```


## How to Run
```bash
curl --location --request GET 'http://127.0.0.1:8081/getVideos?page=1'
```
- Open PostMan
    - click file->import->Raw text
    - paste the curl request and continue.

Alternatively 
- paste the curl request into any terminal.

## API Reference

#### Get Video Details in descending order of publish date

```http
  GET /getVideos?page = ${page_number}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `page_number` | `int` | **Required**. the page_no |



## Documentation

- This API fetches recent video details.
- Uses Flask framework to support its backend.
- Psql is used as a persistance layer.
- This API refreshes its video list(i.e->persits in db) every 1 min
- This API uses 15 API keys for db refresh rate of 1 min 
    - ensures atleast 1 API in not exhusted.
    - Proof:
        - Number of minutes in a day = 1440
        - Each KEY has 10000 tokens.
        - Cost for each search call : 100 tokens
        - required number of keys : 1440/(1min * 100 token) = 14.4 
        - so 15 tokens ensures all of them dont expire.



## 🚀 About Me
I'm a backend developer working @ SIXT R&D India.
