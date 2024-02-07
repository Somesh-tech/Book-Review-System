## Book Review System.

The Book review system is system for enthusitic readers who wants to find book info with authentic reviews.
The readers can even share theie personal review for a book/Novel.

## API References: 

#### Get all  the Book available.

```http
  GET /api/all_books
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `all_books` | `string` | This will retireeve allbooks available in our database |

#### Get Book by providing author name.

```http
  GET /api/all_books/{author}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `author`  | `string` | This will make sure that you be given book/novel for a specific author.|

#### Get Book by providing publication year.

```http
  GET /api/all_books/year/{pub_year}
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `author`      | `integer` | This will make sure that you be given book/novel for a specific year. |

#### Get Book by providing author name.

```http
  GET /api/view_review/{title}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`   | `string` | This endpoint will retriev all the review ralated to a particular book/novel. |

```http
  POST /api/submit_review
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `submit_review`| `string` | This endpoint will let you to submit a review for a specific book/novel.|

```http
  POST /api/add_book
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `add_book`  | `string` | This endpoint will a new book to the collection. |

## Installation

To install all the required libraries for the project.
:: Follow the below steps ::

1.Navigate to your working directory, and open the terminal.
2. Run the following command - pip install -r .\requirements.txt

    