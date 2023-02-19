import movie_svc
import requests.exceptions


def main():
    print_header()
    search_event_loop()


def print_header():
    print("---------------------")
    print("     MOVIE SEARCH APP")
    print("---------------------")
    print()


def search_event_loop():
    search = 'ONCE_THOUGH_LOOP'

    while search != 'x':
        try:
            search = input("Movie search text (x to exit): ")
            if search != 'x':
                results = movie_svc.find_movies(search)
                print("Found {} results".format(len(results)))
                for r in results:
                    print("{} -- {}".format(r.year, r.title))
        except requests.exceptions.ConnectionError:
            print("Error: Connection error.")
        except ValueError:
            print("Error: Search text is required")
        except Exception as x:
            print("Ooops! Something goes wrong. Unexpected error: {}".format(x))
    print("exiting...")


if __name__ == '__main__':
    main()

