echo Enter CMD

read cmd

if [ $cmd == "build" ]; then
  bash cmd/build.sh
fi

if [ $cmd == "rm" ]; then
  bash cmd/rm.sh
fi

if [ $cmd == "pip" ]; then
  bash cmd/pip.sh
fi

# Sorry for the bad syntax, I had issues developing this
