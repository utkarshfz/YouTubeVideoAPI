
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
- This API uses multiple keys switchs to another if one is depleted



## 🚀 About Me
I'm a backend developer working @ SIXT R&D India.
LinkedIn : https://www.linkedin.com/in/utkarsh-verma-214255164/
