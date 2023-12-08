from .jsonr import (
    __version__,
    __author__,
    __author_email__,
    __license__,
    __copyright__,
    __credits__,
    __maintainer__,
    __email__,
    __status__,
    __topic__,
    __license_type__,
    __url__,
    __github__,
    __repo__,
    __keywords__,
)

def main():
    jsonr_table: dict = {
        'version': __version__,
        'author': __author__,
        'author_email': __author_email__,
        'license': __license__,
        'copyright': __copyright__,
        'credits': __credits__,
        'maintainer': __maintainer__,
        'status': __status__,
        'topic': __topic__,
        'license_type': __license_type__,
        'url': __url__,
        'github': __github__,
        'repo': __repo__,
        'keywords': __keywords__,
    }
    for key, value in jsonr_table.items():
        print(f'{key}: {value}')

if __name__ == '__main__':
    main()
