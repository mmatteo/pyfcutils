default: setup.py
		/usr/bin/env python setup.py build
		@echo ""
		@echo "The numpy deprecation warning is a feature of cython and is no cause for alarm!"
		
install: default
		/usr/bin/env python setup.py install --user --record installed_files.txt

clean:
		/usr/bin/env python setup.py clean
		rm src/fcutils.c

distclean: clean
		rm -rf build

uninstall:
		@echo 'Check the installed_filex.txt file for all install files and remove them by hand.'
		@echo 'Example: "rm $$(cat installed_files.txt)"'
		@echo 'Make sure it does not remove files you want to keep.'
		@echo 'Good Luck!'
