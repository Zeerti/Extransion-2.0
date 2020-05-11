import eel


def main():
    try:
        print('Starting EEL GUI...')
        eel.init('web')
        eel.start('index.html', port=8000, mode='edge', cmdline_args=['--start-fullscreen'])
    except EnvironmentError:
        print("\n****************\nFailed auto-launching edge. Attemping to load default browswer\n****************\n\nPlease navigate to localhost:8000/index.html manually if it doesn't automatically open")
        # If Chrome isn't found, fallback to Microsoft Edge on Win10 or greater
        try:
            eel.start('index.html', port=8000, mode=False)
        except:
            raise

if __name__ == '__main__':
    main()