# try:
#     open("database.sqlite")
# except OSError as exc:
#     raise RuntimeError('unable to handle error') from exc

# def func():
#     raise ConnectionError
#
# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc


try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None
