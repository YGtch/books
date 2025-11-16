![Pytest](https://github.com/YGtch/books/actions/workflows/pytest.yml/badge.svg)
# books
## Environment setup
1. run
`source scripts/setup.sh`

## Project aims
The aim of our project is to create a books-club telegram bot for periodic novel publishing. Bot will collect a chapter from each participant and then
on certain date will send them back all at ones. This type of book club is great for writers for publishing their books among friends as well as for
clubs exploring classical literature. For well known pieces syncronization with database will be added.

Some other features for managing and comfortable usage are also planned.

## Running tests
For complete testing simply run

```python3 -m pytest tests```

To test a separate module run

```python3 -m pytest tests/module```
