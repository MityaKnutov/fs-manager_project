import argparse
from src import file_oper as fop
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Файловый менеджер")
    parser.add_argument('--command', type=str, required=True, help='Команда')
    parser.add_argument('--path', type=str, help='Путь к папке или файлу')
    parser.add_argument('--source', type=str, help='Исходный путь для move/copy')
    parser.add_argument('--destination', type=str, help='Конечный путь для move/copy')
    return parser.parse_args()

def main():
    args = parse_args()
    try:
        if args.command == 'list':
            if not args.path:
                print("Пожалуйста, укажите --path")
                return
            items = fop.list_directory(args.path)
            for item in items:
                print(item)

        elif args.command == 'create_folder':
            if not args.path:
                print("Пожалуйста, укажите --path")
                return
            if fop.create_folder(args.path):
                print(f"Папка создана: {args.path}")

        elif args.command == 'delete':
            if not args.path:
                print("Пожалуйста, укажите --path")
                return
            if fop.delete(args.path):
                print(f"Удалено: {args.path}")

        elif args.command == 'move':
            if not args.source or not args.destination:
                print("Пожалуйста, укажите --source и --destination")
                return
            if fop.move(args.source, args.destination):
                print(f"Перемещено {args.source} в {args.destination}")

        elif args.command == 'copy':
            if not args.source or not args.destination:
                print("Пожалуйста, укажите --source и --destination")
                return
            if fop.copy(args.source, args.destination):
                print(f"Скопировано {args.source} в {args.destination}")

        else:
            print("Неизвестная команда")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == '__main__':
    main()