#!/usr/bin/bash
PERMS=755
DEST=/usr/bin
if [[ -z "${VIRTUAL_ENV}" ]]; then
  echo "Please activate venv"
  exit 1
fi

read -pr "Install discord-notify (and link notify-discord) to ${DEST}? (y/n) " yn
case $yn in
  [Yy]* )
    pyinstaller --onefile notify.py
    cp -v dist/notify "${DEST}/discord-notify"
    chmod -v $PERMS "${DEST}/discord-notify"
    ln -s -f -v "${DEST}/discord-notify" "${DEST}/notify-discord"
  ;;
  * ) echo "Ok, no then :(";;
esac
