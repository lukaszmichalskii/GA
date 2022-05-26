import argparse

from ga_app.ga_app import GAApp


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filepath', type=str, required=True, help='Filepath to graph saved in .txt file')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    filepath: str = args.filepath
    app = GAApp(filepath)
    app.run()
